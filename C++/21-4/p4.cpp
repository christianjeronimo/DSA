/*
 * @filename p4.cpp
 * Main function for the hybrid radic_bucket algorithm
 */

#include "radix_bucket.h"
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
