```cpp
//
//  int_rate.hpp
//  Simple_int
//
//  Created by Paul Laliberte on 2/4/16.
//  Copyright © 2016 Paul Laliberte. All rights reserved.
//

#ifndef int_rate_hpp
#define int_rate_hpp

#include <iostream>

class ir {
public:
    ir(double rate);
    ir(const ir &v);
    ir &operator = (const ir &v);
    ~ir();
    
    double singlePeriod(double period);
    
private:
    double m_rate;
};

inline double ir::singlePeriod(double value)
{
    double f = value * (1 + this->m_rate);
    return f;
}

#endif /* int_rate_hpp */
```
