#include <iostream>

using namespace std;

void staircase(int n) {
    //Line
    
    
    for(int i = 1; i <= n; i++){
        //Elements in Line
        if(i == n){      //Prints without Line, spaces (line)
           
            for(int j = 0; j < i; j++){
                cout << "#";
            }
            
        } else {        //Prints with newline and space (all except last line)
            //Prints n - i spaces
            for(int j = 0; j < (n-i); j++){
                cout << " ";
            }
            //Prints i characters
            for(int j = 0; j < i; j++){
                cout << "#";
            }
            cout << endl;   //Endline for ith line
        }
    }
}

int main()
{
    int n;
    cin >> n;
    staircase(n);
    return 0;
}
