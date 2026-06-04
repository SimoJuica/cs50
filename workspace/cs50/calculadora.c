#include <stdio.h>

int main(void)
{
    float num1, num2;
    int choice;

    printf("=== Calculator ===\n");
    printf("1. Add\n");
    printf("2. Subtract\n");
    printf("3. Multiply\n");
    printf("4. Divide\n");


    printf("Choose an option: ");
    scanf("%d", &choice);

    printf("Enter first number: ");
    scanf("%f", &num1);


    printf("Enter second number:");
    scanf("%f", &num2);

    if (choice == 1)
{
       printf(""Result: %.2f\n", num1 + num2);
}
    else if ( choice == 2)
{
    printf("Result: %.2f\n", num1- num2);
}      
else if (choice == 3)
{
    printf("Result: %.2f\n", num1 * num2);
}
else if (choice == 4)
{ 
    if(num2 != 0)
    { 
        printf("Result: %.2f\n", num1 / num2);

    }    
    else 
    {
        printf("Error:Cannot divide by zero.\n");
    }
}
else
 { 
    printf("Invalid option.\n");
 }   

 return 0;

}