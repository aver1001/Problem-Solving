package 박승수;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;

public class A050_BJ6987_월드컵 {
	static int[] verseA ; 			// 누가누가 경기했는지 적어놓을 배열 A
	static int[] verseB ; 			// 누가누가 경기했는지 적어놓을 배열 B
	static ArrayList<Team> Answer;	// 정답을 넣어놓을것
	static ArrayList<Team> Now;		// 현재 진행사항을 넣어놓을 것
	static boolean answer;			// 백트레킹을 위한 변수
	
	public static void main(String[] args) throws IOException {
		verseA = new int[15];
		verseB = new int[15];
		
		
		int cnt = 0;
		for (int i = 0; i < 6; i ++) {		// 2개씩 뽑아 조합을 구해 경기들을 정해준다
			for (int j = i+1; j<6; j++) {
				verseA[cnt] = i;
				verseB[cnt++] = j;
			}
		}
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		for (int test_case = 0; test_case < 4; test_case++) {
			String[] temp = br.readLine().split(" ");
			Answer = new ArrayList<>();
			Now = new ArrayList<>();
			answer = false;
			for(int idx = 0; idx < 18; idx+=3) {	// 입력을 받아서 정답과 현재값을 초기화 해준다 
				Answer.add(new Team(Integer.parseInt(temp[idx]),Integer.parseInt(temp[idx+1]),Integer.parseInt(temp[idx+2])));
				Now.add(new Team(0,0,0));
			}
			
			solution(0);		// DFS 진행
			if (answer) {
				System.out.println(1);
			}else {
				System.out.println(0);
			}
			
			

		}
	}
	public static boolean isOk() {		// 백트레킹을 위해 더 진행이 불가능할경우 false return
		for(int teamNum = 0; teamNum <6 ;teamNum ++) {
			if (Now.get(teamNum).win > Answer.get(teamNum).win) { //만약 목표보다 더 이겨버리면 안됨
				return false;
			}
			if (Now.get(teamNum).lose > Answer.get(teamNum).lose) { //만약 목표보다 더 져버리변 안됨
				return false;
			}
			if (Now.get(teamNum).draw > Answer.get(teamNum).draw) { //만약 목표보다 더 비겨버리면 안됨
				return false;
			}

		}
		
		
		return true;
	}
	
	
	public static void solution(int v) {
		if (answer) {	//이미 가능하다면 더 진행하지 않는다.
			return;
		}
		
		if (v == 15) {	//마지막까지 왔다면 이게 정답과 같은지 확인한다
				for(int idx = 0; idx <6; idx ++) { // 하나라도 다를경우 return 해서 끝내준다
					if (Now.get(idx).draw != Answer.get(idx).draw || Now.get(idx).lose != Answer.get(idx).lose ||  Now.get(idx).win != Answer.get(idx).win) {
						return;
					}
			}
				answer = true; // 가능하다고 표시해준다
			return;
		}
		
		if (isOk()) {
			// A 승
			Now.get(verseA[v]).win++; 	//각각의 승리, 패배를 더하고 뺴준뒤 DFS 진행한다
			Now.get(verseB[v]).lose++;
			solution(v+1);
			Now.get(verseA[v]).win--;
			Now.get(verseB[v]).lose--;
			
			// B 승
			Now.get(verseA[v]).lose++;
			Now.get(verseB[v]).win++;
			solution(v+1);
			Now.get(verseA[v]).lose--;
			Now.get(verseB[v]).win--;
			
			// 무승부
			Now.get(verseA[v]).draw++;
			Now.get(verseB[v]).draw++;
			solution(v+1);
			Now.get(verseA[v]).draw--;
			Now.get(verseB[v]).draw--;
		}

	}
		

}

class Team{
	int win;	//승리수를 넣을 변수
	int lose;	//패배수를 넣을 변수
	int draw;	//동점수를 넣을 변수
	
	@Override
	public String toString() { // 디버깅용
		return "Team [win=" + win + ", draw=" + draw + ", lose=" + lose + "]";
	}

	Team(int win, int draw, int lose ){
		this.win = win;
		this.lose = lose;
		this.draw = draw;
	}
}
