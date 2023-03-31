package 박승수;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class B009_BJ12865_평범한배낭 {
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] temp = br.readLine().split(" ");
		int N = Integer.parseInt(temp[0]);			//물품의 수 N
		int K = Integer.parseInt(temp[1]);			//버틸수 있는 무게 K
		
		int[][] DP = new int[N+1][K+1];				//납색 진행할 DP
	
		int weight;
		int cost;
		for (int i = 1; i < N+1; i ++) {
			temp = br.readLine().split(" ");
			weight = Integer.parseInt(temp[0]);		//물건의 무게와
			cost = Integer.parseInt(temp[1]);		//가격을 받은뒤
			
			//납색을 진행한다.
			for (int idx = 1; idx < K+1; idx ++) {
				//만약 이 물건보다 가벼운 무게라면
				//이전의 값을 가져와 넣어준다
				if (idx < weight) {
					DP[i][idx] = DP[i-1][idx];
					
				//이 물건을 넣을 수 있다면
				//이전의 값과, 이전에 (지금의 무게 - 이 물건의 무게)의 최대값 + 지금의 물건을 넣는것 중 최대값을 넣어준다
				}else {
					DP[i][idx] = Math.max(DP[i-1][idx],DP[i-1][idx-weight]+cost);
				}
			}
		}
		
		//마지막에 써있는 값이 최대
		System.out.println(DP[N][K]);
		
		
	}
}
