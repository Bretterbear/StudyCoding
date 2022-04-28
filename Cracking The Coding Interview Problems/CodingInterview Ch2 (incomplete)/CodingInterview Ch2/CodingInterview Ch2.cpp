// CodingInterview Ch2.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <list>
#include <unordered_set>
using namespace std;

//2.1
void deleteDubs(list <int>&);

int main()
{
    //2.1
	list<int> lList = { 1,2,3,1,2,4,5 };
	for (list<int>::iterator it = lList.begin(); it != lList.end(); ++it)
	{
		cout << *it << " - ";
	}

	cout << "\n";

	deleteDubs(lList);

	for (list<int>::iterator it = lList.begin(); it != lList.end(); ++it)
	{
		cout << *it << " - ";
	}

	return 0;
}

//2.1
void deleteDubs(list <int>& lList)
{
	unordered_set<int> set;
	list<int>::iterator it = lList.begin();

	while (it != lList.end())
	{
		if (set.find(*it) == set.end()) {
			set.insert(*it);
			++it;
		}
		else
			it = lList.erase(it);			
	}
	return;
}