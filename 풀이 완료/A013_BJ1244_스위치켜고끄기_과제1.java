package 박승수;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class A013_BJ1244_스위치켜고끄기_과제1 {

	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); // 버퍼로 받기위해 버퍼 객체 선
		int N = Integer.parseInt(br.readLine()); // N을 받아온뒤 정수로 변환
		String s[] = br.readLine().split(" "); // 전구상태 받아와서 공백으로 분리 후 문자열 배열에 넣어주기
		int Students = Integer.parseInt(br.readLine()); // 학생수 받아서 정수로 변환
		for (int i = 0; i <Students; i ++) { // 학생수만큼 for문 돌면서 
			String temp[] = br.readLine().split(" "); // 문자열 받아 공백으로 분리 
			int sexs = Integer.parseInt(temp[0]); //성별과 
			int cnt = Integer.parseInt(temp[1]); // 번호로 나눠준다.
			
			//남학생
			if (sexs == 1) { // 남학생일경우 
				for (int idx = cnt-1; idx <N; idx += cnt) { //cnt 만큼 점프하면서  1 ->0 0 ->1 바꿔주기 0번 인덱스가 1이므로 주
					if (s[idx].equals("0")) { // 0일경우
						s[idx] = "1"; // 1로변경
					}else {// 1일경우 
						s[idx] = "0"; //0으로 변경
					}
				}
			}
			//여학생
			else {
				cnt -= 1; // 인덱스 맞춰주기 위해 1 빼준뒤 
				if (s[cnt].equals("0")) { // 초기 인덱스값은 무조건 변경이기 때문에 1과 0 서로 변환
					s[cnt] = "1";
				}else {
					s[cnt] = "0";
				}
				int lt = cnt-1;// 왼쪽으로 탐색할 포인터 선언
				int rt = cnt+1;// 오른쪽으로 탐색할 포인터 선언
				while (true) {
					if (0<=lt && rt < N && s[lt].equals(s[rt])) { // 범위를 넘지 않고, 좌우 포인터의 값이 같을경우 값 변환 진
						if (s[lt].equals("0")) {
							s[lt] = "1";
						}else {
							s[lt] = "0";
						}
						
						if (s[rt].equals("0")) {
							s[rt] = "1";
						}else {
							s[rt] = "0";
						}
					}else { // 만족하지 않을경우 break로 멈
						break;
					}
					lt -= 1; //포인터 하나씩 옮김
					rt += 1;
					
				}
				
			}
		}
		
		
	for (int idx = 0; idx <N; idx ++) {
		System.out.printf("%s ",s[idx]);
		if ((idx+1) % 20 == 0) {
			System.out.println();
		}
	}
		
		
		
	}

}
