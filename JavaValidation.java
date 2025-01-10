public class InputValidation{
    public static String sanitizeInput(String input){
        return input.replace("<", "&lt;").replace(">", "&gt;"); // Prevent XSS
    }

    public static void main(String[] args){
        String userInput = "<script>alert('xss')</script>";
        String safeInput = sanitizeInput(userInput);
        System.out.println("Sanitized input: "+ safeInput);
    }
}