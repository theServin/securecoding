public class NullPointerExample{
    public static String getValue(String value){
        return value != null ? value : "Default Value"; // Explicit null check
    }

    public static void main(String[] args){
        String value = getValue("Secure Value");
        System.out.println("Value: "+value);
    }
}
