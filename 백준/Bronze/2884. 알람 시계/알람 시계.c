#include <stdio.h>

int main()
{
	int hour, min, time;
	scanf("%d %d", &hour, &min);
	time = hour * 60 + min;
	if (time < 45)
		time += 1440;
	time -= 45;
	printf("%d %d", time / 60, time % 60);
	return 0;
}