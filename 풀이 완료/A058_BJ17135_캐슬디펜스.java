package 박승수;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;

public class A058_BJ17135_캐슬디펜스 {
	static int Y;
	static int X;
	static int D;
	static int[] Archer = new int[3];
	static ArrayList<Monster> monsterList;
	static ArrayList<Monster> CopyMonsterList;
	static int answer = 0;
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] temp = br.readLine().split(" ");
		Y = Integer.parseInt(temp[0]);					//배열의 크기
		X = Integer.parseInt(temp[1]);
		D = Integer.parseInt(temp[2]);					//궁수들의 사거리
		
		monsterList = new ArrayList<Monster>();
		
		for (int y = 0; y < Y; y++) {
			temp = br.readLine().split(" ");
			for (int x = 0; x < X; x++) {
				if (Integer.parseInt(temp[x]) == 1) {
					monsterList.add(new Monster(y,x));	//배열을 입력받으면서 적들의 위치를 파악한다.
				}
			}
		}
		
		Combinations(0,0);								//조합을 구한다.
		System.out.println(answer);
	}
	
	public static int Attack() {
		
		int hap = 0;
		Monster[] temp = new Monster[3];		//3명의 궁수가 각각 타겟팅할 몬스터 배열을 만들어 주고
		for (int idx = 0; idx < 3; idx ++) {
			temp[idx]=findEnemy(Y,Archer[idx]);	//궁수의 타겟팅 적을 배열에 넣어준다.
		}
		for (int idx = 0; idx < 3; idx ++) {
			if (temp[idx].x != 999999) {
				for (int jdx = 0; jdx < CopyMonsterList.size();jdx++) {		//타겟팅에 포함되는 친구들은 죽여준다.
					if (CopyMonsterList.get(jdx).x == temp[idx].x && CopyMonsterList.get(jdx).y == temp[idx].y) {
						hap += 1;
						CopyMonsterList.remove(jdx);
						jdx--;
						
					}
				}
			}
		}
		
		return hap;	//몇명 죽였는지 리턴해준다.
		
	}
	
	public static Monster findEnemy(int y, int x) {
		Monster Target = new Monster(999999,999999);	// 존재할수 없는 몬스터위치로 초기화 해주고
		int minDis = Integer.MAX_VALUE;
		for (int idx = 0; idx < CopyMonsterList.size(); idx ++) { // 몬스터를 순회하면서
			int dis = canAttack(y,x,CopyMonsterList.get(idx).y,CopyMonsterList.get(idx).x);	//거리를 계산한
			if (dis <= D) {											//공격할 수 있는 범위라면 
				if (dis == minDis) {								//최소거리와 같아면
					if (Target.x < CopyMonsterList.get(idx).x) {	//x가 더 작은친구로 변경한다.
						continue;
					}else {
						Target = CopyMonsterList.get(idx);
					}
				}else if (dis < minDis) {							//이번에 거리가 최소라면
					Target = CopyMonsterList.get(idx);				//타겟으로 설정한
					minDis = dis;									//최소거리를 업데이트 해준다
				}
			}
		}
		
		return Target;												//이 궁수의 타겟을 리턴한다.
		
	}
	
	public static int canAttack(int mx, int my, int ax, int ay) {
		return Math.abs(mx-ax) + Math.abs(my-ay);	
	}
	
	public static void moveEnemy() {
		for (int idx = 0; idx < CopyMonsterList.size(); idx ++) {	//살아있는 적들을 순회하면서
			CopyMonsterList.get(idx).y += 1;						//아래로 한칸 옮겨주고
			if (CopyMonsterList.get(idx).y >= Y){					// 범위를 넘어가는 친구는 삭제해준다.
				CopyMonsterList.remove(idx);
				idx--;
			}
		}
	}
	
	public static int check() {
		int hap = 0;
		while (true) {
			if (CopyMonsterList.size() == 0) {	//더이상 적이 없다면 진행하지 않는다
				break;
			}
			
			hap += Attack();		//공격해서 죽은 적을 더해주고
			moveEnemy();			//적을 움직여준다 
		}	
		return hap;					//총 몇명 죽일수 있는지 리턴한다.
		
	}
	
	public static void Combinations(int v, int start) {
		if(v == 3) {										//조합을 다 구했다면
			CopyMonsterList = new ArrayList<Monster>();
			for (int idx = 0; idx < monsterList.size(); idx ++) {		// 몬스터들의 위치를 복사한뒤
				CopyMonsterList.add(new Monster(monsterList.get(idx).y,monsterList.get(idx).x));
			}
			answer = Math.max(answer, check()); 	//check로 몇명 죽일수 있나 확인한뒤 최대값으로 바꿔놓는다.
			return;
		}
		
		for (int i = start; i < X; i ++) {		// 재귀적으로 조합을 구해주고,
			Archer[v] = i;
			Combinations(v+1,i+1);
		}
		
	}

}

class Monster{
	int y;
	int x;
	
	Monster(int y, int x) {
		this.y = y;
		this.x = x;
	}
	
}
