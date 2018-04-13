#include <stdio.h>
#include <stdlib.h>

int checkPalindrome(int no, int noLen) {
	int i = 0, devideNo = 10, isPalindrome = 0;
	int *numbers = (int*)malloc(sizeof(int)*(noLen*2));
	
	for (i = 0; i < (noLen-1)*2; i++) {
		devideNo = devideNo * 10;
	}

	for (i = 0; i < noLen*2; i++) {
		numbers[i] = no / devideNo; // 가장 큰 자릿수 값부터 배열에 차례대로 담는다.
		//printf("%d\n", numbers[i]);
		no = no % devideNo; // 나머지값으로 변경
		devideNo = devideNo / 10; // 자릿수 변경
	}

	// 대칭 값 체크
	for (i = 0; i < noLen; i++) {
		if (numbers[i] == numbers[(noLen*2)-(i+1)]) {
			isPalindrome = 1;
		}
		else {
			isPalindrome = 0;
			break;
		}
	}

	free(numbers);

	return isPalindrome;
}

// 숫자 뒤집는 함수 신박하네 ㅠㅠ
int reverse(int n) {
	//printf("number = %d\n", n);
	int reversed = 0;
	while (n > 0) {
		reversed = (10 * reversed) + (n % 10);
		//printf("reversed = %d\n", reversed);
		n = n / 10;
	}
	return reversed;
}

int isPalindrome(int n) {
	return n == reverse(n) ? 1 : 0;
}

void main(void) {
	/*
	A palindromic number reads the same both ways.The largest palindrome made from the product of two 2 - digit numbers is 9009 = 91 × 99.
	Find the largest palindrome made from the product of two 3 - digit numbers.

	팰린드롬은 좌우 대칭의 숫자나 문자를 말한다.
	세자리의 정수를 곱해서 가장 큰 팰린드롬 수를 찾는 문제!
	아니 이게 겨우 4번 문제라는게 말이 되는건가.. -_-;

	생각해보자.
	세자리 정수 곱해서 나오는 자릿수는 최대 6자리.
	앞3 뒤3이 대칭을 이뤄야 한다.
	패턴을 찾아야한다..

	헐 숫자 뒤집는 거 대박....
	또 한번 좌절감을 느끼고 갑니다.

	*/

	/* answer */
	int largestPalindrome = 0, a=900;
	while (a<=999) {
		int b = 900;
		while (b<=999) {
			if (isPalindrome(a*b) && a*b > largestPalindrome) {
				largestPalindrome = a * b;
			}
			b = b + 1;
		}
		a = a + 1;
	}

	printf("largestPalindrome===%d\n", largestPalindrome);
	return;
	
	/* my anwer */
	int noLen = 3, limit=1000, sNum = 900, max=0, i=0, j=0;	
	for (i = sNum; i < limit; i++) {
		for (j = sNum + 1; j < limit; j++) {
			//printf("%d*%d = %d\n", i, j, i*j);
			// 대칭인지 체크.
			// 기존 최대값보다 크면 담는다.
			if (checkPalindrome(i*j, noLen)) {
				if (i*j > max) {
					max = i * j;
				}
			}
		}
	}
	printf("max==%d\n", max);

}