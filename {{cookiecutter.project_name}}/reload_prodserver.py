#!/usr/bin/env python3
import shlex
import subprocess

subprocess.run(shlex.split(
    'docker-compose '
    # Use production files
    '-f docker-compose.yml '
    '-f docker-compose.production.yml '
    # Start services...
    'up '
    # ... but only web...
    '--no-deps '
    # ... rebuild it...
    '--build '
    # ... re-create volumes...
    '--renew-anon-volumes '
    # ... and start it in the background
    '-d web'
))
subprocess.run(shlex.split('docker image prune -f'))
