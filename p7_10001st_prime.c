#include <stdio.h>

int main(void) {
	/*
	By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

	What is the 10001st prime number?

	10001번째 소수를 찾는 문제.

	전에 썼던 함수를 응용해서 써보자.

	12 약수
	1 2 3 4 6 12
	이 중에 소수는 
	2 3
	아 지금은 목표값(12)이 없구나. 
	그냥 소수의 나열만 필요하네.
	*/

	int num = 2; // 2부터 체크 시작..
	int primeFactor = 0, factorCnt = 0;
	for (int i = 2; factorCnt < 10001; i++) {
		//printf("%d\n", i);
		// 나누어 떨어지는 경우
		if (num%i == 0) {
			if (i == num) {// 나누어 떨어진 수가 자기자신과 같다면, 소수.
				//printf("I am a prime facotr = %d\n", num);
				factorCnt++;
				if (num > primeFactor) {
					primeFactor = num;
				}
			}
			else { // 소수가 아닌 경우 다음 수 체크
				//printf("I am not a prime facotr = %d\n", num);
			}
			num++; // 다음 수로 넘어간 다음..
			i = 1; // 2부터 다시 나누기 해본다.
		}
		// 나누어 떨어지지 않는 경우 떨어질때까지 i++ 하면서 나눠본다. 자기자신이 나올때까지 루프문이 돈다면, 그 수는 소수임.
		// 그런식으로 소수를 계속 찾아낸다.
	}
	

	printf("%d\n", factorCnt);
	printf("%d\n", primeFactor); //104743

	return 0;
}