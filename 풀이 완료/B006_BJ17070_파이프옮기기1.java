package 박승수;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class B006_BJ17070_파이프옮기기1 {
	static int[] dy = {0,1,1};
	static int[] dx = {1,1,0};
	static int N;
	static int board[][];
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		//N*N 의 공간의 정보를 저장할 배열 크기 입력
		N = Integer.parseInt(br.readLine());
		//공간 초기화
		board = new int[N][N];
		
		
		//공간 입력 받기
		String[] temp;
		for (int y = 0; y < N; y ++) {
			temp = br.readLine().split(" ");
			for(int x = 0; x < N; x ++) {
				board[y][x] = Integer.parseInt(temp[x]);
			}
		}
		System.out.println(solution(0,1,0));
		
	}
	
	public static int solution(int y, int x, int direct) {
		//마지막에 도착했다면, 1회 성공한것이므로 1 리턴해줌
		if (y == N-1 && x == N-1) {
			return 1;
		}
		
		// 몇번 성곤했는지 저장할 변수
		int hap = 0;
		//가로로 왔을경우
		if (direct == 0) {
			//가로로 이동
			if (isRange(y, x+1,0)) {
				hap += solution(y,x+1,0);
			}
			//대각으로 이동
			if (isRange(y+1, x+1,1)) {
				hap += solution(y+1, x+1,1);
			}
		//대각으로 왔을경우 
		}else if(direct == 1) {
			//가로로 이동
			if (isRange(y, x+1,0)) {
				hap += solution(y,x+1,0);
			}
			//대각으로 이동
			if (isRange(y+1, x+1,1)) {
				hap += solution(y+1, x+1,1);
			}
			//아래로 이동
			if (isRange(y+1, x,2)) {
				hap += solution(y+1, x,2);
			}
		//아래로 왔을경우
		}else if(direct == 2) {
			//대각으로 이동
			if (isRange(y+1, x+1,1)) {
				hap += solution(y+1, x+1,1);
			}
			//아래로 이동
			if (isRange(y+1, x,2)) {
				hap += solution(y+1, x,2);
			}
		}
		return hap;
		
	}
	
	// 갈수있는지 확인하는 메서드
	public static boolean isRange(int y, int x,int direct) {
		
		//범위안에 들어가고
		if (0 <= y && y < N && 0<= x && x < N && board[y][x] == 0) {
			//대각이였을 경우 3곳다 비었는지 확인해야함
			if (direct == 1) {
				return isRange(y-1,x,2) && isRange(y, x-1, 0);
			}
			return true;
		}else {
			return false;
		}
		
	}

}
