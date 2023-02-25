package 박승수;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;

public class A065_BJ15683_감시 {
	static ArrayList<CCTV> cctvList;
	static int Y;
	static int X;
	static int[][] board;
	static int answer = Integer.MAX_VALUE;
	

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] temp = br.readLine().split(" ");
		Y = Integer.parseInt(temp[0]);
		X = Integer.parseInt(temp[1]);
		
		board = new int[Y][X];									//사무실의 정보를 받을 배열 선언
		cctvList = new ArrayList<CCTV>();						//cctv 정보를 담을 리스트 선언
		int cnt = 0;
		for (int y = 0; y < Y; y++) {
			temp = br.readLine().split(" ");
			for(int x = 0; x < X; x ++) {
				board[y][x] = Integer.parseInt(temp[x]);		//사무실의 정보를 입력하고
				if (board[y][x] != 0 && board[y][x] != 6) {		//CCTV일경우
					cctvList.add(new CCTV(y,x,board[y][x]));	//cctvList에 넣어준다
				}
			}
		}
		
		DFS(0,board);											//DFS돌려 모든 경우의수를 탐색해본뒤
		System.out.println(answer);								//사각지대의 최소를 구해준다
		

	}
	
	public static void check(int[][] board) {	//사각지대의 개수를 구하는 메서드
		int hap = 0;								//초기 사각지대의 개수를 0으로 만들어 놓
		for (int y = 0; y < Y; y++) {				//사무실을 순회하
			for (int x = 0; x < X; x++) {
				if (board[y][x] == 0) {				//사각지대일경우
					hap ++;							//사각지대의 개수를 더해준다 
				}
			}
		}
		
		answer = Math.min(hap, answer);				//사각지대의 최솟값을 업데이트 해준다
	}
	
	public static int[][] cctvRange(int y, int x, int dy, int dx,int[][] board) {		//각 CCTV의 방향에 따라서 보이는 위치를 사각지대가 아님으로 바꿔놓는다
		while (true) {
			y += dy;								//현재 y좌표 + CCTV방향
			x += dx;								//현재 x좌표 + CCTV방향
			
			if (0 <= y && y < Y && 0 <= x && x < X) {				//범위를 벗어나지 않고
				if(board[y][x] == 0 ||board[y][x] == 9) {			//비어있을경우(빈칸이거나, 시야에 포함되는 곳이거나)
					board[y][x] = 9;								//시야에 포함된다고 표시한다
				}else if (board[y][x] == 1 || board[y][x] == 2 || board[y][x] == 3 || board[y][x] == 4 || board[y][x] == 5) {	//만약 CCTV일경우 넘어간다
					continue;
				}else if(board[y][x] == 6) {						//벽일경우 그만확인한다
					break;
				}
				
			}else {			//범위가 넘어갔어도 그만 확인한다
				break;
			}
		}
		
		return board;
	}
	
	public static void DFS(int v,int[][] board) {
		if (v == cctvList.size()) {	//모든 CCTV의 방향의대한 탐색이 끝났다
			check(board);			//사각지대의 개수를 업데이트한
			return;
		}
		
		int[][] temp;							//사무실의 상태를 복사해서 저장할 변수를 선언하고
		
		if(cctvList.get(v).type == 1) {			//CCTV의 종류가 1번일경우
			temp = copyBoard(board);			//배열을 복사해서
			cctvRange(cctvList.get(v).y, cctvList.get(v).x,1,0,temp); //4방향으로 CCTV를 돌려본뒤
			DFS(v+1,temp);						//DFS를 진행한다.
			
			temp = copyBoard(board);
			cctvRange(cctvList.get(v).y, cctvList.get(v).x,0,1,temp);
			DFS(v+1,temp);
			
			temp = copyBoard(board);
			cctvRange(cctvList.get(v).y, cctvList.get(v).x,-1,0,temp);
			DFS(v+1,temp);
			
			temp = copyBoard(board);
			cctvRange(cctvList.get(v).y, cctvList.get(v).x,0,-1,temp);
			DFS(v+1,temp);
			
		}else if (cctvList.get(v).type == 2) {	//CCTV의 종류가 2번일경우
			temp = copyBoard(board);			//배열을 복사해서
			cctvRange(cctvList.get(v).y, cctvList.get(v).x,-1,0,temp); //2방향으로 CCTV를 돌려본뒤
			cctvRange(cctvList.get(v).y, cctvList.get(v).x,1,0,temp);
			DFS(v+1,temp);						//DFS를 진행한다.
			
			temp = copyBoard(board);
			temp = cctvRange(cctvList.get(v).y, cctvList.get(v).x,0,-1,temp);
			temp = cctvRange(cctvList.get(v).y, cctvList.get(v).x,0,1,temp);
			DFS(v+1,temp);
			
		}else if (cctvList.get(v).type == 3) {	//CCTV의 종류가 3번일경우
			temp = copyBoard(board);			//배열을 복사해서
			temp = cctvRange(cctvList.get(v).y, cctvList.get(v).x,1,0,temp);	//4방향으로 CCTV를 돌려본뒤
			temp = cctvRange(cctvList.get(v).y, cctvList.get(v).x,0,1,temp);	
			DFS(v+1,temp);						//DFS를 진행한다.
			
			temp = copyBoard(board);
			temp = cctvRange(cctvList.get(v).y, cctvList.get(v).x,1,0,temp);
			temp = cctvRange(cctvList.get(v).y, cctvList.get(v).x,0,-1,temp);
			DFS(v+1,temp);
			
			temp = copyBoard(board);
			temp = cctvRange(cctvList.get(v).y, cctvList.get(v).x,-1,0,temp);
			temp = cctvRange(cctvList.get(v).y, cctvList.get(v).x,0,-1,temp);
			DFS(v+1,temp);
			
			temp = copyBoard(board);
			temp = cctvRange(cctvList.get(v).y, cctvList.get(v).x,-1,0,temp);
			temp = cctvRange(cctvList.get(v).y, cctvList.get(v).x,0,1,temp);
			DFS(v+1,temp);
			
		}else if (cctvList.get(v).type == 4) {	//CCTV의 종류가 4번일경우
			temp = copyBoard(board);
			temp = cctvRange(cctvList.get(v).y, cctvList.get(v).x,0,1,temp);	//4방향으로 CCTV를 돌려본뒤
			temp = cctvRange(cctvList.get(v).y, cctvList.get(v).x,-1,0,temp);
			temp = cctvRange(cctvList.get(v).y, cctvList.get(v).x,0,-1,temp);
			DFS(v+1,temp);						//DFS를 진행한다.
			
			temp = copyBoard(board);
			temp = cctvRange(cctvList.get(v).y, cctvList.get(v).x,1,0,temp);
			temp = cctvRange(cctvList.get(v).y, cctvList.get(v).x,-1,0,temp);
			temp = cctvRange(cctvList.get(v).y, cctvList.get(v).x,0,-1,temp);
			DFS(v+1,temp);
			
			temp = copyBoard(board);
			temp = cctvRange(cctvList.get(v).y, cctvList.get(v).x,1,0,temp);
			temp = cctvRange(cctvList.get(v).y, cctvList.get(v).x,0,1,temp);
			temp = cctvRange(cctvList.get(v).y, cctvList.get(v).x,0,-1,temp);
			DFS(v+1,temp);
			
			temp = copyBoard(board);
			temp = cctvRange(cctvList.get(v).y, cctvList.get(v).x,1,0,temp);
			temp = cctvRange(cctvList.get(v).y, cctvList.get(v).x,0,1,temp);
			temp = cctvRange(cctvList.get(v).y, cctvList.get(v).x,-1,0,temp);
			DFS(v+1,temp);
			
		}else if (cctvList.get(v).type == 5) {	//CCTV의 종류가 5번일경우
			temp = copyBoard(board);
			temp = cctvRange(cctvList.get(v).y, cctvList.get(v).x,1,0,temp);	//CCTV를 돌려본뒤
			temp = cctvRange(cctvList.get(v).y, cctvList.get(v).x,0,1,temp);
			temp = cctvRange(cctvList.get(v).y, cctvList.get(v).x,-1,0,temp);
			temp = cctvRange(cctvList.get(v).y, cctvList.get(v).x,0,-1,temp);
			DFS(v+1,temp);						//DFS를 진행한다.
		}
		
	}
	
	public static int[][] copyBoard(int[][] board){	//배열을 복사해서 리턴하는 메서드
		int[][] temp = new int[Y][X];
		
		for (int y = 0; y < Y; y++) {
			for (int x = 0; x < X; x++) {
				temp[y][x] = board[y][x];
			}
		}
		
		return temp;
	}
	
	public static void printBoard(int[][] board) {	//디버깅용 배열 출력해보는 메서드
		for (int[] b: board) {
			System.out.println(Arrays.toString(b));
		}
		System.out.println();
	}
	
	
	static class CCTV{					//CCTV의 정보를 담을 객체
		int y;				//CCTV의 y 위치
		int x;				//CCTV의 x 위치
		int type;			//CCTV의 종류
		
		public CCTV(int y, int x, int type) {
			super();
			this.y = y;
			this.x = x;
			this.type = type;
		}
		
	}

}


