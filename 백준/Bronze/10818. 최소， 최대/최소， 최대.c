#include <stdio.h>

int main()
{
	int N, i, t;
	int max=-1000000, min=1000000;
	scanf("%d", &N);
	for (i = 0; i < N; i++)
	{
		scanf("%d", &t);
		if (t >= max)
			max = t;
		if (t <= min)
			min = t;
	}
	printf("%d %d", min, max);
	return 0;
}