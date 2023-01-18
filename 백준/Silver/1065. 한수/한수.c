#include <stdio.h>

int main()
{
	int num[1000] = { 0 };
	int i, a, b, c, n, count=0;
	for (i = 0; i < 1000; i++)
	{
		if (i < 100)
			num[i]++;
		else
		{
			a = i / 100;
			b = i / 10 - 10 * a;
			c = i - 100 * a - 10 * b;
			if (2 * b == a + c)
				num[i]++;
		}
	}
	scanf("%d", &n);
	for (i = 1; i <= n; i++)
	{
		if (num[i] == 1)
			count++;
	}
	printf("%d", count);
	return 0;
}