package 박승수;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class A032_BJ2493_탑 {

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		String[] temp = br.readLine().split(" ");
		int[] arr = new int[N];
		
		for (int idx = 0; idx < N; idx ++) {
			arr[idx] = Integer.parseInt(temp[idx]);
		}
		
		int[] result = new int[N];
		
		for (int idx = 1 ; idx < N; idx ++) { 
			int target = idx-1; // target을 idx로 잡아줌. arr에 0번부터 들어잇으니 -1해서 넣어줌
			while (target != -1) { // target이 -1이 아닐떄까지
				if (arr[target] >= arr[idx]) { // 만약 타겟이 더 높거나 같다면
					result[idx] = target+1; // result에 target+1 넣어줌
					break;
				}else {
					target = result[target]-1; // 그게아니라면 target을 바꿔주고 계속 진행
				}
			}
		}
		
		StringBuilder sb = new StringBuilder();
		
		for (int i : result) {
			sb.append(i).append(" ");
		}
		System.out.println(sb.toString());
		

	}

}
