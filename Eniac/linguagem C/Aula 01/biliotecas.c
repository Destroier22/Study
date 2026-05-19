//biblioteca padrão da liguagem c para entrada e saída (scanf & printf)
#include <stdio.h>

//biblioteca para comando system
#include <stdlib.h>

//biblioteca para comando LC_ALL para puxar o "portuguese"
#include <locale.h>
setlocale(LC_ALL, "portuguese");
//biblioteca para manipulação de string
#include <string.h>
//strcmp = comparar string

//strcpy = atribuir valor a string
char teste[20];
strcpy(teste, "teste 1 ok");