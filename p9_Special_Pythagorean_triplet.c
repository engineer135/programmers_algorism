#include <stdio.h>
#include <stdlib.h>

int main(void) {
	/*
	A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

	a2 + b2 = c2
	For example, 32 + 42 = 9 + 16 = 25 = 52.

	There exists exactly one Pythagorean triplet for which a + b + c = 1000.
	Find the product abc.

	연달아 있는 숫자 중에 더해서 1000이 되는 수를 찾는 건가????? 
	그런 수는 없는데...
	아니면 그냥 세숫자 중에 더해서 1000이 되는 걸 찾어???
	그건 너무 많은데...

	위키백과에 따르면
	피타고라스 삼조 = a제곱 + b제곱 = c제곱을 만족시키는 세 양의 정수!!!
	결국 저 세 양의 정수를 구하고, 그 정수의 합이 1000이 되는 수를 찾으면 된다.
	
	*/

	int result = 0, result2 = 0, temp=0, temp2=0, isBreak = 0, a=0, b=0, c=0;
	for (int i = 0; i < 500; i++) {
		isBreak = 0;
		result = i * i;
		//printf("i= %d, result = %d\n", i, result);
		for (int j = 0; j < i; j++) {
			temp = j * j;
			for (int k = j+1; k < i; k++) {
				temp2 = k * k;
				if (temp + temp2 == result) {
					//printf("temp= %d, temp2= %d, sum = %d\n", temp, temp2, temp + temp2);
					//a = j;
					//b = k;
					//isBreak = 1;
					//break;
					// 값을 하나만 찾는게 아니므로 break 하면 안됨.. 여기서 헤맸음. ㅜㅜ

					//printf("a+b+c = %d\n", j+k+i);
					if (j + k + i == 1000) {
						a = j;
						b = k;
						isBreak = 1;
						break;
					}
				}
			}
			if (isBreak)break;
		}

		// 피타고라스 삼조를 만족하는 경우
		if (isBreak) {
			c = i;
			//printf("It's Pythagorean triplet a=%d, b=%d, c=%d\n", a, b, c);
			printf("a,b,c=%d,%d,%d\n", a,b,c);
			printf("a+b+c=%d\n", a + b + c);

			// 세 정수의 합이 1000이면 break
			// 이상하다.. 1000이 되는 케이스가 없다. -_-
			if (a+b+c == 1000) {
				printf("complete!!!"); // 
				break;
			}
		}
	}
	
	return 0;
}