/*
 * Filename LinkedList.h
 * Part of Assignment 1 in c++
 * Linked lists, stacks, and queues
 */

#pragma once
#include <iostream>
#include <string>

class LinkedList {
private:
  struct Node {
    std::string data;
    Node* next;
    Node* prev;

    Node(std::string d) {
      data = d;
      next = nullptr;
      prev = nullptr;
    }
  };

  Node* head;
  Node* tail;

public:
  LinkedList();
  ~LinkedList();
  bool isEmpty();
  void insertFront(std::string word);
  void insertRear(std::string word);
  std::string removeFront();
  std::string removeRear();
  std::string toString();
};
