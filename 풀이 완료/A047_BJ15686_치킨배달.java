package 박승수;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.List;
import java.util.StringTokenizer;

public class A047_BJ15686_치킨배달 { // 치킨배달 클래스 시작
    static int N; // 집 수 N
    static int M; // 남겨놔야하는 치킨 집 수 M
    static List<int[]> chickenHouse; // 치킨 집 리스트
    static List<int[]> house; // 집 리스트
    static int[][][] length; // 집과 치킨집 사이의 거리
    static HashSet<Integer> arr; // 뽑은 치킨집 인덱스
    static int min; // 최소 값
    
    
    
    public static void main(String[] args) throws IOException { // main 메소드 시작
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); // 입력 시작
        StringTokenizer st = new StringTokenizer(br.readLine()); // 집 수와 치킨 집 수를 입력 받기 위한 스트링 토크나이져
        // 입력 시작
        N = Integer.parseInt(st.nextToken()); // 집 수 입력
        M = Integer.parseInt(st.nextToken()); // 남겨놔야 하는 치킨집 수 입력
        chickenHouse = new ArrayList<>(); // 치킨 집 위치 입력 배열 생성
        house = new ArrayList<>(); // 집 위치 입력 배열 생성
        int temp = 0;
        for(int i = 1; i<=N; i++) { // 지도 행 시작
            st = new StringTokenizer(br.readLine()); // 행마다 열 입력을 위한 스트링 토크나이져
            for(int j = 1; j<=N; j++) { // 지도 열 시작
                temp = Integer.parseInt(st.nextToken()); // 지도 입력
                if(temp == 1) { // 집 이라면 시작
                    house.add(new int[] {i,j}); // 집 위치를 추가
                } // 집 이라면 끝
                if(temp == 2) { // 치킨 집이라면
                    chickenHouse.add(new int[] {i,j}); // 치킨 위치를 추가
                } // 치킨 집이라면 끝
            } // 지도 열 끝
        } // 지도 행 끝
        length = new int[house.size()][chickenHouse.size()][2]; // 집과 치킨집 사이의 거리를 저장해두는 배열 생성
        // 입력 끝
        
        
        // 거리 계산 시작
        for(int i=0; i<house.size(); i++) { // 집마다 거리 계산 시작
            getLength(i,house.get(i)); // 집마다 거리를 구하는 메소드
        } // 집마다 거리 계산 끝
        // 거리 계산 끝
        
        // 정렬 시작
        for(int i=0; i<length.length; i++) {
            Arrays.sort(length[i], (o1,o2) -> o1[1]-o2[1]);
        }
        // 정렬 끝
        
        min = Integer.MAX_VALUE;
        
        arr = new HashSet<>();
        Combination(0,0);
        // 치킨 집 조합
        System.out.println(min);    
    }
    
    public static void getLength(int index, int[] a) { // 집마다 거리를 구하는 메소드 시작
        for(int i=0; i<chickenHouse.size(); i++) { // 집마다 치킨 집 계산 시작
            length[index][i][0] = i; // 배열에 인덱스 저장 완료
            length[index][i][1] = Math.abs(a[0]-chickenHouse.get(i)[0])+Math.abs(a[1]-chickenHouse.get(i)[1]); // 배열에 인덱스에 거리 저장 완료
        } // 집마다 치킨 집 계산 끝
    } // 집마다 거리를 구하는 메소드 끝
    
    public static void Combination(int cnt, int start) { // 조합 메소드 시작
        // 기저 조건
        if(cnt == M) { // M개를 고른 치킨 집 출력 끝
            getMinChickenHouse(); // 치킨 집 거리 최소 합을 구하는 메소드
            return; 
        } // M개를 고른 치킨 집 출력 끝
        // 우도 부분
        for(int i=start; i<chickenHouse.size(); i++) { // 치킨 집 사이즈만큼 돌기
            arr.add(i); // 치킨 집 인덱스를 뽑음
            Combination(cnt+1, i+1); // 뽑고나서 다음 뽑기 출발
            arr.remove(i);
        } // 치킨 집 사이즈만큼 돌기 끝
    } // 조합 메소드 끝
    
    private static void getMinChickenHouse() { // 치킨 집 거리 최소 합을 구하는 메소드
        int sum = 0;
        for(int i=0; i<house.size(); i++) {
            for(int j=0; j<chickenHouse.size(); j++) {
                // 만약에 배열을 확인 하였을때 최소인 거리를 가지는 치킨이 선택했다면
                if(arr.contains(length[i][j][0])) {
                    sum += length[i][j][1];
                    break;
                }
            }
        }
        if(min>=sum) {
            min = sum;
        }
    } // 치킨 집 거리 최소 합을 구하는 메소드 끝
} // 치킨배달 클래스 끝