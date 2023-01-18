import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class Main{


    public static void main(String[] args){

        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int K = sc.nextInt();

        Queue<Integer> queue = new LinkedList<>();
        LinkedList<Integer> list1 = new LinkedList<>();

        for (int i = 1; i <= N; i++){
            queue.offer(i);
        }

        while (!queue.isEmpty()){
            for (int j = 0; j < K - 1; j++)
                queue.offer(queue.poll());
            list1.add(queue.poll());
        }

        System.out.print("<");
        for (int i = 0; i < list1.size() - 1; i++)
            System.out.print(list1.get(i) + ", ");
        System.out.println(list1.get(list1.size() - 1) + ">");
    }
}