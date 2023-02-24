package 박승수;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;

public class A019_BJ12891_DNA비밀번호 {
	static HashMap<Character, Integer> table = new HashMap<Character, Integer>(); //문제에서 줄 최소 알파벳의 개수 저장할 HashMap
	static HashMap<Character, Integer> cnt = new HashMap<Character, Integer>(); //문자가 몇개인지 확인할 HashMap
	
	static int S; // 전체 문자열의 길이 S
	static int P; // 우리가 만들어야할 문자열의 길이 P
	static String target; //주어진 문자열
	public static void main(String[] args) throws IOException{
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] temp;
		
		temp = br.readLine().split(" ");
		S = Integer.parseInt(temp[0]); // 전체 문자열의 길이 입력
		P = Integer.parseInt(temp[1]); // 우리가 만들어야할 문자열의 길이 입력
		target = br.readLine(); // 주어진 문자열
		temp = br.readLine().split(" ");
		
		
		table.put('A', Integer.parseInt(temp[0])); // 문제에서 줄 최소 알파벳의 개수 저장할 HashMap에 변수 넣기
		table.put('C', Integer.parseInt(temp[1]));
		table.put('G', Integer.parseInt(temp[2]));
		table.put('T', Integer.parseInt(temp[3]));
		cnt.put('A',0); //문자가 몇개인지 확인할 HashMap에 변수 넣기
		cnt.put('C', 0);
		cnt.put('T', 0);
		cnt.put('G', 0);
		
		int lt = 0; //우리가 확인할 문자열의 왼쪽
		int rt = P-1; // 우리가 확인할 문자열의 오른쪽 
		int answer = 0; // 답을 넣을 answer 
		
		for (int idx = 0; idx < rt+1; idx++) { //초기 0번부터 P-1까지 P길이의 문자열의 문자 개수를 파악
			cnt.put(target.charAt(idx), cnt.getOrDefault(target.charAt(idx), 0)+1); // 문자개수확인할 HashMap에 문자개수 +
		}
		
		while(true) {
			if (isOk()) { // 만약 주어진 요구사항에 만족한다면
				answer ++; // 정답 += 1
			}
			if (rt == S-1) { // 마지막 까지 확인이 끝났다면
				break; // 그만 탐색
			}
			
			lt ++; // 왼쪽끝 += 1
			rt ++; // 오른쪽 끝 += 1
			
			cnt.put(target.charAt(lt-1), cnt.get(target.charAt(lt-1))-1); // 왼쪽의 문자는 더이상 포함되지 않으므로 개수확인에서 하나 빼줌
			cnt.put(target.charAt(rt), cnt.get(target.charAt(rt))+1);	  // 새로 들어온 문자를 개수확인에서 하나 더해줌
		}
		
		
		System.out.println(answer); // 정답 출력
	}
	
	public static boolean isOk() {
		for(char c: table.keySet()) { //  'A', 'C', 'G', 'T'를 돌면서
			if (cnt.get(c) < table.get(c)) { // 주어진 요구사항이 만족하지 못할경우
				return false; // false return
			}
		}
		return true; // 다 만족하면 true return
	}


}
