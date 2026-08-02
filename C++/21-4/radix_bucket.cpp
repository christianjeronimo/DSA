/*
 * @filename radix_bucket.cpp
 * Part of assignment 4
 * Sorting in constant time
 */

#include "radix_bucket.h"
#include <cmath>
#include <vector>

namespace {
  constexpr int digits = 9;

  void rbsort(std::vector<int> &arr) {
    int divisor = 1;
    
    for (int index = 0; index < digits; index++) {
      std::vector<std::vector<int>> buckets(10);

      for (int number : arr) {
	int value = (number / divisor) % 10;
	buckets[value].push_back(number);
      }

      int i = 0;
      for (const auto &bucket : buckets) {
	for (int num : bucket) {
	  arr[i] = num;
	  i++;
	}
      }

      divisor *= 10;       
    }
  }
}

void sort(std::vector<int> &arr) {
  if (!arr.empty()) {
    rbsort(arr);
  }
}
