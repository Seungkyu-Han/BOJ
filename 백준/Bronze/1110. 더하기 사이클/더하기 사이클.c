#include <stdio.h>

int main()
{
	int num, m_num, count=1;
	int a, b;
	scanf("%d", &num);
	a = num % 10;
	b = (num / 10 + num % 10)%10;
	m_num = 10 * a + b;
	while (num!=m_num)
	{
		a = m_num % 10;
		b = (m_num / 10 + m_num % 10) % 10;
		m_num = 10 * a + b;
		count++;
	}
	printf("%d", count);
	return 0;
}