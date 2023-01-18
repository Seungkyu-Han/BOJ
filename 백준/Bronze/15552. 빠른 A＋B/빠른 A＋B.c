#include <stdio.h>

int main()
{
	double i, a;
	int num1, num2;
	scanf("%lf", &a);
	for (i = 0; i < a; i++)
	{
		scanf("%d %d", &num1, &num2);
		printf("%d\n", num1 + num2);
	}
	return 0;
}