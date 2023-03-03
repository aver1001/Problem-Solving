package 박승수;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;

public class A072_BJ17143_낚시왕 {	
	static int Y;
	static int X;
	static ArrayList<ArrayList<ArrayList<Shark>>> board;
	static int answer;
	static ArrayList<Shark> sharkList;
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		String[] temp =  br.readLine().split(" ");
		Y = Integer.parseInt(temp[0]);					//수조의 크기 Y
		X = Integer.parseInt(temp[1]);					//수조의 크기 X
		int M = Integer.parseInt(temp[2]);				//상어의 수 M
		
		board = new ArrayList<ArrayList<ArrayList<Shark>>>();	//상어를 저장할 2차원 배열
		sharkList = new ArrayList<Shark>();						//상어를 저장할 배열
		
		for (int y = 0; y < Y; y ++) {
			board.add(new ArrayList<ArrayList<Shark>>());
			for (int x = 0; x < X; x ++) {
				board.get(y).add(new ArrayList<Shark>());
			}
			
		}
		
		for(int idx = 0; idx < M; idx ++) {
			temp =  br.readLine().split(" ");
			int y = Integer.parseInt(temp[0])-1;	// 상어의 y위치 
			int x = Integer.parseInt(temp[1])-1;	// 상어의 x위치
			int s = Integer.parseInt(temp[2]);	// 상어의 속도
			int d = Integer.parseInt(temp[3]);	// 상어의 이동방향
			int z = Integer.parseInt(temp[4]);	// 상어의 크기
			
			Shark tempShark = new Shark(y,x,s,d,z);
			board.get(y).get(x).add(tempShark);		//2차원수조 배열에 상어 넣기
			sharkList.add(tempShark);				//상어들의 정보 저장
		}
		
		
		
		
		// 1. 낚시왕이 오른쪽으로 한 칸 이동한다.
		for(int idx = 0; idx < X; idx++) {
			// 2.	낚시왕이 있는 열에 있는 상어 중에서 땅과 제일 가까운 상어를 잡는다.
			//		상어를 잡으면 격자판에서 잡은 상어가 사라진다.
			fishing(idx);
			// 3. 상어가 이동한다.
			moveAllShark();
		}
		System.out.println(answer);
		
		
		
		
	}
	
	public static void fishing(int x) {	//낚시왕이 상어를 잡는 메서드
		
		for (int y = 0; y < Y; y ++) {							//y축으로 쭉 내려가면서
			if (! board.get(y).get(x).isEmpty()) { 				//상어가 있다면
				sharkList.remove(board.get(y).get(x).get(0));	//상어 리스트에서 지우고
				answer += board.get(y).get(x).get(0).size; 		//그 위치의 상어를 제거하고 무개를 더해준다
				board.get(y).get(x).clear();					//그 위치의 상어를 지워준다
				break;
			}
		}
	}
	
	public static void moveAllShark() {			//모든 상어가 이동하는 메서드
		for (Shark s : sharkList) {				//상어의 위치를 순회하면서
			board.get(s.y).get(s.x).remove(s);	//이전위치의 상어를 없애주고
			moveOneShark(s,s.speed);			//상어를 움직여준다
			board.get(s.y).get(s.x).add(s);		//상어의 움직인 위치를 넣어준다
		}
		eatShark();					//같은 위치에 있는 상어들을 큰거만 남겨놓는다
		
	}
	
	public static void moveOneShark(Shark s,int remainSpeed) {	//상어 한마리를 이동시키는 메서드
		if (s.direct == 1) { 							//상
			remainSpeed = remainSpeed % (2*Y-2);			//한바퀴 돌아서 자기자리 처리
			if (s.y-remainSpeed < 0) {						//남은거 이동하면 방향이동 해야할 경우
				int temp  = s.y;
				s.y =  0;									//y는 맨위로 이동하고
				s.direct = 2;								//방향전환 한 후
				moveOneShark(s, -(temp-remainSpeed));				//한번더 움직인다
			}else {
				s.y = s.y-remainSpeed;
			}
		}else if (s.direct == 2) {		//하
			remainSpeed = remainSpeed % (2*Y-2);	
			if (s.y + remainSpeed >= Y) {
				int temp = s.y;
				s.y = Y-2;
				s.direct = 1;
				moveOneShark(s, (temp+remainSpeed-Y));
			}else {
				s.y = s.y+remainSpeed;
			}
		}else if (s.direct == 3) {		//우
			remainSpeed = remainSpeed % (X*2 -2);
			if (s.x + remainSpeed >= X) {
				int temp = s.x;
				s.x = X-2;
				s.direct = 4;
				moveOneShark(s,(temp+remainSpeed-X));
			}else {
				s.x = s.x+remainSpeed;
			}
		}else if (s.direct == 4) {		//좌
			remainSpeed = remainSpeed % (X*2 -2);
			if (s.x-remainSpeed < 0) {
				int temp = s.x;
				s.x = 0;
				s.direct = 3;
				moveOneShark(s,-(temp-remainSpeed));
			}else {
				s.x = s.x-remainSpeed;
			}
		}
	}
	
	public static void eatShark() {							//이동후 중복된 위치에 있는 상어들을 처리하는 메서드
		for (int y = 0; y < Y; y ++) {
			for (int x = 0; x < X; x ++) {					//모든 위치를 순회하면서
				if(board.get(y).get(x).size() >= 2 ) {		//2마리 이상 있을경우
					
					Shark KingShark = new Shark(0, 0, 0, 0, -1);	//그 위치의 왕상어를 미리 만들어놓고
					for (Shark s : board.get(y).get(x)) {			//상어들을 순회하면서
						if (KingShark.size < s.size) {				//왕상어보다 클경우
							sharkList.remove(KingShark);			//왕좌에서 내려온 왕상어를 제거하고
							KingShark = s;							//왕상어를 바꿔준다
						}else {
							sharkList.remove(s);					//더 작으면 이상어는 죽음
						}
					}
					board.get(y).get(x).clear();					//이 칸 비워주고
					board.get(y).get(x).add(KingShark);				//왕상어만 남겨줌
				}
			}
		}
	}
	
	public static class Shark{
		int y;
		int x;
		int speed;
		int direct;
		int size;
		
		public Shark(int y, int x,int speed, int direct, int size) {
			super();
			this.y = y;
			this.x = x;
			this.speed = speed;
			this.direct = direct;
			this.size = size;
		}
		


	}
	
}


