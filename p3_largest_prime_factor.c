#include <stdio.h>

/*
typedef enum _boolean {
	FALSE,
	TRUE
} boolean;

// �Ҽ����� üũ
boolean checkPrimeFactor(long long num) {
	for (long long i = num / 2; i > 2; i--) {
		if (num % i == 0) {// ������ �������� ���� �ִٸ�, ����� �ִٴ� ����̹Ƿ� �Ҽ��� �ƴ�.
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

	// 2���� (�ڱ��ڽ�/2)������ üũ�ϸ� �ȴ�. ����� (�ڱ��ڽ�/2)���� Ŭ �� ���� �����̴�.
	// ���� ū ����� ã���� �ȴ�.
	for (long long i = num/2; i > 2; i--) {
	printf("%lld\n", i);
	//printf("num % i === %lld\n", (num % i));
	if (num % i == 0) {
	printf("��� %lld\n", i);
	// �Ҽ����� üũ
	if(checkPrimeFactor(i)) {
	printf("�Ҽ� ���� %lld\n", i);
	num = i; // �Ҽ� ��´�.
	break;
	}
	}
	else {
	//printf("��� �ƴ� %lld\n", i);
	}
	}

	printf("largest prime factor === %lld\n", num);
	*/

	/*
	�Ʒ� ������ �̿��ؼ� �˰��� �ٽ� §��...
	10 �� ���
	2 5 10

	10%2 = 0
	5%2 = 1
	5%3 = 2
	5%4 = 1
	5%5 = 0

	1 ��
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

	printf("largestPrimeFactor : %lld\n", largestPrimeFactor); // 6857 �� ���...........
	// �̰� difficulty�� 5%�� ������ � ������ ���´ٴ°��� �Ф�

	printf("end\n");

}