package 박승수;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class A021_SWEA2001_파리퇴치_과제3 {
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine()); // 테스트케이스의 수 
		String[] temp; // 입력받을 임시배열 
		int N; // N*N 배열 만들 변수
		int M; // M*M 으로 반복적으로 더할 변수
		int board[][]; // 2차원 배열 저장할 변수
		int hap; // M*M 의 합 더할 변수
		int answer; // 정답을 저장할 변수
		for (int test_case = 1; test_case < T+1; test_case++) { // 테스트 케이스 수 만큼 반복하며
			temp = br.readLine().split(" ");	//변수들을 받아줌
			N = Integer.parseInt(temp[0]);
			M = Integer.parseInt(temp[1]);
			board = new int [N][N];
			answer = 0;	//매 케이스마다 answer 을 0으로(정답은 정수들의 합이므로 0으로 설정) 초기화 해줌
			
			for (int y = 0; y < N; y ++) { // 배열 입력 받음
				temp = br.readLine().split(" ");
				for (int x = 0; x <N; x++) {
					board[y][x] =  Integer.parseInt(temp[x]);
				}
			}
			
			for (int y = 0; y<N-M+1; y++) {
				for (int x = 0; x < N-M+1; x++) { // x,y를 순회하는데, M*M사이즈로 확인할거라 N-M+1 까지만 확인해야 out of index 오류나지 않음
					hap = 0; // hap 0으로 초기
					for (int addX=0; addX<M;addX++) {
						for(int addY=0; addY<M; addY++) { // M*M안에 있는 숫자들을 다 더해줌
							hap += board[y+addY][x+addX]; 
						}
					}
					answer = Math.max(answer, hap); // 지금 더한 숫자와, 여태까지의 최대값중 최대를 answer에 넣어줌
				}
			}
			System.out.printf("#%d %d\n",test_case,answer); // 정답 출력
			
		}
	}
}
