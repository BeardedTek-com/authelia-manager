#!/usr/bin/env bash
source venv/bin/activate
python -m pip install -r requirements.txt
uwsgi --http 0.0.0.0:5000 --wsgi-file authelia-manager.py --callable app --workers 4 --uid 1000 --gid 1000