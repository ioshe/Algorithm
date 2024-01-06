import java.util.Scanner;


public class Main { //파스칼케이스-대문자로 시작하는 카멜케이스
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in); //스캐너 객체 - 다 쓰고 반환해줘야 함
		boolean[] visited = new boolean[42];
		int answer = 0;
		// boolean visited[] = new boolean[42];
		// boolean visited[41 + 1];
		// System.out.println(Arrays.toString(visited));
		for(int i = 0; i < 10 ; i++) {
			int num = sc.nextInt();
			//System.out.println(num);
			int remain = num % 42;
//			System.out.println(remain);
//			System.out.println(visited[remain]);
			if (!visited[remain]) {
				visited[remain] = true;
				answer += 1;
			}
		}
		System.out.println(answer);
	}
}