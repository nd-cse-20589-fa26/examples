#!/usr/bin/env python3

import os
import sys

target    = sys.argv[1]
bin_paths = os.environ['PATH'].split(':')

for bin_path in bin_paths:
    target_path = os.path.join(bin_path, target)
    if os.path.exists(target_path):
        print(target_path)
        sys.exit(0)

sys.exit(1)
