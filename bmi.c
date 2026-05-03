#include <stdio.h>

int main (void)
{
  float weight;
  float height;

  printf("Enter your weight in kg:");
  scanf("%f", &weight);

  printf("Enter your height in meters:");
  scanf("%f", &height);

  float bmi = weight / (height * height);
  printf("Your BMI is: %.2f\n", bmi);

}