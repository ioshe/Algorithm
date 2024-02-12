#include <stdio.h>

int main(void){
	int N, i, han = 0, k, a[3];
	scanf("%d",&N);
	for(i=0; i<=N; i++){
		if(0 < i && i < 100) han = i;
		else if(i == 1000 ) break;
		else{
			k=0; int t = i;
			while(t>0){
				a[k] = t%10;
				t /= 10;
				k++;
			}
			if (a[2] - a[1] == a[1] - a[0]) {
				han++;
			}
		}		
	}
	printf("%d\n", han);
	return 0;
}
