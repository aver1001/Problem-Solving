package 박승수;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.PriorityQueue;

/*
 * 1. 리스트 정렬 시 comparable
 * 2. 절대값 작은 값 -> 다수일 경우, 가장 작은 수(음수) &&& 제거
 * 3.
 */

public class A037_BJ11286_절댓값힙 {

	static PriorityQueue<pair> pq = new PriorityQueue<>(); // pair
	static StringBuilder sb = new StringBuilder();

	public static void main(String[] args) throws NumberFormatException, IOException {
		// TODO Auto-generated method stub

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter wr = new BufferedWriter(new OutputStreamWriter(System.out));

		int n = Integer.parseInt(br.readLine());// n

		int x = 0;
		for (int i = 0; i < n; i++) {
			x = Integer.parseInt(br.readLine());
			CommandHandle(x);
		}

		wr.write(sb.toString());
		wr.close();
		br.close();
	}

	static void CommandHandle(int command) {
		if (command == 0) // 0
		{
			if (pq.isEmpty())
				sb.append(0).append("\n");
			else
				sb.append(pq.poll().Original).append("\n");

			return;
		}
		pq.add(new pair(Math.abs(command), command));
	}
}

class pair implements Comparable<pair> {
	int Abs; // 절댓값
	int Original; // 원본

	public pair() {
	}

	public pair(int Abs, int Original) {
		this.Abs = Abs;
		this.Original = Original;
	}

	@Override
	public int compareTo(pair p) {
		if (this.Abs < p.Abs)
			return -1; // 비교기준 : 오름차순.

		else if (this.Abs == p.Abs) {
			if (this.Original < p.Original)
				return -1;
		}

		return 1;
	}

}