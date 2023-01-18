#include <stdio.h>

int main(void)
{
	int a[5], sum=0;
	for (int i = 0; i < 5; i++)
	{
		scanf("%d", &a[i]);
		if (a[i] <= 40)
			a[i] = 40;
		sum += a[i];
	}
	printf("%d", sum / 5);
	return 0;
}