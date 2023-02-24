package 박승수;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class A029_BJ1158_요세푸스문제 {
	static int[] root;
	static int N;

	public static void main(String[] args) throws IOException {
		StringBuilder sb = new StringBuilder();
		sb.append("<");
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] temp =br.readLine().split(" ");
		N = Integer.parseInt(temp[0]); 
		int M = Integer.parseInt(temp[1]);
		
		root = new int[N+1]; // 경로 압축하기 위해 자신의 root를 담을 배열 선언
		
		for (int idx = 0; idx < N+1; idx ++) {
			root[idx] = idx; // root에 자신을 넣음
		}
		int now = M;
		for (int idx = 0; idx < N; idx ++) {

			sb.append(union(now)).append(", "); // 나와 내 다음친구를 union 해준다.
			//다음칸으로 이동
			for(int i = 0; i <M-1; i ++) {
				now = find(now)+1; // 이때 다음칸의 부모를 찾아서 그것을 위치로 잡아준다.
				if (now > N) { // N 넘어갈경우를 위해
					now -= N;
				}
			}
			
			
		}
		sb.deleteCharAt(sb.length()-1);
		sb.deleteCharAt(sb.length()-1);
		sb.append(">");
		System.out.println(sb.toString());
	
	}
	
	public static int union(int a) {
		a = find(a); // 자신의 부모를 찾고
		int b;
		if (a == N) { // 만약 마지막 친구라면
			b = find(1);  // 원형으로 union Find 가능하게 1번째를 찾아봄
		}else {
			b = find(a+1);
		}

		root[a] = b;
		
		return a;

		
	}
	
	public static int find(int x) {
		if (root[x] ==x) { // 자신이 root라면 return x
			return x;
		}
		return root[x] = find(root[x]); // 자신이 root가 아니라면 재귀적으로 구해줌
		
	}

}
