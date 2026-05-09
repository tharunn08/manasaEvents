#!/bin/bash
echo "Starting MANASA Events Server..."
cd "$(dirname "$0")"
python3 start_server.py
