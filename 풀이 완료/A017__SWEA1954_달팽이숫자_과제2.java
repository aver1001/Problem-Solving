package 박승수;
import java.util.*;
public class A017__SWEA1954_달팽이숫자_과제2 {
	static int board[][]; //달팽이 board 만들 변수 선언
	static int[] dy = {0,1,0,-1}; // 우 하 좌 상 순서로 움직이도록 방향설정 
	static int[] dx = {1,0,-1,0}; // 우 하 좌 상 순서로 움직이도록 방향설정 
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in); // 입력이 몇개안돼서 scanner로 받아옴
		int T = sc.nextInt(); // TestCase 입력 받기
		for (int test_case = 1; test_case < T+1; test_case++) { // testCase 만큼 순회하기
			System.out.printf("#%d\n", test_case); // 몇번쨰 testCase인가 출력하기
			soultion(sc.nextInt()); // 달팽이 배열 만들기
		}
		

	}
	
	public static void soultion(int N) {
		board = new int[N][N]; // N*N으로 달팽이 배열 넣을 자리 만들어주기 
		
		int y = 0;	// 움직이기 전 위치
		int x = 0;	// 움직이기 전 위치
		int idx = 0; // 움직일 방향
		int ty = 0; // 움직일 위치 
		int tx = 0; // 움직일 위치 
		int cnt = 1; // 달팽이 배열에 넣을 
		while (true) { // 무한루프
			
			board[y][x] = cnt; // board의 y,x좌표에 cnt 값 넣어주기
			if (cnt == N*N) { // 만약 N*N == cnt일경우 모든 좌표 다 돌았기때문에 완성이므로 break
				break;
			}
			
			ty = y+dy[idx]; // 다음 움직일 방향 설정
			tx = x+dx[idx]; // 다음 움직일 방향 설정
			if (0<= ty && ty <N && 0<= tx && tx < N && board[ty][tx] == 0) { // 방향을 바꾸지 않아도 된다면
				y = ty;
				x = tx; //그대로 진행하고
				cnt ++; //cnt++ 해줘서 배열에 넣을값 늘려주기
				
			}else { // 방향을 바꿔야 한다면
				idx += 1;  // 방향을 바꿔주기위해 +1 해주고
				idx %= 4; // 만약 4가 된다면 4번째 방향은 없기때문에 %4 해줘서 0으로 바꿔주기 
			}
			
		}
		
		for (y = 0; y<N ; y++) {
			for (x = 0; x < N; x ++) {
				System.out.printf("%d ",board[y][x]); // 출력해주기 
			}
			System.out.println();
		}
		
		
	}

}
