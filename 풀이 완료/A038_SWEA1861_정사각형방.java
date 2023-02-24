package 박승수;

/*
 * 1. 이차원배열 값이 1~n^2
 * 2. 상하좌우 이동 가능 ( 단, 1 커야함
 * 3. 완전탐색 (방번호(이차원배열값)과 이동횟수(최대값) 출력
 * -> 최대값 여러개일 때, 방번호 작은 것 출력
 */
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class A038_SWEA1861_정사각형방 {
	static int[] dy = { 0, 0, 1, -1 };//상하로 움직일 방향 배열
	static int[] dx = { 1, -1, 0, 0 };//좌우로 움직일 방향 배열
	static int[][] arrCnt;//방문여부, 이동횟수
	static int[][] arr;//n by n 크기의 방 입력받을 배열
	static int N;//배열의 한 변 크기
	static StringBuilder str=new StringBuilder("");//출력할 문자열

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));//버퍼로 입력
		//int T = Integer.parseInt(br.readLine()); // Test Case 수 입력
		for (int test_case = 1; test_case < 2; test_case++) {//테스트 케이스

			N = Integer.parseInt(br.readLine()); // 배열 크기 입력

			arr = new int[N][N];//방을 입력받을 배열 생성
			arrCnt = new int[N][N];//방 이동횟수 배열 생성

			int Max = -1;//최대 이동횟수 변수 -1 초기화
			int Answer = N * N;//방 위치에 대해 초기화

			for (int y = 0; y < N; y++) { // 배열 입력
				String temp[] = br.readLine().split(" ");//한 라인 입력받고
				for (int x = 0; x < N; x++) {
					arr[y][x] = Integer.parseInt(temp[x]);//방 이차원배열에 저장
				}
			}

			for (int y = 0; y < N; y++) {
				for (int x = 0; x < N; x++) {
					System.out.println("Y :"+y+"  X :"+x);
					if (arrCnt[y][x] == 0) { // 방문하지 않았다면
						System.out.println("DFS 시작!");
						int temp = DFS(y, x);//dfs 재귀 호출
						if (temp > Max) {//순회한 이동 횟수가 저장된 최대값보다 크다면
							Max = temp;//최대값 업데이트
							Answer = arr[y][x];//최대 이동횟수를 가진 방 위치를 저장
						} else if (temp == Max && arr[y][x] < Answer) {//최대값이 다수일 때, 방번호가 이미 저장된 방 위치보다 더 작으면
							Answer = arr[y][x];//방 위치 업데이트
						}
						printBoard(arrCnt);
					}
					
				}
			}
			str.append("#").append(test_case).append(" ").append(Answer).append(" ").append(Max).append("\n");//테스트케이스별 출력문
		}
		System.out.println(str);//총 결과 출력
	}

	public static int DFS(int y, int x) {//재귀함수 시작
		if (arrCnt[y][x] != 0) {//이미 방문했던 곳이면
			return arrCnt[y][x];//재귀 종료
		}
		

		for (int idx = 0; idx < 4; idx++) {//총 4번 방향을 바꿈
			int ty = y + dy[idx];//0,0,상,하
			int tx = x + dx[idx];//좌,우,0,0

			if (0 <= ty && ty < N && 0 <= tx && tx < N && arr[y][x] + 1 == arr[ty][tx]) { // 범위를 넘어가지 않는다면
				return arrCnt[y][x] = DFS(ty, tx) + 1;//방 이동횟수 업데이트하면서 이동
			}
		}
		arrCnt[y][x] += 1;//if문에 들어가지 않았을 경우(범위 벗어날 때)에 방 이동횟수 추가
		return arrCnt[y][x];//재귀 종료

	}
	
	public static void printBoard(int[][] arr) {
		for(int[] a : arr) {
			System.out.println(Arrays.toString(a));
		}
		System.out.println();
		
	}
}