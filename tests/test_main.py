from src import main
import subprocess
import sys

try:
  import unittest
except ImportError:
  print("Trying to Install required module: unittest\n")
  subprocess.check_call([sys.executable, "-m", "pip", "install", 'unittest'])
finally:
  import unittest

class Testmain(unittest.TestCase):
    def test_main(self):
        self.assertEqual(main.testmain("https://steamcommunity.com/market/search?appid=322330#p", 3, 0), "Successful run")
    
    
if __name__=="main":
    unittest.main()