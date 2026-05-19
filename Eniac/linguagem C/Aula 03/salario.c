#include <stdio.h>
#include <stdlib.h>
#include <locale.h>
int main(){
    float salario, salNovo, aumento, salLiq;
    setlocale(LC_ALL, "portuguese");
    printf("Digite seu salário: ");
    scanf("%f", &salario);
    if(salario <= 3000){
        aumento = salario/100*15.45;
    }else if(salario > 3000.0 && salario <= 5500.0) {
        aumento = salario/100*10.15;
    } else {
        aumento = salario/100*7.5;
    }
    salNovo = salario + aumento;
    salLiq = salNovo-(salNovo/100*20.5);
    printf("O seu aumento salarial foi de R$%.2f, seu salário atual é R$%.2f \n", aumento, salNovo);
    printf("Seu salário sem impostos é igual a R$%.2f", salLiq);
    system("pause");
    return 0;
}
/* Este programa recebe o salário bruto atual de um funcionário e 
calcular o novo salario bruto com aumento de acordo com a faixa salarial e 
mostre o salario liquido a receber sabendo imposto a pagar 20.5%.
------------------------------------------------------------------------
 | para salario <= 3000.0 o aumento: 15.45%                         |
------------------------------------------------------------------------
 | para salario > 3000.0, mas o salario <= 5500.0 o aumento: 10.15% |
------------------------------------------------------------------------
 | para salario > 5500.0 o aumento: 7.5%                            |  
-----------------------------------------------------------------------*/
