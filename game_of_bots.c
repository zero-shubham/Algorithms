#include <stdio.h>
#include <string.h>

int main(){
    char ini[1000000],fin[1000000];
    int i=0,j=0,loop,s, flag=0;
    scanf("%d",&loop);
    while(loop>0){
        scanf("%s %s",ini,fin);
        s= strlen(ini);
        flag=i=j=0;
        while(i<s && j<s && flag==0){
            if(ini[i]=='B'){
                while(fin[j]!='B'){
                    if(fin[j]=='A'){
                        flag=1;
                        break;
                    }
                    j++;
                }
                i = j+1;
                j++;
            }

            else if(fin[j]=='A'){
                while(ini[i]!='A'){
                    if(ini[i]=='B'){
                        flag=1;
                        break;
                    }
                    i++;
                }
                j=i+1;
                i++;
            }
            else if(ini[i]=='A' && fin[j]=='B'){
                flag=1;
                break;
            }
            else{
                i++;
                j++;
            }
        }
        if(flag==0){
            printf("Yes\n");
        }
        else
            printf("No\n");
        loop--;
    }
    return 0;
}
