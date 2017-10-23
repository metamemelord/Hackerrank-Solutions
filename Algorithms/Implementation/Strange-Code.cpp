/*
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 00:16:22 2017

@author: MetaMemeLord-
"""
*/

#include<iostream>

int main()
{
    long long n,val=3;
    std::cin>>n;
    while (n > val)
    {
        n -= val;
        val *= 2;
    }
    std::cout<<val-n+1<<std::endl;
    return 0;
}
