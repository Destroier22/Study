#include <stdio.h>
#include <stdlib.h>
#include <locale.h>
#include <string.h>
int main (){
    float imc, peso, altura;
    char res[20];
    setlocale(LC_ALL, "portuguese");
    printf("Qual é a sua altura? ");
    scanf("%f", &altura);
    printf("Qual é o seu peso? ");
    scanf("%f", &peso);
    imc = peso / (altura*altura);
    if(imc < 18.00){
        strcpy(res, "só o osso");
    } else if(imc >= 18.00 && imc < 25.00){
        strcpy(res, "normal");
    } else if(imc >= 25.00 && imc < 30.00){
        strcpy(res, "sobrepeso");
    } else if(imc >= 30.00 && imc < 40.00){
        strcpy(res, "obeso");
    } else {
        strcpy(res, "obesidade mórbida");
    }
    getchar();
    printf("Seu IMC é: %.2f\n", imc);
    printf("Classificação: %s\n", res);
    system("pause");
    return 0;
}