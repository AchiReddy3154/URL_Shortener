import os
import multiprocessing

# Server socket
port = os.getenv('PORT', '10000')
bind = f"0.0.0.0:{port}"

# Worker processes
workers = multiprocessing.cpu_count() * 2 + 1
threads = 4
worker_class = 'sync'

# Timeout
timeout = 120

# Logging
accesslog = '-'
errorlog = '-'
loglevel = 'info'

# Reload
reload = True if os.getenv('ENVIRONMENT') == 'development' else False

# SSL (if needed)
# keyfile = '/path/to/keyfile'
# certfile = '/path/to/certfile'

# Process naming
proc_name = 'url-shortener'

# Server mechanics
daemon = False
pidfile = None
umask = 0
user = None
group = None
tmp_upload_dir = None

# Limits
max_requests = 1000
max_requests_jitter = 50
graceful_timeout = 30
keep_alive = 2
