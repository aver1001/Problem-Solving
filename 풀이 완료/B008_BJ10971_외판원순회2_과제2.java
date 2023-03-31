package 박승수;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class B008_BJ10971_외판원순회2_과제2 {
	static boolean[] isVisited;
	static int[][] cost;
	static int N;
	static int start;
	
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		//장소의 갯수 N
		N = Integer.parseInt(br.readLine());
		//이동간의 cost를 저장할 배열
		cost = new int[N][N];
		
		//배열 입력
		String[] temp;
		for (int y= 0; y < N; y ++) {
			temp = br.readLine().split(" ");
			for (int x = 0; x < N; x++) {
				cost[y][x] = Integer.parseInt(temp[x]);
			}
		}
		
		//방문처리를 저장할 변수
		isVisited = new boolean[N];
		//최솟값을 찾아야 하기 때문에 최대값으로 선언
		int answer = Integer.MAX_VALUE;
		
		//모든 위치를 시작점으로 DFS진행
		for (int i = 0; i < N; i ++) {
			//시작점 표시
			start = i;
			//방문처리
			isVisited[i] = true;
			//DFS 진행
			answer = Math.min(answer,solution(i,0,0)); 
			isVisited[i] = false;
		}
		
		System.out.println(answer);
		
		
	}
	
	public static int solution(int Loc,int cnt,int hap) {
		//만약 순회 다 했다면
		if(cnt == N-1) {
			//시작위치로 이동이 불가능하면
			if (cost[Loc][start] == 0) {
				//불가능한 경우이므로, 최대값 리턴
				return Integer.MAX_VALUE;
			}else {
				//현재까지의 값 + 지금위치에서 시작점까지의 이동의 cost 더해서 리턴
				return hap + cost[Loc][start];
			}
			
		}
		
		//최대값으로 초기화 후
		int min = Integer.MAX_VALUE;
		// 가능한 모든 경우를 다 이동한 후
		for (int nextLoc = 0; nextLoc < N; nextLoc ++) {
			if (isVisited[nextLoc] == false && cost[Loc][nextLoc] != 0) {
				isVisited[nextLoc] = true;
				// 이동들의 최솟값을 받아온뒤
				min = Math.min(min,solution(nextLoc,cnt+1,hap+cost[Loc][nextLoc]));
				isVisited[nextLoc] = false;
			}
		}
		//최솟값 리턴
		return min;
		
	}

}
