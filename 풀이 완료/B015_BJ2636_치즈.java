package 박승수;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;

public class B015_BJ2636_치즈 {
	static int[][] board;			//치즈의 정보를 저장할 배열
	static boolean[][] isMelted;	//한시간이 지난후 녹을 치즈들을 저장할 배열
	static int Y;					//치즈를 놓은 곳의 세로 크기
	static int X;					//치즈를 놓은 곳의 가로 크기
	
	static int[] dy = {0,0,1,-1};	//4방향 탐색할 배열선언
	static int[] dx = {1,-1,0,0};
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] temp;
		
		temp = br.readLine().split(" ");
		Y = Integer.parseInt(temp[0]);				//치즈판의 세로 크기
		X = Integer.parseInt(temp[1]);				//치즈판의 가로 크기
		
		board = new int[Y][X];						//치즈판 초기화
		
		for(int y = 0; y< Y; y++) {					//치즈판 입력
			temp = br.readLine().split(" ");
			for(int x = 0; x < X; x ++) {
				board[y][x] = Integer.parseInt(temp[x]);
			}
		}
		
		solution();	//문제 해결
		
	}
	
	public static void solution() {
		/*
		 * 문제를 해결할 메인 함수.
		 * 치즈가 다 녹을때까지 녹는 치즈를 찾고.
		 * 녹여주고, 다 녹을때까지의 시간과, 직전의 치즈 개수를 출력한다.
		 */
		
		int meltTemp;			//몇개를 녹였는지 저장할 임시 변수
		int answer=0;			//1시간전 남은 치즈의 개수를 저장할 변수
		int cnt = 0;			//치즈를 다 녹이는데 몇시간이 걸렸는지 저장할 변수 
		while (true) {
			findMeltCheese();			//공기에 맞닿아 녹을 치즈들을 찾고
			meltTemp = meltCheese();	//치즈를 녹인뒤, 녹은 치즈들의 개수를 리턴받는다.
			
			if (meltTemp == 0) {		//만약 녹은 치즈가 하나도 없다면.
				break;					//다 녹인것이기 때문에 탈출한다
			}
			cnt ++;						//치즈가 녹았다면, 1시간을 추가해주고
			answer = meltTemp;			//녹은 치즈의 개수를 저장해놓는다.
		}
		
		System.out.println(cnt);		//다 녹는것 몇초 걸렸는지 출력
		System.out.println(answer);		//1시간전에는 몇개 남았었는지 출력
		
	}
	
	public static void findMeltCheese() {
		/*
		 * 녹을 치즈를 찾는 함수.
		 * 왼쪽맨위는 무조건 비어있기 때문에 0,0에서 시작해서
		 * BFS를 돌며 공기라면 계속 BFS를 돌아준다.
		 * 이때, isMelted 변수로 방문체크와, 녹일치즈를 동시에 체킹해준다.
		 * 		=> BFS를 돌며, 방문체크를 해주고, 공기라면 큐에 추가, 치즈라면 추가하지 않는다.
		 */
		isMelted = new boolean[Y][X];	//방문체크와 녹은치즈를 동시에 저장할 변수
		
		Queue<Loc> queue = new ArrayDeque<>();	//BFS를 사용할 큐를 생성하고
		queue.add(new Loc(0,0));				//왼쪽 맨위, 0,0 을 넣어준다
		
		Loc temp;		//큐에서 뺀 위치를 저장할 변수
		int ty;			//4방탐색시 y좌표를 저장할 변수
		int tx;			//4방탐색시 x좌표를 저장할 변수
		
		while(!queue.isEmpty()) {		//큐가 빌때까지
			temp = queue.poll();		//큐에서 하나 뺀뒤
			
			for (int idx = 0; idx < 4; idx ++) {	//4방탐색을 진행하며
				ty = temp.y+dy[idx];
				tx = temp.x+dx[idx];
				
				//좌표를 넘어가지 않고, 아직 방문 안했을경우
				if(isRange(ty, tx) && isMelted[ty][tx] == false) {
					isMelted[ty][tx] = true;	//방문표시 해주고
					if (board[ty][tx] == 0) {	//만약 치즈가 아니라면 큐에 넣어준다.
						queue.add(new Loc(ty,tx));
					}
				}
			}
		}
	}
	
	public static int meltCheese() {
		/*
		 * 녹일 치즈를 탐색했다면
		 * 실제로 치즈를 녹이는 함수.
		 * 치즈를 녹인 뒤 몇개의 치즈를 녹였는지 리턴함.
		 */
		
		int meltCnt = 0;	//녹인 치즈의 개수를 저장할 변수
		for(int y=0; y<Y; y++) {		//모든 곳을 방문하면서
			for(int x=0; x<X; x++) {
				//방문했고, 치즈라면
				if(isMelted[y][x] == true && board[y][x] == 1) {
					board[y][x] = 0;	//빈칸으로 바꿔주고
					meltCnt ++;			//하나 녹였다고 표시
				}
			}
		}
		return meltCnt;	//녹인 치즈의 개수 리턴
	}
	
	public static boolean isRange(int y, int x) {
		/*
		 * 좌표가 board의 범위를 벗어나는지, 벗어나지 않는지 확인해서
		 * boolean으로 리턴하는 함수
		 */
		if(0 <= y && y < Y && 0 <=x && x<X ) {
			return true;
		}
		return false;
	}
	
	static class Loc{
		int y;
		int x;
		public Loc(int y, int x) {
			super();
			this.y = y;
			this.x = x;
		}
	}
	
}
