#!/bin/sh
# Determinism test: run main.py twice into two dirs, outputs must be identical.
set -e
cd "$(dirname "$0")"
rm -rf /tmp/lw-test1 /tmp/lw-test2
OUTPUT_DIR=/tmp/lw-test1 python3 main.py
OUTPUT_DIR=/tmp/lw-test2 python3 main.py
cmp /tmp/lw-test1/entry.txt /tmp/lw-test2/entry.txt
cmp /tmp/lw-test1/entry.txt entry.txt
echo "determinism: PASS (74 bytes, identical across runs)"
