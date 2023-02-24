package 박승수;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class A016__BJ11660_구간합구하기5 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); // 입력받을 버퍼리더 선언
		StringBuilder sb = new StringBuilder(); // 시간초과로 인해 스트링 빌더 만들어서 한번에 출력하기로 변경
		String[] temp = br.readLine().split(" "); // 입력받아서 공백으로 분리
		int N = Integer.parseInt(temp[0]); // 분리후 0번 인덱스 정수로 변환후 N으로 선언
		int M = Integer.parseInt(temp[1]); // 분리후 1번 인덱스 정수로 변환후 M으로 선언
		
		int board[][] = new int[N][N]; // 입력받을 N*N 배열 선언
		
		for (int y = 0; y < N; y ++) { //y 위치 순회
			temp = br.readLine().split(" "); // 입력아서 공백으로 분리
			for (int x = 0; x < N; x++) { // x위치 순회 
				board[y][x] = Integer.parseInt(temp[x]); // 배열에 값 채워주기
			}
		}
		
		//누적합 만들기
		// x 줄마다 누적합을 만들어놓음
		int hapBoard[][] = new int[N][N+1]; // 누적합 저장할 N*N+1 배열 선언
		for (int y = 0; y < N; y++) { // y 위치 순회 
			for (int x = 1; x < N+1; x ++) { // x 위치 순회 1번인덱스부터 돌아야 out of index 안나옴. 
				hapBoard[y][x] = hapBoard[y][x-1] + board[y][x-1]; //누적합 = 이전 누적합의 값 + 더할 값
			} 
		}
		
		
		
		// x1, y1, x2, y2, answer 선언;
		int x1 ;
		int x2 ;
		int y1 ;
		int y2 ;
		int answer;
		for (int test_case = 0; test_case < M; test_case ++) {
			answer = 0; // 누적합 저장할 변수 0으로 초기화
			temp = br.readLine().split(" "); // 공백으로 분리
			y1 =  Integer.parseInt(temp[0]); // y1값 삽입
			x1 =  Integer.parseInt(temp[1]); // x1값 삽입
			y2 =  Integer.parseInt(temp[2]); // y2값 삽입
			x2 =  Integer.parseInt(temp[3]); // x2값 삽입
			for (int y = y1-1; y<y2 ; y++) { // y1 ~ y2까지 순회하면서 
				answer += hapBoard[y][x2]-hapBoard[y][x1-1]; // 누적합을 구해 더해준다
			}
			sb.append(answer).append("\n"); // 시간초과로 스트링빌더로 더해서 한번에 출력
			
		}
		System.out.println(sb.toString()); // 결과 출력 
		
	}

}
