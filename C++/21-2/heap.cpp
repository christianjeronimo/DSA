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

int MinimumHeap::min_of_3(int i, int left, int right) {
  int minimum = i;
  if (left < size && heap[left] < heap[minimum]) {
    minimum = left;
  }

  if (right < size && heap[right] < heap[minimum]) {
    minimum = right;
  }

  return minimum;
}

void MinimumHeap::heapify(int i) {
  int minimum = min_of_3(i, left(i), right(i));
  if (minimum != i) {
    swap(i, minimum);
    heapify(minimum);
  }
}

void MinimumHeap::swap(int i, int j) {
  std::swap(heap[i], heap[j]);
}

void MinimumHeap::Build_heap() {
  for (int i = size / 2 - 1; i >= 0; --i) {
    heapify(i);
  }
}

void MinimumHeap::decrease_key(int i, int key) {
  if (i < 0 || i >= size) {
    return;
  }

  if (key > heap[i]) {
    return;
  }

  heap[i] = key;

  while (i > 0 && heap[parent(i)] > heap[i]) {
    swap(i, parent(i));
    i = parent(i);
  }
}

bool MinimumHeap::insert(int data){

}

int MinimumHeap::extract_min() {

}

std::pair<int*, int> MinimumHeap::heap_sort() {

}

std::string MinimumHeap::to_string() {

}
