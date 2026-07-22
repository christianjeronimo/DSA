/*
 * @filename stack.cpp
 * Part of Assignment 1 in c++
 * Linked lists, stacks, and queues
 */

#include <iostream>
#include "stack.h"

Stack::Stack() {

}

std::string Stack::toString(){
  return list.toString();
}

void Stack::push(std::string word) {
  list.insertFront(word);
}

std::string Stack::pop() {
  return list.removeFront();
}

bool Stack::isEmpty() {
  return list.isEmpty();
}
