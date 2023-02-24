package 박승수;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class A049_BJ1074_Z {
	
	// N 입력의 최대는 15
		// 2^15^2 = 10억 쯤이기 때문에 0.5초 시간제한에서 걸림.
		// 브루드포스가 아닌 다른 방법으로 문제를 해결해야함.
		static int y;	//	r => y
		static int x;	//  c => x
		
		public static void main(String[] args) throws IOException {
			BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
			String[] temp = br.readLine().split(" ");
			int N = Integer.parseInt(temp[0]);
			y = Integer.parseInt(temp[1]);
			x = Integer.parseInt(temp[2]);
			System.out.println(solution(N,0));
		}
		
		public static int solution(int n,int hap) {
			// n은 2^n이 한변임을 알리는 n
			// hap 은 지금까지 가져온 인덱스의 합
			
			if (n == 1) {	// 더 분할 안될경우
				if (y == 0 & x == 0) {
					return hap + 0;
				}else if (y == 0 & x == 1){
					return hap + 1;
				}else if (y == 1 & x == 0) {
					return hap + 2;
				}else if (y == 1 & x == 1) {
					return hap + 3;
				}
			}
			

			int mid = (int) Math.pow(2,n)/2; // 먼저 변의 중간 값을 알아낸다.
			int Add = (int) Math.pow(Math.pow(2,n),2) / 4;	// 더해줄값 미리 저장

			if (x < mid && y < mid) { // 왼쪽 위
				return solution(n-1,hap);	// n-1을 통해 사분할해서 다음 확인한
				
			}else if (x >= mid && y < mid) { // 오른쪽 위
				x -= mid;	// x좌표를 빼 다음 분할정복이 가능하도록 한다.
				return solution(n-1,hap+Add); // n-1을 통해 사분할해서 다음 확인하고 이전의 모든 인덱스를 더해준다
				
			}else if (x < mid && y >= mid) { // 왼쪽 아래
				y -= mid;	// y좌표를 빼 다음 분할정복이 가능하도록 한다.
				return solution(n-1,hap+Add * 2); // n-1을 통해 사분할해서 다음 확인하고 이전의 모든 인덱스를 더해준다
				
			}else {//오른쪽 아래
				x -= mid;	// x좌표를 빼 다음 분할정복이 가능하도록 한다.
				y -= mid;	// y좌표를 빼 다음 분할정복이 가능하도록 한다.
				return solution(n-1,hap +Add * 3); // n-1을 통해 사분할해서 다음 확인하고 이전의 모든 인덱스를 더해준다
			}
			
		}

}
