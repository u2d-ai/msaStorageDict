#!/bin/sh -e
set -x

autoflake --remove-all-unused-imports --recursive --in-place msaStorageDict docs_src --exclude=__init__.py
black msaStorageDict docs_src
isort msaStorageDict docs_src
