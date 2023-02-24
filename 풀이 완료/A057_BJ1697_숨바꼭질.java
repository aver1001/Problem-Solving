package 박승수;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Deque;

public class A057_BJ1697_숨바꼭질 {
	static int K;
	static int N;
	static int[] DP = new int[100001];

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] temp = br.readLine().split(" ");
		int N = Integer.parseInt(temp[0]);			//시작지점
		K = Integer.parseInt(temp[1]);				//도착지점
		Arrays.fill(DP,100001); 					//갈수있는 입력의 최대치를 최대 이동거리로 초기화 한다.
		
		if (N == K) {
			System.out.println(0);					// 만약 시작지점과 도착지점이 같다면 0을  출력하고 종료한다 
		}else {
			BFS(N);									// BFS로 이동해보고
			System.out.println(DP[K]);				// K이동까지의 최소거리를 출력한다.
		}
		
		
		
	}
	
	public static void BFS(int N) {
		Deque<DIS> queue = new ArrayDeque<DIS>(); 		//움직임 저장할 큐를 만들어주고
		queue.add(new DIS(N,0));						//초기위치를 저장해준다. 
		while (!queue.isEmpty()) {						//큐가 빌때까지
			DIS nowDIS = queue.removeFirst();			//큐에서 정보하나 빼고 계산을 진행한다.
			if (nowDIS.loc*2 <= 100000 && DP[nowDIS.loc*2] > nowDIS.times+1) {	// 최대입력을 넘어가지 않고, 최소 이동횟수 일경우
				DP[nowDIS.loc*2] = nowDIS.times+1;								// DP 업데이트 한다음
				queue.add(new DIS(nowDIS.loc*2,nowDIS.times+1));				// 큐에 넣어준다 
			}
			
			if (nowDIS.loc+1 <= 100000 && DP[nowDIS.loc+1] > nowDIS.times+1) {	// 최대입력을 넘어가지 않고, 최소 이동횟수 일경우
				DP[nowDIS.loc+1] = nowDIS.times+1;								// DP 업데이트 한다음
				queue.add(new DIS(nowDIS.loc+1,nowDIS.times+1));				// 큐에 넣어준다 
			}
			
			if (nowDIS.loc-1 >= 0 &&DP[nowDIS.loc-1] > nowDIS.times+1) {		// 최소입력을 넘어가지 않고, 최소 이동횟수 일경우
				DP[nowDIS.loc-1] = nowDIS.times+1;								// DP 업데이트 한다음
				queue.add(new DIS(nowDIS.loc-1,nowDIS.times+1));				// 큐에 넣어준다 
			}
			
		}
	}

}

class DIS{
	int loc;
	int times;
	
	DIS(int loc, int times){
		this.loc = loc;
		this.times = times;
	}
}
