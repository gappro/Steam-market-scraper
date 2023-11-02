import subprocess
import sys

try:
  print("Testing main")
  subprocess.check_call([sys.executable, "-m", "unittest", "tests.test_main.Testmain"])
except LookupError:
  print("Erorr")
finally:
  print("Successful termination")