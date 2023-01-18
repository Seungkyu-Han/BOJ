import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

public class Main {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        Set<Integer> hashset = new HashSet<>();

        int N = sc.nextInt();
        for(int i = 0; i < N; i++){
            int n = sc.nextInt();
            hashset.add(n);
        }

        StringBuilder result = new StringBuilder();

        int M = sc.nextInt();
        for(int i = 0; i < M; i++){
            int m = sc.nextInt();

            if(hashset.contains(m)){
                result.append(1 + "\n");
            }
            else{
                result.append(0 + "\n");
            }
        }

        System.out.println(result);
    }
}
