package 박승수;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class A041_SWEA5215_햄버거다이어트 {
	static int N;
	static int L;
	static int Score[] ;
	static int Kcal[] ; 

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));	//입력 받을 StringBuffer
		StringBuilder sb = new StringBuilder();										//출력 할 StringBuilder
		int T = Integer.parseInt(br.readLine());				// TestCase 개수 저장할 T
		for (int test_case = 1; test_case < T+1; test_case++) { // TestCase 만큼 진행
			String[] temp = br.readLine().split(" ");			// 입력
			N = Integer.parseInt(temp[0]);						// 재료의수 N
			L = Integer.parseInt(temp[1]);						// 제한 칼로리 L
			Score = new int[N];									// 각각 음식의 점수를 저장할 ScoreList 배열
			Kcal = new int[N];									// 각각 음식의 칼로리를 저장할 KcalList 배열
			for (int idx = 0; idx < N; idx ++) {
				temp = br.readLine().split(" ");
				Score[idx] = Integer.parseInt(temp[0]);			// 음식의 점수 입력
				Kcal[idx] = Integer.parseInt(temp[1]);			// 음식의 칼로리 입력
			}
			
			sb.append("#").append(test_case).append(" ").append(solution(0,0,0)).append("\n"); // 출
		}
		System.out.println(sb.toString());
		
	}
	
	public static int solution(int v,int score, int kcal) {
		if (kcal > L) return 0;		//제한칼로리를 넘었을경우 0 리턴
		if (v == N) return score;	//마지막 재료까지 선택했을경우 점수 리턴
		return Math.max(solution(v+1,score+Score[v],kcal+Kcal[v]),solution(v+1,score,kcal));
	}

}
