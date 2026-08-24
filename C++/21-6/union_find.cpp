/*
 * @filename union_find.cpp
 * part of Assignment #6: Amazing Union-Find
 * Maze generation with Disjoint Sets
 */

#include "union_find.h"

DisjointSet::DisjointSet(int size) : size(size), sets(size) {
  rank = new int[size];
  parent = new int[size];

  for (int i = 0; i < size; i++) {
    rank[i] = 0;
    parent[i] = i;
  }
}

DisjointSet::~DisjointSet() {
  delete[] rank;
  delete[] parent;
}

void DisjointSet::link(int x, int y) {
  if (x == y) return;

  if (rank[x] > rank[y]) {
    parent[y] = x;
  } else {
    parent[x] = y;
    if (rank[x] == rank[y]) {
      rank[y]++;
    }
  }
}

int DisjointSet::find(int x) {
  if (x < 0 || x >= size) {
    return -1;
  }

  if (x != parent[x]) {
    parent[x] = find(parent[x]);
  }
  
  return parent[x];
}

int DisjointSet::num_sets() {
  return sets;
}

bool DisjointSet::union_(int x, int y) {
  if (x < 0 || x >= size || y < 0 || y >= size) {
    return false;
  }

  int root_x = find(x);
  int root_y = find(y);

  if (root_x == root_y) {
    return false;
  }

  link(root_x, root_y);
  sets--;
  return true;
}
