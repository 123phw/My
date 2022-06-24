import java.util.Arrays;
import java.util.Comparator;
import java.util.LinkedHashSet;
import java.util.Scanner;

public class Solution {
	static int n, m;
	static int[][] data;
	static int[] pillar;
	static boolean[] isVisited;
	static LinkedHashSet<String> ans;

	public static void main(String[] args) {
		//Solution s = new Solution();
		Scanner sc = new Scanner(System.in);
		n = sc.nextInt();
		data = new int[n][2];
		int maxL=-34;
		int maxH=-29;
		int maxHIndex=-1;
		for(int i=0; i<n; i++) {
			data[i][0]= sc.nextInt();
			data[i][1]= sc.nextInt();
			if (maxL<data[i][0]) {
				maxL=data[i][0]; //마지막 인덱스값
			}
			if (maxH<data[i][1]) {
				maxH=data[i][1]; //가장 큰 높이
				maxHIndex=data[i][0]; //가장 큰 높이의 인덱스
			}
		}
		pillar = new int[maxL+1];
		for(int i = 0; i<data.length; i++) {
			pillar[data[i][0]]=data[i][1];
		}
		int temp=0;
		int sum=0;
		for(int i=0; i<maxHIndex+1; i++) {//left합
			if (pillar[i]>temp) {
				temp=pillar[i];
				
			}
			sum+=temp;
		}
		
		temp=0;
		for(int i=maxL; i>maxHIndex; i--) {
			if(pillar[i]>temp) {
				temp=pillar[i];
			}
			sum+=temp;
		}
		System.out.println(sum);
	}
}
