package 박승수;
import java.util.*;
public class A009_BJ15649_N과M_1 {
	
	static int[] numbers; //조합 넣을 배열 선언
	static boolean[] isSelected; //선택했는지 확인용 배열 선언
	static int N; // N C M
	static int M; // N C M
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in); //입력받을 Scanner 객체 생성
		
		N = sc.nextInt(); // N 입력
		M = sc.nextInt(); // M 입력
		isSelected = new boolean[N+1]; // 0번 인덱스 pass하고 선택하기 때문에 N+1 까지 선언해야 out of index 안남
		numbers = new int[M]; // 조합을 넣을 배열 선택할 개수 M으로 초기화
		permutation(0); // 조합 재귀 시작
	}
	
	public static void permutation(int n) {
		if (n== M) { // 원하는 조합의 개수가 완성되었을경우
			for(int idx=0; idx<M; idx++) { // 각각의 순서를 순회하며
		    	System.out.print(numbers[idx] + " "); //출력
		    }
			System.out.println(); // 개행 출력
			return;
		}
		
		for (int idx = 1; idx <= N; ++idx) { // 1번부터 순서대로 선택하면서
			if (isSelected[idx]) { // 선택햇다면
				continue; // 넘어감
			}
			numbers[n] = idx;  // 지금 순서에 선택한 숫자 넣어줌
			isSelected[idx] = true; // 선택했다고 표시
			permutation(n+1); // 재귀 
			isSelected[idx] = false; // 선택한거 풀어주기 
		}
	}

}
