#include <stdio.h>

int main()
{
	int i, a, num1, num2;
	scanf("%d", &a);
	for (i = 0; i < a; i++)
	{
		scanf("%d %d", &num1, &num2);
		printf("%d\n", num1 + num2);
	}
	return 0;
}