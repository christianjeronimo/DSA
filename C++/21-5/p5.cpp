/*
 * @filename p5.cpp
 * Main function for the hashtable dataset
 */

#include "hashtable.h"
#include <iostream>
#include <string>
#include <fstream>
#include <cctype>

void load_file(const std::string &filename, HashTable &hashtable) {
  std::ifstream file(filename);
  if (!file.is_open()) {
    std::cout << "File not found.\n";
    return;
  }

  std::string line;
  while (std::getline(file, line)) {
    if (line.empty()) continue;
    size_t space_pos = line.find(' ');
    if (space_pos != std::string::npos) {
      std::string key_str = line.substr(0, space_pos);
      std::string value = line.substr(space_pos + 1);
      bool is_digit = true;
      for (char c : key_str) {
	if (!isdigit(c)) {
	  is_digit = false;
	  break;
	}
      }

      if (is_digit && key_str.length() == 9) {
	int key = std::stoi(key_str);
	hashtable.insert(key, value);
      }
    }
  }
}

int main() {
  HashTable hashtable(178000);
  std::string choice;

  while (true) {
    std::cout << "(1)load (2)insert (3)delete (4)search (5)clear (6)save "
	      << "(7)quit -- Your choice? ";
    std::getline(std::cin, choice);
    int num = 0;
    try {
      num = std::stoi(choice);
    } catch (...) {
      std::cout << "Invalid choice.\n";
      continue;
    }
    switch (num) {
    case 1: {
      std::cout << "read hash table - filename?  ";
      std::string filename;
      std::getline(std::cin, filename);
      load_file(filename, hashtable);
      break;
    }
    case 2: {
      std::cout << "Input new record: \n";
      std::string line;
      std::getline(std::cin, line);

      size_t space_pos = line.find(' ');
      if (space_pos != std::string::npos) {
	std::string key_str = line.substr(0, space_pos);
	std::string value = line.substr(space_pos + 1);

	bool is_digit = true;
	for (char c : key_str) {
	  if (!isdigit(c)) is_digit = false;
	}

	if (is_digit && key_str.length() == 9) {
	  int key = std::stoi(key_str);
	  hashtable.insert(key, value);
	} else {
	  std::cout << "invalid key format.\n";
	}
      }

      break;
    }
    case 3: {
      std::cout << "delete record - key? ";
      std::string key_str;
      std::getline(std::cin, key_str);
      try {
	int key = std::stoi(key_str);
		hashtable.remove(key);
      } catch (...) {
	std::cout << "invalid key input.\n";
      }

      break;
    }
    case 4: {
      std::cout << "search for record - key? ";
      std::string key_str;
      std::getline(std::cin, key_str);
      try {
	int key = std::stoi(key_str);
	hashtable.search(key);
      } catch (...) {
	std::cout << "invalid key input.\n";
      }

      break;
    }
    case 5: {
      hashtable.clear();
      std::cout << "Clearing hash table.\n";
      break;
    }
    case 6: {
      std::cout << "Write hash table - filename? ";
      std::string filename;
      std::getline(std::cin, filename);
      hashtable.save(filename);
      break;
    }
    case 7: {
      return 0;
    }
    default: {
      std::cout << "Invalid choice. Please select 1-7.\n";
      break;
    }
    }
  }
}
