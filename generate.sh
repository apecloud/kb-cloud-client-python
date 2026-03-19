#!/bin/bash

set -e
set -x

PROJ_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
GENERATOR_DIR="$PROJ_ROOT/.generator"
OUTPUT_DIR="$PROJ_ROOT/src/kb_cloud_client"

# Find Python 3.10+
if command -v python3.10 &>/dev/null; then
    PYTHON=python3.10
elif command -v python3 &>/dev/null; then
    PYTHON=python3
else
    echo "ERROR: Python 3.10+ is required"
    exit 1
fi

echo "Using Python: $($PYTHON --version)"

# Install generator dependencies if needed
$PYTHON -m pip install click PyYAML jsonref jinja2 python-dateutil -q

# Remove previously generated module directories.
# Admin lives at kbcloud/admin/ (nested, mirrors Go api/kbcloud/admin).
rm -rf "$OUTPUT_DIR/kbcloud" "$OUTPUT_DIR/kbcloud_admin" "$OUTPUT_DIR/kbcloud_data"

# Run generator
PYTHONPATH="$GENERATOR_DIR/src" $PYTHON -m generator \
    "$GENERATOR_DIR/schemas/openapi.yaml" \
    "$GENERATOR_DIR/schemas/adminapi.yaml" \
    -o "$OUTPUT_DIR"

echo "Code generation complete!"
