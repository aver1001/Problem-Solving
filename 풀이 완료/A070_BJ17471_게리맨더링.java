package 박승수;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class A070_BJ17471_게리맨더링 {
	static int[] root;
	static boolean[] isChoise;
	static int N;
	static ArrayList<ArrayList<Integer>> table;
	static int answer = Integer.MAX_VALUE;
	static int[] population;
	
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		N =Integer.parseInt(br.readLine());		 			//구역의 개수 N
		String[] temp = br.readLine().split(" ");
		population = new int[N];							//구역들의 인구수저장할 배열
		for (int idx = 0; idx < N; idx ++) {
			population[idx] = Integer.parseInt(temp[idx]);	//구역마다 인구수 저장
			
		}
		table = new ArrayList<ArrayList<Integer>>();
		for (int i = 0; i < N; i ++) {
			temp = br.readLine().split(" ");
			table.add(new ArrayList<Integer>());			//구역들의 연결관계 저장
			int t = Integer.parseInt(temp[0]);
			for(int idx = 1; idx < t+1; idx ++) {
				table.get(i).add(Integer.parseInt(temp[idx])-1);
			}
		}
		
		isChoise = new boolean[N];							//부분집합을 위한 isChoise 배열
		
		DFS(0);												//모든 경우의수 실행
		if (answer == Integer.MAX_VALUE)					//만약 결과값이 바뀌지 않았다면, 연결상에 문제가 있다는 것이므로 -1 출
			answer = -1;
		System.out.println(answer);							//최소거리 출력
	}
	
	public static void DFS(int v) {
		if (v == N) {										//부분집합을 다 구했다면
			
			List<Integer> aList = new ArrayList<>();		//aList, bList에 각각의 구역을 넣어주고
			List<Integer> bList = new ArrayList<>();
			for (int i = 0; i < N; i++) {					
				if (isChoise[i])
					aList.add(i);
				else
					bList.add(i);
			}
			if (aList.size() == 0 || bList.size() == 0) 	// 한 구역이라도 있어야함.
				return;
			
			if (check(aList) && check(bList)) { 			// 두 구역이 각각 연결되었는지 확인
				getPeopleDiff(); 							// 인구수의 차이를 구해서 최솟값 업데이트
			}
			return;
		}
		
			isChoise[v] = true;			//부분집합 구해주기
			DFS(v+1);
			isChoise[v] = false;
			DFS(v+1);
	}
	
	private static boolean check(List<Integer> list) {		//지역구들이 이어져 있는지 확인하는 메서드

		Queue<Integer> q = new LinkedList<Integer>();
		boolean[] visited = new boolean[N];
		visited[list.get(0)] = true;
		q.offer(list.get(0));
		
		int count = 1; 					// 방문한 지역 개수
		while (!q.isEmpty()) {			// 0번쨰부터 BFS로 쭉 이어보고
			int cur = q.poll();
			for (int i = 0; i < table.get(cur).size(); i++) {
				int y = table.get(cur).get(i);
				if(list.contains(y) && !visited[y]) { // 선거구에 해당하고, 아직 미방문
					q.offer(y);
					visited[y] = true;
					count ++;
				}
			}
		}
		if(count==list.size())	 // 선거구에 해당하는 지역수와 방문한 지역수가 같은 경우 다 이어져 있음
			return true;
		else					// 다를경우 이어져 있지 않음.
			return false;
	}
	
	private static void getPeopleDiff() { // 3. 선거구의 인구 차 구하기
			
		int pA = 0, pB = 0;
		for (int i = 0; i < N; i++) {
			if (isChoise[i])
				pA += population[i];		//A구역 사람과 
			else
				pB += population[i];		//B구역 사람을 구해서
		}
		int diff = Math.abs(pA - pB);		//두 인구의 차의 절대값으로
		answer = Math.min(answer, diff);	//최솟값을 갱신한다
	}


}

