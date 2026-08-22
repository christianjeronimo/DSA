/*
 * @filename union_find.h
 * part of Assignment #6: Amazing Union-Find
 * Maze generation with Disjoint Sets
 */

#pragma once

class DisjointSet {
private:
  int* rank;
  int* parent;
  int size;
  int sets;
  void link(int x, int y);
public:
  DisjointSet(int size);
  ~DisjointSet();
  int find(int x);
  int num_sets();
  bool union_(int x, int y);
};
