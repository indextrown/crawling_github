public class exam_4 {
    public static void main(String[] args) {
        int n = rollDie();
        System.out.printf("주사위의 눈: %d", n);
    }
    
    public static int rollDie() {
        double x = 6 * Math.random();
        int temp = (int) x;  //강제형변환
        return temp + 1;     //step3
    }
}
//p2
//외부 함수 앞에 변수 존재 => 반환을 하는구나