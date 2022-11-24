public class exam_5 {
    public static void main(String[] args) {
        int n = 4;
        int s = square(n);
        System.out.printf("한 변의 길이가 %d인 정사각형의 넓이: %d", n, s);
    }

    public static int square(int length) {
        return length * length;
    }
}
//p4
//변수에 length * length 저장하고 return에 변수를 넣어주면 깔끔
//int ret;
//ret = length * length;
//return ret;