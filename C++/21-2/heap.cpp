/*
 * @filename heap.cpp
 * part of Assignment 2
 * Integer Minimum Heap and Priority Queue
 */

#include "heap.h"
#include <string>
#include <utility>

MinimumHeap::MinimumHeap(int cap) {
  capacity = cap;
  size = 0;
  heap = new int[cap];
}

MinimumHeap::~MinimumHeap() {
  delete[] heap;
}

int MinimumHeap::parent(int i) {
  return ((i - 1) / 2);
}

int MinimumHeap::left(int i) {
  return ((2 * i) + 1);
}

int MinimumHeap::right(int i) {
  return ((2 * i) + 2);
}

