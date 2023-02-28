package 박승수;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class A066_SWEA3289서로소집합 {
    static int[] root;
 
    public static void main(String[] args) throws NumberFormatException, IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = null;
        int T = Integer.parseInt(br.readLine());					// 테스트 케이스 수 입력
         
        for (int test_case = 1; test_case < T+1; test_case ++) {
            sb = new StringBuilder();
            sb.append("#").append(test_case).append(" ");
            String[] temp = br.readLine().split(" ");
             
            int n = Integer.parseInt(temp[0]);						//총 원소의 개수 n
            int m = Integer.parseInt(temp[1]);						//총 연산의 개수 m
             
            root = new int[n+1];									//자신의 부모를 바라볼 배열
            for (int idx = 0; idx < n+1; idx ++) {
                root[idx] = idx;									//처음은 자신은 자신을 보도록 설정
            }
             
            for (int idx = 0; idx < m; idx ++) {
                temp = br.readLine().split(" ");
                int commend = Integer.parseInt(temp[0]);
                int A = Integer.parseInt(temp[1]);
                int B = Integer.parseInt(temp[2]);
                 
                if (commend == 0) {									//합집합 연산의 경우
                    union(A,B);										//union 해준다
                }else {
                    if (find(A) == find(B)) {						//둘이 같은 구역에 포함되는지 확인하기 위해서 부모가 같은지 보자
                        sb.append(1);								//같다면 1
                    }else {
                        sb.append(0);								//다르다면 0
                    }
                }
            }
             
        System.out.println(sb.toString());
        }
         
         
         
 
    }
     
    public static void union(int a, int b) {
        a = find(a);			//서로의 부모를 찾아서
        b = find(b);
         
        if (a<b) {				//부모를 바꿔준다
            root[b] = a;		//작은값을 기준으로 병합
        }else {
            root[a] = b;
        }
    }
     
    public static int find(int x) {
        if (x != root[x]) {						//최상위 부모가 아닐경우
            return root[x] = find(root[x]);		//내 부모를 찾는다
        }
         
        return root[x];							//내 부모 리턴
    }
 
}