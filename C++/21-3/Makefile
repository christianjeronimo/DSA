# Makefile for assignment 3

# CXX - compiler, CXXFLAGS - compiler flags
CXX = g++
CXXFLAGS = -Wall -Wextra -pedantic -std=c++23

p3: p3.cpp quicksort.o
	$(CXX) $(CXXFLAGS) $^ -o $@

heap.o: quicksort.cpp quicksort.h
	$(CXX) $(CXXFLAGS) -c quicksort.cpp -o $@

.PHONY: clean
clean:
	rm -f *.o p3
