/*
 * @filename quicksort.cpp
 * Part of assignment 3
 */

#include "quicksort.h"
#include <vector>
#include <algorithm>

namespace {
  constexpr int mo3_value = 15;
  
  int median_of_three(std::vector<int> &arr, int left, int right) {
    int middle = left + (right - left) / 2;
    int a = arr[left];
    int b = arr[middle];
    int c = arr[right];

    if ((a < b && b < c) || (c < b && b < a)) {
      return middle;
    } else if ((b < a  && a < c) || (c < a && a < b)) {
      return left;
    } else {
      return right;
    }
  }

  int lomuto_partition(std::vector<int> &arr, int left, int right) {
    int pivot;
    
    if ((right - left + 1) > mo3_value) {
      int mid = median_of_three(arr, left, right);
      std::swap(arr[mid], arr[right]);
      pivot = arr[right];
    } else {
      pivot = arr[right];
    }

    int i = left - 1;
    for (int j = left; j < right; j++) {
      if (arr[j] < pivot) {
	i++;
	std::swap(arr[i], arr[j]);
      }
    }

    std::swap(arr[i + 1], arr[right]);
    return i + 1;
  }

  void quicksort(std::vector<int> &arr, int left, int right) {
    if (left < right) {
      int pivot_index = lomuto_partition(arr, left, right);
      quicksort(arr, left, pivot_index - 1);
      quicksort(arr, pivot_index + 1, right);
    }
  }
}

void sort(std::vector<int> &arr) {
  if (!arr.empty()) {
    quicksort(arr, 0, arr.size() - 1);
  }
}
