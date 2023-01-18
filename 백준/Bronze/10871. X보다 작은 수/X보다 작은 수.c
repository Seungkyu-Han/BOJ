#include<stdio.h>

int main()
{
	int N ,X,num;
	scanf("%d %d", &N, &X);

	for (int i = 1; i <= N; i++)
	{
		scanf("%d", &num);
		if (X > num)
			printf("%d\n", num);
	}

	return 0;	

}