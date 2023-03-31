package 박승수;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.math.BigInteger;

public class B005_BJ1010_다리놓기 {
	static int N,M;
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		//	테스트 케이스 수 
		int T = Integer.parseInt(br.readLine());
		
		//왼쪽갯수, 오른쪽 개수
		int n,m;
		for (int test_case = 1; test_case < T+1; test_case ++) {
			String[] temp = br.readLine().split(" ");
			n = Integer.parseInt(temp[0]);
			m = Integer.parseInt(temp[1]);
			// 결국 mCn을 구하면 된다
			System.out.println(solution(n,m));
		}
	}
	
	public static BigInteger solution(int n,int m) {
		//OverFlow 나기때문에, BigInteger를 사용한다.
		return factorial(m).divide(factorial(n).multiply(factorial(m-n)));
	}

	public static BigInteger factorial(int num) {
		//팩토리얼 구해주는 함수
		BigInteger answer = new BigInteger("1");
		for (int i = 1; i < num+1; i ++) {
			
			answer = answer.multiply(new BigInteger(Integer.toString(i)));
		}
		return answer;
		
	}

}
