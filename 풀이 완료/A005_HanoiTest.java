package 박승수;

public class A005_HanoiTest {
	private static void hanoi(int cnt, int from, int temp, int to) {
		if (cnt == 1) {
	        System.out.println(cnt+":"+from + "->" + to);
	        return;
	    }
		//맨바닥을 제외한 그 윗부분 움직이기
	    hanoi(cnt - 1, from, to, temp);
	    System.out.println(cnt+":"+from + "->" + to);
	    //맨바닥 움직이기
	    hanoi(cnt -1, temp, from, to);
	
    }      

	public static void main(String[] args) {
		hanoi(3,1,2,3);
	}

}
