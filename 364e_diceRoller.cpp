/* 
CHALLENGE 364
DIFFICULTY: EASY
DND DICE ROLLER
Author: Sam Haynes
Date: 07/12/2018
Original language: Python 3

Fairly straight forward function, however learned to use a lot of my preexisting knowledge in 
getting the input to work properly!
 */





#include <iostream>
#include <cstdlib>
#include <string>

int rollDice(int dice, int sides) {
  int result = 0;
  for(int i = 0; i < dice; i++) {
    result += (rand() % sides) + 1;
  }
  return result;
}

int main() {
  while(true) {
    std::string input;
    std::cout << "Dice to roll: ";
    std::cin >> input;
    std::cout << "Result:    " 
              << rollDice(input[0] - 48, 
                          atoi(input.substr(2, input.length() - 1).c_str())) 
              << std::endl;
  }
}