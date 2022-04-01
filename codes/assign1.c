#include<stdio.h>
#include<math.h>

// To check whether it is the root of 4x*x-5x-3=0
int  ret(float a)
{
float t,p,t1,p1;

t=5+sqrt(73);

p=5-sqrt(73);
/* This is to convert it into two decimal places*/
t1=(int)((t*100+0.5)/8);
t=t1/100;

p1=(int)((p*100-0.5)/8);
p=p1/100;

if(a==t||a==p)
    return 0;
else return 1;
}


int main()
{
float a,b;

// Taking two distinct numbers upto two decimal points from the user
 scanf("%f%f",&a,&b);

if(ret(a)==0&&ret(b)==0)
{
printf(" Both are roots of the given equation\n");
}
else
printf(" Both are not roots of the given equation\n");
}

