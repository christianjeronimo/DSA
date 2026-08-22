# Makefile for assignment 5

# CXX - compiler, CXXFLAGS - compiler flags
CXX = g++
CXXFLAGS = -Wall -Wextra -pedantic -std=c++23

p5: p5.cpp hashtable.o
	$(CXX) $(CXXFLAGS) $^ -o $@

hashtable.o: hashtable.cpp hashtable.h
	$(CXX) $(CXXFLAGS) -c hashtable.cpp -o $@

.PHONY: clean
clean:
	rm -f *.o p5
