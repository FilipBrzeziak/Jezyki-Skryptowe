import java.util.InputMismatchException;
import java.util.Scanner;

public class AVG {
    private static double getIntFromUser() {
        Scanner scanner = new Scanner(System.in);
        int i=0;
        double sum = 0;
        while (scanner.hasNext()) {
            try {
                double x= scanner.nextDouble();
                sum+=x;
                i++;
            } catch (InputMismatchException e) {
                scanner.next();
            }
        }
        return sum /i;
    }

    public static void main(String[] args) {
        System.out.println("AVG");
        System.out.println(getIntFromUser());
    }
}

