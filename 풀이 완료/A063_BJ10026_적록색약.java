package 박승수;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;

public class A063_BJ10026_적록색약 {
	static char[][] board;				//색들을 저장할 배열
	static int N;						//배열의 크기를 저장할 변수
	static int[] dy = {0,0,1,-1};		//이동할 방향들을 미리 설정
	static int[] dx = {-1,1,0,0};
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine());
		
		board = new char[N][N];					//색들 저장할 배열 초기화
		
		for (int y = 0; y < N; y++) {
			String temp = br.readLine(); 
			for (int x = 0; x < N; x ++) {
				board[y][x] = temp.charAt(x);	//색들을 배열에 넣어준다
			}
		}
		
		System.out.printf("%d %d",nomalArea(),sickArea());		//아픈사람의 구역과 평범한 사람들의 구역을 출력
	}
	
	public static int nomalArea() {						//평범한 사람들의 구역을 리턴할 메서드
		boolean[][] isCheck = new boolean[N][N];		//방문 확인용 배열
		Pos temp;										//좌표를 넣을 변수 미리 선언 
		int answer = 0;									//구역이 몇개인지 저장할 변수
		for (int y = 0; y < N; y ++) {
			for (int x = 0; x < N; x++) {
				if (!isCheck[y][x]) {					//모든 배열을 순회하며 만약 방문 안했을경우
					answer ++;							//구역을 +1 해주고
					Queue<Pos> queue = new ArrayDeque<Pos>();	//큐를 만든뒤
					queue.add(new Pos(y,x));			//이번 좌표를 큐에 넣어주고
					isCheck[y][x] = true;				//방문했다 표시한다
					
					while (!queue.isEmpty()) {			//큐가 빌때까지 BFS 돈다
						temp = queue.remove();
						
						for (int idx = 0; idx < 4; idx++) {	//4방향 탐색
							int ty = temp.y + dy[idx];
							int tx = temp.x + dx[idx];
						
						if (0<= ty && ty < N && 0 <= tx && tx < N && isCheck[ty][tx] == false) {	//범위확인, 방문확인
							if (board[temp.y][temp.x] == board[ty][tx]) {		//같은색일경우
								isCheck[ty][tx] = true;							//방문 표시 후
								queue.add(new Pos(ty,tx));						//큐에 추가
							}
							
						}
					}
					}
				}
			}
		}
		return answer;			//구역 몇개인지 리턴
		
	}
	
	public static int sickArea() {						//색맹들의 구역을 리턴할 메서드
		boolean[][] isCheck = new boolean[N][N];		//방문 확인용 배열
		Pos temp;										//좌표를 넣을 변수 미리 선언 
		int answer = 0;									//구역이 몇개인지 저장할 변수
		for (int y = 0; y < N; y ++) {
			for (int x = 0; x < N; x++) {
				if (!isCheck[y][x]) {					//모든 배열을 순회하며 만약 방문 안했을경우
					answer ++;							//구역을 +1 해주고
					Queue<Pos> queue = new ArrayDeque<Pos>();	//큐를 만든뒤
					queue.add(new Pos(y,x));			//이번 좌표를 큐에 넣어주고
					isCheck[y][x] = true;				//다음좌표를 미리 방문했다 표시한다
					
					while (!queue.isEmpty()) {			//큐가 빌때까지 BFS 돈다
						temp = queue.remove();
						
						for (int idx = 0; idx < 4; idx++) {	//4방향 탐색
							int ty = temp.y + dy[idx];
							int tx = temp.x + dx[idx];
						
						if (0<= ty && ty < N && 0 <= tx && tx < N && isCheck[ty][tx] == false) {	//범위확인, 방문확인
							//같은색일경우 또는 R,G 일경우
							if (board[temp.y][temp.x] == board[ty][tx] ||(board[temp.y][temp.x] == 'R' && board[ty][tx] == 'G')||(board[temp.y][temp.x] == 'G' && board[ty][tx] == 'R')) {
								isCheck[ty][tx] = true;	//다음좌표 방문했다 표시한다
								queue.add(new Pos(ty,tx));	//큐에 추가해준다 
							};
							
						}
					}
					}
				}
			}
		}
		return answer;			//구역 몇개인지 리턴
	}
	

}

class Pos{
	int y;
	int x;
	
	public Pos(int y, int x) {
		super();
		this.y = y;
		this.x = x;
	}

}
