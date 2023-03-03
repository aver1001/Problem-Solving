package 박승수;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.PriorityQueue;

public class A071_BJ1753_최단경로 {
	static int [] minDis;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		String[] temp = br.readLine().split(" ");
		int V = Integer.parseInt(temp[0]);			//정점의 개수
		int E = Integer.parseInt(temp[1]);			//간선의 개수
		
		int K = Integer.parseInt(br.readLine());	//시작점
		
		ArrayList<HashSet<Vertex>> table = new ArrayList<HashSet<Vertex>>(V+1);		// 노드의 관계를 저장할 배열
		
		for (int idx = 0;idx < V+1; idx ++) {
			table.add(new HashSet<Vertex>());			//배열 초기화
		}
		
		for (int idx = 0; idx < E; idx ++) {
			temp = br.readLine().split(" ");
			int u = Integer.parseInt(temp[0]);			//시작점
			int v = Integer.parseInt(temp[1]);			//끝점
			int cost = Integer.parseInt(temp[2]);		//거리
			
			table.get(u).add(new Vertex(u, v, cost));	//관계 저장
		}
		
		
		minDis = new int[V+1];							//거리를 저장할 배열 변수 최대치로 초기화
		for (int idx = 0; idx < V+1; idx ++) {
			minDis[idx] = Integer.MAX_VALUE;
		}
		
		PriorityQueue<Vertex> PQ = new PriorityQueue<Vertex>();
		PQ.add(new Vertex(K, K, 0));					//PQ 에 시작점을 넣어주고
		minDis[K] = 0;									//시작점 거리는 0으로 초기화 한다
		while (!PQ.isEmpty()) {
			Vertex nowVertex = PQ.poll();				//큐에서 빼서
			
			for (Vertex nextVertex : table.get(nowVertex.to)) {		//큐에서 갈수있는곳 중
				if ( minDis[nextVertex.to]> nextVertex.weight + nowVertex.weight) {	//여태까지의 거리 + 지금 움직일 거리가 최소일경우
					minDis[nextVertex.to] = nextVertex.weight + nowVertex.weight;	//최솟값을 업데이트해주고
					PQ.add(new Vertex(nextVertex.to,nextVertex.to,minDis[nextVertex.to]));	//큐에 넣어준다
				}
			}
		}
		
		StringBuilder sb = new StringBuilder();		
		for(int idx = 1; idx < V+1; idx ++) {
			if (minDis[idx] == Integer.MAX_VALUE) {		//최소거리가 최대일경우
				sb.append("INF").append("\n");			//무한대로 출력한다
			}else {
				sb.append(minDis[idx]).append("\n");	//최소거리를 출력한다
			}
		}
		
		System.out.println(sb.toString());
		
		
		
	}
	
	public static class Vertex implements Comparable<Vertex>{
		int from;
		int to;
		int weight;
		
		public Vertex(int from, int to, int weight) {
			this.from = from;
			this.to = to;
			this.weight = weight;
		}

		@Override
		public int compareTo(Vertex o) {
			return Integer.compare(this.weight, o.weight);
		}
		
	}

}
