package 박승수;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class A056_BJ1260_DFS와BFS {
	static HashMap<Integer,HashSet<Integer>> nodeInfo;
	static boolean[] isVisited; 
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] temp = br.readLine().split(" ");
		int N = Integer.parseInt(temp[0]);					//정점의 개수 N
		int M = Integer.parseInt(temp[1]);					//간선의 개수 M
		int V = Integer.parseInt(temp[2]);					//시작 정점의 번호 V
		
		nodeInfo = new HashMap<Integer,HashSet<Integer>>();	//노드 정보를 저장할 HashMap, 중복 제거를 위해 value를 Set으로 설정
		
		
		for (int idx = 1; idx < N+1; idx++) {
			nodeInfo.put(idx, new HashSet<Integer>());		//노드 정보 초기
		}
		
		for (int idx = 0; idx < M; idx ++) {
			temp = br.readLine().split(" ");				//노드 정보 삽입 
			int a = Integer.parseInt(temp[0]);
			int b = Integer.parseInt(temp[1]);
			
			nodeInfo.get(a).add(b);
			nodeInfo.get(b).add(a);
		}
		isVisited = new boolean[N+1];						//방문 확인 배열 초기화
		isVisited[V] = true;								//초기 방문노드는 방문했다고 표시
		DFS(V);												//DFS 진행 
		System.out.println();
		
		isVisited = new boolean[N+1];						//방문 확인 배열 초기화
		isVisited[V] = true;								//초기 방문 노드는 방문 했다고 표시
		BFS(V);												//BFS 진행 
		
		
	}
	
	public static void DFS(int node) {
		System.out.printf("%d ",node);			//방문한 노드 출력 
		
		ArrayList<Integer> temp = new ArrayList<Integer>(nodeInfo.get(node));	//방문해야할 노드 List로 뺴서
		Collections.sort(temp);													//오름차순 정렬
		
		for (int idx = 0; idx < temp.size(); idx ++) {				//방문해야할 노드들 순회하면서
			int nextNode = temp.get(idx);
			
			if (isVisited[nextNode] == false) {						//방문하지 않았을경우
				isVisited[nextNode] = true;							//방문했다고 표시 후
				DFS(nextNode);										//DFS 진행 
			}
		}
		
	}
	
	public static void BFS(int initNode) {
		Deque<Integer> queue = new ArrayDeque<Integer>();			//BFS 진행할 큐 만들기
		isVisited[initNode] = true;									//초기노드 방문했다고 표시
		queue.addLast(initNode);									//초기노드 큐에 넣어줌
		
		while (queue.size() !=0) {
			int node = queue.removeFirst();							//큐에서 하나 제거
			System.out.printf("%d ",node);							//방문한 노드 출력
			ArrayList<Integer> temp = new ArrayList<Integer>(nodeInfo.get(node));	//방문해야할 노드 List로 뺴서
			Collections.sort(temp);									//오름차순 정렬 
			
			for (int idx = 0; idx < temp.size(); idx ++) {
				int nextNode = temp.get(idx);
				
				if (isVisited[nextNode] == false) {					//방문하지 않았을경우
					isVisited[nextNode] = true;						//방문했다고 표시 후
					queue.addLast(nextNode);						//BFS 진행하기 위해 큐에 삽입 
				}
			}
		}
	}
}



