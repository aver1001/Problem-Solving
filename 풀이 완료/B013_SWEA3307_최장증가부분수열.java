package 박승수;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class B013_SWEA3307_최장증가부분수열 {
	static ArrayList<Integer> LIS;
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		int T = Integer.parseInt(br.readLine());	//test case 수 입력
		
		int N;			//입력될 숫자의 개수
		String[] temp;	//입력용 임시 변수
		int loc;		//이진탐색으로 찾은 자신의 위치를 저장할 변수
		int num;		//입력받은 숫자를 저장할 변수
		
		for(int test_case = 1; test_case < T+1; test_case++) {
			LIS = new ArrayList<>();				//ArrayList를 초기화 한 후 
			N = Integer.parseInt(br.readLine());	//숫자의 개수를 입력받는다
			
			temp = br.readLine().split(" ");
	
			for (int idx = 0; idx < N ; idx ++) {	//숫자를 순회하면서
				num = Integer.parseInt(temp[idx]);
				loc = findLoc(num);					//숫자가 들어갈 위치를 이진탐색으로 찾는다
				if (loc == LIS.size()) {			//만약 가장 큰 숫자라면, 마지막에 넣어준다.
					LIS.add(num);
				}else {								//그게아니라면
					if(num < LIS.get(loc)) {		//내 위치의 값이 나보다 클 경우
						LIS.set(loc, num);			//이 위치의 값을 나로 변경한다
					}	
				}
			}
			//ArrayList의 길이가, 최장 증가수열임.
			sb.append("#").append(test_case).append(" ").append(LIS.size()).append("\n");
			
			
		}
		//출력
		System.out.println(sb.toString());
	}
	
	public static int findLoc(int target) {
		/*
		 * 이진탐색으로 자신의 위치를 찾는 메서드
		 */
		int lt = 0;					// 왼쪽
		int rt = LIS.size();		// 오른쪽을 정해주고
		int mid = (int)(rt+lt)/2;	// 중간지점을 구한다
		
		while (lt < rt) {
			if (LIS.get(mid) >= target) { 	//만약 값이 나보다 크다면 rt를 중간으로 바꿔줘 왼쪽을 탐색한다
				rt = mid;
			}else {							//만얄 값이 나보다 작다면 lt를 중간으로 바꿔줘 오른쪽을 탐색한다
				lt = mid+1;
			}
			mid = (int)(rt+lt)/2;			//중간지점을 변경해준다
		}
		
		return mid;
		
		
		
	}
}
