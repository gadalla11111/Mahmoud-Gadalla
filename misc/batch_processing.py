"""
Message Batches API — ready-to-run examples.
Covers: create, poll, retrieve results, cancel, prompt caching, extended output.
Requires: ANTHROPIC_API_KEY with credits.
"""

import os
import time

import anthropic
from anthropic.types.message_create_params import MessageCreateParamsNonStreaming
from anthropic.types.messages.batch_create_params import Request
from dotenv import load_dotenv

load_dotenv()

client = anthropic.Anthropic()
MODEL = os.environ.get("COOKBOOK_MODEL", "claude-haiku-4-5")  # cheapest model for demos


# ── 1. Create a batch ────────────────────────────────────────────────────────

def create_batch(prompts: list[tuple[str, str]]) -> str:
    """Submit a list of (custom_id, prompt) pairs as a single batch.
    Returns the batch ID."""
    batch = client.messages.batches.create(
        requests=[
            Request(
                custom_id=cid,
                params=MessageCreateParamsNonStreaming(
                    model=MODEL,
                    max_tokens=1024,
                    messages=[{"role": "user", "content": prompt}],
                ),
            )
            for cid, prompt in prompts
        ]
    )
    print(f"Batch created: {batch.id}  status={batch.processing_status}")
    return batch.id


# ── 2. Poll until done ───────────────────────────────────────────────────────

def wait_for_batch(batch_id: str, poll_interval: int = 60) -> anthropic.MessageBatch:
    """Poll every `poll_interval` seconds until the batch ends."""
    while True:
        batch = client.messages.batches.retrieve(batch_id)
        if batch.processing_status == "ended":
            print(f"Batch {batch_id} done. counts={batch.request_counts}")
            return batch
        print(f"Batch {batch_id} still processing... ({batch.request_counts})")
        time.sleep(poll_interval)


# ── 3. Retrieve results ──────────────────────────────────────────────────────

def print_results(batch_id: str) -> dict[str, str]:
    """Stream results and return {custom_id: text} for succeeded requests."""
    results = {}
    for result in client.messages.batches.results(batch_id):
        match result.result.type:
            case "succeeded":
                text = result.result.message.content[0].text
                results[result.custom_id] = text
                print(f"[{result.custom_id}] OK: {text[:80]}...")
            case "errored":
                err = result.result.error.error
                if err.type == "invalid_request_error":
                    print(f"[{result.custom_id}] Validation error: {err.message}")
                else:
                    print(f"[{result.custom_id}] Server error: {err.message}")
            case "expired":
                print(f"[{result.custom_id}] Expired — resubmit")
            case "canceled":
                print(f"[{result.custom_id}] Canceled")
    return results


# ── 4. Cancel a batch ────────────────────────────────────────────────────────

def cancel_batch(batch_id: str) -> None:
    batch = client.messages.batches.cancel(batch_id)
    print(f"Cancel initiated: {batch.id}  status={batch.processing_status}")


# ── 5. List all batches ──────────────────────────────────────────────────────

def list_batches(limit: int = 20) -> None:
    for batch in client.messages.batches.list(limit=limit):
        print(f"{batch.id}  {batch.processing_status}  created={batch.created_at}")


# ── 6. Prompt caching example ────────────────────────────────────────────────

def create_cached_batch(shared_context: str, questions: list[tuple[str, str]]) -> str:
    """All requests share a large cached system prompt."""
    batch = client.messages.batches.create(
        requests=[
            Request(
                custom_id=cid,
                params=MessageCreateParamsNonStreaming(
                    model=MODEL,
                    max_tokens=1024,
                    system=[
                        {"type": "text", "text": "You are a helpful analyst.\n"},
                        {
                            "type": "text",
                            "text": shared_context,
                            "cache_control": {"type": "ephemeral"},
                        },
                    ],
                    messages=[{"role": "user", "content": question}],
                ),
            )
            for cid, question in questions
        ]
    )
    print(f"Cached batch created: {batch.id}")
    return batch.id


# ── 7. Extended output (beta, Opus/Sonnet only) ───────────────────────────────

def create_extended_output_batch(prompts: list[tuple[str, str]]) -> str:
    """Up to 300k output tokens per request. Opus 4.6/4.7/4.8 or Sonnet 4.6 only."""
    batch = client.beta.messages.batches.create(
        betas=["output-300k-2026-03-24"],
        requests=[
            Request(
                custom_id=cid,
                params=MessageCreateParamsNonStreaming(
                    model="claude-opus-4-6",
                    max_tokens=300_000,
                    messages=[{"role": "user", "content": prompt}],
                ),
            )
            for cid, prompt in prompts
        ],
    )
    print(f"Extended-output batch created: {batch.id}")
    return batch.id


# ── Demo ─────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    # Basic batch
    batch_id = create_batch([
        ("q1", "What is the capital of France?"),
        ("q2", "What is 12 * 12?"),
        ("q3", "Name three programming languages."),
    ])

    # In production use wait_for_batch(batch_id).
    # Here we just show the pattern without blocking.
    print("\nTo poll and retrieve results, run:")
    print(f"  batch = wait_for_batch('{batch_id}')")
    print(f"  results = print_results('{batch_id}')")
