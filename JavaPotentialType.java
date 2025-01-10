public class JavaPotentialType{
   public static void main(String[] args) {
      int x = 10;
      int y = Integer.parseInt("20"); // Can throw NumberFormatException
      System.out.println("Sum: " + (x + y));
      }
}