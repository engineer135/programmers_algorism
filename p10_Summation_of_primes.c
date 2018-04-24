#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>
#include <string.h>

int main(void) {
	/*
	The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
	Find the sum of all the primes below two million.
	*/

	printf("start...");

	clock_t before;
	double result;
	before = clock();

	unsigned long long sum = 0;
	/* 이게 내가 짠 소스 */
	/*
	for (int i = 5; i < 2000000; i++) {
		for (int j = 2; j <= i/2; j++) {
			//printf("i, j %d, %d\n", i, j);
			if (i%j == 0) {
				//printf("not a prime number! %d\n", i);
				break;
			}
			if (i%j != 0 && j == i/2) {
				//printf("prime number! %d\n", i);
				sum += i;
				break;
			}
		}
	}
	*/

	/* optimizing the sieve 라는.. 소수 구할때 가장 빠른? 알고리즘이라는데.. 잘 안된다. 일단 github 올려놓고 좀 더 보자. */
	printf("%f\n",sqrt(10));

	int limit = 20;
	int sievebound = (limit - 1) / 2; // last index of sieve
	int *sieve = malloc(sizeof(int) * sievebound); //동적할당
	memset(sieve, 0, sizeof(int) * sievebound); // 0으로 초기화
	int crosslimit = (sqrt(limit) - 1) / 2;

	printf("sievebound %d\n", sievebound);
	printf("crosslimit %d\n", crosslimit);

	for (int i = 1; i < crosslimit; i += 2) {
		printf("i %d\n", i);
		if (!sieve[i]) { // 2*i+1 is prime. mark multiples
			printf("sieve[i] %d\n", sieve[i]);
			for (int j = 2 * i*(i + 1); j < sievebound; j = 2 * i + 1) {
				printf("j %d\n", j);
				sieve[j] = 1; // true
			}
		}
	}
	sum = 2;
	for (int i = 0; i < sievebound; i++) {
		printf("i %d\n", i);
		printf("sieve[i] %d\n", sieve[i]);
		if (!sieve[i]) {
			sum = sum + (2 * i + 1);
		}
	}

	printf("prime number sum %lld\n", sum); // 142913828917
	// 여기에 준소수인 2와 3을 더하면 
	// 142913828922

	result = (double)(clock() - before) / CLOCKS_PER_SEC;
	printf("걸린시간은 %5.2f 입니다\n", result); // 470.66 초...

	free(sieve);

	return 0;
}