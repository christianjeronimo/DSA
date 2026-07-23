/*
 * @filename heap.h
 * Part of assignment 2: Integer Minimum Heap and Priority queue
 */

#pragma once
#include <iostream>
#include <utility>
#include <string>

class MinimumHeap {
private:
  int* heap;
  int capacity;
  int size;
  int parent(int i);
  int left(int i);
  int right(int i);
  int min_of_3(int i, int left, int right);
  void heapify(int i);
  void swap(int i, int j);
  void build_heap();
public:
  MinimumHeap(int cap);
  ~MinimumHeap();
  void decrease_key(int i, int key);
  bool insert(int data);
  int extract_min();
  std::pair<int*, int> heap_sort();
  std::string to_string();
};
