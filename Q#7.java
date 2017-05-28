//Question no. 7
//Ankit Mittal
//Solving a problem on Java for the first time!!


public class findingtheprime {

    public static void main(String[] args) {

        System.out.println(nthprime(10001));    /*finding the 10001th prime number*/

    }

    /* ths will return the 10001thprime number  */
    public static long nthprime(long n) {

        int numberOfPrimes = 0;
        long prime = 1;

        while (numberOfPrimes < n) {
            prime++;
            if (isprime(prime)) {
                numberOfPrimes++;
            }
        }
        return prime;
    }

    /* returns true only if n happens to be a  prime number */

    public static boolean isprime(long n) {

        if (n < 2)
          return false;

        else if (n == 2)
          return true;

        for (int i = 2; i < Math.pow(n, 0.5) + 1; i++)

            if (n % i == 0)

                return false;

        return true;
    }
}
