#!/usr/bin/env python3
import os
import pathlib
import shlex
import subprocess
import sys
import time


ADDRESS = '0.0.0.0'
PORT = '5000'


def get_started_containers():
    data = subprocess.run(['docker-compose', 'ps'], capture_output=True).stdout
    return [
        line.split(' ', 1)[0]
        for line in data.decode().split('\n')[2:]
        if line
    ]


script_dir = pathlib.Path(__file__).parent.resolve()

if os.getcwd() != str(script_dir):
    print(f'Working directory is now {script_dir}.')
    os.chdir(script_dir)

if get_started_containers():
    print('Stopping docker services...')
    subprocess.run(shlex.split('docker-compose down'), capture_output=True)

run_dir_path = pathlib.Path('run')

if run_dir_path.exists():
    print('Cleaning up old run/ folder... (uses sudo)')
    command = f'sudo rm -rf {run_dir_path}'
    print(command)
    time.sleep(.1)
    subprocess.run(shlex.split(command))

print('Starting docker services (building web image if needed)...')
try:
    subprocess.run(
        shlex.split('docker-compose up -d'),
        capture_output=True,
        check=True,
    )
except subprocess.CalledProcessError as exception:
    print(f'Failed to start docker services:\n{exception.stderr.decode()}')
    sys.exit(1)

wsgi_sock_path = run_dir_path / 'wsgi.sock'

if not wsgi_sock_path.exists():
    print('Waiting for wsgi.sock to become available...')

    while not wsgi_sock_path.exists():
        time.sleep(.1)

print(f'Starting dev server on http://{ADDRESS}:{PORT}/...')
subprocess.run(shlex.split(
    'uwsgi --master '
    '--plugin http '  # For Debian and friends
    f'--http {ADDRESS}:{PORT} '
    f'--http-to {wsgi_sock_path}'
), capture_output=True)
