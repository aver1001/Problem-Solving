package 박승수;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class A061_BJ2865_나는위대한슈퍼스타K {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] temp = br.readLine().split(" ");
		int N = Integer.parseInt(temp[0]);		//예선 참가자 수 N
		int M = Integer.parseInt(temp[1]);		//장르의 갯수 M
		int K = Integer.parseInt(temp[2]);		//본선 진출자 K
		
		ArrayList<Double> maxVal = new ArrayList<Double>();		//각각의 최고 능력치를 구할 배열
		for (int idx = 0; idx < N+1; idx ++) {					//배열 초기화
			maxVal.add(0.0);
		}
		
		for (int idx = 0; idx < M; idx ++) {
			temp = br.readLine().split(" ");
			for (int i = 0; i < 2*N; i+=2) {					//각각의 능력치를 받아
				double score = Double.parseDouble(temp[i+1]);
				int user = Integer.parseInt(temp[i]);
				if (maxVal.get(user) < score){					//그사람의 최고 능력치랑 비교해봤을때 이게 더 최고라면
					maxVal.set(user, score);					//이 능력치로 바꿔준다
				}
				
			}
			
		}
		Collections.sort(maxVal,(o1,o2) -> -o1.compareTo(o2));	//능력치들을 내림차순 정렬해서
		double answer = 0;
		for (int idx = 0; idx < K; idx ++) {
			answer += maxVal.get(idx);							//K개 만큼만 더한다
		}
		System.out.println(String.format("%.1f", answer));		//소수점 1의자리까지 보이게 반올림 해서 출력
	}

}
