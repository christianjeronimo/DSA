/*
 * @filename hashtable.cpp
 * Part of assignment 5
 * Hash table data structure
 */

#include "hashtable.h"
#include <string>
#include <list>
#include <memory>
#include <utility>
#include <cmath>
#include <iostream>
#include <iterator>

HashTable::HashTable(int cap) {
  capacity = cap;
  table = new std::list<std::unique_ptr<Record>>[capacity];
}

HashTable::~HashTable() {
  delete[] table;
}

int HashTable::hash(int key) {
  return 0;
}

std::pair<int, int> HashTable::find(int key) {
  return {0, 0}
}

void HashTable::insert(int key, std::string value) {

}

void HashTable::search(int key) {

}

void HashTable::remove(int key) {

}

void HashTable::clear() {

}
