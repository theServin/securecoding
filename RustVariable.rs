fn main(){
   let x: i32 = 10;
   let y: i32 = "20".parse().unwrap_or(0); // Explicit handling of parsing errors
   println!("Sum: {}", x + y);
}