package 박승수;

import java.io.BufferedReader; // 입력을 위해 import
import java.io.BufferedWriter; // 출력을 위해 import
import java.io.IOException; // 입출력 예외 처리를 위해 import
import java.io.InputStreamReader; // 입력을 위해 import
import java.io.OutputStreamWriter; // 출력을 위해 import

public class A045_BJ2839_설탕배달 {

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in)); // 입력을 위해 BufferedReader 객체 생성
        BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(System.out)); // 출력을 위해 BufferedWriter 객체 생성

        int N = Integer.parseInt(reader.readLine()); // 설탕의 무게 N 입력

        writer.write(Integer.toString(sugar(N))); // 봉지의 개수를 구하여 리턴하는 함수를 호출하여 결과 출력
        
        reader.close(); // BufferedReader 객체 반환
        writer.close(); // BufferedWriter 객체를 반환하며 시스템 출력

    }
    
    // N : 설탕의 무게
    public static int sugar(int N) { // 봉지의 개수를 구하여 리턴하는 함수
        int fiveCount = N / 5; // 5kg 봉지의 개수의 최댓값
        for (int i = fiveCount; i >=0; i--) { // 5kg 봉지의 개수를 줄여가며 각 경우 확인
            int n = N - i * 5; // 5kg 무게의 봉지를 제외하고 남은 설탕의 무게
            if (n % 3 == 0) return i + n / 3; // 남은 설탕은 3kg으로 채울 수 있다면 해당 봉지의 개수 리턴
        }
        return -1; // 5kg, 3kg으로 만들 수 없는 설탕의 무게이므로 -1 출력
    }

}



