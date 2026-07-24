/*
 * @filename heap.cpp
 * part of Assignment 2
 * Integer Minimum Heap and Priority Queue
 */

#include "heap.h"
#include <string>
#include <utility>
#include <algorithm>
#include <sstream>
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

void MinimumHeap::build_heap() {
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
  if (size == capacity) {
    return false;
  }

  int i = size;
  heap[i] = data;
  size++;
  decrease_key(size - 1, data);
  return true;
}

int MinimumHeap::extract_min() {
  if (size == 0) {
    return 0;
  }

  int min_value = heap[0];
  heap[0] = heap[size - 1];
  --size;
  heapify(0);
  return min_value;
}

std::pair<int*, int> MinimumHeap::heap_sort() {
  int* sorted_arr = new int[size];
  std::copy(heap, heap + size, sorted_arr);

  int* original_heap = heap;
  int original_size = size;
  heap = sorted_arr;

  for (int i = size - 1; i > 0; --i) {
    swap(0, i);
    size--;
    heapify(0);
  }

  heap = original_heap;
  size = original_size;

  return std::make_pair(sorted_arr, original_size);
  
}

std::string MinimumHeap::to_string() {
  std::stringstream content;
  content << "heap size " << size << ": ";

  for (int  i = 0; i < size; i++) {
    content << heap[i];

    if (i < size - 1) {
      content << ", ";
    }
  }
  
  return content.str();
}
