"""news-image-20261124: write the entry image to /output/entry.png.

The entry image (news.png, a JPEG stored under the .png name the rules
require) is copied verbatim to the output directory. No network, no
re-encoding: the bytes the judge sees are exactly the bytes in the repo.
"""

import hashlib
import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "news.png"
OUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
DST = OUT_DIR / "entry.png"
MAX_BYTES = 1_048_576


def main() -> None:
    data = SRC.read_bytes()
    assert len(data) <= MAX_BYTES, f"news.png is {len(data)} bytes, over the 1 MiB cap"
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SRC, DST)
    copied = DST.read_bytes()
    assert hashlib.sha256(copied).hexdigest() == hashlib.sha256(data).hexdigest(), "copied entry.png differs from news.png"
    print(f"wrote {DST} ({len(copied)} bytes, sha256 {hashlib.sha256(copied).hexdigest()})")


if __name__ == "__main__":
    main()
