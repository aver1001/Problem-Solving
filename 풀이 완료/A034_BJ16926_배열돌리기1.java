package 박승수;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class A034_BJ16926_배열돌리기1 {
	static int N;
	static int M;
	static int R;
	static int[] dx = {0,1,0,-1};
	static int[] dy = {1,0,-1,0};
	static int board[][];
	static int min;
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		String[] temp = br.readLine().split(" ");
		N = Integer.parseInt(temp[0]); //배열의 크기 N 입력
		M = Integer.parseInt(temp[1]); //배열의 크기 M 입력
		R = Integer.parseInt(temp[2]); //회전시킬 횟수 R 입력
		
		board = new int[N][M]; // 숫자 채워넣을 board 선언
		
		for(int i = 0; i< N; i ++) { // board 채워넣기
			temp = br.readLine().split(" "); 
			for(int j = 0; j < M; j ++) {
				board[i][j] = Integer.parseInt(temp[j]);
			}
		}
		
		min = Math.min(N, M); // N,M중 최솟값을 구해 회전시킬 칸? 구해줌
		
		for (int idx = 0; idx < R; idx ++) { // R번만큼 회전
			rotate();
			
		}
		printBoard(board); // board출력 
		
		

	}
	
	static void rotate() {
    	
    	for(int i=0; i<min/2; i++) { // 회전 시킬 그룹의 갯수 구하기
    		int x = i;
    		int y = i;
    		
    		int temp = board[x][y]; // 마지막에 넣을 값 미리 빼놓음
    		
    		int idx = 0; // 우, 하, 좌, 상 방향으로 이동하며 반시계 방향으로 값 넣을 인덱스
    		while(idx < 4) { // 왼쪽으로 넣는, 위로 넣는, 오른쪽으로 넣는, 아래로 넣는 연산을 차례로 수행
    			int nx = x + dx[idx];
    			int ny = y + dy[idx];
    			
    			// 범위 안이라면
    			if(nx < N-i && ny < M-i && nx >= i && ny >= i) {
    				board[x][y] = board[nx][ny];
    				x = nx;
    				y = ny;
    			} 
    			// 범위를 벗어났다면 다음 방향으로 어감
    			else {
    				idx++;
    			}
    			
    		}
    		
    		board[i+1][i] = temp; // 빼 놓은 값 넣어 줌
    	}
    }
	
	public static void printBoard(int[][] board) {
		StringBuilder sb = new StringBuilder();
		for (int[] a: board) {
			for (int b : a) {
				sb.append(b).append(" ");
			}
			sb.append("\n");
		}
		System.out.println(sb.toString());
	}

}
