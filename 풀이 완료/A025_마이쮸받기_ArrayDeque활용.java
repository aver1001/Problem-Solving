package 박승수;

import java.util.ArrayDeque;
import java.util.ArrayList;

public class A025_마이쮸받기_ArrayDeque활용 {

	public static void main(String[] args) {
		ArrayDeque<ArrayList <Integer>> queue = new ArrayDeque<ArrayList <Integer>>(); // 마이쮸 	받을 줄 Deque 선언 (번호, 받을 마이쮸 수)
		ArrayList<Integer> temp;
		int Mychew = 20; // 총 가지고 있는 마이쮸 
		int peopleCnt = 1; // 사람의 번호
		
		while (true) {
			ArrayList<Integer> arr = new ArrayList<Integer>(); // 새로운 사람 추가
			arr.add(peopleCnt++); // 사람의 번호를 넣고 다음을 위해 +1
			arr.add(1); // 마이쮸는 처음에 1개씩만 가져갈 수 있음
			queue.addLast(arr); // 줄스러 감 
			
			temp = queue.removeFirst(); // 마이쮸 받아갈 사람 선택
			Mychew -= temp.get(1); // 마이쮸 먹기
			temp.set(1, temp.get(1)+1); // 다음에 가져갈 마이쮸 카운팅 + 1
			
			queue.addLast(temp); // 다시 줄스러 가기
	
			if (Mychew <= 0) { // 만약 마이쮸 20개가 다 팔렸을경우 멈춘뒤 
				break;
			}
			
		}
		
		System.out.println(temp.get(0)); // 마지막으로 받아간 사람 출력

	}

}
