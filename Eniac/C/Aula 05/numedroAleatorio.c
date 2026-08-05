#include <stdio.h>
#include <stdio.h>
#include <time.h>
int main(){
    int num, cont;
    srand(time(NULL));
    cont = 1;
    while(cont <= quant){
        num = rand()%60 + 1;
        printf("%d", num);
        cont++
    }
    printf("\n");
    system("pause");
    return 0;
}