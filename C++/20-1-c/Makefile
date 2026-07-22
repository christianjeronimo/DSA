# Makefile for assignment 1

CXX = g++
CXXFLAGS = -Wall -Wextra -pedantic -std=c++23

p1: main.cpp LinkedList.o stack.o
	$(CXX) $(CXXFLAGS) $^ -o $@

stack.o: stack.cpp stack.h LinkedList.h
	$(CXX) $(CXXFLAGS) -c stack.cpp -o $@

LinkedList.o: LinkedList.cpp LinkedList.h
	$(CXX) $(CXXFLAGS) -c LinkedList.cpp -o $@

.PHONY: clean
clean:
	rm -f *.o p1
