package 박승수;

public class A002_ArrayTest {
    static int arr[] = { 10, 20, 30 };

    private static void printArray1() {
        for (int i = 0; i< arr.length; i++) {
        	System.out.println(arr[i]);
        }
    }

    private static void printArray1(int i) {
    	System.out.println(arr[i]);
    	if (i+1 == arr.length) {
    		return;
    	}
    		printArray1(i+1);
    }

    public static void main(String[] args) {
        printArray1();
        System.out.println("=========================");
        printArray1(0);
    }

}