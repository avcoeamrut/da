#include <iostream>
using namespace std;

int fibonacci(int fib)
{
	if(fib==0)
		return 0;
	if(fib==1||fib==2){
		return 1;
	}
	else{
		return(fibonacci(fib-1)+fibonacci(fib-2));
	}
}

int main()
{
	cout<<"\nEnter number:";
	int n;
	cin>>n;
	for(int i=1;i<=n;i++){
		cout<<fibonacci(i)<<" ";
	}
	return 0;
}