/*
 * Filename stack.h
 * Part of assignment 1
 * Linked Lists, Stacks and Queues
 */

#include "LinkedList.h"
#include <iostream>

class Stack {
private:
  LinkedList list;
public:
  Stack();
  std::string toString();
  void push(std::string word);
  std::string pop();
  bool isEmpty();
};
