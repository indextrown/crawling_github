//점수와 학년을 입력 받아 60점 이상이면 합격, 미만이면 불합격을 출력한다. 4학년의 경우 70점 이상이어야 합격이다
import java.util.Scanner;
public class test4 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int score;
		int schoolgrade;
		
		System.out.printf("점수를 입력하시오");
		score = sc.nextInt();
		
		System.out.printf("학년읍 입력하시오,");
		schoolgrade = sc.nextInt();
		
		if (score>=60)
		{
			if(schoolgrade != 4)
			{
				System.out.printf("합격입니다");
			}
			else if (score >= 70)
			{
				System.out.printf("합격입니다");
			}
			else 
			{
				System.out.printf("불합격입니다");
			}
				
		}
		else
		{
			System.out.printf("불합격입니다");
		}
	
	}}
