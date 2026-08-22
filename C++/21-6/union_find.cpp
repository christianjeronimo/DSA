/*
 * @filename union_find.h
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
  return 0;
}

int DisjointSet::num_sets() {
  return 0;
}

bool DisjointSet::union_(int x, int y) {
  return true;
}
