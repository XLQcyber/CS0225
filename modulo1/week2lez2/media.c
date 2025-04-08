
#include <stdio.h>

int main()
{
    float primo_numero;
    float secondo_numero;
    float media;
    
    printf("Inserisci il primo numero: ");
    scanf("%f", &primo_numero);

    printf("Inserisci il secondo numero: ");
    scanf("%f", &secondo_numero);

    media = (primo_numero + secondo_numero)/2;
    printf("Il risultato della media è: %f\n", media);

    return 0;
}
