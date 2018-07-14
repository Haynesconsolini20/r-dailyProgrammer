# CHALLENGE 363
# DIFFICULTY: EASY
# I BEFORE E
# Author: Sam Haynes
# Date: 07/14/2018

# This was a great lesson in some basic string functions in python. Thanks to all the great people posting
# solutions that helped me refine mine!




import unittest

def check(word):
  if "cie" in word:
    return False
  elif "ei" in word.replace("cei", ""):
      return False
  else:
    return True

class wordTest(unittest.TestCase):
  def test_a(self):
    self.assertEqual(check("a"), True)
  def test_zombie(self):
    self.assertEqual(check("zombie"), True)
  def test_transceiver(self):
    self.assertEqual(check("transceiver"), True)
  def test_veil(self):
    self.assertEqual(check("veil"), False)
  def test_icier(self):
    self.assertEqual(check("icier"), False)


suite = unittest.TestLoader().loadTestsFromTestCase(wordTest)
testResult = unittest.TextTestRunner(verbosity=2).run(suite)


#Bonus Challenge 1
import requests
result = 0
for word in requests.get("https://norvig.com/ngrams/enable1.txt").text.splitlines():
  if check(word) == False:
    result += 1
print(result) #2169