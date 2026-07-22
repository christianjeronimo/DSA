/*
 * Filename LinkedList.cpp
 * Part of Assignment 1 in c++
 * Linked lists, stacks, and queues
 */

#include <iostream>
#include <sstream>
#include "LinkedList.h"

LinkedList::LinkedList() {
  head = nullptr;
  tail = nullptr;
}

LinkedList::~LinkedList() {
  while (!isEmpty()) {
    removeFront();
  }
}

bool LinkedList::isEmpty() {
  return head == nullptr;
}

void LinkedList::insertFront(std::string word) {
  if (word.empty()) {
    return;
  }

  Node* node = new Node(word);

  if (head == nullptr) {
    head = node;
    tail = node;
  } else {
    node->next = head;
    head->prev = node;
    head = node;
  }
}

void LinkedList::insertRear(std::string word) {
  if (word.empty()) {
    return;
  }

  Node* node = new Node(word);

  if (head == nullptr) {
    head = node;
    tail = node;
  } else {
    node->prev = tail;
    tail->next = node;
    tail = node;
  }
}

std::string LinkedList::removeFront() {
  if (head == nullptr) {
    return "";
  }

  std::string data = head->data;
  Node* temp = head;

  if (head == tail) {
    head = nullptr;
    tail = nullptr;
  } else { 
    head = head->next;
    head->prev = nullptr;
  }

  delete temp;
  return data;
  
}

std::string LinkedList::removeRear() {
  if (head == nullptr) {
    return "";
  }

  std::string data = tail->data;
  Node* temp = tail;

  if (head == tail) {
    head = nullptr;
    tail = nullptr;
  } else {
    tail = tail->prev;
    tail->next = nullptr;
  }

  delete temp;
  return data;

}

std::string LinkedList::toString(){
  std::stringstream collect;
  Node* current = head;

  while(current != nullptr) {
    collect << current->data;
    if (current->next != nullptr) {
      collect << " ";
    }
    current = current->next;
  }

  return collect.str();
}
