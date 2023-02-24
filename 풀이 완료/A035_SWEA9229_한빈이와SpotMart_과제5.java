package 박승수;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class A035_SWEA9229_한빈이와SpotMart_과제5 {

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); // 입력받을 BufferedReader
		StringBuilder sb = new StringBuilder(); //출력할 StringBuilder
		
		int N;			//과자의 개수
		int M;			//무게 합 제한
		int T;			//Test_case 개수
		int answer;		//정답 저장할 변수
		int[] snack;	//각 과자의 무개를 저장할 정수형 배열
		String[] temp;	//입력값을 잠시 넣어둘 문자열 배열
		
		T = Integer.parseInt(br.readLine()); // test_cas 수 T
		
		for (int test_case = 1; test_case < T+1; test_case++) { // test_case 수 만큼 반복문을 돌면서 
			
			temp = br.readLine().split(" ");	// N,M을 받아준다.
			N = Integer.parseInt(temp[0]);		// N 정수로 변환
			M = Integer.parseInt(temp[1]);		// M 정수로 변환
			
			snack = new int [N]; 							// 과자의 무개를 넣을 snack 배열을 N 으로 초기화 해준다.
			temp = br.readLine().split(" ");				// sncak 무개를 받아온다.
			for (int idx = 0; idx < N; idx++) {				// snack개수만큼 반복문을 돌며
				snack[idx] = Integer.parseInt(temp[idx]);	// snack의 무개를 정수로 바꿔서 snack 배열에 넣어준다.
			}
			
			answer = -1; 							// 정답을 -1로 미리 초기화 한다. 넣을수 없는 경우 바로 -1로 출력이 되도록 하기 위함.
			for (int i = 0 ; i < N; i ++) {			// N개에서 2개를 고르는 조합을 구한다.
				for (int j = i+1; j < N; j++) {		
					if (snack[i] + snack[j] > M) {	// 만약 두 과자를 합쳐서 무게 제한보다 무거울 경우 계산하지 않고 넘어간다.
						continue;
					}
					answer = Math.max(answer, snack[i] + snack[j]);	//지금까지 가방에 넣은 과자의 합의 최대와, 지금 과자두개의 합중 큰 값 answer에 넣어준다.
				}
			}
			sb.append("#").append(test_case).append(" ").append(answer).append("\n"); // 정답을 StringBuilder에 추가해준다.
		}
		
		System.out.println(sb.toString()); // 정답 출력

	}

}
