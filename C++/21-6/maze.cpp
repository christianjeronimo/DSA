/*
 * @filename maze.cpp
 * part of Assignment #6: Amazing Union-Find
 * Maze generation with Disjoint Sets
 */

#include "maze.h"
#include <iostream>
#include <iomanip>

Maze::Maze(int n) : n(n) {
  grid = new int[n * n];
  sets = new DisjointSet(n * n);

  for (int i = 0; i < n * n; i++) {
    grid[i] = 15;
  }

  if (n >= 1) {
    grid[0] = 11;
    grid[n * n - 1] = 14;
  }
}

Maze::~Maze() {
  delete[] grid;
  delete sets;
}

