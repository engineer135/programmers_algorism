#include <stdio.h>

void main(void) {
	/*
	2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
	What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
	*/

	//int sNum = 10, devideNum = 2, devideNumCnt = 9, divisibleCnt = 0, divisibleNum = 0;
	int sNum = 20, devideNum = 2, devideNumCnt = 19, divisibleCnt = 0, divisibleNum = 0;
	while (1) {
		//printf("%d\n", sNum);
		divisibleCnt = 0;
		devideNum = 2;
		while (devideNum <= sNum) {
			if (sNum%devideNum == 0) {// ������ �������� ���
				divisibleCnt++;
				if (divisibleCnt == devideNumCnt) {// ��� ���� �� ������ �������� ��� break
					divisibleNum = sNum;
					break;
				}
			}
			else {// ������ �������� �ʴ� ���
				break;
			}
			devideNum++;
		}

		if (divisibleNum > 0) {
			break;
		}
		sNum++;
	}

	printf("������ �������� ���� �ּҰ� = %d\n", divisibleNum); //232792560

	// �̰� �ð��� �� �ɸ��� �ϴµ� ��·�ų� ���� ������ �Ѵ�.
	// ������ �ôµ� ���� �����غ��δ�.
	// �����ٵ� ���ϰ� �α׵� ���ϰ� �ϴ°� ������... �н��Ѵ� -_-;;
	
}