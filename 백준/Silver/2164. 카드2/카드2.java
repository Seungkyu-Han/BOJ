import java.util.*;

public class Main {
    public static void main(String[] args){

        Scanner sc = new Scanner(System.in);

        int num = sc.nextInt();

        Queue<Integer> card = new LinkedList<>();

        for(int i = 1; i <= num; i++)
            card.add(i);

        while(card.size() > 1){
            card.poll();
            card.add(card.poll());
        }

        System.out.println(card.poll());
    }
}
