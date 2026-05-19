//biblioteca padrão da liguagem c para entrada e saída (scanf & printf)
#include <stdio.h>

//biblioteca para comando system
#include <stdlib.h>

//biblioteca para comando LC_ALL para puxar o "portuguese"
#include <locale.h>

#include <string.h>
int main(){
    //biblioteca para manipulação de string
    setlocale(LC_ALL, "portuguese");

    char nome1 [10], nome2 [10];
    //strcmp = comparar string
    strcmp();
    //strcpy = atribuir valor a string
    char teste [20];
    strcpy(teste, "teste 1 ok");
    system("pause");
    return 0;
}