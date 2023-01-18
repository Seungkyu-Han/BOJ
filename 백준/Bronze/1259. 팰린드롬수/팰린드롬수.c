#include <stdio.h>

int reverse(int num);

int main(void){

    int ans;
    scanf("%d", &ans);

    while (ans){
        if (reverse(ans)){
            printf("yes\n");
        }
        else{
            printf("no\n");
        }
        scanf("%d", &ans);
    }


    return 0;


}

int reverse(int num){

    int tmp_num = num;
    int reverse_num = 0;

    while (num > 0){
        reverse_num = reverse_num * 10 + (num % 10);
        num /= 10;
    }

    while (tmp_num > 0){
        if (tmp_num % 10 != reverse_num % 10){
            return 0;
        }
        else{
            tmp_num /= 10;
            reverse_num /= 10;
        }
    }

    return 1;

}