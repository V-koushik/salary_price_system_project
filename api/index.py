import sys
import os

root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
backend_dir = os.path.join(root_dir, "backend")

sys.path.insert(0, backend_dir)
sys.path.insert(0, root_dir)

from backend.app import app as _app
app = _app
