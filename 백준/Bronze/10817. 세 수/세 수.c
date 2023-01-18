#include <stdio.h>

int main()
{
	int a, b, c, num;
	scanf("%d %d %d", &a, &b, &c);
	int ab, bc, ca;
	ab = a - b;
	bc = b - c;
	ca = c - a;
	if (ab > 0)
	{
		if (bc > 0)
			num = b;
		else
		{
			if (ca > 0)
				num = a;
			else
				num = c;
		}
	}
	else
	{
		if (bc > 0)
		{
			if (ca > 0)
				num = c;
			else
				num = a;
		}
		else
		{
			num = b;
		}
	}
	printf("%d", num);
	return 0;
}