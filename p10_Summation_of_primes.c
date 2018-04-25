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

	printf("start...\n");

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

	/* The sieve of Eratosthenes */
	/* 오 진짜 된다... 0.05초 걸림... 신비한 수학의 세계 ㅠㅠ */
	int limit = 2000000;
	int crosslimit = sqrt(limit); // limit의 제곱근까지만 계산하면 됨. 9의 제곱근은 3.. 9의 약수중에 가장 큰 수는 3임. 그러니까 오케이?
	int *sieve = malloc(sizeof(int)*limit); // limit만큼 동적할당
	memset(sieve, 0, sizeof(int) * limit); // 0으로 초기화

	printf("crosslimit===%d\n", crosslimit);
	for (int n = 2; n < limit; n += 2) { // 2로 나눠지는 수들은 소수가 안되니까 1로 바꿔주는 거 같음.
										 //printf("n===%d\n", n);
		sieve[n] = 1;
	}
	for (int n = 3; n <= crosslimit; n += 2) {
		if (!sieve[n]) {// n번째 sieve 배열 값이 0일때만 타도록.. 즉 2로 나눠 떨어지는 수가 아닐때만.
			for (int m = n * n; m <= limit; m = m + (2 * n)) {// ... ㅇ_ㅇ;; n값은 3, 5, 7등일텐데.. 그 배수들도 소수가 될 수 없으므로 1로 바꿔주는듯????
															  //printf("m===%d\n", m);
				sieve[m] = 1;
			}
		}
	}

	for (int n = 2; n < limit; n++) {
		if (!sieve[n]) {// 0인 애들은 소수임. 더하자.
						//printf("sieve[%d]==%d\n", n, sieve[n]);
			sum += n;
		}
	}
	sum = sum + 2; // 소수 2를 더해준다. 완료.



				   /* optimizing the sieve 라는.. 소수 구할때 가장 빠른? 알고리즘이라는데.. 잘 안된다. 일단 github 올려놓고 좀 더 보자. */
				   /* 위에 있는 식을 좀 더 최적화한 거라는데.. 대단들하다. 위에것도 충분한 거 같은데 이걸 또 최적화하겠다고.... 근데 잘 안된다. 식이 틀린거 같은데 뭐가 틀린지 모르겠다는 -_- */
				   /*
				   int limit = 10;
				   int sievebound = (limit - 1) / 2; // last index of sieve
				   int *sieve = malloc(sizeof(int) * sievebound); //동적할당
				   memset(sieve, 0, sizeof(int) * sievebound); // 0으로 초기화
				   int crosslimit = (sqrt(limit) - 1) / 2;

				   printf("sievebound %d\n", sievebound);
				   printf("crosslimit %d\n", crosslimit);

				   for (int i = 1; i <= crosslimit; i++) {
				   printf("i %d\n", i);
				   if (!sieve[i]) { // 2*i+1 is prime. mark multiples
				   printf("sieve[i] %d\n", sieve[i]);
				   for (int j = 2 * i*(i + 1); j <= sievebound; j = j + (2 * i + 1)) {
				   printf("j %d\n", j);
				   sieve[j] = 1; // true
				   }
				   }
				   }
				   sum = 2;
				   for (int i = 0; i < sievebound; i++) {
				   //printf("i %d\n", i);
				   //printf("sieve[i] %d\n", sieve[i]);
				   if (!sieve[i]) {
				   sum = sum + (2 * i + 1);
				   }
				   }
				   */

	printf("prime number sum %lld\n", sum); // 142913828917
											// 여기에 준소수인 2와 3을 더하면 
											// 142913828922

	result = (double)(clock() - before) / CLOCKS_PER_SEC;
	printf("걸린시간은 %5.2f 입니다\n", result); // 470.66 초...

	free(sieve);

	return 0;
}