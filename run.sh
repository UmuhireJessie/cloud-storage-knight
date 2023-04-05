#!/bin/sh
# Apply alembic migrations
alembic upgrade head

# Start server
gunicorn -w ${NUM_WORKERS:-4} -k uvicorn.workers.UvicornWorker app:app --bind 0.0.0.0:5000
