#include <iostream>
#include <math.h>
using namespace std;

long checkEvenOdd(long d)
{
    if (d % 2 == 0)
    {
        return 1;
    }
    else
    {
        return 0;
    }
}
string solution(long n)
{
    long even = 0, odd = 0;
    for (long i = 1; i <= sqrt(n); i++)
    {
        if (n % i == 0)
        {
            // If divisors are equal,
            // count only one
            if (n / i == i)
            {
                int check = checkEvenOdd(i);
                (check == 1) ? even += 1 : odd += 1;
            }

            else
            {
                long nd=n/i;
                long val1=checkEvenOdd(i);
                long val2=checkEvenOdd(nd);
                if (val1==1 && val2==1)
                {
                    even+=2;
                }else if (val1==0 && val2==0)
                {
                    odd+=2;
                }else{
                    even+=1;
                    odd+=1;
                }
                
                
            }
        }
    }
    if(even==odd){
        return "PASS";
    }else if ((even+odd)%2 ==0)
    {
        return "BUY";
    }else{
        return "SELL";
    }
    
}

int main()
{
    long n;
    cin >> n;
    string answer = solution(n);
    cout << answer << endl;
}