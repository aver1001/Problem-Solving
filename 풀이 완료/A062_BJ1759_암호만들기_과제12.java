package 박승수;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;

public class A062_BJ1759_암호만들기_과제12 {
	static ArrayList<Character> cList;
	static int L;
	static int C;
	static char[] choose;
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] temp = br.readLine().split(" ");
		L = Integer.parseInt(temp[0]); 				//서로 다른 알파벳 L
		C = Integer.parseInt(temp[1]);				//암호의 길이 C
		
		temp = br.readLine().split(" ");
		cList = new ArrayList<Character>();			//알파벳들을 저장할 배열
		choose = new char [L];						//선택한 알파벳을 저장할 배열
		for (int idx = 0; idx < C; idx ++) {
			cList.add(temp[idx].charAt(0));
		}
		
		Collections.sort(cList);					//알파벳 증가하는 순서로 만들어야 하기 때문에 정렬
		solution(0, 0,0,0);							// 조합 진행
	}
	
	public static void solution(int v,int start, int mo,int za) {
		if (v == L) {					//암호의 길이만큼 선택한 
			if (mo >= 1 && za >= 2) {	//모음이 1개이상 자음이 2개이상일경우
				printArr();				//print 해준다
			}
			return;
		}
		
		for (int idx = start; idx < C; idx ++) {
			choose[v] = cList.get(idx);			//조합 선택
			if (cList.get(idx) == 'a' || cList.get(idx) == 'e' || cList.get(idx) == 'i' || cList.get(idx) == 'o'|| cList.get(idx) == 'u') {
				solution(v+1, idx+1,mo+1,za);	// 모음일경우 모음 +1 해서 조합
			}else {
				solution(v+1, idx+1,mo,za+1);	// 자음일경우 자음 +1 해서 조합
			}
			
		}
	}
	
	public static void printArr() {		// 정답 출력하기 위한 메서드
		for (char c : choose) {
			System.out.printf("%c",c);
		}
		System.out.println();
	}

}
