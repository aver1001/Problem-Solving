package 박승수;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;

public class A023_SWEA1218_괄호짝짓기_배열활용 {

	public static void main(String[] args) throws IOException {
		ArrayList<Character> stack = new ArrayList<Character>(); //스택으로 사용할 ArrayList 선언
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); // 입력 받을 BufferReader 선언
		
		
		for(int i = 1; i < 11; i ++) {
			stack.clear(); // 스택 초기화
			int N = Integer.parseInt(br.readLine()); // 문자열의 길이 입력
			String target = br.readLine(); // 문자열 입력
			

			for (int idx = 0; idx < N; idx++) { // 문자열을 하나씩 순회하면서
				if (stack.size() == 0) { // 만약 스택이 비어있다면
					stack.add(target.charAt(idx)); // 스택에 문자열을 넣어준뒤 다음 반복문을 진행한다
					continue;
				}
				
				//만약 지금 순회한 문자열과 stack의 peek가 괄호를 열고닫는 순서에 맞을경우 stack에 pop을 한뒤 push는 진행하지 않고 넘어간다.
				//size와 인덱스의 괴리가 1 있기때문에 이를 처리하기 위해 -1 해줘야함.
				if (((stack.get(stack.size()-1)) == '(' && target.charAt(idx) == ')')|| ((stack.get(stack.size()-1)) == '[' && target.charAt(idx) == ']') || ((stack.get(stack.size()-1)) == '{' && target.charAt(idx) == '}') || (stack.get(stack.size()-1)) == '<' && target.charAt(idx) == '>') {
					stack.remove(stack.size()-1);
					continue;
				}
				
				stack.add(target.charAt(idx)); // 아무것도 해당되지 않았을경우 괄호를 스택에 넣어줌
			}
			
			
			if(stack.size() == 0) { // 만약 스택에 뭐가 남아있다면 괄호의 짝이 맞지 않은것이고 비어있다면 괄호의 짝이 맞는것.
				System.out.printf("#%d %d\n",i,1);
			}else {
				System.out.printf("#%d %d\n",i,0);
			}
			
		}
		
		

	}


}
