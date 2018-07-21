#!/bin/sh
cd src
gunicorn -b 0.0.0.0:5000 main:app --daemon