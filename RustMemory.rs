fn get_value(opt: Option<&str>) -> &str{
    match opt{
        Some(val) => val,
        None => "Default Value", // Safe handling of absence
    }
}

fn main(){
    let value = get_value(Some("Secure Value"));
    println!("Value: {}", value);
}