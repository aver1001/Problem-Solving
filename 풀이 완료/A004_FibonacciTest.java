package 박승수;
import java.util.*;
public class A004_FibonacciTest {
    // 피보나치 n항을 계산하여 리턴 
    public static long fibo(int n) { 
        if (n <= 1) return n;
        return fibo(n - 1) + fibo(n - 2); // 어떤 문제가 있는지 주석을 달아보세요
        // 입력값이 커질수록 계산해야 하는 수가 지수적으로 증가한다.
        // 중복된 값들이 있기때문에 시간복잡도를 줄일 수 있는 방법이 존재할 것.
    }
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        System.out.println(fibo(N));
    }

}