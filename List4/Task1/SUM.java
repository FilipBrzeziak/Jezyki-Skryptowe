import java.util.InputMismatchException;
import java.util.Scanner;

public class SUM {
    private static double getIntFromUser() {
        Scanner scanner = new Scanner(System.in);
        double sum = 0.0;
        while (scanner.hasNext()) {
            try {
                double x = scanner.nextDouble();
                sum = sum + x;
            } catch (InputMismatchException e) {
                scanner.next();
            }
        }
        return sum;
    }

    public static void main(String[] args) {
        System.out.println("SUM");
        System.out.println(getIntFromUser());
    }
}

