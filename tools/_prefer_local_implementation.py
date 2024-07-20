import os
import sys

if not (getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS')):
    src_dir = os.path.dirname(os.path.abspath(__file__))
    local_path = os.path.join(src_dir, "..", "python")
    if os.path.exists(local_path):
        sys.path.insert(0,local_path)
