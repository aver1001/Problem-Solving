package 박승수;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Iterator;
import java.util.TreeSet;

public class B012_BJ2239_스도쿠_과제3 {
	static int[][] board;
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		//스토쿠의 정보를 받을 배열 선언
		board = new  int[9][9];
		String temp;
		//스토쿠의 정보 입력
		for(int y=0; y<9; y++) {
			temp = br.readLine();
			for(int x=0; x<9;x++) {
				board[y][x] = temp.charAt(x)-'0';
			}
		}
		solution(0, 0);
	}
	
	public static void solution(int y, int x) {
		//끝까지 도착했다면, 출력하고 종료
		if (y == 8 && x == 9) {
			printAnswer();
			System.exit(0);
		}
		
		//x가 범위를 넘어갔다면, 아랫칸으로 이동
		if (x == 9) {
			x = 0;
			y += 1;
		}
		
		//만약 숫자를 채워넣어야 한다면
		if (board[y][x] == 0) {
			//채울수 있는 숫자를 검색한 후
			Iterator<Integer> e =  findNum(y,x).iterator();
			while(e.hasNext()) {
				//숫자를 채우고
				board[y][x] = e.next();
				//다음칸으로 넘어감
				solution(y,x+1);
				//원상복구
				board[y][x] = 0;	
			}
		}else {
			//칸이 이미 채워졌다면 다음칸으로 바로 이동
			solution(y,x+1);
		}
		
	}
	
	public static TreeSet<Integer> findNum(int Y,int X) {
		//가능한 숫자들을 저장할 TreeSet
		//TreeSet의 경우 1-9,의 순서가 보장된상태로 iterator가 나온다.
		TreeSet<Integer> treeSet = new TreeSet<Integer>();
		//처음 1~9의 숫자를 넣어준뒤
		for (int i = 1; i <10; i ++) {
			treeSet.add(i);
		}
		//가로 확인 하며 있는 숫자 제거
		for(int x = 0; x < 9; x ++) {
			treeSet.remove(board[Y][x]);
		}
		//세로 확인 하며 있는 숫자 제거
		for(int y = 0; y < 9; y ++) {
			treeSet.remove(board[y][X]);
		}
		//3칸씩 나뉜 칸 속에서 왼쪽 위로 이동
		if (Y%3 != 0) {
			Y -= Y%3;
		}
		if (X%3 != 0) {
			X -= X%3;
		}
		
		//네모 확인 하며 있는 숫자 제거
		for (int y = Y; y<Y+3; y++) {
			for(int x=X; x<X+3; x++) {
				treeSet.remove(board[y][x]);
			}
		}
		return treeSet;
	}
	
	public static void printAnswer() {
		StringBuilder sb = new StringBuilder();
		for(int[] arr: board) {
			for(int i: arr) {
				sb.append(i);
			}
			sb.append("\n");
		}
		System.out.println(sb.toString());
	}

}
