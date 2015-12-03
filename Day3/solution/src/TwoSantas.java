import java.io.File;
import java.io.FileNotFoundException;
import java.util.*;

/**
 * Created by Phil on 12/3/2015.
 */
public class TwoSantas {

    public static void main(String[] args) throws FileNotFoundException{
        String fileName = args[0];

        Scanner sc = new Scanner(new File(fileName));



        List<Coordinate> robolst = new ArrayList<>();
        List<Coordinate> santaslst = new ArrayList<>();
        Coordinate home = new Coordinate(0,0);

        Coordinate santa = new Coordinate(0,0);
        Coordinate robo = new Coordinate(0,0);
        santaslst.add(santa);
        robolst.add(robo);

        while(sc.hasNext()) {
            String ch = sc.next();

            for (int i = 0; i < ch.length(); i++) {
                char charac = ch.charAt(i);
                if (i %2 == 1) {

                    switch (charac) {
                        case '>':
                            santa.setRow(santa.getRow() + 1);
                            Coordinate c = new Coordinate(santa.getRow(), santa.getCol());
                            //set.add(c);
                            santaslst.add(c);
                            break;
                        case '<':
                            santa.setRow(santa.getRow() - 1);
                            Coordinate h = new Coordinate(santa.getRow(), santa.getCol());
                            //set.add(h);
                            santaslst.add(h);
                            break;
                        case '^':
                            santa.setCol(santa.getCol() + 1);
                            Coordinate b = new Coordinate(santa.getRow(), santa.getCol());
                            //set.add(b);
                            santaslst.add(b);
                            break;
                        case 'v':
                            santa.setCol(santa.getCol() - 1);
                            Coordinate g = new Coordinate(santa.getRow(), santa.getCol());
                            //set.add(g);
                            santaslst.add(g);
                            break;
                    }
                }
                else{
                    switch (charac) {
                        case '>':
                            robo.setRow(robo.getRow() + 1);
                            Coordinate c = new Coordinate(robo.getRow(), robo.getCol());
                            //set.add(c);
                            robolst.add(c);
                            break;
                        case '<':
                            robo.setRow(robo.getRow() - 1);
                            Coordinate h = new Coordinate(robo.getRow(), robo.getCol());
                            //set.add(h);
                            robolst.add(h);
                            break;
                        case '^':
                            robo.setCol(robo.getCol() + 1);
                            Coordinate b = new Coordinate(robo.getRow(), robo.getCol());
                            //set.add(b);
                            robolst.add(b);
                            break;
                        case 'v':
                            robo.setCol(robo.getCol() - 1);
                            Coordinate g = new Coordinate(robo.getRow(), robo.getCol());
                            //set.add(g);
                            robolst.add(g);
                            break;
                    }
                }
            }
        }
        Set<Coordinate> roboSet = new HashSet<>(robolst);
        Set<Coordinate> santasSet = new HashSet<>(santaslst);
        roboSet.addAll(santasSet);
        System.out.println(roboSet.size());
    }
}
