fn divide(a: i32, b: i32) -> Result<i32, &'static str>{
	if b == 0 {
		Err("Cannot divide by zero")
	} else {
		Ok(a / b)
	}
}

fn main(){
	let result = divide(10, 0);
	
	match result {
		Ok(value) => println!("Result is: {}", value),
		Err(_) => println!("An error occurred!"),
	}
}