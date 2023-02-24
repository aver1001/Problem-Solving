package 박승수; 

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class A046_BJ16435_스네이크버드 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[] arr; // 과일 높이 정보 배열
        int N, L; // N: 과일의 개수, L: 버드 초기 길이
        String[] temp;
        
        
        // 입력 받기 시작
        temp = br.readLine().split(" ");
        N = Integer.valueOf(temp[0]);
        L = Integer.valueOf(temp[1]);
        
        arr = new int[N];
        temp = br.readLine().split(" ");
        for(int i = 0; i<N; i++) {
            arr[i] = Integer.valueOf(temp[i]);
        }
        // 입력 받기 끝
        
        
        Arrays.sort(arr); // 과일 높이 정보 오름차순 정렬
        
        for(int h : arr) { // 과일 높이와 버드 길이 반복 비교
            if(L < h) { // 버드의 길이보다 과일 높이가 높을 때
                break; // 반복문 종료
            }
            L++; // 버드 과일 먹고 길이 길어짐
        }
        
        System.out.println(L); // 결과 출력 (버드 길이)
    }
}