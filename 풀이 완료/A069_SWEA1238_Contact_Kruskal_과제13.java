package 박승수;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.HashSet;

public class A069_SWEA1238_Contact_Kruskal_과제13 {
	static ArrayList<HashSet<Integer>> table;
	static ArrayList<Integer> check;
	
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		for (int test_case = 1; test_case < 11; test_case ++) {	//테스트 케이스 10개를 받는다
			String[] temp = br.readLine().split(" ");
			
			int N = Integer.parseInt(temp[0]);					//명령어? 의 개수 N
			int Start = Integer.parseInt(temp[1]);				//전화를 시작하는 위치
			
			temp = br.readLine().split(" ");
			table = new ArrayList<HashSet<Integer>>(101);			//전화의 관계를 저장할 테이블
			check = new ArrayList<Integer>(101);					//각각 몇번째에 전화를 받았는지의 대해 저장할 check
			for(int idx = 0; idx < 101; idx ++) {
				table.add(new HashSet<Integer>());				//테이블 초기화
				check.add(0);									//체크 초기화
			}
			
			int from;											//전화를 거는 사람을 저장할 변수 선언
			int to;												//전화를 받는 사람을 저장할 변수 선언
			
			for (int idx = 0; idx < N; idx+= 2) {
				from = Integer.parseInt(temp[idx]);				//from 입력
				to = Integer.parseInt(temp[idx+1]);				//to 입력
				table.get(from).add(to);						//table에 관계 입력
			}
			
			System.out.printf("#%d %d\n",test_case,solution(Start));	//결과 출력
		}
		
		

	}
	
	public static int solution(int start) {							//시작점을 받아주고
		ArrayDeque<Integer> queue = new ArrayDeque<Integer>();		//큐를 만들어 준다
		
		int nowNode;				
		queue.add(start);				//시작점을 큐에 넣어주고
		check.set(start, 1);			//시작점에 전화받은 순서 1을 넣어준다
		
		while (!queue.isEmpty()) {		//큐가 빌때까지 진행
			 nowNode = queue.pop();		//큐에서 노드를 하나 빼서
			
			for(int nextNode : table.get(nowNode)) {			//이 노드가 전화가능한 사람들을 순회한다
				if (check.get(nextNode) == 0) {					//만약 전화를 처음받는 사람이라면
					check.set(nextNode, check.get(nowNode)+1);	//전화를 몇번쨰로 받았는지 체크해주고
					queue.add(nextNode);						//큐에 다시 넣어준다
				}
			}

		}
		
		int max = 0;								//전화를 가장 늦게받은 횟수를 저장할 변수
		int answer = 0;								//가장 늦게받은 사람을 저장할 변수
			
		for (int idx = 1; idx < 101; idx ++) {		//모든 사람을 순회하면서
			if (max <= check.get(idx)) {			//만약 가장늦게받았거나, 같을경우
				answer = idx;						//가장 늦게받은 사람을 바꿔준다
				max = check.get(idx);					//전화를 동시에 받았을경우 번호가 큰 순서기 때문에 이렇게 로직 구현
			}
		}
		
		
		return answer;								//정답 리턴
	}

}
