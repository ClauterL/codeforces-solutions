#!/usr/bin/env python3
"""Luo uusi ratkaisutiedosto templatesta.

Käyttö: python scripts/new.py 1000 1352C
"""
import sys, pathlib, shutil
if len(sys.argv) != 3:
    sys.exit(__doc__)
root = pathlib.Path(__file__).resolve().parent.parent
dst = root / "solutions" / sys.argv[1] / (sys.argv[2] + ".py")
dst.parent.mkdir(parents=True, exist_ok=True)
if dst.exists():
    sys.exit(f"on jo olemassa: {dst}")
shutil.copy(root / "template.py", dst)
print(dst)
