#include <stdio.h>
#include <stdlib.h>
#include <math.h>

typedef struct node{
    int data;
    struct node *next;
}node;

int t,size,n,j,i,input,pos_c,pos_r,tmp;


void hashify(){
    pos_r = (tmp%10)% n;
    tmp = tmp/10;
    pos_c = (tmp%10)% n;
    tmp = tmp/10;
}

int main(){
    scanf("%d",&t);
    while(t>0){
    node **arr;
        scanf("%d",&size);
        n = sqrt(size);
        if(n*n < size)
            n++;
        arr = (node**)malloc(n * sizeof(node*));
        for(i=0; i<n; i++){
            arr[i] = (node*)malloc(n * sizeof(node));
        }

        for(i=0;i<n;i++)
            for(j=0;j<n;j++){
                (arr[i][j]).data = -999999;
                arr[i][j].next = NULL;
            }

        while(size>0 && size<=100000){
            node *tpointer=NULL;
            int flag=0;
            scanf("%d",&input);

            if(input<0)
                tmp = -1 * input;
            else
                tmp = input;

            hashify();
            while(tmp != 0 && arr[pos_r][pos_c].data != -999999){
                hashify();
            }
            if(arr[pos_r][pos_c].data!=-999999){
                for(i=0;i<n;i++){
                    for(j=0;j<n;j++){
                        if(arr[i][j].data==-999999){
                                flag=1;
                                break;
                        }
                    }
                    if(flag==1)
                        break;
                }
                arr[i][j].data = input;
                tpointer = &arr[pos_r][pos_c];
                while((*tpointer).next != NULL)
                    tpointer = (*tpointer).next;
                (*tpointer).next = &arr[i][j];
            }
            else{
                arr[pos_r][pos_c].data = input;
            }
        size--;
        }

        /*for(i=0;i<n;i++){
            printf("\n");
            for(j=0;j<n;j++)
                printf("%d\t",arr[i][j].data);
        }*/

        scanf("%d",&size);
        while(size>0){
            int flag=0;
            node *tpointer=NULL;
            scanf("%d",&input);

            if(input<0)
                tmp = -1 *input;
            else
                tmp = input;

            hashify();
            while(arr[pos_r][pos_c].data != input){
                if(arr[pos_r][pos_c].next!=NULL){
                    tpointer = arr[pos_r][pos_c].next;
                        while((*tpointer).next != NULL && (*tpointer).data != input){
                            tpointer = (*tpointer).next;
                        }
                        if((*tpointer).data==input){
                            flag=1;
                            break;
                        }
                }
                hashify();
                if(tmp==0)
                    break;
            }
            if(arr[pos_r][pos_c].data==input || flag==1)
                printf("Yes\n");
            else
                printf("No\n");
        size--;
        }


    t--;
    }
    return 0;
}
