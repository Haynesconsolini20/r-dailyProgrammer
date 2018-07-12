#include <cmath>
#include "simpleTest.h"
/**************************************************************************************************************
*CHALLENGE 365
*DIFFICULTY: EASY
*KNUTH UP ARROW NOTATION
*Author: Sam Haynes
*Date: 07/12/2018
*Original language: Python 3
*
*This was a tough one, and it took me much longer than I'd like to admit. But a little bit of teamwork
*with my roommate and a good night's sleep made the answer very clear the next morning. The difficult part
*with this one was figuring out how to persist the result value through multiple computations. The key
*turned out to be using it as the exponent, even in the base power case.
***************************************************************************************************************/
long knuth(long base, long level, long n) {
  if (level == 1)
    return pow(base, n);
  else {
    long result = base;
    for (int i = 0; i < n - 1; i++)
      result = knuth(base, level - 1, result);
    return result;
  }
}


int main() {
  assertEquals(knuth(2,1,4), (long)16, "2 ^ 4");
  assertEquals(knuth(2,2,3), (long)16, "2 ^^ 3");
  assertEquals(knuth(2,2,4), (long)65536, "2 ^^ 4");
  assertEquals(knuth(2,3,3), (long)65536, "2 ^^^ 3");
  assertEquals(knuth(1, 1, 0), (long)1, "1 ^ 1");
  assertEquals(knuth(1,2,0), (long)1, "1 ^^ 0");
  assertEquals(knuth(-1, 3, 3), (long)-1, "-1 ^^^ 3");
  return 0;
}