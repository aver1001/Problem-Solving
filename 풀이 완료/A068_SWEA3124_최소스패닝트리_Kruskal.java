package 박승수;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class A068_SWEA3124_최소스패닝트리_Kruskal {
	static int root[];		//부모를 저장할 root 미리 전역변수로 선언

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine());
		
		for (int test_case = 1; test_case < T+1; test_case++) {		//test_case수 만큼 실행
			String[] temp = br.readLine().split(" ");
			int V = Integer.parseInt(temp[0]);						//정점의 개수 V
			int E = Integer.parseInt(temp[1]);						//간선의 개수 E
			
			root = new int[V+1];
			for (int idx = 0; idx <V+1; idx++) {					//루트 자기자신으로 초기화
				root[idx]=idx;
			}
			
			
			ArrayList<pos> posList = new ArrayList<pos>();
			
			for (int idx = 0; idx < E; idx ++) {
				temp = br.readLine().split(" ");
				int A = Integer.parseInt(temp[0]);					//A와 B는 C의 가중치로 연결되어있
				int B = Integer.parseInt(temp[1]);
				int C = Integer.parseInt(temp[2]);
				posList.add(new pos(A,B,C));						//좌표들을 넣어준다
			}
			Collections.sort(posList, (o1,o2) -> o1.Cost-o2.Cost);	// Cost 오름차순 기준으로 정렬
			
			long answer = 0;
			for (pos tempPos :posList ) {							//간선들을 돌면서
				if (find(tempPos.A) != find(tempPos.B)) {			//서로의 부모가 다를경우
					union(tempPos.A,tempPos.B);						//두개를 합쳐준다
					answer += tempPos.Cost;							//이 간선을 사용할 것이기 때문에 총 가중치에 더해준다
				}
				
			}
			System.out.printf("#%d %d\n",test_case,answer);			//테스트케이스와 총 가중치를 더해준다
			
		}

	}
	
	public static class pos{
		int A;
		int B;
		int Cost;
		
		public pos(int a, int b, int cost) {
			super();
			A = a;
			B = b;
			Cost = cost;
		}
	}
	
	public static void union(int a, int b) {		//두 부모를 찾아 결합시켜주는 메소드
		a = find(a);								//a의 부모를 찾고
		b = find(b);								//b의 부모를 찾고
		
		if (a > b) {								// 큰친구를 작은쪽으로 합쳐줌
			root[b] = a;
		}else {
			root[a] = b;
		}
		
	}
	
	public static int find(int x) {					//부모를 찾는 메소드
		if (x != root[x]) {							//부모가 자기자신일떄까지 재귀적으로 찾아
			return root[x] = find(root[x]);
		}
		return root[x];
		
	}

}

