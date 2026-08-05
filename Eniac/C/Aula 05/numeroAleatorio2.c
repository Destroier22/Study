#include <stdio.h>
#include <stdio.h>
#include <locale.h>
#include <time.h>
int main(){
    int num, cont, quant, digit;
    
    setlocale(LC_ALL,"portuguese");
    srand(time(NULL));
    printf("Qunatos números você quer gerar? ");
    scanf("%d", &quant);
    printf("Qunatos digitos você quer em cada número? ");
    scanf("%d", &digit);
    cont = 1;
    while(cont <= quant){
        num = rand()%digit + 1;
        printf("%d", num);
        cont++;
    }
    printf("\n");
    system("pause");
    return 0;
}