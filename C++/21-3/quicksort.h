/*
 * @filename quicksort.h
 * Part of assignment 3
 * quicksort class object
 */

#pragma once
#include <iostream>
#include <vector>

class QuickSort {
private:
  std::vector<int> arr;
  int mo3_value;
  int median_of_three(int left, int right);
  int lomuto_partition(int left, int right);
  void quick_sort(int left, int, right);
 public:
  QuickSort(std::vector<int>, int mo3);
  void sort();
};
