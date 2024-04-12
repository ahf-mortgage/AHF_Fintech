#!/bin/bash
cd /home/ubuntu/AHF_Fintech/AHF_Fintech
sudo cp -r static /var/www/html/static/
source venv/bin/activate 
export PYTHONPATH=/home/ubuntu/AHF_Fintech/AHF_Fintech

exec gunicorn --bind 0.0.0.0:8000 core.wsgi:application
