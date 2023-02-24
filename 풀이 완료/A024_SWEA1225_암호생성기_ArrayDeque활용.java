package 박승수;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;

public class A024_SWEA1225_암호생성기_ArrayDeque활용 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); // 입력을 받을 BufferReader 선언
		StringBuilder sb = new StringBuilder(); // 출력을 빠르게 할 StringBuilder 선언
		
		ArrayDeque<Integer> queue = new ArrayDeque<Integer>(); //큐로 사용할 deque 선언
		
		for (int i = 0; i < 10; i ++) {
			queue.clear(); // 큐 초기화
			int test_case = Integer.parseInt(br.readLine()); // 테스트 케이스 번호 입력
			String[] temp = br.readLine().split(" ");
			sb.append("#").append(test_case).append(" ");
			for (int idx = 0; idx < 8; idx++) { // 문제에서 사용할 8개의 정수 입력
				queue.addLast(Integer.parseInt(temp[idx]));
			}
			
			
			int cnt = 1;
			int t = 0;
			while (true) {
				t = queue.pop()-cnt; // 숫자를 pop 한뒤 cnt만큼 빼주고
				
				if (t <= 0) { // 만약 t <=0 이라면 암호 완성이기 때문에 큐에 0넣어주고 break;
					queue.addLast(0);
					break;
				}else { //완성되지 않았다면 다시 큐에 삽입
					queue.addLast(t); 
				}
				
				
				cnt ++; // 뺄 숫자 cnt +1 해주고
				if (cnt == 6) // 1~5 반복이기 때문에 6이 될경우 1로 변경
					cnt = 1;
			}
			
			for (int num : queue) { // 완성된 암호 StringBuilder로 합쳐놓기
				sb.append(num).append(" ");
			}
			sb.append("\n");
			
		}
		
		System.out.println(sb.toString()); // 정답 출력
	}

}
