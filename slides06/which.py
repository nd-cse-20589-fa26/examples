#!/usr/bin/env python3

import os
import sys

target    = sys.argv[1]
bin_paths = os.environ['PATH'].split(':')

for bin_path in bin_paths:
    target_path = os.path.join(bin_path, target)
    if os.access(target_path, os.X_OK):
        print(os.path.realpath(target_path))
        sys.exit(0)

print(f'no {target} in ({os.environ["PATH"]})')
sys.exit(1)
