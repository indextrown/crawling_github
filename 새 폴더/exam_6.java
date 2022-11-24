public class exam_6 {
    public static void main(String[] args) {
    	//파라메타 값이 틀리니까 메서드 중복 가능
    	//같아도 가능하지만 무의미
        turnOn(30);
        turnOn(19);
    }

    public static void turnOn(int temperature) {
        if (temperature > 25) {
            System.out.printf("현재 온도 %d도, 에어컨을 가동합니다.", temperature);
        }
    }
}
//p3
//파라메타 2개 받으려면 9행부터 끝까지 한개 더 필요함