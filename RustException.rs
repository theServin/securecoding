use std::fs::File;
use std::io::{self, Read};

fn read_file(file_path: &str) -> Result<String, io::Error>{
    let mut file = File::open(file_path)?;
    let mut content = String::new();
    file.read_to_string(&mut content)?;
    Ok(content)
}

fn main(){
    match read_file("example.txt"){
        Ok(content) => println!("File content: {}", content),
        Err(e) => eprintln!("Error reading file: {}", e),
    }
}