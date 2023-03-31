package 박승수;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;

public class B003_BJ1463_1로만들기 {
	
	public static void main(String[] args) throws NumberFormatException, IOException {
		//입력을 위한 버퍼리더 선언
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		//숫자 N 입력
		int N = Integer.parseInt(br.readLine());
		//방문처리를 확인할 boolean 배열 선언 
		boolean[] isVisited = new boolean[N+1];
		//BFS를 할 Queue 선언
		Queue<Check> queue = new ArrayDeque<>();
		//Queue에 시작값, 연산횟수 추가
		queue.add(new Check(N,0));
		
		Check temp = null;
		
		//BFS를 돌면서
		while (!queue.isEmpty()) {
			// 값을 뺴서
			 temp = queue.poll();
			 
			 //목푯값인 1에 도착하면 break
			 if (temp.num == 1) {
				 break;
			 }
			 // 만약 이미 방문했다면 더 방문할필요 없음
			 if (isVisited[temp.num]) {
				 continue;
			 }
			 
			 //방문표시
			 isVisited[temp.num] = true;
			 
			 //3으로 나누어 떨어질경우 /3 연산 해준뒤 큐에 넣기
			 if(temp.num%3 == 0) {
				 queue.add(new Check((int)temp.num/3, temp.cnt+1));
			 }
			 
			 //2로 나누어 떨어질경우 /2 연산 해준뒤 큐에 넣기
			 if (temp.num% 2 == 0) {
				 queue.add(new Check((int)temp.num/2, temp.cnt+1));
			 }
			 
			 // -1 연산후 큐에 넣기
			 queue.add(new Check(temp.num-1, temp.cnt+1));
		}
		
		System.out.println(temp.cnt);
	}
	
	static class Check{
		int num,cnt;
		//숫자와 연산 횟수 저장할 클래스 선언
		public Check(int num, int cnt) {
			this.num = num;                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
			this.cnt = cnt;
		}
		
	}
}
