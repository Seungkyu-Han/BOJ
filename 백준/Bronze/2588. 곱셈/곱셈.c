#include <stdio.h>

int main()
{
	int num1, num2;
	scanf("%d %d", &num1, &num2);
	int a, b, c;
	a = num2 % 10;
	b = num2 % 100 - a;
	c = num2 - b - a;
	printf("%d\n%d\n%d\n%d", num1 * a, (num1 * b)/10, (num1 * c)/100, num1 * num2);
	return 0;
}