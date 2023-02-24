package 박승수;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class A052_BJ1992_쿼드트리_과제9 {
	static int[][] board;
	static StringBuilder sb = new StringBuilder();

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		board = new int[N][N];
		
		for (int y = 0; y < N; y++) {
			String temp = br.readLine();
			for(int x = 0; x < N; x++) {
				board[y][x] = temp.charAt(x) - '0';
			}
		}
		solution(0,0,N,board[0][0] == 0 ? true : false);
		
		System.out.println(sb.toString());
	}
	
	static boolean check(int row, int col, int size, boolean zeroFlag) {//정사각형이 모두 같은 값인지 체크하는 메소드
		for (int i = row; i < row + size; i++) {//(row,col)부터 확인하면서
			for (int j = col; j < col + size; j++) {
				if (zeroFlag == true && board[i][j] == 1) {//만약 (row,col)의 값이 0이고 배열값이 1이라면
					return false;//false 리턴
				}
				if (zeroFlag == false && board[i][j] == 0) {//만약 (row,col)의 값이 1이고 배열값이 0이라면
					return false;//false 리턴
				}
			}
		}
		return true;//모두 일치한다면 true 리턴
	}
	
	public static void solution(int row, int col, int size, boolean zeroFlag) { // 좌표 기준은 왼쪽 위로 설정한다 
		if(check(row, col, size, zeroFlag)) {//만약 그 정사각형의 값이 모두 일치한다면
			sb.append(zeroFlag==true?0:1);//그 값으로 압축하고
			return;//재귀 종료
		}
		
		
		sb.append("(");//괄호를 열면서 4개의 칸으로 분리
		solution(row, col, size / 2, board[row][col] == 0 ? true : false);//왼쪽 위칸
		solution(row, col + size / 2, size / 2, board[row][col + size / 2] == 0 ? true : false);//오른쪽 위칸
		solution(row + size / 2, col, size / 2, board[row + size / 2][col] == 0 ? true : false);//왼쪽 아래칸
		solution(row + size / 2, col + size / 2, size / 2, board[row + size / 2][col + size / 2] == 0 ? true : false);//오른쪽 아래칸
		sb.append(")");//재귀 끝날 때 괄호 닫음
		
	}

}
