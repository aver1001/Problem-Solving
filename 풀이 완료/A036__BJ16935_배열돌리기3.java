package 박승수;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.BufferedWriter;
import java.io.OutputStreamWriter;
import java.io.IOException;

public class A036__BJ16935_배열돌리기3 {

	static int N; // 행의 길이 N
	static int M; // 열의 길이 M
	static int[][] arr; // 원본 배열을 저장할 이차원 배열

	public static void main(String[] args) throws IOException {
		BufferedReader reader = new BufferedReader(new InputStreamReader(System.in)); // 입력을 위한 BufferedReader 객체 생성
		BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(System.out)); // 출력을 위한 BufferedWriter 객체 생성
		StringBuilder builder = new StringBuilder(); // 출력을 위한 StringBuilder 객체 생성

		String[] input = reader.readLine().split(" "); // 공백으로 구분되는 N, M, R 입력
		N = Integer.parseInt(input[0]); // 행의 길이 N 입력
		M = Integer.parseInt(input[1]); // 열의 길이 M 입력
		int R = Integer.parseInt(input[2]); // 연산 횟수 R 입력

		arr = new int[N][M]; // 원본 배열을 저장할 이차원 배열 생성
		int[] operations = new int[R]; // 입력된 연산을 저장할 배열 생성

		for (int i = 0; i < N; i++) { // 행의 길이만큼 반복
			input = reader.readLine().split(" "); // 공백으로 구분되는 배열 한 행의 정보 입력
			for (int j = 0; j < M; j++) { // 열의 길이만큼 반복
				arr[i][j] = Integer.parseInt(input[j]); // 배열의 정보 저장
			}
		}

		input = reader.readLine().split(" "); // 공백으로 구분되는 연산 입력
		for (int i = 0; i < R; i++) { // 연산 횟수만큼 반복
			operations[i] = Integer.parseInt(input[i]); // 입력된 연산 저장
		}

		for (int operation : operations) { // 모든 연산에 대해 반복
			operateArr(operation); // 입력된 연산에 따라 연산을 수행하고 원본 배열에 그 결과를 저장하는 함수 호출
			N = arr.length; // 행의 길이 갱신
			M = arr[0].length; // 열의 길이 갱신
		}

		for (int i = 0; i < N; i++) { // 행의 길이만큼 반복
			for (int j = 0; j < M; j++) { // 열의 길이만큼 반복
				builder.append(arr[i][j]).append(" "); // 배열의 원소와 출력 형식을 위한 공백 출력
			}
			builder.append("\n"); // 출력 형식을 위한 줄바꿈 출력
		}

		writer.write(builder.toString()); // StringBuilder 문자열 BufferedWriter에 출력

		reader.close(); // BufferedReader 객체 반환
		writer.close(); // BufferedWriter 객체를 반환하며 시스템 출력
	}

	public static void operateArr(int operation) { // 입력된 연산에 따라 연산을 수행하고 원본 배열에 그 결과를 저장하는 함수
		int[][] result = new int[N][M]; // 연산 결과를 저장할 배열 생성

		switch (operation) { // 입력된 연산에 따라 각 동작 수행
		case 1: // 상하 반전 연산
			for (int i = 0; i < N; i++) { // 행의 길이만큼 반복
				for (int j = 0; j < M; j++) { // 열의 길이만큼 반복
					result[i][j] = arr[N - 1 - i][j]; // 행 반전, 열 유지
				}
			}
			break; // 더 이상의 동작을 수행하지 않음
		case 2: // 좌우 반전 연산
			for (int i = 0; i < N; i++) { // 행의 길이만큼 반복
				for (int j = 0; j < M; j++) { // 열의 길이만큼 반복
					result[i][j] = arr[i][M - 1 - j]; // 행 유지, 열 반전
				}
			}
			break; // 더 이상의 동작을 수행하지 않음
		case 3: // 오른쪽으로 90도 회전하는 연산
			result = new int[M][N]; // 행, 열의 길이가 바뀐 새로운 배열 생성
			for (int i = 0; i < M; i++) { // 기존 배열의 열의 길이만큼 반복
				for (int j = 0; j < N; j++) { // 기존 배열의 행의 길이만큼 반복
					result[i][j] = arr[N - 1 - j][i]; // 행: 끝에서 기존 열을 뺀 값, 열: 기존 행
				}
			}
			break; // 더 이상의 동작을 수행하지 않음
		case 4: // 왼쪽으로 90도 회전하는 연산
			result = new int[M][N]; // 행, 열의 길이가 바뀐 새로운 배열 생성
			for (int i = 0; i < M; i++) { // 기존 배열의 열의 길이만큼 반복
				for (int j = 0; j < N; j++) { // 기존 배열의 행의 길이만큼 반복
					result[i][j] = arr[j][M - 1 - i]; // 행: 기존 열, 열: 끝에서 기존 행을 뺀 값
				}
			}
			break; // 더 이상의 동작을 수행하지 않음
		// 배열 4분할 시 각 구역의 번호는 아래와 같음
		// 1 2
		// 4 3
		case 5: // 4분할 구역 이동 연산 ( 1 -> 2 -> 3 -> 4 -> 1 )
			// 1 <- 4
			for (int i = 0; i < N / 2; i++) { // 1번 구역에 대해 반복
				for (int j = 0; j < M / 2; j++) { // 1번 구역에 대해 반복
					result[i][j] = arr[N / 2 + i][j]; // 4번 구역의 값을 차례로 저장
				}
			}
			// 2 <- 1
			for (int i = 0; i < N / 2; i++) { // 2번 구역에 대해 반복
				for (int j = M / 2; j < M; j++) { // 2번 구역에 대해 반복
					result[i][j] = arr[i][j - M / 2]; // 1번 구역의 값을 차례로 저장
				}
			}
			// 3 <- 2
			for (int i = N / 2; i < N; i++) { // 3번 구역에 대해 반복
				for (int j = M / 2; j < M; j++) { // 3번 구역에 대해 반복
					result[i][j] = arr[i - N / 2][j]; // 2번 구역의 값을 차례로 저장
				}
			}
			// 4 <- 3
			for (int i = N / 2; i < N; i++) { // 4번 구역에 대해 반복
				for (int j = 0; j < M / 2; j++) { // 4번 구역에 대해 반복
					result[i][j] = arr[i][M / 2 + j]; // 3번 구역의 값을 차례로 저장
				}
			}
			break; // 더 이상의 동작을 수행하지 않음
		case 6: // 4분할 구역 이동 연산 ( 1 <- 2 <- 3 <- 4 <- 1 )
			// 1 <- 2
			for (int i = 0; i < N / 2; i++) { // 1번 구역에 대해 반복
				for (int j = 0; j < M / 2; j++) { // 1번 구역에 대해 반복
					result[i][j] = arr[i][M / 2 + j]; // 2번 구역의 값을 차례로 저장
				}
			}
			// 2 <- 3
			for (int i = 0; i < N / 2; i++) { // 2번 구역에 대해 반복
				for (int j = M / 2; j < M; j++) { // 2번 구역에 대해 반복
					result[i][j] = arr[N / 2 + i][j]; // 3번 구역의 값을 차례로 저장
				}
			}
			// 3 <- 4
			for (int i = N / 2; i < N; i++) { // 3번 구역에 대해 반복
				for (int j = M / 2; j < M; j++) { // 3번 구역에 대해 반복
					result[i][j] = arr[i][j - M / 2]; // 4번 구역의 값을 차례로 저장
				}
			}
			// 4 <- 1
			for (int i = N / 2; i < N; i++) { // 4번 구역에 대해 반복
				for (int j = 0; j < M / 2; j++) { // 4번 구역에 대해 반복
					result[i][j] = arr[i - N / 2][j]; // 1번 구역의 값을 차례로 저장
				}
			}
			break; // 더 이상의 동작을 수행하지 않음
		}

		arr = result; // 연산 결과가 저장된 배열을 원본 배열로 설정
	}

}