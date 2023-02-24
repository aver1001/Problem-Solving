package 박승수;
import java.util.*;
public class A011__SWEA1210_Ladder1 {
	static int arr[][]; // 사다리 입력받을 배열
	static int dy[] = {0,0,1}; // 움직일 방향 미리 정의 
	static int dx[] = {-1,1,0};// 움직일 방향 미리 정의
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		for (int test_case = 1; test_case < 11; test_case++) { // 테스트 케이스는 10개
			 arr = new int[100][100]; // 사다리 입력을 받을 100*100 배열선언
			 sc.nextInt(); // test case 번호는 for문을 통해 처리중이므로 입력 하나 버리기
			 			 
			 for (int y = 0; y <100;y++) {
				 for (int x = 0; x < 100; x ++) {
					 arr[y][x] = sc.nextInt(); // 사다리 입력 받기
				 }
			 }
			 for (int x = 0; x < 100; x ++) {
				 if (arr[0][x] == 1 && ladderDown(0,x)==2) { // 만약 사다리가 출발하는 위치라면 아래로 내려가서 2가 나올경우 출력
					 System.out.printf("#%d %d\n",test_case,x);
					 break; // 시간복잡도 줄이기위해 더 탐색하지 않음.
				 }
			 }
		}

	}
	
	public static int ladderDown(int y,int x) {
		//System.out.println(y);
		int ty = 0; // 움직일 방향 미리 선언
		int tx = 0; // 움직일 방향 미리 선언
		int answer = 0; // return 밑에서 한번에 받기위해 선언
			
			for (int idx = 0; idx <3; idx++) {
				ty = y+dy[idx]; // 3방향 순서대로 탐색
				tx = x+dx[idx];
				
				if (0<= ty && ty < 100 && 0<= tx && tx < 100 && arr[ty][tx] != 0) { // 움직일 방향이 배열을 넘어가지 않고, 갈수 있을경우 진행
					if (ty == 99) { // 마지막에 도착하면 결과가 무엇인지 리턴
						return arr[ty][tx];
					}
					arr[ty][tx] = 0; // 움직엿다고 표시해서 뒤로 돌아가는 일 없도록 설정
					answer = ladderDown(ty,tx); // 재귀적으로 받아온 값을 다시 리턴해주기위해 answer에 넣음. 
					arr[ty][tx] = 1; // 움직인거 표시 되돌리기
					break;
				}
			}
		return answer; //받아온값(가장 아래 위치) 리턴
	}

}
