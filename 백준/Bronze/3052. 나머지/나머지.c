#include <stdio.h>

int main()
{
	int r[42] = { 0 };
	int i, a, count=0;
	for (i = 0; i < 10; i++)
	{
		scanf("%d", &a);
		r[a % 42]++;
	}
	for (i = 0; i < 42; i++)
	{
		if (r[i] != 0)
			count++;
	}
	printf("%d", count);
	return 0;
}