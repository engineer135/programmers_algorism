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
			if (sNum%devideNum == 0) {// 나누어 떨어지는 경우
				divisibleCnt++;
				if (divisibleCnt == devideNumCnt) {// 모든 수가 다 나누어 떨어지는 경우 break
					divisibleNum = sNum;
					break;
				}
			}
			else {// 나누어 떨어지지 않는 경우
				break;
			}
			devideNum++;
		}

		if (divisibleNum > 0) {
			break;
		}
		sNum++;
	}

	printf("나누어 떨어지는 공통 최소값 = %d\n", divisibleNum); //232792560

	// 이건 시간이 좀 걸리긴 하는데 어쨌거나 답이 나오긴 한다.
	// 정답을 봤는데 뭔가 복잡해보인다.
	// 제곱근도 구하고 로그도 구하고 하는거 같은데... 패스한다 -_-;;
	
}