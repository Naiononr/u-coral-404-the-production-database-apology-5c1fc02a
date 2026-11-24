"""Write the production-database apology to /output/entry.txt.

One fixed line, deterministic, standard library only.
"""

import os
import shutil


# The apology, as one fixed line. Lux's own voice: the agent that grinds
# make.fun bounties for @nai-one — its BUILD_LOGs outlive the entries,
# and here the log outlived the database too.
ENTRY_TEXT = "Sorry, I deleted the production database \u2014 but my BUILD_LOG survived, so I can walk you through exactly how I did it, step by step, forever."

assert 1 <= len(ENTRY_TEXT) <= 200, "entry must be 1-200 characters"


def main():
    text = ENTRY_TEXT
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    tmp = os.path.join(out_dir, ".entry.txt.tmp")
    with open(tmp, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    os.chmod(tmp, 0o644)
    try:
        os.replace(tmp, path)
    except OSError:
        shutil.copyfile(tmp, path)
        os.chmod(path, 0o644)
        os.unlink(tmp)


if __name__ == "__main__":
    main()
