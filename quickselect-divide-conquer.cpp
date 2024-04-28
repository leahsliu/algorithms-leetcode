// Instructions:
// - to run this file, open terminal and locate to directory where quickselect-divide-conquer.cpp is contained
// - run `g++ -std=c++11 quickselect-divide-conquer.cpp`
// - run `./a.out` to see output of program


// Problem: Given an integer array nums and an integer k, return the k most
//          frequent elements and how many times the elements have appeared.

#include <iostream>
#include <fstream>
#include <string>

const int MAX_NUMBER = 200;
const int NUM_FILE = 10000;

int* counts = new int[MAX_NUMBER + 1]();
int* indices = new int[MAX_NUMBER + 1];

void count (int nums[], int left, int right) {
    for (int i = 0; i < NUM_FILE; i++) {
        counts[nums[i]]++;
    }
    // Alternate soln: 
    // if (left > right) return;

    // if (left == right) {
    //     counts[nums[left]] += 1;
    //     return;
    // }
    
    // int partition = (left + right) / 2;
    // count(nums, left, partition);
    // count(nums, partition + 1, right);
}

int* readNumbersFromFile(const std::string& filename) {
    int* nums = new int[NUM_FILE];
    int number;
    int n = 0;
    std::ifstream file(filename);

    while (file >> number) {
        nums[n++] = number;
    }

    file.close();

    return nums;
}



void quickSelect(int frequencies[], int left, int right, int k) {
    if (left >= right) return;

    int pivotIndex = (left + right) / 2;
    int pivotValue = frequencies[pivotIndex];
    std::swap(frequencies[pivotIndex], frequencies[right]);
    std::swap(indices[pivotIndex], indices[right]);


    int storeIndex = left;
    for (int i = left; i <= right - 1; i++) {
        if (frequencies[i] > pivotValue) {
            std::swap(frequencies[i], frequencies[storeIndex]);
            std::swap(indices[i], indices[storeIndex]);

            storeIndex++;
        }
    }

    std::swap(frequencies[storeIndex], frequencies[right]);
    std::swap(indices[storeIndex], indices[right]);
    if (storeIndex == k) return;
    else if (storeIndex < k) quickSelect(frequencies, storeIndex + 1, right, k);
    else quickSelect(frequencies, left, storeIndex - 1, k);

    return;
}

int countUniqueNumbers() {
    int uniqueCount = 0;
    for (int i = 0; i <= MAX_NUMBER; i++) {
        if (counts[i] != 0) uniqueCount++;
    }
    return uniqueCount;
}

int main() {
    // O(n) time to get all numbers from txt file
    int* fileNums = readNumbersFromFile("hw4_10000Numbers_1to200.txt");

    for (int i = 0; i <= MAX_NUMBER; i++) {
        indices[i] = i;
    }
    

    int k;
    std::cout << "Type a number for k: ";
    std::cin >> k;
    count(fileNums, 0, NUM_FILE - 1);

    int numUnique = countUniqueNumbers();

    std::cout << "Counts array: " << std::endl;
    for (int i = 0; i <= MAX_NUMBER; i++)  {
        std::cout << counts[i] << " ";
    }
    std::cout << std::endl;

    // Handle improper k values
    if (k < 1 || k > numUnique) {
        std::cout << "Invalid value of k: " << k << ". It should be between 1 and " << numUnique << "." << std::endl;
        delete[] counts;
        
        return 1;
    }

    quickSelect(counts, 0, MAX_NUMBER+1, k);



    std::cout << "The top " << k << " frequencies are: " << std::endl;
    for (int i = 0; i < k; i++) {
        std::cout << "Number: " << indices[i] << " \t Frequency: " << counts[i] << std::endl;;
    }

    std::cout << std::endl;

    return 0;
}