#!/bin/bash
uvicorn app.app:app --host 0.0.0.0 --port ${PORT:-4000}
