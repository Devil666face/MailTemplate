command = '/var/www/NotionPrint/venv/bin/gunicron'
pythonpath = '/var/www/NotionPrint'
bind = '127.0.0.1:8001'
workers = 3
user = 'www-data'
limit_request_field_size = 0
raw_env = 'DJANGO_SETTINGS_MODULE=config.settings'
