#include <iostream>

using namespace std;


class Mass
{
public:
	int n;
	int *a;
	int in_out();
};

class One : public Mass
{
public:
	Mass T;
	int head, n;
	int *a;
	int func();
		
};

class Two : public One 
{
public:
	One ichi;
	int summ;
	int func();
		
};

class Three : public Two 
{
public:
	Mass T;
	One ichi;
	Two ni;
	int in_out();
		
};


int Mass::in_out()
{
	cin >> n;
	a = new int [n];
	for (int i = 0; i<n; i++) {
//		if (i<n-1) {
			cin >> a[i];
//			cout << a[i] << " ";
//		}
//		else {
//			cin >> a[i];
//			cout << a[i] << endl;
//		}
	}
	return a[n];
}

int One::func() 
{
	T.in_out();
	n = T.n;
	a = T.a;
	head = a[0];
	for (int i=1; i<n; i++) {
		head -= a[i];
	}
//	cout << "Min: " << head << endl;
	return head;
}

int Two::func() 
{
	ichi.func();
	summ = ichi.a[0];
	for (int i=1; i<ichi.n; i++ ) {
		summ += ichi.a[i];
	}
//	cout << "Sum: " << summ;
	return summ;
}

int Three::in_out() 
{

	
	cout << "Array dimensions: " << ni.func() << endl;
	cout << "Array dimensions: " << ichi.func() << endl;


}





	
int main() {
	setlocale(LC_ALL, "rus");
	Three Da;
	Da.in_out();
	return 0;
	
	
}
	
	


