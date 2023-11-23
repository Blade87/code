/* https://www.linkedin.com/feed/update/urn:li:activity:7132774313652330497/ */

/* C++ */
#include <iostream>
#include <stdint.h>
#include <string>

using namespace std;

int main()
{
    cout<< "The all numbers <1000"<< endl;
    string const a="568 1200 1000 23 987 1111 5287";
    int32_t top_boundary = 1000;
    
    string str_of_numbers = a;
    string str_delimiter = " ";
    int8_t b_comma = 0;
    
    size_t position= str_of_numbers.find(str_delimiter);
    cout<< "[";
    while ( string::npos != position)
    {
        string str_number = str_of_numbers.substr(0, position);
        int32_t number = stoi(str_number, nullptr);
        str_of_numbers = str_of_numbers.substr(position+1);
        position= str_of_numbers.find(str_delimiter);
        if (number < top_boundary)
        {
            if (0 == b_comma)
            {
                cout<< number;
                b_comma = 1;
            }
            else
            {
                cout<< ","<< number;
            }
        }
    }
    cout<< "]"<< endl;

    return 0;
}