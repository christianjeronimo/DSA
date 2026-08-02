# Makefile for asignment 4

# CXX - compiler, CXXFLAGS - compiler flags
CXX = g++
CXXFLAGS = -Wall -Wextra -pedantic -std=c++23

p4: p4.cpp radix_bucket.o
	$(CXX) $(CXXFLAGS) $^ -o $@

radix_bucket.o: radix_bucket.cpp radix_bucket.h
	$(CXX) $(CXXFLAGS) -c radix_bucket.cpp -o $@

.PHONY: clean
clean:
	rm -f *.o p4
