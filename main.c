#include <stdio.h>
#include "average.h"

//I added calculation and print of the average of 1.0, 2.0, and 3.0

int main() {
    double arr[] = {1.0, 2.0, 3.0, 4.0};

    double result = average(4, arr);
    double result2 = average(3, arr);

    printf("The average of 1, 2, 3 and 4 is: %.4f\n", result);
    printf("The average of 1, 2 and 3 is: %.4f\n", result2);

    return 0;    
}

