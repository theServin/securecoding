import java.util.concurrent.atomic.AtomicInteger;
public class ConcurrencyExample{
    public static void main(String[] args) {
        AtomicInteger counter = new AtomicInteger(0);

        Thread[] threads = new Thread[5];
        for (int i = 0; i < 5; i++){
            threads[i] = new Thread(() -> counter.incrementAndGet());
            threads[i].start();
        }

        for (Thread thread : threads){
            try{
                thread.join();
            }catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            }
        }
        System.out.println("Final count: " + counter.get());
    }
}