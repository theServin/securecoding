use std::sync::{Arc, Mutex};
use std::thread;

fn main(){
    let counter = Arc::new(Mutex::new(0));

    let mut handles = vec![];
    for _ in 0..5{
        let counter = Arc::clone(&counter);
        handles.push(thread::spawn(move || {
            let mut num = counter.lock().unwrap();
            *num += 1;
        }));
    }

    for handle in handles{
        handle.join().unwrap();
    }

    println!("Final count: {}", *counter.lock().unwrap());
}