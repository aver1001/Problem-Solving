package 박승수;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class A018_BJ2961_도영이가만든맛있는음식 {
	static int N; //재료의 갯수를 받을 변수
	static int[] S; // 재료들의 신맛을 저장할 변수
	static int[] B; // 재료들의 쓴맛을 저장할 변수 
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine()); // 재료의 갯수 입력
		S = new int[N]; // 신맛 저장할 배열변수 초기화 
		B = new int[N]; // 쓴맛 저장할 배열변수 초기화 
		
		String [] temp;
		for (int idx = 0; idx < N; idx ++) { // 재료의 갯수동안 반복문을 돌며
			temp = br.readLine().split(" ");
			S[idx] = Integer.parseInt(temp[0]); // 각각의 배열에 신맛과
			B[idx] = Integer.parseInt(temp[1]); // 쓴맛을 저장한다
		}
		System.out.println(solution(0,1,0)); // 결과 출력 신맛의경우 곱이기 때문에 0이아닌 1을 넣어야함.
		
	}
	
	private static int solution(int n,int sMul, int bHap) { // 몇번째 재료인지 저장할 n, 신맛의 곱 sMul, 쓴맛의 합 bHap
		if (n == N) { // 마지막 재료까지 끝났다면
			if (sMul == 1 && bHap == 0) // 하나도 안넣은 경우
				return Integer.MAX_VALUE; // 최대값을 넣어줘서 불가능하도록 조
			return Math.abs(sMul-bHap); // 신맛과 쓴맛의 차의 절대값을 리턴
		}
		//재료를 넣엇을경우, 재료를 안넣었을경우를 나눠서 그들의 최솟값을 리턴
		return Math.min(solution(n+1,sMul*S[n],bHap+B[n]),solution(n+1,sMul,bHap));
	}

}
