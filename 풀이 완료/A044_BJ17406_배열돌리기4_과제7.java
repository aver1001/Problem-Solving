package 박승수;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

/*
 * 회전 연산이 하나일 경우 : 최소값 출력
 * 회전 연산이 여러 개일 경우 : 순열로 순서 구해서, 모두 탐색 후 최소값 출력
 * 
 * 회전 연산 정보 (r,c,s)
 * 사각형 왼쪽 위 (r-s,c-s)
 * 사각형 오른쪽 아래 (r+s,c+s)
 * 
 * 사각형 시계방향 회전
 * 
 * 행별 sum 중에서의 최소값 출력
 */

public class A044_BJ17406_배열돌리기4_과제7 {
	StringBuilder str = new StringBuilder("");

	static int n, m, k;// 배열 사이즈, 회전 횟수

	static int[][] arr;// 입력받는 배열
	static int[][] copyArr;// 여러번 반복할 배열
	static int[] r;// ex) 3
	static int[] c;// ex) 4
	static int[] s;// ex) 2

	static boolean[] isSel;// 순열 선택 플래그
	static int[] order;// 회전 순번
	static int[] dx = { 1, 0, -1, 0 };// 행에 대한 방향 배열
	static int[] dy = { 0, 1, 0, -1 };// 열에 대한 방향 배열

	static int min = Integer.MAX_VALUE;// 출력할 행의 합 결과

	public static void main(String[] args) throws IOException {
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));// 버퍼로 입력
		StringTokenizer st = new StringTokenizer(in.readLine(), " ");// 첫째줄 입력(배열크기 n by m, 회전연산개수 k)
		n = Integer.parseInt(st.nextToken());// 배열의 크기(행 개수)
		m = Integer.parseInt(st.nextToken());// 배열의 크기(열 개수)
		k = Integer.parseInt(st.nextToken());// 회전 연산 횟수

		arr = new int[n][m];// n by m 배열 생성
		copyArr = new int[n][m];// n by m 배열 생성
		r = new int[k];// 회전 연산 정보의 기준 행 인덱스
		c = new int[k];// 회전 연산 정보의 기준 열 인덱스
		s = new int[k];// 회전 연산 정보의 차이

		isSel = new boolean[k];// 0번부터 k번까지 택했는지 여부
		order = new int[k];// 회전 순번

		for (int i = 0; i < n; i++) {// n줄에 걸쳐
			st = new StringTokenizer(in.readLine(), " ");// 한 라인 입력 받고
			for (int j = 0; j < m; j++) {// 열의 개수만큼
				arr[i][j] = Integer.parseInt(st.nextToken());// 배열값 저장
			}
		}

		for (int i = 0; i < k; i++) {// 회전연산 입력 수만큼
			st = new StringTokenizer(in.readLine(), " ");// 한 라인 입력 받고
			r[i] = Integer.parseInt(st.nextToken()) - 1;// 회전의 중심 좌표 x(인덱스 0부터 시작하므로 -1)
			c[i] = Integer.parseInt(st.nextToken()) - 1;// 회전의 중심 좌표 y(인덱스 0부터 시작하므로 -1)
			s[i] = Integer.parseInt(st.nextToken());// 사각형의 너비 구할 변수
		}
		// ------------------------------------input----------------------------

		sol(0);// 회전 순번에 대한 재귀함수 호출

		System.out.println(min);// 행별 합의 최소값 출력
	}

	static public void sol(int cnt) {
		if (cnt == k) {// k번까지의 순열 구해서
			for (int i = 0; i < n; i++) {
				for (int j = 0; j < m; j++) {
					copyArr[i][j] = arr[i][j];// 배열 복사하고
				}
			}
			for (int e : order) {// 순번에 대해
				rotate(r[e], c[e], s[e]);// r,c,s 넘겨서 rotate 호출
			}
			findMin();// 최소값 구하기
			return;// 재귀 종료
		}
		for (int i = 0; i < k; i++) {// 0에서 k-1까지의 숫자 중
			if (isSel[i])// 선택되었었다면
				continue;// 반복 x

			isSel[i] = true;// 선택
			order[cnt] = i;// 순열 구하기
			sol(cnt + 1);// 다음 순번 구하기
			isSel[i] = false;// 선택 풀어주기
		}
	}

	static void findMin() {
		int hap = 0;// 행별 합
		int hMin = Integer.MAX_VALUE;// 행별 합의 최소값 초기화
		for (int[] a : copyArr) {
			hap = 0;// 합 0으로 초기화 후
			for (int b : a) {
				hap += b;// 같은 행의 열 데이터 모두 더해서
			}
			hMin = Math.min(hap, hMin);// 최소값 구함
		}
		min = Math.min(hMin, min);// 배열에서의 구해진 최소값과 기존 최소값 비교해 업데이트
	}

	static void rotate(int r, int c, int s) {// 회전 연산 함수
		for (int i = 0; i < (2 * s + 1) / 2; i++) { // 회전 시킬 그룹의 갯수 구하기
			int x = r - s + i;// 왼쪽 위 행
			int cx = x;// 왼쪽 위 행 값 저장
			int y = c - s + i;// 왼쪽 위 열
			int cy = y;// 왼쪽 위 열 값 저장
			int temp = copyArr[x][y]; // 마지막에 넣을 값 미리 빼놓음

			int idx = 0;// 4방향 돌기 위해 초기화
			while (idx < 4) {
				int nx = x + dx[idx];// 방향 설정
				int ny = y + dy[idx];// 방향 설정

				// 범위 안이라면
				if (nx <= (r + s) - i && ny <= (c + s) - i && nx >= r - s + i && ny >= c - s + i) {
					copyArr[x][y] = copyArr[nx][ny];// 값 업데이트
					x = nx;// 다음 인덱스 넘어가기
					y = ny;// 다음 인덱스 넘어가기
				}
				// 범위를 벗어났다면 다음 방향으로 넘어감
				else {
					idx++;// 방향 바꿈
				}
			}

			copyArr[cx][cy + 1] = temp; // 빼 놓은 값 넣어 줌
		}
	}
}
