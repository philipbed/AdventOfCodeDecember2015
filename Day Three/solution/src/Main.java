import javax.security.auth.callback.CallbackHandler;
import java.io.File;
import java.io.FileNotFoundException;
import java.util.*;

public class Main {

    public static void main(String[] args) throws FileNotFoundException{
        String fileName = args[0];

        Scanner sc = new Scanner(new File(fileName));


        Set<Coordinate> set = new HashSet<>();

        List<Coordinate> lst = new ArrayList<>();
        Coordinate home = new Coordinate(0,0);
        lst.add(home);
        Coordinate copy = home;
        while(sc.hasNext()) {
            String ch = sc.next();

            for (int i = 0; i < ch.length(); i++) {
                char charac = ch.charAt(i);
                switch (charac) {
                    case '>':
                        copy.setRow(copy.getRow() + 1);
                        Coordinate c =new Coordinate(copy.getRow(),copy.getCol());
                        //set.add(c);
                        lst.add(c);
                        break;
                    case '<':
                        copy.setRow(copy.getRow() - 1);
                        Coordinate h = new Coordinate(copy.getRow() ,copy.getCol());
                        //set.add(h);
                        lst.add(h);
                        break;
                    case '^':
                        copy.setCol(copy.getCol() + 1);
                        Coordinate b = new Coordinate(copy.getRow(), copy.getCol());
                        //set.add(b);
                        lst.add(b);
                        break;
                    case 'v':
                        copy.setCol(copy.getCol() - 1);
                        Coordinate g = new Coordinate(copy.getRow(), copy.getCol());
                        //set.add(g);
                        lst.add(g);
                        break;
                }
            }
        }
        Set<Coordinate> s = new HashSet<>(lst);
        System.out.println(s.size());
    }
}
