#include <stdio.h>

int main(void)
{
    char name[50];
    int pin;
    int option;
    float balance = 1000.00;
    float amount;

    printf("Enter your name: ");
    scanf("%49s", name);
    while(getchar() != '\n');

    printf("Enter your PIN: ");
    scanf("%i", &pin);
    while(getchar() != '\n');

    if (pin != 1234)
    {
       printf("Wrong PIN. Access denied.\n");
       return 0;
    }

    printf("\nWelcome, %s!\n", name);

    do 
    {

        printf("\n--- ATM Menu ---\n");
        printf("1. Check balance\n");
        printf("2. Deposit\n");
        printf("3. Withdraw\n");
        printf("4. Exit\n");
        printf("Choose an option: ");
        scanf("%i", &option);
        while(getchar() !='\n');

        if(option == 1)
        {
            printf("Your balance is: $%.2f\n", balance);

        }
        else if (option == 2)
        {
            printf("Enter amount to deposit: ");
            scanf("%f", &amount);
            while(getchar() != '\n');
            balance = balance + amount;
            printf("Deposited $%.2f. New balance: $%.2f\n", amount, balance);
        }
        else if (option == 3)
        {
            printf("Enter amount to withdraw: ");
            scanf("%f", &amount);
            while(getchar() != '\n');
            if (amount > balance)
            {
                printf("Insulfficient funds.\n");
            }
            else
            {
                balance = balance - amount;
                printf("Withdrawn $%.2f. New balance: $%.2f\n", amount, balance);
            }
        } 
        else if (option != 4)
        {
            printf("Invalid option.\n");
        }
    }
    while (option != 4);
    
    printf("\nThank you, %s.Goodbye!\n", name);
}   