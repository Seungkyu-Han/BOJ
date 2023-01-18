import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();

        double L = sc.nextDouble(), W = sc.nextDouble(), H = sc.nextDouble();

        double l = 0, r = Math.min(L, Math.min(W, H));
        double mid;

        for(int i = 0; i < 1000000; i++){
            mid = (l + r) / 2;
            long total = (long)(L / mid) * (long)(W / mid) * (long)(H / mid);

            if(total >= N){
                l = mid;
            }
            else{
                r = mid;
            }
        }

        System.out.println(r);

    }
}