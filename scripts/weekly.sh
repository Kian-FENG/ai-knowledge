#!/bin/sh
set -eu
cd "$(dirname "$0")/.."
scripts/python scripts/generate-indices.py
scripts/python scripts/capability_report.py
bash tests/run.sh
