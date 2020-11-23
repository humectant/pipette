#!/usr/bin/env bash

set -e
set -x

python -m pytest --cov=app --cov-report=term-missing app/tests "${@}"