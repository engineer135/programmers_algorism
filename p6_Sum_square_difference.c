#include <stdio.h>

int main(void) {
	/*
	The sum of the squares of the first ten natural numbers is,

	12 + 22 + ... + 102 = 385 
	1~10까지 제곱을 더한다.
	The square of the sum of the first ten natural numbers is,

	(1 + 2 + ... + 10)2 = 552 = 3025
	1~10까지 더한 후 제곱을 구한다.
	Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

	Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
	*/

	int square = 0, sum = 0;
	for (int i = 1; i <= 100; i++) {
		square = square + (i * i);
		sum = sum + i;
	}
	printf("%d\n", square);
	printf("%d\n", sum * sum);
	printf("%d\n", (sum * sum) - square); //25164150 너무 쉬운데...???
	return 0;
}