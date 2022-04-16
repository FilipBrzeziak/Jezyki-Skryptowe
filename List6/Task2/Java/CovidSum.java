import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class CovidSum {
    public static int covidSum(String country, int month) throws FileNotFoundException {
        int covidCases = 0;
        ArrayList<ArrayList<String>> listOfLists = new ArrayList<>();
        File file = new File("Covid.txt");
        Scanner sc = new Scanner(file);
        sc.nextLine();
        while (sc.hasNextLine()) {
            String line = sc.nextLine();
            ArrayList<String> covidDate = new ArrayList<>(List.of(line.split("\t")));
            listOfLists.add(covidDate);
        }

        for (ArrayList<String> listOfList : listOfLists) {
            if (month == Integer.parseInt(listOfList.get(2)) && listOfList.get(6).equals(country)) {
                covidCases = covidCases + Integer.parseInt(listOfList.get(4));
            }
        }
        return covidCases;
    }
}
