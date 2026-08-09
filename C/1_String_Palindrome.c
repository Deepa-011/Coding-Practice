#include <stdio.h>
#include <string.h>

int main() {
    char str[100];
    int left, right, palindrome = 1;

    printf("Enter a string: ");
    fgets(str, sizeof(str), stdin);

    str[strcspn(str, "\n")] = '\0';

    left = 0;
    right = strlen(str) - 1;

    while (left < right) {
        if (str[left] != str[right]) {
            palindrome = 0;
            break;
        }

        left++;
        right--;
    }

    if (palindrome)
        printf("The string is a Palindrome.\n");
    else
        printf("The string is not a Palindrome.\n");

    return 0;
}
