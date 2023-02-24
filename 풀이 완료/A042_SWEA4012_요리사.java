package 박승수;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.StringTokenizer;

public class A042_SWEA4012_요리사 {

	static int N; // N : 식재료의 개수
	static int[] collec; // collec : 조합을 임의로 저장해두는 배열
	static int[][] arr; // arr : 요리의 시너지를 저장하는 배열
	static ArrayList<int[]> collecs; // collecs : 조합을 저장해두는 배열

	public static void main(String[] args) throws IOException { // 시작
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); // br : 사용자 입력을 위한 BufferedReader
		StringBuilder sb = new StringBuilder(); // sb : 입력 출력을 위한 StringBuilder
		int T = Integer.parseInt(br.readLine()); // T : 테스트 케이스 개수

		for (int test_case = 1; test_case <= T; test_case++) { // 테스트 케이스 시작
			N = Integer.parseInt(br.readLine()); // N : 식재료의 개수
			arr = new int[N][N]; // arr : 요리의 시너지를 저장하는 배열
			collec = new int[N / 2]; // collec : 조합을 임의로 저장해두는 배열
			collecs = new ArrayList<>(); // collecs : 조합을 저장해두는 배열
			for (int i = 0; i < N; i++) { // 사용자 입력 받기위한 반복문 ( 시너지 )
				StringTokenizer st = new StringTokenizer(br.readLine(), " "); // 공백을 기준으로 나누기
				for (int j = 0; j < N; j++) { // 사용자 입력 받기위한 반복문 ( 시너지 )
					arr[i][j] = Integer.parseInt(st.nextToken()); // 요리의 시너지를 저장
				}
			}

			collection(0, 0); // N개중에 N/2개를 고르기 위한 collection
			int result = 99999999; // result: 결과값 변수
			for (int i = 0; i < collecs.size() / 2; i++) { // 조합에서 맨위와 맨아래를 요리 A, B로 두고 반복 진행
				int min = Math.abs(cook(collecs.get(i)) - cook(collecs.get(collecs.size() - i - 1))); // 요리 A와 요리 B의 차를
																										// 저장
				if (result > min)
					result = min; // 요리의 차가 최소면 저장
			}

			sb.append("#").append(test_case).append(" ").append(result).append('\n'); // 요리의 최소값 출력 저장
		}
		System.out.print(sb); // 결과 출력

	}

	private static void collection(int cnt, int start) { // N개중에 N/2개를 고르기 위한 collection
		if (cnt == N / 2) { // N개 중에 N/2개를 뽑았을 때
			collecs.add(Arrays.copyOfRange(collec, 0, collec.length)); // collecs에 해당 조합을 저장
			return;
		}

		for (int i = start; i < N; i++) { // 조합을 구하는 반복문
			collec[cnt] = i;
			collection(cnt + 1, i + 1);
		}
	}

	private static int cook(int[] tmp) { // 시너지의 합을 구하는 함수
		int sum = 0; // sum : 시너지의 합
		for (int i = 0; i < tmp.length; i++) { // 시너지의 합을 구하는 반복문
			for (int j = 0; j < tmp.length; j++) { // 시너지의 합을 구하는 반복문
				if (i == j)
					continue; // 같은 재료일 때 제외
				sum += arr[tmp[i]][tmp[j]]; // 시너지의 합 저장
			}
		}
		return sum; // 시너지의 합 return
	}
}