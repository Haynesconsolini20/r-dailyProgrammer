/*******************************************************************
 * SIMPLE_TEST_H
 * A collection of functions for basic testing without heavy libraries
 * ******************************************************************/

#ifndef SIMPLE_TEST_H
#define SIMPLE_TEST_H
#include <iostream>
template<class T>
void assertEquals(T input, T expected, std::string testName) {
  std::cout << "Running test " << testName << "...";
  if (input == expected)
    std::cout << "SUCCESS\n";
  else 
    std::cout << "FAILURE\n";
}
#endif