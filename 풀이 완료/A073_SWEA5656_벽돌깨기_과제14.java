package 박승수;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

/*
 * 프림알고리즘과 다엑스트라 알고리즘의 차이점.
 *
 * 프림 알고리즘은 MST 최소 신장트리를 구하는 알고리즘이고
 * 다엑스트라는 한 정점에서 모든 정점까지의 거리를 구하는 알고리즘이다.
 *
 * 그렇기 때문에 알고리즘 구성에서 약간의 차이가 있다.
 * 프림 알고리즘은 단순히 방문여부를 저장해놓고 방문했다면 넘어가지만
 * 다엑스트라 알고리즘은 거리를 저장해놓고 최소거리보다 작을경우만 진행한다.
 * 
 */

public class A073_SWEA5656_벽돌깨기_과제14 {
	static int X;					//너비를 저장할 변수
	static int Y;					//높이를 저장할 변수
	static int N;					//최대 구슬 발사 횟수를 저장할 변수
	
	static int[] dy = {0,0,1,-1};	//탐색을 위한 방향 미리 설정
	static int[] dx = {1,-1,0,0};	
	
	static int answer;				//정답을 저장할 변수

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int T = Integer.parseInt(br.readLine());
		
		for (int test_case = 1; test_case < T+1; test_case ++) {	//테스트 케이스 수 입력
			String[] temp = br.readLine().split(" ");
			N = Integer.parseInt(temp[0]);							//구슬 발사 횟수 저장
			X = Integer.parseInt(temp[1]);							//너비 저장
			Y = Integer.parseInt(temp[2]);							//높이 저장
			answer = Integer.MAX_VALUE;								//남은 벽돌의 최솟값을 구해야하기 때문에 최대값으로 초기화
			
			int[][] board = new int[Y][X];							//벽돌상태 초기화
			
			for (int y = 0; y < Y; y ++) {
				temp = br.readLine().split(" ");
				for (int x = 0; x < X; x ++) {
					board[y][x] = Integer.parseInt(temp[x]);		//벽돌 상태 저장
				}
			}
			solution(0, board);										//해결 로직 실행
			System.out.printf("#%d %d\n",test_case,answer);			//남은 벽돌의 최솟값 출력
		}
	}
	
	public static void solution(int v, int[][] board) {				//정답을 구하는 메서드 DFS적으로 모든 경우를 구한다
		if (v == N) {												//마지막 구슬까지 쐈을경우
			remainWall(board);										//남은 벽돌의 최소를 업데이트 해준다
			return;
		}
		
		int[][] tempBoard;											//임시저장 보드를 만들어놓고
		for (int x = 0; x < X; x++) {								//모든 x에서
			tempBoard = boardCopy(board);							//보드를 복사한뒤
			dropBall(x,tempBoard);									//복사한 보드에서 x좌표에 구슬을 떨어트려본다
			solution(v+1,tempBoard);								//다음 구슬로 넘어간다
		}
		
	}
	
	public static void dropBall(int x, int[][] board) { 			//x지점에서 구슬을 쏘는 메서드
		for (int y = 0; y < Y; y++) {								//x지점에서 y축 전체를 확인하면서
			if( board[y][x] != 0) {									//벽돌일 경우
				distoryWall(y,x,board,board[y][x]);					//벽돌을 파괴하고
				break;												//종료한다
			}
		}
		downWall(board);											//벽돌들을 내린다
	}
	
	public static void distoryWall(int y, int x, int[][] board,int range) {	//벽돌을 파괴하는 메서드 
		int ty;					//임시변수 미리 선언
		int tx;					//임시변수 미리 선언
		
		for (int idx = 0; idx < 4; idx ++) {		//4방향을 돌면서
			
			for(int dis = 1; dis < range; dis++) {	//벽돌의 파괴 범위만큼의 범위까지 확인한다
				ty = y+dy[idx]*dis;					//다음 위치에 가서
				tx = x+dx[idx]*dis;
				if (RangeCheck(ty, tx)) {			//범위안에 들어가고
					if (board[ty][tx] != 1 && board[ty][tx] != 0) {	//범위가 2 이상이라 더 확인해야 할 경우
						int nextRange = board[ty][tx];				//다음범위를 미리 뺴놓은뒤
						board[ty][tx] = 0;							//0으로 파괴하고
						distoryWall(ty,tx,board,nextRange);			//재귀적으로 넘겨준다
					}else {
						board[ty][tx] = 0;							//더 확인 필요 없으면 0으로 바꿔주고 넘겨준다
					}
				}else {								//범위밖을 벗어났을경우
					break;							//멈춰준다
				}
			}
		}
		
		board[y][x] = 0;							//자기 자신 위치 0으로 변경
		
	}
	
	public static void downWall(int[][] board) {				//파괴된 벽들을 아래로 내리는 메서드
		for (int x = 0; x < X; x ++) {	//x축을 순서대로 돌면서
			for (int sub = 1; sub < Y; sub ++) {
				for (int y = 0; y < Y-sub; y ++) {	//y축 0번 인덱스부터 시작해서 자기인덱스 +1이 0 이라면 sawp 해준다(버블정렬같은 느낌)
					if (board[y+1][x] == 0) {
						int temp = board[y][x];
						board[y][x] = 0;
						board[y+1][x] = temp;
					}
				}
			}
			
		}
		
	}
	
	public static boolean RangeCheck(int y, int x) {	//범위를 벗어나는지 확인하는 메서드
		if (0 <= y && y < Y && 0 <= x && x < X) {		//상하좌우 범위를 넘어가지 않았을경우
			return true;								//true return
		}
		return false;									//아닐경우 false return
	}
	
	public static void printBoard(int[][] board) {		//디버깅용 보드 출력하는 메서드
		for(int[] arr : board) {
			System.out.println(Arrays.toString(arr));
		}
		System.out.println();
	}
	
	public static int[][] boardCopy(int[][] board) {	//보드를 복사하는 메서드
		int[][] tempBoard = new int[Y][X];				//복사할 임시보드를 선언하고
		
		for (int y = 0; y < Y; y++) {					//복사를 진행해준다
			for (int x = 0; x < X; x++) {
				tempBoard[y][x] = board[y][x];
			}
		}
		
		return tempBoard;								//복사한 배열 리턴
	}
	
	public static void remainWall(int[][] board) {		//남은 벽돌의 개수를 세는 메서드
		int hap = 0;									//총합을 저장할 변수를 선언하고
		for (int y = 0; y < Y; y++) {
			for (int x = 0; x < X; x ++) {
				if (board[y][x] != 0) {					//벽돌이 있을경우
					hap ++;								//총합 +1 
				}
			}
		}
		
		answer = Math.min(answer, hap);					//최솟값 업데이트
	}

}
