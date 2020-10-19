#!/usr/bin/env python3
import shlex
import subprocess

subprocess.run(shlex.split('docker-compose stop web'))
subprocess.run(shlex.split('docker-compose rm -f web'))
subprocess.run(shlex.split('docker image prune -f'))
subprocess.run(shlex.split('docker volume prune -f'))
subprocess.run(shlex.split(
    'docker-compose '
    # Use production files
    '-f docker-compose.yml '
    '-f docker-compose.production.yml '
    # Start services...
    'up '
    # ... but only web...
    '--no-deps '
    # ... and start it in the background
    '-d web'
))
