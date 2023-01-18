#include <stdio.h>

int main()
{
	int i, t, num1, num2;
	scanf("%d", &t);
	for (i = 1; i <= t; i++)
	{
		scanf("%d %d", &num1, &num2);
		printf("Case #%d: %d + %d = %d\n", i, num1, num2, num1 + num2);
	}
	return 0;
}