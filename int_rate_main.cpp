```cpp
//
//  main.cpp
//  Simple_int
//
//  Created by Paul Laliberte on 2/4/16.
//  Copyright © 2016 Paul Laliberte. All rights reserved.
//

#include <iostream>
#include "int_rate.hpp"


int main(int argc, const char * argv[]) {
    
    double rate;
    double value;
    
    std::cout << "Enter interest rate: ";
    std::cin >> rate;
    
    std::cout << "Enter value amount: ";
    std::cin >> value;
    
    ir irCalculator(rate);
    double res = irCalculator.singlePeriod(value);
    
    std::cout << "Result: " << res << std::endl;
    
    return 0;
}
```
