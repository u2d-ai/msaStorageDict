#!/usr/bin/env bash

set -e
set -x

mypy msaStorageDict
flake8 msaStorageDict docs_src
black msaStorageDict docs_src --check
isort msaStorageDict docs_src scripts --check-only

