#!/bin/sh

echo "Run Proxy..."
mitmdump -s proxy.py -k  --ssl-insecure --set MITM_REMOTE_PORT=true
