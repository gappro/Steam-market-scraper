import subprocess
import sys

try:
  import requests
except ImportError:
  print("Trying to Install required module: requests\n")
  subprocess.check_call([sys.executable, "-m", "pip", "install", 'requests'])
finally:
  import requests

try:
  import bs4
except ImportError:
  print("Trying to Install required module: bs4\n")
  subprocess.check_call([sys.executable, "-m", "pip", "install", 'bs4'])
finally:
  import bs4