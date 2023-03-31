package 박승수;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.HashMap;
import java.util.Queue;

public class B014_BJ1194_달이차오른다가자 {
	static int Y;				//공간의 크기
	static int X;
	
	static char[][] board;		//공간의 정보를 저장할 배열
	
	static int[] dy = {1,-1,0,0};	//4방탐색용 배열 선언
	static int[] dx = {0,0,1,-1};
	
	static HashMap<Character, Integer> keyNum;	//key를 숫자로 변환하기 위한 HashMap
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] temp = br.readLine().split(" ");
		Y = Integer.parseInt(temp[0]);			//세로 크기 입력
		X = Integer.parseInt(temp[1]);			//가로 크기 입력
		
		board = new char[Y][X];					//board초기화
		
		String inputs;
		Queue<Loc> queue = new ArrayDeque<>();	//Bfs 탐색용 큐 생성
		
		for (int y = 0; y < Y; y ++) {			//공간을 입력 받으며
			inputs = br.readLine();
			for(int x = 0; x < X; x ++) {
				board[y][x] = inputs.charAt(x);
				if (board[y][x] =='0') {		//민수가 있을경우
					queue.add(new Loc(y,x,0,0));//시작지점이므로 큐에 넣어주고
					board[y][x] = '.';			//빈칸으로 변경한다
				}
			}
		}
		
		hashMapInit();		//HashMap에 알파벳과 키 번호를 매칭시켜줌
		
		Loc tempLoc;
		boolean [][][] DP = new boolean[Y][X][1<<7];		//Y,X와 key의 획득 상황을 DP로 만듦
		int ty;
		int tx;
		while (!queue.isEmpty()) {	//큐가 빌때까지 BFS
			tempLoc = queue.poll();
			
			for (int idx = 0; idx < 4; idx ++) {
				ty = tempLoc.y + dy[idx];		//4방탐색
				tx = tempLoc.x + dx[idx];
				
				if(isRange(ty, tx)) {	//범위를 벗어나는지 확인
					//만약 빈칸이고, 현재 상태에서 방문한적이 없다면
					if (board[ty][tx] == '.' && DP[ty][tx][tempLoc.key] == false) {
						DP[ty][tx][tempLoc.key] = true;		//방문 표시 해주고
						queue.add(new Loc(ty,tx,tempLoc.key,tempLoc.cnt+1));	//cnt+1해서 큐에 추가
					}
					//만약 벽이라면 더이상 진행 불가능하기 때문에 continue
					else if (board[ty][tx] == '#') {
						continue;
					}
					//만약 소문자라면, key를 추가한상태로, 방문한적이 없을경우 진행
					else if (Character.isLowerCase(board[ty][tx]) && DP[ty][tx][tempLoc.key | 1<<keyNum.get(board[ty][tx])] ==false) {
						DP[ty][tx][tempLoc.key | 1<<keyNum.get(board[ty][tx])] = true;	//방문 표시 해주고
						queue.add(new Loc(ty,tx,tempLoc.key | 1<<keyNum.get(board[ty][tx]),tempLoc.cnt+1));	//키를 추가해주고, cnt +1 해서 큐에 추가
					}
					//만약 대문자라면, 키를 가지고 있는지 확인하고, 방문하지 않았다면 진행
					else if (Character.isUpperCase(board[ty][tx]) && (tempLoc.key & 1<<keyNum.get(board[ty][tx]))!= 0 && DP[ty][tx][tempLoc.key] == false){						
						DP[ty][tx][tempLoc.key] = true;		//방문표시 해주고
						queue.add(new Loc(ty,tx,tempLoc.key,tempLoc.cnt+1));	//cnt +1해서 큐에 추가
					}
					//만약 도착지라면
					else if (board[ty][tx] == '1') {
						//몇번 이동했는지 출력하고 종료
						System.out.println(tempLoc.cnt+1);
						System.exit(0);
					}
				}
				
				
			}
			
			
		}
		//여기까지 왔다면, 출구에 접근이 불가능하다는 의미이므로 -1 출
		System.out.println(-1);
		
		
	}
	
	public static void hashMapInit() {
		/*
		 * key를 비트마스킹으로 표시할것이기 때문에
		 * 알파벳과 key를 매칭해줄것임.
		 * 빠른 접근속도를 위해 HashMap 사용
		 */
		keyNum = new HashMap<Character, Integer>();
		
		keyNum.put('a', 1);
		keyNum.put('b', 2);
		keyNum.put('c', 3);
		keyNum.put('d', 4);
		keyNum.put('e', 5);
		keyNum.put('f', 6);
		
		keyNum.put('A', 1);
		keyNum.put('B', 2);
		keyNum.put('C', 3);
		keyNum.put('D', 4);
		keyNum.put('E', 5);
		keyNum.put('F', 6);
	}
	
	public static boolean isRange(int y, int x) {
		//범위 확인하는 메서드
		if(0 <= y && y < Y && 0 <= x && x < X) {
			return true;
		}
		return false;
	}
	
	static class Loc{
		int y;
		int x;
		int key;
		int cnt;
		public Loc(int y, int x, int key, int cnt) {
			super();
			this.y = y;
			this.x = x;
			this.key = key;
			this.cnt = cnt;
		}
		
		
	}
	
}
