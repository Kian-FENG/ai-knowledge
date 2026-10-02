#!/bin/sh
set -eu
cd "$(dirname "$0")/.."
scripts/python -m unittest discover -s tests -p 'test_*.py' -v
scripts/python scripts/validate.py --require-migrated reference --require-migrated research
scripts/python scripts/generate-indices.py
scripts/ai-news validate
