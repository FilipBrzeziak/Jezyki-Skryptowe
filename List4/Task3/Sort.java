import java.util.*;

public class Sort {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        List<List<String>> lines = new ArrayList<>();
        String line = null;
        int counter=0;
        while (scanner.hasNext()) {
            line = scanner.nextLine();
            counter++;
            if (!line.isEmpty()){
                lines.add(List.of(line.split("    ")));
            }
        }
        lines.sort(new Comparator<List<String>>() {
            @Override
            public int compare(List<String> o1, List<String> o2) {
                int val1 = Integer.parseInt(o1.get(2));
                int val2 = Integer.parseInt(o2.get(2));
                return Integer.compare(val1, val2);
            }

        });
        for (int i=0; i<lines.size();i++){
            for (int j=0; j<lines.get(i).size();j++) {
                System.out.print(lines.get(i).get(j)+"\t");
            }
            System.out.println();
        }
    }
}
