import java.util.Arrays;
import java.util.LinkedHashSet;
import java.util.Scanner;

public class Main {
	static int n,m;
	static int[] data, mm;
	static boolean[] isVisited;
	static LinkedHashSet<String> ans;

	public static void main(String[] args) {
		Scanner sc= new Scanner(System.in);
		n = sc.nextInt();
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
		ans.forEach(System.out::println);
	}

	
	static void dfs(int cnt) {
		if(cnt==m) {
			StringBuilder sb = new StringBuilder();
			for(int p : mm) {
				sb.append(p).append(' ');
			}
			ans.add(sb.toString());
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
