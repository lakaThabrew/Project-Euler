#include <iostream>
#include <cmath>
using namespace std;

// Function to count number of divisors
int countDivisors(long long n) {
    int count = 0;
    long long sqrtN = sqrt(n);

    for (long long i = 1; i <= sqrtN; ++i) {
        if (n % i == 0) {
            count += 2; // i and n/i
        }
    }

    if (sqrtN * sqrtN == n) {
        count--; // perfect square correction
    }

    return count;
}

int main() {
    long long triangle = 0;
    int n = 1;

    while (true) {
        triangle += n; // nth triangle number
        int divisors = countDivisors(triangle);

        if (divisors > 500) {
            cout << "First triangle number with over 500 divisors: " << triangle << endl;
            break;
        }

        n++;
    }

    return 0;
}
