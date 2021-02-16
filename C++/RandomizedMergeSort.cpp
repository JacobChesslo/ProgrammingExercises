//
//  RandomizedMergeSort.cpp
//  
//
//  Created by Jacob Chesslo on 12/16/20.
//

#include <iostream>
#include <ctime>
#include <cstdlib>
using namespace std;

void merge(int arr[], int l, int m, int r)
{
    int n1 = m - l + 1;
    int n2 = r - m;
 
    // Create temp arrays
    int L[n1], R[n2];
 
    // Copy data to temp arrays L[] and R[]
    for (int i = 0; i < n1; i++)
        L[i] = arr[l + i];
    for (int j = 0; j < n2; j++)
        R[j] = arr[m + 1 + j];
 
    // Merge the temp arrays back into arr[l..r]
 
    // Initial index of first subarray
    int i = 0;
 
    // Initial index of second subarray
    int j = 0;
 
    // Initial index of merged subarray
    int k = l;
 
    while (i < n1 && j < n2) {
        if (L[i] <= R[j]) {
            arr[k] = L[i];
            i++;
        }
        else {
            arr[k] = R[j];
            j++;
        }
        k++;
    }
 
    // Copy the remaining elements of
    // L[], if there are any
    while (i < n1) {
        arr[k] = L[i];
        i++;
        k++;
    }
 
    // Copy the remaining elements of
    // R[], if there are any
    while (j < n2) {
        arr[k] = R[j];
        j++;
        k++;
    }
}

void mergeSort(int A[], int l, int r){
    if ( 1 >= r ){
        return;
    }
    
    int m = ( l + r - 1 ) / 2;
    mergeSort( A, l, m );
    mergeSort( A, m + 1, r );
    merge(A, l, m, r);
    
}

// Prints Array out
void printArray(int A[], int n){
    for ( int i = 0; i < n; i++){
        cout << A[i] << " ";
    }
    cout << endl;
}

/*
// Fills Array with Random Numbers
int * makeArray(int n){
    //Creates an array of size n
    int arr[n];
    
    //Fills array with random numbers,
    for ( int i = 0; i < n; i++){
        
        //Initializes Pseudo-Random Number j in [ 1 , 1000 ]
        int j = ( rand() % 1000 ) + 1;
        
        //Fills ith spot of Pseudo-Random array with j
        arr[i] = j;
    }
    
    //Returns array to main
    return arr;
}
 */

int main(){
    //Seeds RNG Once at start of program
    srand( time( NULL ) );
    
    //Initializes n, the size of the array;
    int n;
    
    //int * ptr; //pointer to hold address of array
    
    //Asks user how many random numbers (from 1 to 1000)
    cout << "How many random numbers do you wish to sort? Choose a number between 1 and 1000: ";
    
    // Inputs n, Checks if n is in [ 1, 1000 ], loops otherwise
    do{
        //User inputs number
        cin >> n;
        
        //Checks if number is in [ 1, 1000 ]
        if ( ( n < 1 ) || ( n > 1000 ) ){
            //Sends out Error message and chance to enter again
            cout << "Error: Please choose a number between 1 and 1000: ";
        }
    } while ( ( n < 1 ) || ( n > 1000 ) );
    
    /*//
    ptr = makeArray(n); //address of
    
    //initializes array of size n
    int arr[n] = makeArray(n);
     */
    
    //Creates an array of size n
    int arr[n];
    
    //Fills array with random numbers,
    for ( int i = 0; i < n; i++){
        
        //Initializes Pseudo-Random Number j in [ 1 , 1000 ]
        int j = ( rand() % 1000 ) + 1;
        
        //Fills ith spot of Pseudo-Random array with j
        arr[i] = j;
    }
    
    cout << "The original array is\n";
    printArray(arr, n);
    
    mergeSort(arr, 0, n - 1);
    
    cout << "The sorted array is\n";
    printArray(arr, n);
    
    return 0;
}
