#include <stdio.h>

int main()
{
	double i, n;
	scanf("%lf", &n);
	for (i = 1; i <= n; i++)
		printf("%.0f\n", i);
	return 0;
}