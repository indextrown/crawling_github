public class exam_1 {
    public static void main(String[] args) {
        double r = 7;  //틀린것 처럼 보이지만 자동으로 7.0으로 가져옴
        //만약 반대로 int그릇에 7.0을 해주면 안됨!!!
        //-> int a = 7.0; 안됨
        //   int a = int(7

        //시험 칠때 함수 명 앞에 있는 double 잘 봐라 안보고 결과값 int로 출력 할 수도 있음
        
        double h = 5;
        volume(r, h);

    }
    
    
    public static void volume(double radius, double height) {
    	double c;
    	c = Math.PI * radius * radius * height;
    	System.out.print(c);
    	//메서드 안에 step4 빼고 다 있다는거 인지해야함!!
    }
}
//패턴 3

