#include <iostream>
#include <vector>

using namespace std;

int main(){

    int N, result = 0;

    cin >> N;

    if (N == 1){
        cout << 0;
        return 0;
    }

    vector<bool> is_prime(N + 1, true);
    vector<int> primes;

    for(int n = 2; n < N + 1; n++)
        if(is_prime[n])
            for(int i = 2 * n; i < N + 1; i += n)
                is_prime[i] = false;

    for(int k = 2; k < N + 1; k++)
        if(is_prime[k])
            primes.push_back(k);

    int start = 0, end = 0;
    int cur = primes[start];

    while(end < primes.size()){
        if(cur == N){
            result ++;
            cur -= primes[start++];
        }
        else if (cur < N){
            cur += primes[++end];
        }
        else{
            cur -= primes[start++];
        }
    }

    cout << result << endl;
    return 0;
}