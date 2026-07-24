/*
 * @filename main.cpp
 * main file for assignment 2
 * Integer Minimum Heap and Priority Queue
 */

#include "heap.h"
#include <string>
#include <iostream>
#include <utility>

int main() {
  int capacity = 2400000;
  MinimumHeap heap(capacity);
  std::string line;

  while (std::getline(std::cin, line)) {
    try {
      int value = std::stoi(line);

      switch (value) {
      case 0:
	std::cout << heap.to_string() << "\n";
	break;
      case -1:
	std::cout << "extract min: " << heap.extract_min() << "\n";
	break;
      case -2: {
	std::pair<int*, int> result = heap.heap_sort();
	std::cout << "sorted array: [";

	for (int i = 0; i < result.second; ++i) {
	  std::cout << result.first[i];
	  if (i < result.second - 1) {
	    std::cout << ", ";
	  }
	}
	
	std::cout << "]\n";
	
	delete[] result.first;
	break;
      }
      default:
	if (value > 0) {
	  if (heap.insert(value)) {
	    std::cout << "insert: " << value << "\n";
	  }
	}
	
	break;
      }
    }

    catch (const std::invalid_argument&) {
      continue;
    }
  }

  return 0;
}
