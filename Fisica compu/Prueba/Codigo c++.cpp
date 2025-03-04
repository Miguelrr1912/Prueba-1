#include <iostream>
using namespace std;

int main() {
    double num1, num2, num3;
    
    cout << "Ingrese el primer número: ";
    cin >> num1;
    cout << "Ingrese el segundo número: ";
    cin >> num2;
    cout << "Ingrese el tercer número: ";
    cin >> num3;
    
    double suma = num1 + num2 + num3;
    double resta = num1 - num2 - num3;
    double multiplicacion = num1 * num2 * num3;
    
    cout << "La suma de los números es: " << suma << endl;
    cout << "La resta de los números es: " << resta << endl;
    cout << "La multiplicación de los números es: " << multiplicacion << endl;
    
    return 0;
}