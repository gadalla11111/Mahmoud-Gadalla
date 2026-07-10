# Skill: zvec

**Trigger:** embedded vector database, in-process vector search, zvec, dense vector index, sparse vector index, hybrid retrieval, full-text search vector, similarity search embedded, DiskANN, vector DB Python, vector search edge device, vector search no server.

---

## What this skill does

Zvec is an in-process (embedded, no separate server) vector database from Alibaba Group — Rust engine, multi-language SDKs, supports dense + sparse + full-text + hybrid search in a single query.

**Source:** `alibaba/zvec` | Open source | Apache 2.0

**Complements:** `anthropic_skills/ai-research` (RAG stack) + `anthropic_skills/data-management` (data pipelines)

---

## Key Capabilities

| Feature | Detail |
|---|---|
| **Dense vector search** | HNSW, flat, IVF index types |
| **Sparse vector search** | SPLADE / BM25-style sparse vectors |
| **Full-text search** | Keyword queries on string fields |
| **Hybrid retrieval** | Combine vector similarity + text + scalar filters in one query |
| **Write-ahead logging** | Durability without external infra |
| **Concurrent reads** | Multiple readers, exclusive write control |
| **DiskANN** | Billion-scale datasets without full RAM requirement |
| **Scale** | Sub-millisecond search over billions of vectors |

---

## SDKs

```bash
pip install zvec           # Python 3.10–3.14
npm install @zvec/zvec     # Node.js
```
Also: Go, Rust, Dart/Flutter native bindings.

**Platforms:** Linux (x86_64, ARM64), macOS (ARM64), Windows (x86_64)

---

## Quick Start (Python)

```python
import zvec

# Create collection with schema
db = zvec.open("./mydb")
col = db.create_collection("docs", dim=1536)

# Insert
col.insert([{"id": 1, "vector": embeddings[0], "text": "hello world"}])

# Dense search
results = col.search(query_vector, top_k=10)

# Hybrid: vector + keyword filter
results = col.search(query_vector, top_k=10, filter="text CONTAINS 'hello'")

# Full-text only
results = col.full_text_search("hello world", top_k=10)
```

---

## When to use vs. alternatives

| Need | Use |
|---|---|
| No infra / embedded / edge device | **zvec** |
| Managed cloud vector DB | Pinecone / Qdrant Cloud |
| Already using Postgres | pgvector |
| Billion-scale + full infra control | Weaviate / Milvus |
| Notebook / local RAG prototype | **zvec** |

---

## Health

```yaml
pass_rate: null
trigger_accuracy: null
cross_references:
  - anthropic_skills/ai-research
  - anthropic_skills/data-management
  - anthropic_skills/scientific-research
archetype: vector-database
```
