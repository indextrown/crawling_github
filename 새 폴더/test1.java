//입력된 수가 3의 배수인지 판별하는 프로그램 작성

import java.util.Scanner;
public class test1{
	public static void main(String[]args) {
		Scanner sc = new Scanner(System.in);
		int num;
		System.out.printf("숫자를 입력하시오");
		num = sc.nextInt();
		
		if (num %3==0)
		{
			System.out.printf("3의 배수입니다");
			
		}
		else
			System.out.printf("3의 배수가 아닙니다");
		
	}
}