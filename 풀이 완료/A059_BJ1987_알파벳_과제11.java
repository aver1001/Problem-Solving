package 박승수;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashSet;

public class A059_BJ1987_알파벳_과제11 {
	static HashSet<Character> check = new HashSet<Character>();	//이미 지나온 알파벳인지 확인할 Set
	static int Y;												//배열의 전체크기 Y * X
	static int X;
	static int[] dy = {0,0,1,-1};								//상하좌우 이동할 변수 미리 선언
	static int[] dx = {1,-1,0,0};
	static char[][] board;										//2차원 배열 선언
	static int answer = 0;										//정답 넣을 변수 선언

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		String[] temp = br.readLine().split(" ");
		Y = Integer.parseInt(temp[0]);				//Y 크기 입력
		X = Integer.parseInt(temp[1]);				//X 크기 입력
		
		board = new char[Y][X];						//입력받은 사이즈로 배열 초기화
		
		for (int y = 0; y < Y; y++) {
			String t = br.readLine();
			for (int x = 0; x < X; x ++) {
				board[y][x] = t.charAt(x);			//배열에 알파벳 입력
			}
		}
		
		answer = 1;									//첫 시작도 이동으로 치기 떄문에 answer 1로 초기화 하고
		check.add(board[0][0]);						//방문한 알파벳에도 넣어준다
		dfs(0,0,1);									//그뒤 1번 간거부터 DFS 돌려준다
		System.out.println(answer);
	}
	
	public static void dfs(int y, int x,int v) {
		
		answer = Math.max(answer, v);				//깊이가 가장 긴것을 넣어야 하기 때문에 최대값 넣어줌
		
		for (int idx = 0; idx < 4; idx ++) {		// 4방향 탐색하
			int ty = y+dy[idx];
			int tx = x+dx[idx];
			
			if (0<= ty && ty < Y && 0<= tx && tx < X && !check.contains(board[ty][tx])) {	//범위넘지않고, 안가본 알파벳일경우
				check.add(board[ty][tx]);		// 알파벳을 사용한걸로 넣어주고
				dfs(ty,tx,v+1);					// DFS 진행한다
				check.remove(board[ty][tx]);	// 알파벳 사용을 취소해준다
			}
		}
	}

}