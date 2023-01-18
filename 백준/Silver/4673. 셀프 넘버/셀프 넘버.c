#include <stdio.h>

int main()
{
	int num[11000] = { 0 };
	int i, a, b, c, d;
	for (i = 0; i < 10000; i++)
	{
		if (i < 10)
		{
			num[2*i]++;
		}
		else if (i < 100)
		{
			a = i / 10;
			b = i - 10 * a;
			num[i + a + b]++;
		}
		else if (i < 1000)
		{
			a = i / 100;
			b = i / 10 - a * 10;
			c = i % 10;
			num[i + a + b + c]++;
		}
		else
		{
			a = i / 1000;
			b = i / 100 - 10 * a;
			c = i / 10 - 100 * a - 10 * b;
			d = i % 10;
			num[i + a + b + c + d]++;
		}
	}
	for (i = 1; i < 10000; i++)
	{
		if (num[i] == 0)
			printf("%d\n", i);
	}
	return 0;
}