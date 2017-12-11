/*
# -*- coding: utf-8 -*-
"""
@author: MetaMemeLord-
"""
*/

#include<bits/stdc++.h>

using namespace std;

int x[100010] = {0};

bool calc(int n)
{
	int k = sqrt(n);
	while(k>1)
	{
		if(n%k == 0)
			return true;
		k--;
	}
	return false;
}

void primCount()
{
    int count = 0;
    for(int i=2;i<=100000;i++)
    {
        if(!calc(i))
            count++;
        x[i] = count;
    }
}

int main()
{
	//int start_s = clock();
	ios_base::sync_with_stdio(false);
    primCount();
	int n,t;
	cin>>t;
	while(t--)
	{
		cin>>n;
		if(x[n]%2) cout<<"Alice"<<endl;
		else cout<<"Bob"<<endl;
	}
	//int stop_s = clock();
	//cout << "time: " << (stop_s-start_s)/double(CLOCKS_PER_SEC)*1000 << endl;
	return 0;
}
