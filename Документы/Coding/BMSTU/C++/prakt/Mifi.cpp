#include <iostream>
#include "math.h"
#include "stdlib.h"

using namespace std;

double fact(double x){
	
if (x>1) {
	return x*=fact(x-1);}
else {return 1;}
}

double g(int k){
	
	double r = fact(k+1)/fact(pow(2*k,2));
	//cout<<"g="<<r<<endl;
	return r;
	
	}
	
double f(double x,int k){
	double r = pow(0.5*x,2*(k+1));
	//cout<<"f="<<r<<endl;
	return r;
	
	}
	
double h(double x,int k){

	double r = tan(x*k);
	//cout<<"h="<<r<<endl;
	return r;
	}
	
double z(double x, int k){
	
//	cout<<"k="<<k<<endl;
	return pow(-1,k)*g(k)*f(x,k)*h(x,k);
	}
	
void S(double x, double eps){
	int k=1;
	double s=0;
	double l = z(x,k);
	//cout<<"|Z="<<l<<endl;
	while (l>eps||l<(-1*eps)){
	
		s+=l;
		k++;
		l =z(x,k);
//		cout<<"|Z="<<l<<endl;
		}
		
		cout<<"Значение S = "<<s<<"\nЗначение N = "<<k-1;
	
	}

int main(int argc, char *argv[]){
    double eps=0,x=0;
    if(argc==3){
      x = atof(argv[1]);
      eps = atof(argv[2]);
    }else{
      cout<<"Введите X и eps\n";
      cin>>x>>eps;
    }
    S(x,eps);
	return 0;
}


