---
name: hyperframes
description: >
  Turn HTML/CSS/JS animations into rendered video. Use when a user wants to
  produce an MP4/GIF/WebM from web markup — motion graphics, animated explainers,
  data-viz loops, title cards — by writing HTML and capturing it frame-by-frame
  with headless Chromium, then encoding with ffmpeg. Trigger on: "render this to
  video", "HTML to MP4", "animate this and export", "make a video from code",
  "motion graphic". Archetype: Workflow Automation. Cross-references
  frontend-design for the visual layer and algorithmic-art for generative frames.
allowed-tools: [Read, Write, Bash, WebFetch]
argument-hint: "<animation concept or HTML file> [--format mp4|gif|webm] [--fps 30] [--duration 5]"
auto-trigger:
  - "render to video"
  - "HTML to MP4"
  - "make a video from code"
  - animated explainer or motion graphic from markup
  - exporting a CSS/JS animation as a video file
do-not-trigger:
  - static image output (use canvas-design)
  - editing existing video footage (out of scope)
  - building an interactive web UI with no export (use frontend-design)
health:
  last_eval: 2026-06-26
  pass_rate: null
  trigger_accuracy: null
  open_issues: []

---

# Hyperframes

Write HTML, render video. The deck/animation is authored as a web page; frames are captured deterministically and encoded into a video file.

---

## Pipeline

```
HTML/CSS/JS animation  →  headless Chromium frame capture  →  ffmpeg encode  →  MP4 / GIF / WebM
```

Determinism is the whole game: the animation must be **driven by an explicit clock**, not wall-time, so every render is identical.

---

## Step 1 — Author the Animation

Build a single self-contained HTML file. Hand the visual layer to `frontend-design` if it needs to look designed.

**Hard rule — drive motion by a frame variable, not real time:**

```html
<script>
  // Exposed so the capture harness can step frames deterministically.
  window.__seekTo = (t) => {
    // t = seconds. Position EVERY animated element from t. No setTimeout, no CSS
    // animations tied to wall-clock — compute state purely from t.
    render(t);
  };
</script>
```

Never use `requestAnimationFrame` loops or CSS `animation:` for the captured layer — they desync from the capture cadence. Compute each frame from `t`.

---

## Step 2 — Capture Frames (headless Chromium)

Use the pre-installed Chromium via Playwright (`/opt/pw-browsers/chromium`). For each frame `i`, call `__seekTo(i/fps)`, then screenshot.

```python
# capture.py — run under the project's Playwright
from playwright.sync_api import sync_playwright
import os

FPS, DURATION = 30, 5
frames = FPS * DURATION
os.makedirs("frames", exist_ok=True)

with sync_playwright() as p:
    b = p.chromium.launch()                       # uses PLAYWRIGHT_BROWSERS_PATH
    pg = b.new_page(viewport={"width": 1920, "height": 1080}, device_scale_factor=2)
    pg.goto(f"file://{os.path.abspath('anim.html')}")
    for i in range(frames):
        pg.evaluate(f"window.__seekTo({i/FPS})")
        pg.screenshot(path=f"frames/{i:05d}.png")
    b.close()
```

Do not run a long-lived server — capture is a finite loop that exits.

---

## Step 3 — Encode (ffmpeg)

| Format | Command |
|---|---|
| **MP4 (H.264)** | `ffmpeg -framerate 30 -i frames/%05d.png -c:v libx264 -pix_fmt yuv420p -crf 18 out.mp4` |
| **WebM (VP9)** | `ffmpeg -framerate 30 -i frames/%05d.png -c:v libvpx-vp9 -crf 30 out.webm` |
| **GIF** | two-pass palette: `ffmpeg -i frames/%05d.png -vf palettegen palette.png` then `ffmpeg -framerate 30 -i frames/%05d.png -i palette.png -lavfi paletteuse out.gif` |

`-pix_fmt yuv420p` is mandatory for MP4 to play in browsers/QuickTime. Use `device_scale_factor=2` for crisp output, then downscale if needed.

---

## Output

Deliver the encoded file via SendUserFile, plus the source `anim.html` so the user can tweak and re-render. State: resolution, fps, duration, codec, file size.

---

## Skill Cross-References

| Situation | Invoke |
|---|---|
| Animation needs real design quality | `frontend-design` |
| Generative/procedural frames (flow fields, particles) | `algorithmic-art` |
| It's actually a slide deck, not a video | `presentation-architect` → `pptx` |
| GIF specifically for Slack reactions | `slack-gif-creator` |

---

## Rules

- **Drive frames by an explicit clock** (`__seekTo(t)`) — never wall-time or rAF for the captured layer.
- **Capture is a finite loop** — never leave a server/browser running.
- **`-pix_fmt yuv420p`** on MP4 or it won't play everywhere.
- **Author self-contained HTML** — no external network deps at render time (flaky frames).
- **Deliver source + video** — the user re-renders by editing HTML, not by re-describing.
