#include <stdio.h>

int main()
{
    int primo_numero;
    int secondo_numero;
    int moltiplicazione;
    
    printf("Inserisci il primo numero: ");
    scanf("%d", &primo_numero);

    printf("Inserisci il secondo numero: ");
    scanf("%d", &secondo_numero);

    moltiplicazione = primo_numero * secondo_numero;
    printf("Il risultato della moltiplicazione è: %d\n", moltiplicazione);

    return 0;
}
