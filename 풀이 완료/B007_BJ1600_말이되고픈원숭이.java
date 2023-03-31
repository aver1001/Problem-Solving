package 박승수;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;

public class B007_BJ1600_말이되고픈원숭이 {
	static int[] Hdy = {-2,-2,-1,-1,1,1,2,2};	//말의 움직임
	static int[] Hdx = {-1,1,-2,2,-2,2,-1,1};
	static int[] dy = {-1,0,0,1};				//원숭이의 움직임
	static int[] dx = {0,-1,1,0};
	
	static int[][] board;
	static int Y;
	static int X;
	static int K;
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		K = Integer.parseInt(br.readLine());
		String[] temp = br.readLine().split(" ");
		X = Integer.parseInt(temp[0]);
		Y = Integer.parseInt(temp[1]);
		
		//벽의 정보를 저장할 배열 선언
		board = new int[Y][X];
		//이동횟수를 저장할 배열 말의 움직임의 횟수를 저장
		int[][][] DP = new int[Y][X][K+1];
		
		//벽 정보 입력
		for(int y = 0 ; y < Y; y++) {
			temp = br.readLine().split(" ");
			for(int x = 0; x < X; x ++) {
				board[y][x] = Integer.parseInt(temp[x]);
			}
		}
		
		
		//BFS 돌릴 큐 선언
		Queue<Loc> queue = new ArrayDeque<Loc>();
		//큐에 초기값 넣고
		queue.add(new Loc(0,0,0,0));
		Loc tempLoc = null;
		int ty;
		int tx;
		
		//BFS 시작
		while (!queue.isEmpty()) {
			tempLoc = queue.poll();
			
			//만약 마지막 위치에 도착했다면 움직임의 횟수 출력하고 종료
			if(tempLoc.y == Y-1 && tempLoc.x == X-1) {
				System.out.println(tempLoc.cnt);
				System.exit(0);
			}
			
			//만약 말의 움직임이 아직 가능할경우
			if (tempLoc.useK < K) {
				//말의 움직임으로 가능한 8가지 경우를 돌면서
				for(int idx = 0; idx < 8; idx ++) {
					ty = tempLoc.y + Hdy[idx];
					tx = tempLoc.x + Hdx[idx];
					//범위내에 있고, 방문하지 않았거나, 더 작은값으로 왔을경우 이동한다
					if (isRange(ty, tx) && (DP[ty][tx][tempLoc.useK+1] == 0 ||tempLoc.cnt+1 < DP[ty][tx][tempLoc.useK+1])) {
						//몇번의 이동으로 왔는지 저장해주고
						DP[ty][tx][tempLoc.useK+1] = tempLoc.cnt+1;
						//큐에 넣어준다
						queue.add(new Loc(ty, tx, tempLoc.cnt+1,tempLoc.useK+1));
					}
				}
				
			}
			//일반적인 원숭이의 움직임 이동 4가지 경우를 돌면서
			for(int idx = 0; idx < 4; idx ++) {
				ty = tempLoc.y + dy[idx];
				tx = tempLoc.x + dx[idx];
				//범위내에 있고, 방문하지 않았거나, 더 작은값으로 왔을경우 이동한다
				if(isRange(ty, tx)&& (DP[ty][tx][tempLoc.useK] == 0 ||tempLoc.cnt+1 < DP[ty][tx][tempLoc.useK])) {
					//몇번의 이동으로 왔는지 저장해주고
					DP[ty][tx][tempLoc.useK] = tempLoc.cnt+1;
					//큐에 넣어준다
					queue.add(new Loc(ty, tx, tempLoc.cnt+1,tempLoc.useK));
				}
			}
			
			
		}
		
		//도착하지 못했을경우 -1을 출력한다
		System.out.println(-1);
	}
	
	public static boolean isRange(int y, int x) {
		if(0<= y && y < Y && 0<= x && x<X && board[y][x] == 0) {
			return true;
		}
		return false;
		
	}
}

class Loc{
	int y;
	int x;
	int cnt;
	int useK;
	public Loc(int y, int x, int cnt,int useK) {
		super();
		this.y = y;
		this.x = x;
		this.cnt = cnt;
		this.useK = useK;
	}
}
