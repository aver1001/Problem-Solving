package 박승수;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class A048_BJ3040_백설공주와일곱난쟁이_과제8 {
	static int num[] = new int[9];		// 입력을 받을 배열
	static int answer[] = new int[7];	// 정답을 넣을 배열
	
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		for (int idx = 0; idx < 9; idx++) {					//입력 받아서 배열에 넣기
			num[idx] = Integer.parseInt(br.readLine());
		}
		Combination(0,0,0);			//조합 시작
		
	}
	
	public static void Combination(int v, int start, int sum) {
		if (v == 7) {
			if (sum == 100) {				//합이 100이 됐을경우 출력
				for(int i : answer) {
					System.out.println(i);
				}
			}
			return;
		}
		
		for(int idx = start; idx < 9; idx ++) {		// 조합을 구함
			answer[v] = num[idx];					// 고른 숫자 배열에 넣어줌
			Combination(v+1, idx+1,sum+num[idx]);	// 재귀적으로 조합을 구
		}
	}

}
