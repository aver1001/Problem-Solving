package 박승수;

import java.util.ArrayDeque;
import java.util.Scanner;

public class A026_BJ2164_카드2_과제4 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in); // 입력이 하나이므로 Scanner로 받아왔음.
		int N = sc.nextInt(); //카드의 개수N;
		ArrayDeque<Integer> queue = new ArrayDeque<Integer>(); // queue로 사용할 Dqueu 선언
		
		for (int idx = N; idx > 0; idx --) {
			queue.addFirst(idx); // 먼저 카드를 넣어줌
		}
		
		int answer = 0; // 꺼낸 카드 번호 저장할 변수 선언
		while(true) {
			if (queue.size() == 1) { // 만약 마지막 카드라면
				answer = queue.removeFirst(); // 뺸뒤 break
				break;
			}
			
			answer = queue.removeFirst(); // 맨 왼쪽의 카드를 하나 뺀뒤
			queue.addLast(queue.removeFirst()); // 하나 더 빼고 맨뒤에다 넣음
		}
		
		System.out.println(answer); // 정답 출력

	}

}
