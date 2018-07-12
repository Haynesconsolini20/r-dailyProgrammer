import unittest

# CHALLENGE 365
# DIFFICULTY: EASY
# KNUTH UP ARROW NOTATION
# Author: Sam Haynes
# Date: 07/12/2018

# This was a tough one, and it took me much longer than I'd like to admit. But a little bit of teamwork
# with my roommate and a good night's sleep made the answer very clear the next morning. The difficult part
# with this one was figuring out how to persist the result value through multiple computations. The key
# turned out to be using it as the exponent, even in the base power case.


def knuth(b, l, n):
  if l == 1:
    return b ** n
  else:
    result = b
    for _ in range(1, n):
      result = knuth(b, l - 1, result)
    return result

class knuthTest(unittest.TestCase):
  def test_oneBang(self):
    self.assertEqual(knuth(2, 1, 4), 16)
  
  def test_twoBangA(self):
    self.assertEqual(knuth(2,2,3), 16)

  def test_twoBangB(self):
    self.assertEqual(knuth(2,2,4), 65536)

  def test_threeBang(self):
    self.assertEqual(knuth(2,3,3), 65536)

  def test_challenge1(self):
    self.assertEqual(knuth(1, 1, 0), 1)

  def test_challenge2(self):
    self.assertEqual(knuth(1,2,0), 1)

  def test_challenge3(self):
    self.assertEqual(knuth(-1, 3, 3), -1)


suite = unittest.TestLoader().loadTestsFromTestCase(knuthTest)
testResult = unittest.TextTestRunner(verbosity=2).run(suite)