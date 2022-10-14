#include<stdio.h>
#include<stdlib.h>
int part(int *a,int l,int h)
{
    int piv=l,i=l,j=h;
    while(i<j)
    {
        while(*(a+i)<=*(a+piv))
        {
            i++;
        }
        while(*(a+j)>*(a+piv))
        {
            j--;
        }
        if(i<j)
        {
            int t=*(a+i);
            *(a+i)=*(a+j);
            *(a+j)=t;
        }
    }
    int t=*(a+piv);
    *(a+piv)=*(a+j);
    *(a+j)=t;
    printf("\n Passing");
    for(int k=0; k<5; k++)
    {
        printf("%d ", *(a+k));
        }
    return j;
}
void quicksort(int *a,int l,int h)
{
    int j;
    if(l<h)
    {
        j=part(a,l,h);
        quicksort(a,l,j-1);
        quicksort(a,j+1,h);
    }
}
void main()
{
    int *a,n,i,mid,j;
    printf("Enter number of elements of array : ");
    scanf("%d",&n);
    a=(int*)malloc(n*sizeof(int));
    if(a!=NULL)
    {
        printf("Enter elements of array : \n");
        for(i=0; i<n; i++)
        {
            scanf("%d",a+i);
        }
        printf("The array is : \n");
        for(i=0; i<n; i++)
        {
            printf("%d ",*(a+i));
        }
        quicksort(a,0,n-1);
        printf("\n");
        printf("The sorted array is :\n");
        for(i=0; i<n; i++)
        {
            printf("%d ",*(a+i));
        }
    }
    else
        printf("Not enough space.\n");
}
