package 박승수;
import java.util.*;
public class A006_SWEA1289_원재의메모리복구하기 {
	static String memory;
	
	public static int recur(int idx, boolean zero) {
		if (idx == memory.length()) {
			return 0;
		}
			if (memory.charAt(idx) == '0') {
				if (zero) {
					return recur(idx+1,zero);
				}else {
					return recur(idx+1,!zero) + 1;
				}
			}else {
				if (zero) {
					return recur(idx+1,!zero) + 1;
				}else {
					return recur(idx+1,zero);
				}
			}
	}

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		
		for (int t = 1; t <= T; t++) {
			int answer = 0;
			boolean zero = true;
			memory = sc.next();
			
			System.out.printf("#%d %d",t,recur(0,zero));
		}
	}

}
