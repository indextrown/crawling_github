//시험점수가 80점이 이상이면 합격 판별을 하는 program 생성
import java.util.Scanner;
public class test {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		System.out.printf("성적을 입력하시오:");
		int grade;                                  //step1
		
		grade = sc.nextInt();                       //step2 키보드를 통해 입력받은 data 값을 grade 에 저장
		System.out.printf("기준점수를 입력하시오:");
		int A;
		A = sc.nextInt();   
		if (grade >= A)                             //step3
		{
			System.out.printf("훅하합니다! 합격입니다");  //step4
		}
		else
		{
			System.out.printf("불합격입니다");          //step4
		}
	}
}


//s1      시험 점수
//s2      입력
//s3      80점이상
//s4      합격/불합격