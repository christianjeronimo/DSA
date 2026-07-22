/*
 * @filename: main.cpp
 * Part of assignment 1
 * Linked Lists, Stacks and Queues
 */

#include <iostream>
#include "stack.h"

int main() {
  Stack stack;
  std::string line;

  while (std::getline(std::cin, line)) {
    stack.push(line);
  }

  while (!stack.isEmpty()) {
    std::cout << stack.pop() << std::endl;
  }

  return 0;
}
