/*
 * @filename p3.cpp
 * Main function for the quicksort algorithm
 * https://stackoverflow.com/questions/17543883/correctly-pad-negative-integers-with-zeros-with-stdcout
 */

#include "quicksort.h"
#include <iostream>
#include <iomanip>

int main() {
  std::vector<int> arr;
  int num;
  
  while (std::cin >> num) {
    arr.push_back(num);
  }

  sort(arr);

  for (int val : arr) {
    std::cout << std::internal << std::setfill('0') << std::setw(9) << val << "\n";
  }

  return 0;
}
