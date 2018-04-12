#include <stdio.h>

/*
typedef enum _boolean {
	FALSE,
	TRUE
} boolean;

// 소수인지 체크
boolean checkPrimeFactor(long long num) {
	for (long long i = num / 2; i > 2; i--) {
		if (num % i == 0) {// 나누어 떨어지는 수가 있다면, 약수가 있다는 얘기이므로 소수가 아님.
			return FALSE;
		}
	}
	return TRUE;
}
*/

void main(void) {
	/*
	The prime factors of 13195 are 5, 7, 13 and 29.
	What is the largest prime factor of the number 600851475143 ?
	*/

	printf("start\n");

	/*
	boolean isPrimeFactor = FALSE;
	long long num = 313;

	// 2부터 (자기자신/2)까지만 체크하면 된다. 약수는 (자기자신/2)보다 클 수 없기 때문이다.
	// 제일 큰 약수만 찾으면 된다.
	for (long long i = num/2; i > 2; i--) {
	printf("%lld\n", i);
	//printf("num % i === %lld\n", (num % i));
	if (num % i == 0) {
	printf("약수 %lld\n", i);
	// 소수인지 체크
	if(checkPrimeFactor(i)) {
	printf("소수 맞음 %lld\n", i);
	num = i; // 소수 담는다.
	break;
	}
	}
	else {
	//printf("약수 아님 %lld\n", i);
	}
	}

	printf("largest prime factor === %lld\n", num);
	*/

	/*
	아래 성질을 이용해서 알고리즘 다시 짠다...
	10 의 약수
	2 5 10

	10%2 = 0
	5%2 = 1
	5%3 = 2
	5%4 = 1
	5%5 = 0

	1 끝
	*/

	long long num = 600851475143;
	long long largestPrimeFactor = 0;
	for (long long i = 2; i <= num; i++) {
		if (num%i == 0) {
			//printf("%d\n", i);
			largestPrimeFactor = i;
			num = num / i;
			i = i - 1;
		}
	}

	printf("largestPrimeFactor : %lld\n", largestPrimeFactor); // 6857 헐 대박...........
	// 이게 difficulty가 5%면 앞으로 어떤 문제가 나온다는건지 ㅠㅠ

	printf("end\n");

}