package 박승수;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class A060_BJ20361_일우는야바위꾼 {
	static int X;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] temp = br.readLine().split(" ");
		
		X = Integer.parseInt(temp[1]);				//초기 공의 위치
		int K = Integer.parseInt(temp[2]);			//움직임의 횟수
		
		for (int idx = 0; idx < K; idx ++) {
			temp = br.readLine().split(" ");
			change(Integer.parseInt(temp[0]),Integer.parseInt(temp[1]));	//공 변경하는 두개의 컵을 인자로 넣어준다
		}
		
		System.out.println(X);

	}
	
	public static void change(int A, int B) { //변경하는 컵 A, B
		if (A == X){				//만약 A가 공이 있다면
			X = B;					//B위치를 공 위치로 넣어준다
		}else if (B == X) {			//만약 B가 공이 있다면
			X = A;					//A위치를 공 위치로 넣어준다
		}
	}

}
