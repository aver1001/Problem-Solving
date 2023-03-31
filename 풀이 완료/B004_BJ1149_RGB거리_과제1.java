package 박승수;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;

public class B004_BJ1149_RGB거리_과제1 {
	public static void main(String[] args) throws NumberFormatException, IOException {
		//입력받을 br 선언
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		//거리들의 갯수 입력
		int N = Integer.parseInt(br.readLine());
		//DP겸 거리의색 칠할때의 cost 저장
		ArrayList<ArrayList<Integer>> DP = new ArrayList<ArrayList<Integer>>();
		
		for (int i = 0; i < N; i ++) {
			ArrayList<Integer> temp = new ArrayList<Integer>();
			String[] t = br.readLine().split(" ");
			//i번 거리의 색칠할때의 값들을 입력 받음
			temp.add(Integer.parseInt(t[0]));
			temp.add(Integer.parseInt(t[1]));
			temp.add(Integer.parseInt(t[2]));
			DP.add(temp);
		}
		
		for(int i = 1; i < N; i ++) {
			//DP[i][N] = min(DP[i][0],DP[i][1],DP[i][2]) => 단 자신의 색을 제외
			DP.get(i).set(0, Math.min(DP.get(i-1).get(1), DP.get(i-1).get(2))+DP.get(i).get(0));
			DP.get(i).set(1, Math.min(DP.get(i-1).get(0), DP.get(i-1).get(2))+DP.get(i).get(1));
			DP.get(i).set(2, Math.min(DP.get(i-1).get(0), DP.get(i-1).get(1))+DP.get(i).get(2));
		}
		//마지막 거리의 색들의합의 최솟값 출력
		System.out.println(Math.min(Math.min(DP.get(N-1).get(0),DP.get(N-1).get(1)), DP.get(N-1).get(2)));
	}

}
