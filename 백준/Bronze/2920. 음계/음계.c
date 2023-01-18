#include <stdio.h>

int main()
{
	int a[8] = { 1,2,3,4,5,6,7,8 }, d[8] = { 8,7,6,5,4,3,2,1 };
	int count=0;
	int i, n;
	for (i = 0; i < 8; i++)
	{
		scanf("%d", &n);
		if (n == a[i])
			count++;
		else if (n == d[i])
			count--;
	}
	if (count == 8)
		printf("ascending");
	else if (count == -8)
		printf("descending");
	else
		printf("mixed");
	return 0;
}