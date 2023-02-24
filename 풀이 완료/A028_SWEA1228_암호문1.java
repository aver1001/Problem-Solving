package 박승수;

import java.util.*;

public class A028_SWEA1228_암호문1 {

	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in); // 입력받을 Scanner
		int N,K;
		for (int t = 1; t <= 10; t++) {
			int count=0;
			N = sc.nextInt();
			LinkedList<Integer> list = new LinkedList<>();		//리스트 선언
			
			for (int i = 0; i < N; i++) list.add(sc.nextInt());	//원본암호문 추가
			
			K = sc.nextInt(); 
			
			for (int q = 0; q < K; q++) {
				String s = sc.next();	//i 제거
				int x =sc.nextInt();	//넣을 인덱스
				int y = sc.nextInt();	//넣을 숫자
				
				for (int i = 0; i < y; i++) {
					list.add(x++, sc.nextInt());	//삽입하면서 x값을 증가시켜 인덱스도 증가
				}
			}
			System.out.printf("#%d ",t); // 테스트 케이스 출력
			while (!(list.isEmpty())) { // list가 빌때까지 또는
				if(count >9) break; // 10개 채워지면 그만
				System.out.print(list.poll() + " "); // 출력
				count++;
			}
			System.out.println();
		}
	}
}
