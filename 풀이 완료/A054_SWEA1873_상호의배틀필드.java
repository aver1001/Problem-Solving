package 박승수;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class A054_SWEA1873_상호의배틀필드 {
	static int Y;					//맵의 크기
	static int X;					
	static int[] dy = {0,0,-1,1};	//왼 오 위 아래
	static int[] dx = {-1,1,0,0};
	static Tank tank;				//탱크
	static char[][] board;			//맵 초기화
	
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine());
		
		for (int test_case = 1; test_case < T+1; test_case ++ ) {
			String [] temp = br.readLine().split(" ");
			Y = Integer.parseInt(temp[0]);					//Y크기 입력
			X = Integer.parseInt(temp[1]);					//X크기 입력
			board = new char[Y][X];
			
			for (int y = 0;  y< Y; y++) {					//맵의 정보를 받아오면서
				String t = br.readLine();					//탱크의 위치를 파악한다.
				for (int x = 0; x < X; x++) {				//탱크 위치가 파악되었다
					board[y][x] = t.charAt(x);				//방향과 위치를 넣어 탱크를 초기화한다.
					if (board[y][x] == '<') {
						tank = new Tank(0,y,x);
						board[y][x] = '.';
					}else if (board[y][x] == '>') {
						tank = new Tank(1,y,x);
						board[y][x] = '.';
					}else if (board[y][x] == '^') {
						tank = new Tank(2,y,x);
						board[y][x] = '.';
					}else if (board[y][x] == 'v') {
						tank = new Tank(3,y,x);
						board[y][x] = '.';
					}
						
				}
			}
			int N = Integer.parseInt(br.readLine());		//명령어의 개수 N
			String Commend = br.readLine();
			
			for (int idx = 0; idx < N; idx ++) {
				if (Commend.charAt(idx) == 'U') {			//U명령어일경우 방향을 위로 바꾸고 이동을 시도한다.
					tank.direction = 2;
					move();
				}else if (Commend.charAt(idx) == 'D') {		//D명령어일경우 방향을 아래로 바꾸고 이동을 시도한다.
					tank.direction = 3;
					move();
				}else if (Commend.charAt(idx) == 'L') {		//L명령어일경우 방향을 왼쪽으로 바꾸고 이동을 시도한다.
					tank.direction = 0;
					move();
				}else if (Commend.charAt(idx) == 'R') {		//R명령어일경우 방향을 오른쪽으로 바꾸고 이동을 시도한다.
					tank.direction = 1;
					move();
				}else if (Commend.charAt(idx) == 'S') {		//S명령어일경우 포탄을 쏴본다.
					shooting();
				}
			}
			
			lastTankLoc();									//탱크의 위치와 방향을 표시해주
			System.out.printf("#%d ",test_case);			//정답을 출력한다
			printBoard();
			
			
		}
 	}
	public static void lastTankLoc() {						//마지막의 탱크의 위치를 맵에 표시하는 메서드
		if (tank.direction == 0) {							//방향을 확인하고
			board[tank.y][tank.x] = '<';					//탱크 위치에 방향을 넣어준다
		}else if (tank.direction == 1) {
			board[tank.y][tank.x] = '>';
		}else if (tank.direction == 2) {
			board[tank.y][tank.x] = '^';
		}else if (tank.direction == 3) {
			board[tank.y][tank.x] = 'v';
		}
		
	}
	
	public static void printBoard() {						//맵을 출력하는 메서드
		for (char[] c : board) {
			for (char cc : c) {
				System.out.printf("%c",cc);
			}
			System.out.println();
		}
	}
	
	public static void move() {								//탱크의 다음 위치를 찾고
		int ty = tank.y + dy[tank.direction];
		int tx = tank.x + dx[tank.direction];
															//범위를 벗어나지 않고, 평지일경우
		if (0<= ty && ty < Y && 0<= tx && tx <X && board[ty][tx] == '.') {
			tank.y = ty;									//이동한다
			tank.x = tx;
		}
	}
	
	public static void shooting() {
		int canonBallY = tank.y;							//포탄의 위치를 탱크 위치로 설정하고
		int canonBallX = tank.x;
		while (true) {
			canonBallY += dy[tank.direction];				//포탄을 한번 움직여준다
			canonBallX += dx[tank.direction];
			if (0<= canonBallY && canonBallY < Y && 0<= canonBallX && canonBallX <X) {	//범위를 벗어나지 않고
				if (board[canonBallY][canonBallX] == '#') {								//강철 벽이라면
					break;																//포탄이 멈춘다
				}
				if (board[canonBallY][canonBallX] == '*') {								//벽돌 벽이라면
					board[canonBallY][canonBallX] = '.';								//벽을 부수고 평지로 바뀐뒤
					break;																//포탄이 멈춘다
				}
				
			}else {																		//범위를 벗어나면 멈춘다
				break;
			}
		}
	}
}

class Tank{
	
	int direction;
	int y;
	int x;
	
	public Tank(int direction, int y, int x) {
		super();
		this.direction = direction;
		this.y = y;
		this.x = x;
	}
	
}