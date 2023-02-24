package 박승수;
import java.util.*;

public class A012_SWEA2805_농작물수확하기 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt(); // 테스트 케이스 개수 입력 받기
		
		for (int test_case = 1; test_case < T+1; test_case++) {
			int N = sc.nextInt(); // N 크기 입력 받기
			int board[][] = new int [N][N]; // 입력받은 N으로 배열선언하기
			sc.nextLine(); // 개행문자 오류로 인해 개행문자 날려주기
			for (int y = 0; y<N; y++) {
				String temp = sc.nextLine(); //한줄 받아온뒤 
				for(int x = 0; x<N; x++) { 
					board[y][x] = temp.charAt(x)-'0'; //문자 하나씩 빼서 숫자로 바꿔서 배열 채워주기
				}
			}
			int hap = 0; // 결과값 저장할것 미리 초기화
				
			int cnt = 0; // 좌우로 한칸씩 빼줄 cnt 선언
			for(int y = N/2;y > -1 ; y--) { // N//2 즉 중간부터 시작해서 위로 (y-1) 이동
				for (int x = cnt; x < N-cnt; x++) { // 좌우를 cnt만큼 빼서 시작해 점점 범위를 줄여나가기
					hap += board[y][x]; // 결과값에 더해주기
				}
				cnt ++; // 좌우를 한칸씩 더 빼기위해 cnt 늘려주기 
			}
			
			cnt = 1; // 좌우로 한칸씩 빼줄 cnt초기화 가장 중간은 이미 더했기때문에 1부터 시작
			for(int y = N/2+1;y < N ; y++) { // 같은이유로 중간+1부터 시작
				for (int x = cnt; x < N-cnt; x++) { // 좌우로 cnt 만큼 빼서 돌려주기 
					hap += board[y][x]; // 결과값에 더해주기 
				}
				cnt++;// 좌우 한칸씩 늘려주기
			}
			
			System.out.printf("#%d %d\n",test_case,hap);
			
			
		}
	}

}
