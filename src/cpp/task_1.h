/*
 * Author: Zokirjonov Xondamir
 * Date: 25.10.2023
 * Name:
 */
#include <iostream>
using namespace std;

class Problem1 {
private:
    unsigned int year;
public:

    void check(){
        cout << "Enter year: ";
        cin >> year;
        if (year%4==0){
            cout << "Leap year: " << endl;
        }
        else{
            cout << "It's not leap year: " << endl;
        }
    }

};
