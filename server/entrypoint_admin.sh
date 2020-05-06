#!/usr/bin/env bash
flask db upgrade
python3 admin.py
flask db upgrade