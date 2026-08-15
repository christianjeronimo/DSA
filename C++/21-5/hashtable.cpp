/*
 * @filename hashtable.cpp
 * Part of assignment 5
 * Hash table data structure
 */

#include "hashtable.h"
#include <string>
#include <list>
#include <memory>
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
  double part = (key * c) - static_cast<int>(key * c);
  return static_cast<int>(capacity * part);
}

void HashTable::insert(int key, std::string value) {
  int index = hash(key);
  table[index].push_back(std::make_unique<Record>(key, value));
}

void HashTable::search(int key) {
  int bucket_idx = hash(key);
  auto &target_list = table[bucket_idx];

  for (auto it = target_list.begin(); it != target_list.end(); ++it) {
    if ((*it)->key == key) {
      std::cout << "Found: " << (*it)->key << " " << (*it)->value << "\n";
      return;
    }
  }

  std::cout << "Search not found: " << key << "\n";
}

void HashTable::remove(int key) {
  int bucket_idx = hash(key);
  auto &target_list = table[bucket_idx];

  for (auto it = target_list.begin(); it != target_list.end(); ++it) {
    if ((*it)->key == key) {
      std::cout << "Delete: " << (*it)->key << " " << (*it)->value << "\n";
      target_list.erase(it);
      return;
    }
  }

  std::cout << "Delete not found: " << key << "\n";
}

void HashTable::clear() {
  for (int i = 0; i < capacity; i++) {
    auto &curr_list = table[i];
    curr_list.clear();
  }
}
