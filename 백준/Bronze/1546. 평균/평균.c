#include <stdio.h>

int main()
{
	int n, i;
	double M[1000];
	scanf("%d", &n);
	double max = 0, total=0;
	for (i = 0; i < n; i++)
	{
		scanf("%lf", &M[i]);
		if (M[i] >= max)
			max = M[i];
	}
	for (i = 0; i < n; i++)
		M[i] = ((double)M[i] / (double)max) * 100;
	for (i = 0; i < n; i++)
		total += (double)M[i];
	printf("%.2f", total / n);
	return 0;
}