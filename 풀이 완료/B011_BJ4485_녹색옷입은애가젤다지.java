package 박승수;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;

public class B011_BJ4485_녹색옷입은애가젤다지 {
	static int [][] board;
	static int [][] DP;
	static int N;
	
	static int[] dy = {0,0,1,-1};
	static int[] dx = {1,-1,0,0};
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		
		String[] temp;
		//몇번째 테스트 케이스 인지 출력할 변수
		int cnt = 1;
		while (true) {
			N = Integer.parseInt(br.readLine());
			//N == 0 일경우 입력의 끝임
			if(N == 0) {
				break;
			}
			
			//도둑루피들의 비용저장할 배열
			board = new int[N][N];
			//DP를 저장할 배열
			DP = new int[N][N];
			
			//입력 받으며, DP는 Max로 초기화
			for(int y = 0; y<N; y ++) {
				temp = br.readLine().split(" ");
				for(int x = 0; x < N; x ++) {
					board[y][x] = Integer.parseInt(temp[x]);
					DP[y][x] = Integer.MAX_VALUE;
				}
			}
			
			//BFS용 queue생성 
			Queue<Loc> queue = new ArrayDeque<Loc>();
			
			//Queue에다 0,0 넣기 
			queue.add(new Loc(0,0,board[0][0]));
			Loc tempLoc;
			
			//Queue가 비워질때까지 BFS 돌면서 
			while(!queue.isEmpty()) {
				tempLoc = queue.poll();
				
				//4방향 탐색
				for(int idx = 0; idx < 4; idx ++) {
					int ty = tempLoc.y + dy[idx];
					int tx = tempLoc.x + dx[idx];
					
					//범위안에 들어오고, 이 곳에 도착했을때의 최솟값일경우
					if (isRange(ty, tx) && DP[ty][tx] > tempLoc.score+board[ty][tx]) {
						//DP 업데이트 해주고
						DP[ty][tx] = tempLoc.score+board[ty][tx];
						//Queue에 넣어준다
						queue.add(new Loc(ty,tx,tempLoc.score+board[ty][tx]));
					}
				}	
			}
			//출력
			sb.append("Problem ").append(cnt++).append(": ").append(DP[N-1][N-1]).append("\n");
		}
		
		System.out.println(sb.toString());
	}
	
	
	public static boolean isRange(int y, int x) {
		//범위 확인
		if (0 <= y && y < N && 0 <= x && x< N) {
			return true;
		}
		return false;
	}
	
	public static class Loc{
		int y;
		int x;
		int score;
		public Loc(int y, int x, int score) {
			super();
			this.y = y;
			this.x = x;
			this.score = score;
		}
	}
}
