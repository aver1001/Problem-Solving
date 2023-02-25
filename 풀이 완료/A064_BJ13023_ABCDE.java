package 박승수;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.HashSet;

public class A064_BJ13023_ABCDE {
	static HashMap<Integer, HashSet<Integer>> table;
	static boolean[] isVisted;
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] temp = br.readLine().split(" ");
		int N = Integer.parseInt(temp[0]);					//사람의 수 N
		int M = Integer.parseInt(temp[1]);					//친구와의 관계수 M
		
		table = new HashMap<Integer, HashSet<Integer>>();	//노드들을 저장할 hashMap 선언
		isVisted = new boolean[N];
		
		for (int idx = 0; idx < N; idx++) {
			table.put(idx, new HashSet<Integer>());			//초기화
		}
		
		
		for (int idx = 0; idx < M; idx ++) {
			temp = br.readLine().split(" ");
			int A = Integer.parseInt(temp[0]);				//노드들을에게 서로를 연결시켜준다
			int B = Integer.parseInt(temp[1]);
			table.get(A).add(B);
			table.get(B).add(A);
		}
		for (int idx = 0; idx < N; idx ++) {				// 시작지점을 모든 시작지점에서 시작하고
			isVisted[idx] = true;							// 방문했다고 표시 후 
			solution(0,idx);								// 재귀적으로 구해본다
			isVisted[idx] = false;							// 표시 제거해준다
		}
		
		System.out.println(0);								// 이런 경우가 없다면 0 출력
		

	}
	
	static public void solution(int v, int node) {
		if (v == 4) {					//재귀가 4깊이 까지 깊어진다면 친구 5명이 있는것이므로
			System.out.println(1);		//1출력하고 
			System.exit(0);				//종료 
		}
		
		for (int nextNode : table.get(node)) {		//갈수있는 노드들을 방문하면서
			if(isVisted[nextNode] == false) {		//방문하지 않은 노드라면
				isVisted[nextNode] = true;			//방문체크 해주고
				solution(v+1,nextNode);				// 다음 노드로 진행
				isVisted[nextNode] = false;			//방문체크 풀어주기
			}
		}
	}


}
