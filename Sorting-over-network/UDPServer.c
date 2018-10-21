
// Server side implementation of UDP client-server model
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <netinet/in.h>


#include <unistd.h>



#define PORT     8080
#define MAXLINE 1024

int * extract(char arr[]){
    int *test = malloc(10* sizeof(int));
    
    int i=0,j,count=0, numc;
    char num[10];


     while(arr[i]!='\0'){
        j = i;
        numc=0;
        while(arr[j]!= ' '){
            num[numc++] = arr[j];
            j++;
        }
        if(numc!=0){
            num[numc] = '\0';
            test[count++] = atoi(num);
            i=j;
        }


        i++;
    }


    return test;
}

void selectionSort(int arr[]) 
{ 
    int i, j, min_idx, tmp; 
  
    // One by one move boundary of unsorted subarray 
    for (i = 0; i < 10-1; i++) 
    { 
        // Find the minimum element in unsorted array 
        min_idx = i; 
        for (j = i+1; j < 10; j++) 
          if (arr[j] < arr[min_idx]) 
            min_idx = j; 
  
        // Swap the found minimum element with the first element 
        tmp = arr[min_idx];
        arr[min_idx] = arr[i];
        arr[i] = tmp; 
    } 
} 


// Driver code
int main() {
    int sockfd;
    char buffer[MAXLINE];
    char unsorted[100];
    struct sockaddr_in servaddr, cliaddr;

    // Creating socket file descriptor
    if ( (sockfd = socket(AF_INET, SOCK_DGRAM, 0)) < 0 ) {
        perror("socket creation failed");
        exit(EXIT_FAILURE);
    }

    memset(&servaddr, 0, sizeof(servaddr));
    memset(&cliaddr, 0, sizeof(cliaddr));

    // Filling server information
    servaddr.sin_family    = AF_INET; // IPv4
    servaddr.sin_addr.s_addr = htonl(INADDR_ANY);
    servaddr.sin_port = htons(PORT);

    // Bind the socket with the server address
    if ( bind(sockfd, (const struct sockaddr *)&servaddr,
            sizeof(servaddr)) < 0 )
    {
        perror("bind failed");
        exit(EXIT_FAILURE);
    }

    int len, n;
    n = recvfrom(sockfd, (char *)buffer, MAXLINE,
                MSG_WAITALL, ( struct sockaddr *) &cliaddr,
                &len);
    buffer[n] = '\0';

    printf("Client : %s\n", buffer);

    memset(&unsorted, '\0', sizeof(unsorted));

    strcat(unsorted,buffer);

    int *c;
    c = extract(unsorted);

    selectionSort(c);
    char num[10], sorted[100];

    for (int i = 0; i < 10; i++)
    {
        sprintf(num, "%d ", c[i]);
        strcat(sorted, num);
    }
    sendto(sockfd, (const char *)sorted, strlen(sorted),
        MSG_CONFIRM, (const struct sockaddr *) &cliaddr,
            len);
    printf("sorted message sent.\n");


    return 0;
}
