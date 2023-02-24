package 박승수;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;


public class A051_BJ3109_빵집 {
	static char[][] board;			// 가스관 위치 적을 2차원 배열 선언
	static int X;					// X크기
	static int Y;					// Y크기
	static int[] dy = {-1,0,1};		// 오른쪽으로 이동할떄 방향설정
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] temp = br.readLine().split(" ");
		Y = Integer.parseInt(temp[0]);
		X = Integer.parseInt(temp[1]);
		
		board = new char[Y][X];
		
		for (int y = 0; y < Y ; y++) {	//배열에 값 넣어주기
			String t = br.readLine();
			for (int x = 0; x < X; x ++) {
				board[y][x] = t.charAt(x);
			}
		}
		
		int answer = 0;
		for (int y = 0; y<Y ; y++) {	//y를 0부터 돌며
			if (board[y][0]=='.') {		//[y][0]이 . 일경우 진행해본다
				if (solution(y,0)) {	//만약 끝까지 도착했을경우
					answer++;			//정답 +1 해준다
				}
				
			}
		}
		
		System.out.println(answer);

	}
	
	public static boolean solution(int y, int x) {
		
		if (x == X-1) {											// 마지막 열까지 왔다면 파이프 설치에 성공한것이기 때문에 true return
			return true;
		}
		
		for (int idx = 0; idx <3; idx ++) { 					// 오른쪽위, 오른쪽, 오른쪽아래 순으로 이동
			int ty = y+dy[idx];
			
			if( ty >= 0 && ty < Y && board[ty][x+1] == '.') {	// 갈수있고, 범위를 넘지 않는다면
				board[ty][x+1] = 'x';							// 일단 x로 바꿔놓는다. 갔던곳은 다시 갈 필요가 없기 때문
				if (solution(ty,x+1)) {							// 끝까지 도착 했다면 true 리턴해준다
					return true;
				}
			}
		}
		
		return false;											// 끝까지 도착 못할경우 여기서 false를 리턴하게 된다
	}

}
