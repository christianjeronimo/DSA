# Makefile for assignment 2

# CXX - compiler, CXXFLAGS - compiler flags
CXX = g++
CXXFLAGS = -Wall -Wextra -pedantic -std=c++23

p2: main.cpp heap.o
	$(CXX) $(CXXFLAGS) $^ -o $@

heap.o: heap.cpp heap.h
	$(CXX) $(CXXFLAGS) -c heap.cpp -o $@

.PHONY: clean
clean:
	rm -f *.o p2
