package 박승수;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;

public class A043_SWEA6808_규영이와인영이의카드게임 { // 클래스 시작
	static StringBuilder result; // 결과 출력을 위한 스트링빌더
	static int totalGame; // 총 게임 수 = 9!
	static int[] myCards; // 내 카드 리스트
	static int[] enemyCards; // 상대 카드 리스트

	public static void main(String args[]) throws Exception { // 메인 메소드 시작
		result = new StringBuilder(); // 스트링빌더 초기화
		totalGame = getTotalGame(); // 9! 을 계산하여 저장.
		int[] allCards; // 모든 카드 리스트, 상대방의 카드 리스트를 얻기 위해 사용
		String[] inputs; // 입력으로부터 받는 한 줄

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); // 버퍼를 이용하여 입력을 받는다.

		int T = Integer.parseInt(br.readLine()); // 반복 횟수를 입력으로부터 받는다.

		for (int test_case = 1; test_case <= T; test_case++) { // 입력 받은 테스트 케이스에 대해
			inputs = br.readLine().split(" "); // 다시 한 줄을 바다서 파싱을 한다.

			myCards = new int[9]; // 내 카드 리스트를 초기화
			enemyCards = new int[9]; // 상대 카드 리스트를 초기화
			allCards = new int[19]; // 모든 카드 리스트를 초기화

			// 카드 패(1~18) 만들기
			for (int i = 1; i <= 18; i++) { // 1부터 18까지
				allCards[i] = i; // 모든 카드에 인덱스와 1대1 대응되게 저장
			} // 반복문 종료

			// 내 카드들 받기
			for (int i = 0; i < 9; i++) { // 받은 입력으로부터
				myCards[i] = Integer.parseInt(inputs[i]); // 내 카드 숫자들을 받아 저장한다.
			} // 반복문 종료

			// 카드 패에서 내 카드들 빼기
			for (int i = 0; i < 9; i++) { // 모든 카드 리스트에서
				allCards[myCards[i]] = 0; // 내가 가진 카드들을 뺀다.
			} // 반복문 종료

			// 남은 카드들 상대방에게 주기
			int k = 0; // 상대방 카드 배열에 접근하기 위한 인덱스
			for (int i = 1; i <= 18; i++) { // 숫자가 1~18이므로 1부터 시작
				if (allCards[i] != 0) { // 만약 모든 카드 리스트에 0이 아닌 값이 있다면(즉 내가 가진 카드가 아니라면)
					enemyCards[k++] = i; // 상대방 카드 리스트에 추가.
				} // 조건문 종료
			} // 반복문 종료

			// next permutation을 구하기 위해 미리 정렬
			Arrays.sort(enemyCards);

			// 현재 내 패와 상대의 패로 승 수 구하기
			int winCount = getWinCount();

			// 결과 저장.
			result.append("#").append(test_case).append(" ").append(winCount).append(" ").append(totalGame - winCount)
					.append("\n");
		} // 반복문 종료
		// 결과 출력
		System.out.println(result);
	}

// 승 수 구하기
	private static int getWinCount() {
		int winTotal = 0; // 총 승 수
		int myPoint = 0; // 내 점수
		int enemyPoint = 0; // 상대방 점수

		// 일단 상대방의 패를 섞으면서
		do {
			myPoint = 0; // 내 점수 0으로 초기화
			enemyPoint = 0; // 상대방 점수 0으로 초기화

			// 매 판의 점수를 저장한다.
			for (int turn = 0; turn < 9; turn++) { // 한 판은 9턴으로 이루어져 있으므로
				if (myCards[turn] < enemyCards[turn]) { // 만약 상대방 패가 나보다 좋으면
					enemyPoint += (myCards[turn] + enemyCards[turn]); // 상대방 점수에 현재 나온 패의 합을 저장.
				} // 조건문 종료
				else { // 만약 내 패가 상대방 패보다 높으면
					myPoint += (myCards[turn] + enemyCards[turn]); // 내 점수에 현재 나온 패의 합을 저장한다.
				} // 조건문 종료

			} // 반복문 종료

			// 만약 내 점수가 더 높으면
			if (myPoint - enemyPoint > 0) {
				winTotal += 1; // 총 승 수 + 1
			}
			// 다음 상대방의 카드를 받는다.
		} while (getNextMixedCard());

		return winTotal; // 총 승 수 리턴
	} // 메소드 종료

// 카드 섞기 (팩토리얼)  next permutation 구현
	private static boolean getNextMixedCard() {
		int i = 8; // n -1 = 8

		// step1. 뒤쪽부터 꼭대기 원소의 위치를 찾는다.
		while (i > 0 && enemyCards[i - 1] >= enemyCards[i]) {
			--i;
		}

		// 즉 i ==0이라 빠져나왔거나 아니면 현재 원소가 앞의 원소보다 크기 때문에 빠져나온거다.
		// 따라서 i==0, 즉 모든 원소가 내림차순이면
		if (i == 0) {
			return false; // false종료
		}

		int j = 8; // j= n-1
		// 꼭대기 바로 앞(i-1)자리에 교환 할 값을 뒤쪽부터 찾는다.
		while (enemyCards[i - 1] >= enemyCards[j]) {
			--j;
		}

		// 찾은 후 스왑
		swap(enemyCards, i - 1, j);

		int k = 8; // k = n-1 = 8
		// 꼭대기부터 맨 뒤까지 오름차순으로 정렬
		while (i < k) {
			swap(enemyCards, i++, k--);
		} // 반복문 종료

		return true; // 참 종료
	}

// 게임 수 (9!) 구하기
	private static int getTotalGame() {
		int result = 1; // 곱셈은 해야 하므로 1 저장.

		for (int num = 1; num <= 9; num++) { // 9! = 1*2*....*8*9
			result *= num; // 각 반복의 num값 만큼 곱해준다.
		}
		return result; // 곱한 결과를 리턴한다.
	}

// 자리 바꾸기 메소드
	private static void swap(int[] input, int i, int j) {
		int temp = input[i];
		input[i] = input[j];
		input[j] = temp;
	}
}