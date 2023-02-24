package 박승수;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class A055_SWEA5644무선충전_과제10 {
	static int[] dy = {0,-1,0,1,0}; 	//이동하는거 미리 정리
	static int[] dx = {0,0,1,0,-1};		//이동하는거 미리 정리
	static int M;						//움직임을 나타낼 M 변수
	static int A;						//충전기의 개수를 나타낼 A 변수
	static int[] user1;					//user1의 움직임을 저장할 배열변수
	static int[] user2;					//user2의 움직임을 저장할 배열변수
	static BC[] bcList;					//충전기의 정보를 저장할 배열변수

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine());
		
		for (int test_case = 1; test_case < T+1; test_case ++) {		//Test Case 수 만큼 순회
			String[] temp = br.readLine().split(" ");
			M = Integer.parseInt(temp[0]);								// 움직일 횟수 M 입력
			A = Integer.parseInt(temp[1]);								// 충전기의 갯수 A 입력
			
			user1 = new int [M+1];										// 유저1의 움직임을 저장할 변수 선언, 처음에도 충전이 가능하므로 M+1해서 선언
			user2 = new int [M+1];										// 유저2의 움직임을 저장할 변수 선언, 처음에도 충전이 가능하므로 M+1해서 선언
			String[] temp1 = br.readLine().split(" ");
			String[] temp2 = br.readLine().split(" ");
			
			for (int idx = 1; idx < M+1; idx ++) {
				user1[idx] = Integer.parseInt(temp1[idx-1]);			// 저장할떄 1번 인덱스부터 저장한다. 처음에 움직이지 않는걸로 시작 충전을 처리
				user2[idx] = Integer.parseInt(temp2[idx-1]);
			}
			
			
			bcList = new BC[A];
			for (int idx = 0; idx < A; idx ++) {						// 충전기의 정보를 받아와서 배열에 넣어준다
				temp = br.readLine().split(" ");						// 좌표를 0,0을 기준으로 잡을거기 때문에 -1 해서 좌표 받아줘야함
				bcList[idx] = new BC(Integer.parseInt(temp[0])-1,Integer.parseInt(temp[1])-1,Integer.parseInt(temp[2]),Integer.parseInt(temp[3]));
			}
			
			System.out.printf("#%d %d\n",test_case,solution());			// solution 실행한다.
			
			
			
		}
	}
	public static boolean isRange(int bcN, int Y, int X) {									//bcN : 충전기의 번호, int Y, int X : 유저의 위치
		if (bcList[bcN].range >= Math.abs(bcList[bcN].x - Y) + Math.abs(bcList[bcN].y-X)) {	//범위안에 들어오는지 확인해서
			return true;																	//범위안에 들어오면 true return		
		}
		return false;																		//범위안에 안들어오면 false return	
	}
	
	public static int solution() {
		int user1Y = 0;			//user1의 초기위치 초기화
		int user1X = 0;
		int user2Y = 9;			//user2의 초기위치 초기화
		int user2X = 9;
		int hap = 0;			//각 경우의 합을 저장할 변수 
		int max;				//한 움직임당 최대값을 저장할 변수
		int answer = 0;			//정답을 저장할 변수
		
		for (int idx = 0; idx < M+1; idx ++) {
			// 움직여주기
			user1Y +=  dy[user1[idx]];						//user1 움직이기
			user1X +=  dx[user1[idx]];
			
			user2Y +=  dy[user2[idx]];						//user2 움직이기
			user2X +=  dx[user2[idx]];
			
			max = 0;										//최대값 초기화
			for (int bc1 = 0; bc1 < A; bc1 ++) {			//모든 충전기의 경우의 수를 돌려서 확인한다.
				for(int bc2 = 0; bc2 < A; bc2 ++) {
					hap = 0;								//합 초기화
					boolean u1State = false;
					boolean u2State = false;
					
					if (isRange(bc1,user1Y,user1X)) {		// user1가 충전기1(bc1)에 범위에 닿는지 확인
						hap += bcList[bc1].power;			// 닿는다면 power를 더해주기
						u1State = true;						// 범위에 닿았다고 표시
					}
					if (isRange(bc2,user2Y,user2X)) {		// user1가 충전기1(bc1)에 범위에 닿는지 확인
						hap += bcList[bc2].power;			// 닿는다면 power를 더해주기
						u2State = true;						// 범위에 닿았다고 표시
					}
					
					if (bc1 == bc2 && u1State && u2State) { // 동일하다면 나눠 갖어야함.
						hap -= bcList[bc1].power;
					}
					
					max = Math.max(max, hap);				// 최대값으로 바꿔놓기
				}
			}
			
			answer += max;									// 최대 충전량을 더해주기
		}
		return answer;										// 정답 return
	}

}

class BC {				//충전기의 정보를 저장할 객체
	int y;				//충전기의 좌표
	int x;
	int range;			//충전기의 범위
	int power;			//충전기의 충전량
	
	BC(int y, int x, int range, int power) {	//생성
		this.y = y;
		this.x = x;
		this.range = range;
		this.power = power;
	}
}
