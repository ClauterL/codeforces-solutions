#!/usr/bin/env python3
"""Aja ratkaisu annetulla syötteellä.

Käyttö:
  python scripts/run.py 800/4A < input.txt
  echo "8" | python scripts/run.py 800/4A
"""
import subprocess, sys, pathlib

if len(sys.argv) != 2:
    sys.exit(__doc__)
path = pathlib.Path(__file__).resolve().parent.parent / "solutions" / (sys.argv[1] + ".py")
if not path.exists():
    sys.exit(f"ei löydy: {path}")
sys.exit(subprocess.call([sys.executable, str(path)], stdin=sys.stdin))
