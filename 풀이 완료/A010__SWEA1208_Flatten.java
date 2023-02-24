package 박승수;
import java.lang.reflect.Array;
import java.util.*;
public class A010__SWEA1208_Flatten {
	static int arr[];
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		// 총 10개의 케이스가 주어짐
		for (int test_case = 1; test_case < 11; test_case++) { //10개의 테스트 입력 받
			int dump = sc.nextInt(); // 움직일수 있는 횟수
			arr = new int[100]; // 가로는 최대 100
			
			for (int idx = 0; idx < 100; idx ++) {
				arr[idx] = sc.nextInt(); //각각의 높이를 받아옴
			}
			// System.out.println(Arrays.toString(arr));
			
			for (int i = 0; i < dump; i ++) {// 제한까지 옮겨봄
				if (move() == false) { // 만약 최대와 최소 같을경우 더 옮길 수 없기때문에 stop
					break;
				}; 
			}
			
			System.out.printf("#%d %d\n",test_case,Arrays.stream(arr).max().getAsInt()-Arrays.stream(arr).min().getAsInt());
			// 다옮긴뒤 배열의 최대와 최소를 빼서 결과값을 출력함
		}

	}
	
	public static boolean move() {
		int max = 0; // 최대값을 저장할 변수 
		int maxIdx = 0; // 최대값의 인덱스를 저장할 변수
		int min = 1001; // 최소값을 저장할 변수 입력이 1~1000 이기 때문에 1001 으로 설정
		int minIdx = 0; // 최솟값의 인덱스를 저장할 변수
		for (int idx = 0; idx < 100; idx ++) {
			if (arr[idx]> max) { // 최대값보다 클경우
				maxIdx = idx; // 최대값의 인덱스 변경
				max = arr[idx]; // 최대값 변경
			}
			if(arr[idx] < min) { // 최솟값보다 작을경우
				minIdx = idx; // 최솟값의 인덱스 변경
				min = arr[idx]; // 최솟값 변경
			}
		}
		if (max==min || max-min == 1) { //더이상 옮겨도 의미가 없을경우 false return 해서 중지
			return false;
		}
		arr[maxIdx] --; // 최소 와 최대 서로 하나씩 옮기
		arr[minIdx] ++;
		return true; // 올바르게 수행했으므로 true return
	}

}
