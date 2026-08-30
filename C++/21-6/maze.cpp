/*
 * @filename maze.cpp
 * part of Assignment #6: Amazing Union-Find
 * Maze generation with Disjoint Sets
 */

#include "maze.h"
#include <iostream>
#include <iomanip>
#include <cmath>

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

int Maze::index(int r, int c) {
  if (r < 0 || r >= n || c < 0 || c >= n) {
    return -1;
  }
  
  return r * n + c;
}

void Maze::remove_wall(int r1, int c1, int r2, int c2) {
  int dr = std::abs(r2 - r1);
  int dc = std::abs(c2 - c1);
  
  if (dr + dc != 1) return;

  dr = r2 - r1;
  dc = c2 - c1;

  if (dr == 1) {
    grid[index(r1, c1)] &= ~2;
    grid[index(r2, c2)] &= ~8;
  } else if (dr == -1) {
    grid[index(r1, c1)] &= ~8;
    grid[index(r2, c2)] &= ~2;
  } else if (dc == 1) {
    grid[index(r1, c1)] &= ~1;
    grid[index(r2, c2)] &= ~4;
  } else if (dc == -1) {
    grid[index(r1, c1)] &= ~4;
    grid[index(r2, c2)] &= ~1;
  }
}

void Maze::generate() {
  return;
}

void Maze::print_maze() {
  for (int r = 0; r < n; r++) {
    for (int c = 0; c < n; c++) {
      std::cout << std::hex << grid[index(r, c)];
    }

    std::cout << "\n";
  }

  std::cout << std::dec;
}
