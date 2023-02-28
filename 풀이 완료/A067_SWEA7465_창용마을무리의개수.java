package 박승수;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashSet;

public class A067_SWEA7465_창용마을무리의개수 {
	static int[] root;
	
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine());
		
		for (int test_case = 1; test_case < T+1; test_case ++) {
			String[] temp = br.readLine().split(" ");
			int N = Integer.parseInt(temp[0]);				//총 원소의 개수 N
			int M = Integer.parseInt(temp[1]);				//입력의 개수 N
			
			root = new int[N+1];							//부모들 넣을 배열 선언
			
			for (int idx = 0; idx < N+1; idx++) {			//부모들 초기화
				root[idx] = idx;
			}
			
			for (int idx = 0; idx < M; idx ++) {
				temp = br.readLine().split(" ");			//A,B를 받아서 유니온 파인드
				int A = Integer.parseInt(temp[0]);
				int B = Integer.parseInt(temp[1]);
				
				union(A,B);
			}
			
			HashSet<Integer> Set = new HashSet<Integer>(); 	//중복제거를 위한 Set	
			
			for (int idx = 1; idx <N+1; idx ++) {				//각각의 원소들의
				Set.add(find(idx));								//부모를 찾아서 Set에 넣어 중복제거를 해준다
			}
			
			System.out.printf("#%d %d\n",test_case,Set.size());	//Set의 원소 개수를 출력한다

			
		}
		
	}

	 public static void union(int a, int b) {
	        a = find(a);			//서로의 부모를 찾아서
	        b = find(b);
	         
	        if (a<b) {				//부모를 바꿔준다
	            root[b] = a;		//작은값을 기준으로 병합
	        }else {
	            root[a] = b;
	        }
	    }
	     
	    public static int find(int x) {
	        if (x != root[x]) {						//최상위 부모가 아닐경우
	            return root[x] = find(root[x]);		//내 부모를 찾는다
	        }
	         
	        return root[x];							//내 부모 리턴
	    }
}
