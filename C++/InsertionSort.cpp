//
//  InsertionSort.cpp
//  
//
//  Created by Jacob Chesslo on 1/29/21.
//

#include <iostream>
#include <ctime>
#include <cstdlib>
using namespace std;

int main(){
    //Seeds RNG once at the start of program
    srand ( time ( NULL ) );
    
    //Initializes n, the size of the array
    int n;
    
    //Asks user how many random numbers from 1 to 1000
    cout << "How many random numbers do you wish to sort? Chose a number between 1 and 1000: ";
    
    //User inputs n, checks if n is in [ 1, 1000 ], loops otherwise
    do{
        //User inputs number
        cin >> n;
        
        //Checks if number is in [ 1, 1000 ]
        if ( ( n < 1 ) || ( n > 1000 ) ){
            //Sends out Error message and chance to enter again
            cout << "Error: please choose a number between 1 and 1000: ";
        }
    } while ( ( n < 1 ) || ( n > 1000 ) );
    
    int arr[n];
    
    for ( int i = 0, i < n, i++ ){
        int j = ( rand () % 1000 ) + 1;
        arr[i] = j;
        cout << arr [i] << " ";
    }
    
    cout << endl;
    
    for ( int j = 2, j < n, j++ ){
        
        key = arr[j];
        
        int i = j - 1;
        
        while ( ( i > 0 ) && ( arr[i] > key ) ){
            arr[i+1] = arr[i];
            i--;
        }
        
        arr[i+1] = key;
    }
    
    for ( int i = 0, i < n, i++ ){
        cout << arr [i] << " ";
    }
    
    return 0;
}
