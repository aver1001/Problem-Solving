package 박승수;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;
public class A014_BJ15650_N과M_2 {
	static int N; // 입력받을 N 선언
	static int M; // 입력받을 M 선언 
	static int[] numbers; // 결과값 입력받을 numbers 선언
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); //입력 받을 BufferReader 선언
		String[] arr = br.readLine().split(" "); // 공백을 문자열 분리
		N = Integer.parseInt(arr[0]); // 분리후 0번 인덱스를 정수로 바꿔서 N으로 설정
		M = Integer.parseInt(arr[1]); // 분리후 1번 인덱스를 정수로 바꿔서 M으로 설정
		numbers = new int[M]; // 입력받은 M으로 결과값 저장할 numbers 초기화
		combination(0,0); // 조합 시작

	}
	
	public static void combination(int n, int start) {
		if (n == M) { // 만약 M까지 모두 선택했다면
			StringBuilder sb = new StringBuilder(); // 스트링빌더를 선언후
			for (int i : numbers) { // 결과값을 순회하면서
				sb.append(i).append(" "); // 스트링 빌더에 결과값 append 해줌
			}
			System.out.println(sb.toString()); // 결과값 출력
			return; // 재귀 정지
		}
		
		for(int idx = start+1; idx < N+1; idx ++) { // 이미 고른것 초과해서 순회시작
			
			numbers[n] = idx; // 결과값 넣어주기
			combination(n+1,idx); // 재귀적으로 다시 불러오기 
		}
	}

}
