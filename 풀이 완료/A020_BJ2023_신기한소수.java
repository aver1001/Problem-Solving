package 박승수;

import java.util.Scanner;

public class A020_BJ2023_신기한소수 {
	static String[] start = {"2","3","5","7"}; // 시작하는 숫자 (가장 왼쪽)은 이 4가지 숫자로 시작됨
	static String[] prime = {"1","3","7","9"}; // 나머지 숫자들은 이 4가지 숫자로 이루어져 있음
	static int N; // 구해야할 문자열의 길이
	static int Now; // 여태까지 구한 숫자 넣을 임시변수
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in); // 입력값이 하나이므로 Scanner로 받아옴
		N = sc.nextInt(); // N받아옴
		
		for (String s : start) {
			find(s); // 시작문자열 4개 각각으로 시작함
		}
		
		
	}
	
	public static void find(String s) {
		
		Now = Integer.parseInt(s); //여러번 변환하지 않도록 정수형으로 변환후 저장
		for (int idx = 2; idx < Math.sqrt(Now); idx++) { //2부터 만든 숫자를 루트한값까지 로 나눈 나머지가 0일경우 이 숫자는 소수임
			if (Now % idx == 0) {
				return; // 소수가 아니면 stop
			}
		}
		
		if (s.length() == N) { // 만약 원하는 문자열길이까지 만들었다면
			System.out.println(s); // 출력 
			return; // 종료
		}
		
		for (String str : prime) { // 나올수 있는 문자열들을 순회하면서
			find(s+str); // 지금까지 만든 숫자 맨뒤에 더해서 재귀적으로 계속 만
		}
		
	}

}
