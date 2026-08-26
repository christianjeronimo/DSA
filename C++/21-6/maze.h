/*
 * @filename maze.h
 * part of Assignment #6: Amazing Union-Find
 * Maze generation with Disjoint Sets
 */

#pragma once
#include "union_find.h"

class Maze {
private:
  int n;
  int* grid;
  DisjointSet* sets;
  int index(int r, int c);
  void remove_wall(int r1, int c1, int r2, int c2);
public:
  Maze(int n);
  ~Maze();
  void generate();
  void print_maze();
};
