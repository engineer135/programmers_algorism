#include <stdio.h>
#include <stdlib.h>

int checkPalindrome(int no, int noLen) {
	int i = 0, devideNo = 10, isPalindrome = 0;
	int *numbers = (int*)malloc(sizeof(int)*(noLen*2));
	
	for (i = 0; i < (noLen-1)*2; i++) {
		devideNo = devideNo * 10;
	}

	for (i = 0; i < noLen*2; i++) {
		numbers[i] = no / devideNo; // ���� ū �ڸ��� ������ �迭�� ���ʴ�� ��´�.
		//printf("%d\n", numbers[i]);
		no = no % devideNo; // ������������ ����
		devideNo = devideNo / 10; // �ڸ��� ����
	}

	// ��Ī �� üũ
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

// ���� ������ �Լ� �Ź��ϳ� �Ф�
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
	A palindromic number reads the same both ways.The largest palindrome made from the product of two 2 - digit numbers is 9009 = 91 �� 99.
	Find the largest palindrome made from the product of two 3 - digit numbers.

	�Ӹ������ �¿� ��Ī�� ���ڳ� ���ڸ� ���Ѵ�.
	���ڸ��� ������ ���ؼ� ���� ū �Ӹ���� ���� ã�� ����!
	�ƴ� �̰� �ܿ� 4�� ������°� ���� �Ǵ°ǰ�.. -_-;

	�����غ���.
	���ڸ� ���� ���ؼ� ������ �ڸ����� �ִ� 6�ڸ�.
	��3 ��3�� ��Ī�� �̷�� �Ѵ�.
	������ ã�ƾ��Ѵ�..

	�� ���� ������ �� ���....
	�� �ѹ� �������� ������ ���ϴ�.

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
			// ��Ī���� üũ.
			// ���� �ִ밪���� ũ�� ��´�.
			if (checkPalindrome(i*j, noLen)) {
				if (i*j > max) {
					max = i * j;
				}
			}
		}
	}
	printf("max==%d\n", max);

}