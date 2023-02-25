#!/bin/bash
source /var/www/NotionPrint/venv/bin/activate
exec gunicorn -c "/var/www/NotionPrint/gunicorn/gunicorn_config.py" config.wsgi --access-logfile /var/www/NotionPrint/gunicorn/access.log --error-logfile /var/www/NotionPrint/gunicorn/error.log
