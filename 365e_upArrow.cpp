#include <cmath>
#include "simpleTest.h"

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