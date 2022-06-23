package CodingTest;
import java.util.Arrays;
import java.util.LinkedHashSet;
import java.util.Scanner;

public class Solution {
	static int n,m;
	static int[] data, mm;
	static boolean[] isVisited;
	static LinkedHashSet<String> ans;

	public static void main(String[] args) {
		Scanner sc= new Scanner(System.in); //scanner객체 생성
		n = sc.nextInt(); //int형 입력 및 리턴
		m = sc.nextInt();
		data = new int[n];
		mm = new int[m];
		isVisited = new boolean[n];
		ans = new LinkedHashSet<>();
		
		for(int i = 0; i<n; i++) {
			data[i] = sc.nextInt();
		}
		Arrays.sort(data);
		dfs(0);
		ans.forEach(System.out::println); //중복제거
	}
	
	static void dfs(int cnt) {
		if(cnt==m) {
			StringBuilder sb = new StringBuilder();
			for(int p : mm) {
				sb.append(p).append(' ');
			}
			ans.add(sb.toString()); //set에 sb값을 String으로 바꿔 추가함
			return;
		}
		for(int i=0; i<n; i++) {
			if(!isVisited[i]) {
				isVisited[i]=true;
				mm[cnt]=data[i];
				dfs(cnt+1);
				isVisited[i]=false;	
			}
		}
			
	}
}

	//https://girawhale.tistory.com/72
	//15663번

