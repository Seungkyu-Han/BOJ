long long sum(int *a, int n) {
	int i;
    long long ans = 0;
    for(i = 0; i< n ; i++){
        ans = ans + a[i];
    }
	return ans;
}
