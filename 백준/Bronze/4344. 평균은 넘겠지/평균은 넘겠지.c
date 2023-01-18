#include <stdio.h>
double average();

int main()
{
	int C, i;
	scanf("%d", &C);
	for (i = 0; i < C; i++)
		average();
	return 0;
}

double average()
{
	int student[1000], sum=0;
	double avg, N, count=0;
	scanf("%lf", &N);
	int i;
	for (i = 0; i < N; i++)
	{
		scanf("%d", &student[i]);
		sum += student[i];
	}
	avg = sum / N;
	for (i = 0; i < N; i++)
	{
		if (student[i] > avg)
			count++;
	}
	printf("%.3f%%\n",  (count / N) * 100);
	return 0;
}