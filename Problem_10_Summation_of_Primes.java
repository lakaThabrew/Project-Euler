// This Java program calculates the sum of all prime numbers below two million
// using the Sieve of Eratosthenes algorithm for efficiency.

public class Problem_10_Summation_of_Primes {
    public static void main(String[] args) {
        final int LIMIT = 2_000_000;
        boolean[] isPrime = new boolean[LIMIT];
        long sum = 0;

        for (int i = 2; i < LIMIT; i++) {
            isPrime[i] = true;
        }
        for (int i = 2; i * i < LIMIT; i++) {
            if (isPrime[i]) {
                for (int j = i * i; j < LIMIT; j += i) {
                    isPrime[j] = false;
                }
            }
        }
        for (int i = 2; i < LIMIT; i++) {
            if (isPrime[i]) {
                sum += i;
            }
        }
        System.out.println("Sum of all primes below two million: " + sum);
    }
}
