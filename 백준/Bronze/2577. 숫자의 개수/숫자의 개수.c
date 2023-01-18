#include <stdio.h>

int main()
{
	int A, B, C;
	scanf("%d %d %d", &A, &B, &C);
	int n[10] = { 0 };
	int Num;
	int i;
	Num = A * B * C;
	while (Num != 0)
	{
		n[Num % 10]++;
		Num = Num / 10;
	}
	for (i = 0; i < 10; i++)
	{
		printf("%d\n", n[i]);
	}
	return 0;
}