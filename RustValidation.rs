fn sanitize_input(input: &str) -> String{
    input.replace('<', "&lt;").replace('>', "&gt;") // Prevent XSS
}

fn main(){
    let user_input = "<script>alert('xss')</script>";
    let safe_input = sanitize_input(user_input);
    println!("Sanitized input: {}", safe_input);
}