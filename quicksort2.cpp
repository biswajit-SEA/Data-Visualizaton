#include <stdio.h>

void swap(int* p,int* q){
   int temp= *p;
    *p = *q;
    *q = temp;
   
}

int partition(int arr[], int low, int high)
{
	int i = low;
	int j = high;
	int pi = arr[low];
	while (i < j)
	{
		while (pi >= arr[i])
			i++;
		while (pi < arr[j])
			j--;
		if (i < j)
			swap(&arr[i], &arr[j]);
	}
	swap(&arr[low], &arr[j]);
	return j;
}

void quickSort(int arr[], int low, int high)
{
	if (low < high)
	{
		int pi = partition(arr, low, high);
		quickSort(arr, low, pi - 1);
		quickSort(arr, pi + 1, high);
	}
}

void printArray(int arr[], int size)
{
	for (int i = 0; i < size; i++)
	{
		printf("%d\t", arr[i]);
	}
	printf("\n");
}

int main()
{
    int i, size ;
	int arr[50];
    printf("Enter size of array\n");
    scanf("%d",&size);
    printf("Enter elments of array\n");
    for (i=0;i<size;i++)
    {
       scanf("%d",&arr[i]);
    }
	printf("Original Array\n");
	printArray(arr, size);
	quickSort(arr, 0, size - 1);
	printf("Sorted Array\n");
	printArray(arr, size);
	return 0;
}
