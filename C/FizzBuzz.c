//
//  FizzBuzz.c
//  
//
//  Created by Jacob Chesslo on 12/14/20.
//

#include <stdio.h>

int main(){

    for (int i = 1; i <= 100; ++i) {
        if ( ( i % 3 == 0 ) && ( i % 5 == 0) )
            printf("FizzBuzz\n");
        else if ( ( i % 3 == 0 ) && ( i % 5 != 0) )
            printf("Fizz\n");
        else if ( ( i % 3 != 0 ) && ( i % 5 == 0) )
            printf("Buzz\n");
        else
            printf("%d\n", i);
    }
    
    return 0;
}
