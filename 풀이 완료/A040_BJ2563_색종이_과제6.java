package 박승수;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class A040_BJ2563_색종이_과제6 {

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine()); // 색종이의 갯수 N
		int board[][] = new int[101][101];		// 색종이를 붙일 board 선언 
		int answer = 0;
		for (int idx = 0; idx < N; idx ++) { // 색종이마다 입력을 받음
			String[] temp = br.readLine().split(" ");
			
			// 왼쪽 위를 x1,y1
			// 오른쪽 아래를 x2,y2로 설정한다
			int y1, y2, x1, x2;
			x1 = Integer.parseInt(temp[0]);
			x2 = x1+10;
			y2 = Integer.parseInt(temp[1]);
			y1 = y2+10;
			
			// 색종이의 맨끝 좌표들에 +1, -1 을 각각 해줘서 누적합을 할 준비를 해준다.
			board[y1][x1] += 1;
			board[y1][x2] -= 1;
			board[y2][x1] -= 1;
			board[y2][x2] += 1;
		}
		
		// x축 기준으로 누적합을 진행해준다.
		for(int y = 1; y < 101; y++) {
			for (int x = 1; x < 101; x++) {
				board[y][x] += board[y][x-1];
			}
		}
		
		// y축 기준으로 누적합을 진행해준다.
		for(int x = 1; x < 101; x++) {
			for (int y = 1; y < 101; y++) {
				board[y][x] += board[y-1][x];
				if (board[y][x] != 0) { // 만약 누적합이 끝난 값이 0이 아닐경우 이 위치는 색종이가 있는것이기 때문에 넓이 += 1 해준다 
					answer ++; 
				}
			}
		}
		System.out.println(answer);
	}


}
