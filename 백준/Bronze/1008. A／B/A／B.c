#include <stdio.h>

int main() {
    int a,b;
    double result;
    scanf("%d %d",&a,&b);
    result=(double)a/(double)b;
    printf("%.9lf",result);
    return 0;
}