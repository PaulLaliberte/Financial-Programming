```tcc
//
//  int_rate.cpp
//  Simple_int
//
//  Created by Paul Laliberte on 2/4/16.
//  Copyright © 2016 Paul Laliberte. All rights reserved.
//

#include "int_rate.hpp"

ir::ir(double rate) : m_rate(rate) {}

ir::~ir() {}

ir::ir(const ir &v) : m_rate(v.m_rate) {}

ir &ir::operator=(const ir &v)
{
    if (&v != this)
    {
        this->m_rate = v.m_rate;
    }
    return *this;
}
```
