package 박승수;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Queue;

public class B010_BJ14502_연구소 {
	static int Y;						//연구소의 크기 Y,X
	static int X;
	
	static int[] dy = {1,-1,0,0};		//4방향 탐색용 배열 선언
	static int[] dx = {0,0,1,-1};
	
	static int[] Choose = new int[3];	//조합의 선택된것들 저장할 배열
	static ArrayList<Loc> wall;			//벽 설치 가능한 위치들을 저장할 배열 
	static int[][] board;				//연구소의 상태를 저장할 배열
	static int[][] copyBoard;			//초기 연구소 상태를 복사할 배열
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] temp = br.readLine().split(" ");

		Y = Integer.parseInt(temp[0]);			//연구소의 Y,X의 크기 입력 
		X = Integer.parseInt(temp[1]);
		
		board = new int[Y][X];					//연구소 초기화
		copyBoard = new int[Y][X];				//복사연구소 초기화
		
		wall = new ArrayList<Loc>();			//가능한 벽들을 저장할 배열 초기화
		for(int y = 0; y < Y; y ++) {
			temp = br.readLine().split(" ");
			for (int x=0; x < X; x++) {
				board[y][x] = Integer.parseInt(temp[x]);	//연구소의 정보를 넣어주고
				if (board[y][x] == 0) {
					wall.add(new Loc(y,x));					//빈곳일경우 벽 설치가 가능하므로, 벽설치 가능 배열에 넣어줌
				}
			}
		}
		System.out.println(combination(0,0));				//정답 출력
	}
	
	public static int combination(int n,int start) {
		if (n == 3) {
			//복사한뒤 시뮬레이션 후 안전구역 계산
			//복사
			boardCopy();
			//벽설치
			wallSetting();
			//시뮬
			return simualtion();
		}
		int answer = 0;

		//조합을 구해주면서
		for(int i = start; i < wall.size(); i++) {
			Choose[n] = i;
			// 결과의 최대값을 찾고
			answer = Math.max(answer, combination(n+1,i+1));
		}
		// 최대를 리턴해줌
		return answer;
		
	}
	//초기 연구소의 모습을 복사해서 복사배열에 넣어주는 메서드
	public static void boardCopy() {
		for (int y = 0; y < Y; y ++) {
			for (int x= 0; x <X; x ++) {
				copyBoard[y][x] = board[y][x];
			}
		}
	}
	
	//조합으로 선택된 것들에 벽들을 설치해주는 메서드
	public static void wallSetting() {
		for (int c:Choose) {
			copyBoard[wall.get(c).y][wall.get(c).x] = 1;
		}
	}
	
	//벽이 설치가 된후, 바이러스를 확산시키는 메서드
	public static int simualtion() {
		for (int y = 0; y < Y; y ++) {
			for (int x = 0; x < X; x ++) {
				if (copyBoard[y][x] == 2) {
					//바이러스일경우, BFS 돌려봄
					bfs(y, x);
				}
			}
		}
		//안전지대의 개수를 계산해 리턴
		return calSavePoint();
	}
	
	public static void bfs(int y, int x) {
		int ty;
		int tx;
		Loc tempLoc;
		
		//BFS 돌릴 queue를 만들고
		Queue<Loc> queue = new ArrayDeque<>();
		queue.add(new Loc(y,x));
		
		//queue가 빌때까지
		while (!queue.isEmpty()) {
			tempLoc = queue.poll();
			
			//4방향 탐색을 하며
			for (int idx = 0; idx < 4; idx ++) {
				ty = tempLoc.y + dy[idx];
				tx = tempLoc.x + dx[idx];
				
				//범위안에 들고, 빈칸일경우
				if (isRange(ty, tx)){
					//바이러스로 바꿔주고
					copyBoard[ty][tx] = 2;
					//큐에 추가함
					queue.add(new Loc(ty,tx));
				}
			}
		}
		
	}
	
	//이동 가능한지 확인하는 메서드, 범위확인, 빈칸확인
	public static boolean isRange(int y, int x) {
		if (0<= y && y <Y && 0<= x && x<X && copyBoard[y][x] == 0) {
			return true;
		}
		return false;
	}
	
	//시뮬레이션 후 안전지대가 몇개인지 계산하는 메서드
	public static int calSavePoint() {
		int answer = 0;
		for (int y = 0; y < Y; y ++) {
			for (int x= 0; x < X; x++) {
				if (copyBoard[y][x] == 0) {
					answer ++;
				}
			}
		}
		return answer;
	}
	
	public static class Loc{
		int y;
		int x;
		
		public Loc(int y, int x) {
			super();
			this.y = y;
			this.x = x;
		}
		
		
	}
}
