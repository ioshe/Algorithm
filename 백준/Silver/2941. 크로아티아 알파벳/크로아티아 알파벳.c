#include <stdio.h>
#include <string.h>

int main(void) {
    char a[101];
    int i =1,cnt = 1;
    scanf("%s",a);
    //printf("글자 크기 %d\n",strlen(a));
    for(i=1; i<strlen(a); i++){
        switch (a[i]){
            case '=' : if(a[i-1] == 'z' && a[i-2] == 'd') cnt--; break;
            case '-' : break;
            case 'j' : if(a[i-1] == 'n' || a[i-1] == 'l') continue; else cnt++; break;
            default : cnt = cnt+1;
        }
        //printf("%d번째 cnt = %d\n",i+1,cnt);
    }
    // for(i=0; i<strlen(a); i++)
    //     printf("%c\n",a[i]);
    printf("%d",cnt);
    return 0;
}