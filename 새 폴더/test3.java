//다중 if-else문 사용하여 입력받은 성적에 대해 학점을 부여하는 프로그램을 작성하라
import java.util.Scanner;
public class test3 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int score;
		char grade;
		score = sc.nextInt();

		if (score >=90)
			System.out.printf("A학점 입니다");
		else if (score >=80)
			System.out.printf("B학점 입니다");
		else if (score >=70)
			System.out.printf("C학점 입니다");
		else
			System.out.printf("F학점 입니다");
		
			
			
		
		
	}
}
