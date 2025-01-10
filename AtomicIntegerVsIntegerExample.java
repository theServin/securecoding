import java.util.concurrent.atomic.AtomicInteger;

public class AtomicIntegerVsIntegerExample{
	private static final int NUM_THREADS = 5;
	private static final int NUM_ITERATIONS = 1000;	
	public static void main(String[] args) throws InterruptedException{
		// Shared variables
		AtomicInteger atomicCounter = new AtomicInteger(0);
		Integer regularCounter = 0;
		// Using a thread-safe AtomicInteger
		Thread[] atomicThreads = new Thread[NUM_THREADS];
		for (int i = 0; i < NUM_THREADS; i++){
			atomicThreads[i] = new Thread(() -> {
				for (int j = 0; j < NUM_ITERATIONS; j++){
					atomicCounter.incrementAndGet();
				}
			});
		}
		// Using a non-thread-safe Integer
		Thread[] regularThreads = new Thread[NUM_THREADS];
		Object lock = new Object();
		for (int i = 0; i < NUM_THREADS; i++){
			regularThreads[i] = new Thread(() -> {
				for (int j = 0; j < NUM_ITERATIONS; j++){
					synchronized (lock){
						regularCounter++;
					}
				}
			});
		}
		// Start all threads
		for (Thread thread : atomicThreads){
			thread.start();
		}
		for (Thread thread : regularThreads){
			thread.start();
		}
		// Wait for all threads to finish
		for (Thread thread : atomicThreads){
			thread.join();
		}
		for (Thread thread : regularThreads){
			thread.join();
		}
		// Results
		System.out.println("Final value of AtomicInteger: " + atomicCounter.get());
		System.out.println("Final value of Integer (with synchronization): " + regularCounter);
	}
}