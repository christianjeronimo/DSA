/*
 * @filename hashtable.h
 * Part of assignment 5
 * Hash table data structure
 */

#pragma once
#include <string>
#include <list>
#include <memory>
#include <utility>

class HashTable {
private:
  struct Record {
    int key;
    std::string value;
    Record(int k, std::string v) : key(k), value(v)  {}
  };

  int capacity;
  const double c = 0.618034;
  std::list<std::unique_ptr<Record>>* table;
  int hash(int key);
  std::pair<int, int> find(int key);
public:
  HashTable(int cap = 100);
  ~HashTable();
  void insert(int key, std::string value);
  void search(int key);
  void remove(int key);
  void clear();
};
