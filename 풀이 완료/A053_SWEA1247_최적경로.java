package 박승수;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class A053_SWEA1247_최적경로 {
	static int N;
	static int[] per;
	static boolean[] choose;
	static Loc Company;
	static Loc Home;
	static Loc[] Customer;
	static int answer;

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine());
		
		for (int test_case = 1; test_case < T+1; test_case ++) {
			answer = Integer.MAX_VALUE;						//정답 최대값으로 초기화
			N = Integer.parseInt(br.readLine());			//고객의 수 
			per = new int[N];								//순열 구할 배열
			choose = new boolean[N];						//순열 구할때 골랐는지 확인할 배열

			Customer = new Loc[N]; 							//고객들의 위치를 저장할 배열
			String[] temp = br.readLine().split(" ");
			Company = new Loc(Integer.parseInt(temp[0]),Integer.parseInt(temp[1]));	//회사 위치 저장
			Home = new Loc(Integer.parseInt(temp[2]),Integer.parseInt(temp[3]));	//집 위치 저장
			
			int cnt = 0;
			for (int idx = 4; idx < N*2+4; idx +=2) {
				Customer[cnt++] = new Loc(Integer.parseInt(temp[idx]),Integer.parseInt(temp[idx+1]));	//고객의 위치 저장
			}
			
			Permutations(0);								//순열 진행
			System.out.printf("#%d %d\n",test_case,answer);
		}

	}
	
	public static void Permutations(int v) {
		if (v == N) {
			answer = Math.min(answer, calAllDistance());	//순열이 만들어졌다면 거리 계산해서 최솟값 갱신
			return;
		}
		
		for (int idx = 0; idx < N; idx ++) {
			if (choose[idx] == false) {						//선택하지 않았다면
				choose[idx] = true;							//선택했다고 표시 후
				per[v] = idx;								//순열에 값 넣어주고
				Permutations(v+1);							//재귀적으로 진행
				choose[idx] = false;						//선택 취소
			}
		}
		
	}
	
	public static int calAllDistance() {
		int hap = 0;
		
		hap += calDistacne(Home,Customer[per[0]]);							//집과 첫번째 고객의 거리 더하기
		for (int idx = 0; idx <N-1; idx++) {
			hap += calDistacne(Customer[per[idx]],Customer[per[idx+1]]);	//고객들의 거리 더하기
		}
		hap += calDistacne(Company,Customer[per[N-1]]);						//마지막 고객과 회사의 거리 구하
		
		
		return hap;
	}
	
	public static int calDistacne(Loc l1, Loc l2) {
		return Math.abs(l1.y - l2.y) + Math.abs(l1.x - l2.x);				//두 위치의 거리 구하기
	}

}

class Loc{
	int y;
	int x;
	
	Loc(int y, int x){
		this.y = y;
		this.x = x;
	}

	@Override
	public String toString() {
		return "Loc [y=" + y + ", x=" + x + "]";
	}
	
}