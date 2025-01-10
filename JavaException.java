import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
public class FileReaderExample{
    public static String readFile(String filePath) throws IOException {
        return Files.readString(Paths.get(filePath));
    }
    public static void main(String[] args){
        try{
            String content = readFile("example.txt");
            System.out.println("File content: "+content);
        }
		catch(IOException e) {
            System.err.println("Error reading file: "+e.getMessage());
        }
    }
}