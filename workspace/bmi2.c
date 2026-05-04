#include <stdio.h>

int main(void)
{
    char name[50];
    char sex[2];
    float weight;
    float height;

    printf("Enter your name: ");
    scanf("%49s", name);
    while(getchar() != '\n');

    printf("Enter your sex (M/F): ");
    scanf("%1s", sex);
    while(getchar() != '\n');

    printf("Enter your weight in kg: ");
    scanf("%f", &weight);
    while(getchar() != '\n');

    printf("Enter your height in meters: ");
    scanf("%f", &height);
    while(getchar() != '\n');

    float bmi = weight / (height * height);
    float ideal_weight = 22.0 * (height * height);

    printf("\n--- Results for %s ---\n", name);
    printf("BMI: %.2f\n", bmi);
    printf("Ideal weight for your height: %.1f kg\n", ideal_weight);

    if (bmi < 18.5)
    {
        printf("Status: Underweight\n");
    }
    else if (bmi < 25.0)
    {
        printf("Status: Normal weight\n");
    }
    else if (bmi < 30.0)
    {
        printf("Status: Overweight\n");
    }
    else
    {
        printf("Status: Obesity\n");
    }
}