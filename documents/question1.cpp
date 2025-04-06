// WAP to find whether the entered number is +ve , -ve or 0 .

#include<iostream>
using namespace std;
int main()
{
   int n;
   cout<<"Enter a number n :";
   cin>>n;
   if (n == 0)
 	cout<<"Entered number is 0";
   else if (n < 0)
   	cout<<"Entered number is -ve";
   else 
   	cout<<"Entered number is +ve";
  return 0;
}
