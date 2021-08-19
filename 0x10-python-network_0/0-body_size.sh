#!/bin/bash
curl -I s "$1" | grep 'Content-Length:'
