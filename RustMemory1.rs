fn main(){
   let mut vec = vec![1, 2, 3];
   let first = &vec[0]; // Immutable borrow
   // vec.push(4); // Error: mutable borrow occurs while immutable borrow exists
   println!("First element: {}", first);
}