#!/usr/bin/env python3
import pathlib
import sys

script_dir = pathlib.Path(__file__).parent.resolve()
wsgi_fifo_path = script_dir / 'run' / 'uwsgi.fifo'

if not wsgi_fifo_path.exists():
    print('Dev server not running, exiting.')
    sys.exit(1)

wsgi_fifo_path.write_text('r')
print('Dev server reloaded.')
