#!/bin/bash
set -o errexit
set -o nounset
set -o pipefail


exec python -m uvicorn app.main:app \
  --host 0.0.0.0 \
  --port 8000
