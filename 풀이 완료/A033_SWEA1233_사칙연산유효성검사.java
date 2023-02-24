package 박승수;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
/*
 * 기본적인 풀이방법
 * 연산이 유효하려면 leaf 노드들은 모두 숫자여야하고,
 * 나머지 노드들은 모두 연산자여야 한다.
 */

public class A033_SWEA1233_사칙연산유효성검사 {
	static int N ;
	static String[] Tree;
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		for (int test_case = 1; test_case < 11; test_case++) { // 10개의 테스트 케이스를 돌면서
			N = Integer.parseInt(br.readLine()); // 노드의 개수를 받고
			Tree = new String[N+1]; // 노드의 개수에 맞게 트리를 만들어 준다.
			
			for (int i = 0; i<N; i ++) { // 노드의 개수만큼 반복문을 돌며
				String[] temp = br.readLine().split(" "); // 노드의 정보를 받아서
				Tree[Integer.parseInt(temp[0])] = temp[1]; // 노드의 정보를 넣어준다.
			}
			if (DFS(1)) { // DFS로 연산이 가능한지 확인하고 결과를 출력한다
				System.out.printf("#%d %d\n",test_case,1);
			}else {
				System.out.printf("#%d %d\n",test_case,0);
			}
			
			
		}
			

	}
	
	public static boolean DFS(int node){
		
		boolean s1 = true; // 오른쪽 자식의 상태 true로 초기화
		boolean s2 = true; // 왼쪽 자식의 상태 true로 초기화
		
		if ((node*2)<= N) { // 리프노드가 아닌데 숫자라면
			if (!(Tree[node].equals("-") | Tree[node].equals("+") | Tree[node].equals("*") | Tree[node].equals("/"))){
				return false; //연산 불가능
			}
		}else { // 리프노드인데 연산자라면
			if (Tree[node].equals("-") | Tree[node].equals("+") | Tree[node].equals("*") | Tree[node].equals("/")) {
				return false;
			}
		}
		
		if ((node*2+1)<= N) { // 더 갈 노드가 남아있다면 아래노드들의 상태를 가져옴
			s1 = DFS(node*2+1);
		}
		if (node*2 <= N) { // 더 갈 노드가 남아있다면 아래노드들의 상태를 가져옴
			s2 = DFS(node*2);
		}
		
		return s1 & s2;
	}

}
