#include <stdio.h>

int main()
{
	int a[9] = { 0 };
	int max = 0, index_of_max = 0;
	int i;
	for (i = 0; i < 9; i++)
	{
		scanf("%d", &a[i]);
		if (a[i] >= max)
		{
			max = a[i];
			index_of_max = i;
		}
	}
	printf("%d\n%d", max, index_of_max+1);
	return 0;
}