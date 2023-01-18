import java.util.Scanner;

public class Main{
	public static void main(String[] args) {
		Scanner s = new Scanner(System.in);
		int num = s.nextInt();
		s.close();
		
		for(int i=1;i<=2*num-1;i++)
		{
			if(i<=num)
				for(int k=1;k <= i;k++)
					System.out.print("*");
			else
				for(int k=1;k <= 2*num-i;k++)
					System.out.print("*");
			if(i<2*num-1)
				System.out.println("");
		}
	}
}