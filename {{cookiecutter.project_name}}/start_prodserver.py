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
    # ... in the background
    '-d'
))
