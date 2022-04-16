import java.io.FileNotFoundException;

public class Main {
    public static void main(String[] args) {
        String country = args[0];
        int month = Integer.parseInt(args[1]);
        try {
            System.out.println(CovidSum.covidSum(country,month));
        } catch (FileNotFoundException e) {
            System.out.println("File not found!");
        }

    }
}
