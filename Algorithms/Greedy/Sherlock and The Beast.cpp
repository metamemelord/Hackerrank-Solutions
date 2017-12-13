/*
# -*- coding: utf-8 -*-
"""
@author: MetaMemeLord-
"""
*/

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int n;
    cin>>n;
    while(n--)
    {
        int t;
        cin>>t;
        if(t<8)
        {
            bool check = true;
            if(t%5 == 0)
            {
                check = false;
                for(int i=0;i<t/5;i++)
                    cout<<33333;
            }
            if(t%3 == 0)
            {
                check = false;
                for(int i=0;i<t/3;i++)
                    cout<<555;
            }
            if(check) cout<<-1<<endl;
            else cout<<endl;
        }
        else
        {
            int i,count = 0;
            int p = t;
            while(t>0)
            {
                if(t%3 == 0)
                    break;
                t -= 5;
            }
            p -= t;
            for(i = 0;i<t;i++) cout<<5;
            for(i=0;i<p;i++) cout<<3;
            cout<<endl;
        }

    }
    return 0;
}
