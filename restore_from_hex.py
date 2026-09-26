#!/usr/bin/env python3
"""Restaura HTML/JS desde partes hex gzip en hex-parts/ (uso interno si hiciera falta)."""
import gzip, json, hashlib
from pathlib import Path
root = Path(__file__).resolve().parent
manifest = json.loads((root/"hex-parts"/"manifest.json").read_text())
for item in manifest:
    hx = "".join((root/"hex-parts"/p).read_text().strip() for p in item["parts"])
    raw = gzip.decompress(bytes.fromhex(hx))
    digest = hashlib.sha256(raw).hexdigest()
    if digest != item["sha256_raw"]:
        raise SystemExit(f"SHA mismatch for {item['path']}: {digest}")
    out = root/item["path"]
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_bytes(raw)
    print(f"OK {item['path']} ({len(raw)} bytes)")
print("Restore complete.")
