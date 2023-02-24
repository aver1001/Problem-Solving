package 박승수;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
public class A015__BJ11659_구간합구하기4 {

	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); // 입력받을 버퍼리더
		
		String[] temp = br.readLine().split(" "); // 입력받아서 공백으로 분리
		int N = Integer.parseInt(temp[0]); // 분리후 0번 인덱스 정수로 변환후 N으로 선언
		int M = Integer.parseInt(temp[1]); // 분리후 1번 인덱스 정수로 변환후 M으로 선언
		int arr[] = new int[N]; // 숫자 입력받을 배열 N의 길이로 초기화
		
		temp = br.readLine().split(" "); // 입력 받아서 공백으로 분리
		for (int idx = 0; idx < N; idx ++) { //N만큼 순회하면서 
			arr[idx] =  Integer.parseInt(temp[idx]); // 입력으로 들어온값 배열에 넣어줌
		}
		
		int hapArr[] = new int[N+1]; // 누적합 저장할 배열선언 0번인덱스는 0으로 둘꺼기 때문에 한칸 늘려서 생성
		for (int idx = 1; idx < N+1; idx ++) { // 1번인덱스부터 돌아야 out of index 안나옴. 
			hapArr[idx] = hapArr[idx-1] + arr[idx-1]; //누적합 = 이전 누적합의 값 + 더할 값
		} 
		
		
		int I;
		int J;
		for (int test_case = 0; test_case < M; test_case ++) { // M개의 테스트 케이스만큼 순회
			temp = br.readLine().split(" "); // 입력받아서 공백으로 분리
			I = Integer.parseInt(temp[0]); // 분리후 0번 인덱스 I로 선언
			J = Integer.parseInt(temp[1]); // 분리후 1번 인덱스 J로 선언
			
			System.out.println(hapArr[J]-hapArr[I-1]); // 누적합의 J - (I-1)으로 정답을 구할 수 있음.
			
		}

	}


}
