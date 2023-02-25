import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class 화산쇄설류 {
	static int[] dy = {0,0,1,-1};
	static int[] dx = {1,-1,0,0};
	
	static int M;
	static int N;
	static boolean[][] hLoc;
	static int[][] board;
	
	static ArrayList<화산> mList;
	static int time;
	
	static int aHeight;
	static int aTime = Integer.MAX_VALUE;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		String[]temp = br.readLine().split(" ");
		M = Integer.parseInt(temp[0]);
		N = Integer.parseInt(temp[1]);
		int V = Integer.parseInt(temp[2]);
		
		temp = br.readLine().split(" ");
		int X = Integer.parseInt(temp[0])-1;
		int Y = Integer.parseInt(temp[1])-1;
		
		board = new int[M][N];
		for(int y = 0; y < M; y ++) {
			temp = br.readLine().split(" ");
			for (int x = 0; x < N; x ++) {
				board[y][x] = Integer.parseInt(temp[x]);
			}
		}
		mList = new ArrayList<화산>();
		
		for (int idx = 0; idx < V; idx ++) {
			temp = br.readLine().split(" ");
			board[Integer.parseInt(temp[0])-1][Integer.parseInt(temp[1])-1] = -1;
			mList.add(new 화산(Integer.parseInt(temp[0])-1,Integer.parseInt(temp[1])-1,Integer.parseInt(temp[2])));
		}
		
		//printBoard();
		solution(X,Y);
		System.out.printf("%d %d",aHeight, aTime);
	}
	
	public static void solution(int X, int Y) {
		Queue<Pos> queue = new ArrayDeque<Pos>();
		boolean[][] isVisited = new boolean[M][N];
		
		queue.add(new Pos(X,Y,0));
		int ty;
		int tx;
		Pos temp;
		while (!queue.isEmpty()) {
			temp = queue.remove();
			isVisited[temp.y][temp.x] = true;
			
			if (temp.cnt != time) {
				time = temp.cnt;
				화산쇄설류이동();
				//printBoard();
			}
			if (aHeight < board[temp.y][temp.x]) {
				aHeight = board[temp.y][temp.x];
				aTime = temp.cnt;
			}
			
			for(int idx = 0; idx < 4 ; idx ++) {
				ty = temp.y + dy[idx];
				tx = temp.x + dx[idx];
				
				if (0<= ty && ty < M && 0<= tx && tx < N && board[ty][tx] != -1 && board[ty][tx] != -2 && isVisited[ty][tx] == false){
					queue.add(new Pos(ty,tx,temp.cnt+1));
					
				}
			}
		}
	}
	
	public static void 화산쇄설류이동() {
		
		hLoc = new boolean[M][N];
		int ty;
		int tx;
		
		for (int y = 0; y < M; y ++) {
			for (int x = 0; x <N; x ++) {
				if (board[y][x] == -2) {
					for(int idx = 0; idx < 4 ; idx ++) {
						ty = y + dy[idx];
						tx = x + dx[idx];
						
						if (0<= ty && ty < M && 0<= tx && tx < N){
							hLoc[ty][tx] = true;
						}
					}
				}
			}
		}
		
		for (int y = 0; y < M; y ++) {
			for (int x = 0; x <N; x ++) {
				if (hLoc[y][x]) {
					board[y][x] = -2;
				}
				
			}
		}
		
		for(화산 h : mList) {
			if (h.time == time) {
				board[h.y][h.x] = -2;
			}
		}
	}
	
	public static void printBoard() {
		for (int[] b : board) {
			System.out.println(Arrays.toString(b));
		}
		System.out.println();
	}

}
class Pos{
	int y;
	int x;
	int cnt;
	
	public Pos(int y, int x, int cnt) {
		super();
		this.y = y;
		this.x = x;
		this.cnt = cnt;
	}
	
}

class 화산{
	int y;
	int x;
	int time;
	
	public 화산(int y, int x, int time) {
		super();
		this.y = y;
		this.x = x;
		this.time = time;
	}
	
}
