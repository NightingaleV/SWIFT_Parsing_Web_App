#!/bin/sh

set -e

npm run build

python manage.py collectstatic --noinput