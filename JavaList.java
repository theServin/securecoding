import java.util.ArrayList;

public class JavaList{
   public static void main(String[] args) {
      ArrayList<Integer> list = new ArrayList<>();
      list.add(1);
      list.add(2);
      list.add(3);
      Integer first = list.get(0);
      list.add(4); // Allowed, but potential for logical issues in concurrent environments
      System.out.println("First element: " + first);
   }
}