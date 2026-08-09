#include <stdio.h>

int main() {
    int arr[100];
    int n, target;
    int left, right, mid;
    int i, found = 0;

    printf("Enter number of elements: ");
    scanf("%d", &n);

    printf("Enter elements in sorted order:\n");

    for (i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }

    printf("Enter element to search: ");
    scanf("%d", &target);

    left = 0;
    right = n - 1;

    while (left <= right) {
        mid = left + (right - left) / 2;

        if (arr[mid] == target) {
            printf("Element found at index %d.\n", mid);
            found = 1;
            break;
        }
        else if (arr[mid] < target) {
            left = mid + 1;
        }
        else {
            right = mid - 1;
        }
    }

    if (!found)
        printf("Element not found.\n");

    return 0;
}
