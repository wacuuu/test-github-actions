#!/bin/bash
DIR=$(realpath $(dirname "$0"))
cd ${DIR}
gunicorn main:app --bind 0.0.0.0:80 --pythonpath / --reload --access-logfile=-

