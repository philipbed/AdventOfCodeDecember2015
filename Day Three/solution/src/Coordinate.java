/**
 * Created by Phil on 12/3/2015.
 */
public class Coordinate {

    private int col;

    private int row;

    public Coordinate(int row,int col){
        this.col = col;

        this.row = row;
    }

    public int getRow(){return row;}

    public int getCol(){return col;}

    public void setRow(int change){this.row = change;}

    public void setCol(int change){this.col = change;}

    public boolean equals(Object o){
        if (! (o instanceof Coordinate))
            return false;
        Coordinate c = (Coordinate) o;
        return (this.col == c.getCol()) && (this.row == c.getRow());
    }

    public int hashCode(){
         //int val = this.col + (2*this.row) +333;

        return this.col + (this.row*1000);
    }

    public String toString(){
        return "("+" "+this.row+", "+this.col+" )";
    }
}
