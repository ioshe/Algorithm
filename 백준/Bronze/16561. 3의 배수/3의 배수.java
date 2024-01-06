import java.util.Scanner;

public class Main {
	public static void main(String args[]) {
		
		//System.in
		Scanner sc = new Scanner(System.in); //스캐너 객체
		int N = sc.nextInt();
		sc.close(); // 객체를 반환
		int count = 0;
		for (int i=3; i<=N-6; i+=3) {
			for (int j=3; j<=N-i-3; j+=3) {
				count++;
			}
		}
		System.out.println(count);
	}
}