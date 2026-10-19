#!/usr/bin/env python3
"""Generate an image with the Gemini API.

Usage:
  python3 brochure/tools/gen_image.py "prompt" out.png [--ref images/x.jpeg ...]
      [--model gemini-3-pro-image] [--aspect 4:3]

Reads GEMINI_KEY from .env.local (project root) or the environment.
--ref passes real product photos so the generated scene keeps the
actual Crosspaulin look (colour, printed branding triangle, eyelets).
"""
import argparse, base64, json, mimetypes, os, pathlib, sys, urllib.request, urllib.error

ROOT = pathlib.Path(__file__).resolve().parents[2]


def load_key():
    env = ROOT / ".env.local"
    if env.exists():
        for line in env.read_text().splitlines():
            if line.strip().startswith("GEMINI_KEY="):
                return line.split("=", 1)[1].strip().strip('"\'')
    key = os.environ.get("GEMINI_KEY") or os.environ.get("GEMINI_API_KEY")
    if not key:
        sys.exit("GEMINI_KEY not found in .env.local or environment")
    return key


def main():
    p = argparse.ArgumentParser()
    p.add_argument("prompt")
    p.add_argument("out")
    p.add_argument("--ref", action="append", default=[])
    p.add_argument("--model", default="gemini-3-pro-image")
    p.add_argument("--aspect", default="4:3")
    a = p.parse_args()

    parts = [{"text": a.prompt}]
    for r in a.ref:
        mime = mimetypes.guess_type(r)[0] or "image/jpeg"
        parts.append({"inline_data": {"mime_type": mime,
                                      "data": base64.b64encode(pathlib.Path(r).read_bytes()).decode()}})
    body = {"contents": [{"parts": parts}],
            "generationConfig": {"responseModalities": ["IMAGE"],
                                 "imageConfig": {"aspectRatio": a.aspect}}}
    req = urllib.request.Request(
        f"https://generativelanguage.googleapis.com/v1beta/models/{a.model}:generateContent",
        data=json.dumps(body).encode(),
        headers={"Content-Type": "application/json", "x-goog-api-key": load_key()})
    try:
        with urllib.request.urlopen(req, timeout=300) as resp:
            data = json.load(resp)
    except urllib.error.HTTPError as e:
        sys.exit(f"HTTP {e.code}: {e.read().decode()[:800]}")

    for cand in data.get("candidates", []):
        for part in cand.get("content", {}).get("parts", []):
            blob = part.get("inlineData") or part.get("inline_data")
            if blob:
                out = pathlib.Path(a.out)
                out.parent.mkdir(parents=True, exist_ok=True)
                out.write_bytes(base64.b64decode(blob["data"]))
                print(out)
                return
    sys.exit("No image returned: " + json.dumps(data)[:800])


if __name__ == "__main__":
    main()
