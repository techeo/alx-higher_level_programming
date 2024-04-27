#!/bin/bash
# Get the byte size of an HTTP response header
curl -s "$1" | wc -c
