/*1-*/
#include<stdio.h>
#include<stdlib.h>
void push(int a[],int *t)
{
    int n;
    (*t)++;
    if(*t<5)
    {
        printf("Enter the element.\n");
        scanf("%d",&n);
        a[*t]=n;
    }
    else
    {
        printf("Overflow Condition\n");
        (*t)--;
    }
}

void pop(int a[],int *t)
{
    if(*t<0)
    {
        printf("Underflow Condition");
        exit(1);
    }
    else
        *t=*t-1;
}

void display(int a[],int *t)
{
    int i;
    for(i=0;i<=*t;i++)
    {
        printf("%d ",a[i]);
    }
    printf("\n");
}

void main()
{
    int ch,a[5],t=-1;
    while(1)
    {
    printf("Enter choice\n1-Push\n2-Pop\n3-Display\n4-Exit\n");
    scanf("%d",&ch);
    switch(ch)
    {
    case 1:
        push(a,&t);
        break;
    case 2:
        pop(a,&t);
        break;
    case 3:
        display(a,&t);
        break;
    case 4:
        exit(1);
    default:
        printf("Invalid Choice\n");
    }
    }
}

/*2-
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<ctype.h>
#include<math.h>
void push(int st[],int *t, int dig)
{
    st[++(*t)]=dig;
}

void pop(int st[],int *t,int r)
{
    st[--(*t)]=r;
}

void main()
{
    char a[50];
    int st[100],i,t=-1;
    printf("Enter the expression.\n");
    gets(a);
    for(i=0;i<strlen(a);i++)
    {
        if(isdigit(a[i]))
            push(st,&t,(a[i]-'0'));
        else
        {
            switch(a[i])
            {
            case '^':
                pop(st,&t,pow(st[t-1],st[t]));
                break;

            case '%':
                pop(st,&t,st[t-1]%st[t]);
                break;

            case '/':
                pop(st,&t,st[t-1]/st[t]);
                break;

            case '*':
                pop(st,&t,st[t-1]*st[t]);
                break;

            case '-':
                pop(st,&t,st[t-1]-st[t]);
                break;

            case '+':
                pop(st,&t,st[t-1]+st[t]);
                break;

            }
        }
    }
    for(i=0;i<=t;i++)
    {
        printf("%d ",st[i]);
    }
}*/

/*3.
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<ctype.h>
void push_st(char st[],int *sp,char inf)
{
    st[++(*sp)]=inf;
}

void push_post(char pf[],int *pp,char inf)
{
    pf[++(*pp)]=inf;
}

void pop(char st[],int *sp)
{
    if(*sp>0)
        *sp=*sp-1;
}

void main()
{
    char inf[50],pf[50],st[50];
    int i,sp=0,pp=-1;
    printf("Enter the expression.\n");
    gets(inf);
    st[0]='(';
    for(i=0;i<strlen(inf);i++)
    {
        if(isdigit(inf[i]))
            push_post(pf,&pp,inf[i]);
        else
        {
            switch(inf[i])
            {
            case '(':
                push_st(st,&sp,inf[i]);
                break;
            case '^':
                if(st[sp]=='^')
                {
                    push_post(pf,&pp,st[sp]);
                    pop(st,&sp);
                    push_st(st,&sp,inf[i]);
                }
                else
                    push_st(st,&sp,inf[i]);
                break;
            case '*':
                if(st[sp]=='^'||st[sp]=='/'||st[sp]=='*')
                {
                    push_post(pf,&pp,st[sp]);
                    pop(st,&sp);
                    push_st(st,&sp,inf[i]);
                }
                else
                    push_st(st,&sp,inf[i]);
                break;
            case '/':
                if(st[sp]=='^'||st[sp]=='*'||st[sp]=='/')
                {
                    push_post(pf,&pp,st[sp]);
                    pop(st,&sp);
                    push_st(st,&sp,inf[i]);
                }
                else
                    push_st(st,&sp,inf[i]);
                break;
            case '+':
                if(st[sp]=='^'||st[sp]=='*'||st[sp]=='/'||st[sp]=='-'||st[sp]=='+')
                {
                    push_post(pf,&pp,st[sp]);
                    pop(st,&sp);
                    push_st(st,&sp,inf[i]);
                }
                else
                    push_st(st,&sp,inf[i]);
                break;
            case '-':
                 if(st[sp]=='^'||st[sp]=='*'||st[sp]=='/'||st[sp]=='+'||st[sp]=='-')
                {
                    push_post(pf,&pp,st[sp]);
                    pop(st,&sp);
                    push_st(st,&sp,inf[i]);
                }
                else
                    push_st(st,&sp,inf[i]);
                break;
            case ')':
                while(st[sp]!='(')
                {
                    push_post(pf,&pp,st[sp]);
                    pop(st,&sp);
                }
                pop(st,&sp);
                break;
            default:
                printf("Invalid\n");
                break;
            }
        }
    }
    for(i=0;i<=pp;i++)
    {
        printf("%c,",pf[i]);
    }
}*/
