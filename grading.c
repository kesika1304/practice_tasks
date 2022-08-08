#include<stdio.h>
float calculation();
float grade[6];
int main()
{
    float total;
    printf("ent grade in math: ");
    scanf("%d",&grade[0]);
    printf("ent grade in C: ");
    scanf("%d",&grade[1]);
    printf("ent grade in eng: ");
    scanf("%d",&grade[2]);
    printf("ent grade in physics: ");
    scanf("%d",&grade[3]);
    printf("ent grade in EG: ");
    scanf("%d",&grade[4]);
    printf("ent grade in c-lab: ");
    scanf("%d",&grade[5]);
    total=calculation();
    printf("cgpa is %f", total);

}

float calculation(){
    int sum=0,i;
    float total;
    grade[0]=grade[0]*4;
    grade[1]=grade[1]*3;
    grade[2]=grade[2]*3;
    grade[3]=grade[3]*4;
    grade[4]=grade[4]*3;
    grade[5]=grade[5]*1.5;
    for (i=0;i<6;i++)
    {
        sum=(sum+grade[i]);
    }
    total=sum/18.5;
    return total;
}
