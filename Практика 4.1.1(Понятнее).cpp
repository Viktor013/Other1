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
	Two ni;
	int in_out();
		
};


int Mass::in_out()
{
	cout << "Введите размер массива: ";
	cin >> n;
	a = new int [n];
	for (int i = 0; i<n; i++) {
		cout << "\n[" << i << "]: ";
		cin >> a[i];
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
	cout << "После вычитания head = " << head << endl;
}

int Two::func() 
{
	ichi.func();
	summ = ichi.a[0];
	for (int i=1; i<ichi.n; i++ ) {
		summ += ichi.a[i];
	}
	cout << "Сумма = " << summ;
	return summ;
}

int Three::in_out() 
{
	ni.func();
}





	
int main() {
	setlocale(LC_ALL, "rus");
	Three Da;
	Da.in_out();
	return 0;
	
	
}
	
	

