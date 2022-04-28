// CodingInterview Ch1.cpp : This file contains the 'main' function. Program execution begins and ends there.
//
#include <string>
#include <algorithm>
#include <iostream>
using namespace std;

//1.8
void arrZeroing(int**, int);

//1.7
void rotateNxN(int**, int);
void printNxN(int**, int);

//1.6
string stringCompression(string);

//1.5
bool isOneEdit(string, string);
bool isOneReplace(string, string);
bool isOneInsert(string, string);

//1.4
bool isPalinPermuteFreq(string);
bool isPalinPermuteFreqV2(string);
void buildCharFreq(string, int*);
int getCharNum(char);
bool checkMaxOneOdd(int*);
bool isPalinPermuteBitVer(string);
int createBitVector(string);
int toggle(int, int);
bool checkExactlyOneBitSet(int);

//1.3
void replaceSpaces(string&, int);
//1.2
bool sortingPermuteMethod(string permString1, string permString2);
bool countPermuteMethod(string permString1, string permString2, int charSetSize = 256);
//1.1
bool isAllUniqueChars(string s, int charSetSize = 256);

//uncomment sections as you need them
int main()
{
	/* 1.8 - Array Zeroing
	//initialize array allocation
	int n=6;
	int** testArr= new int*[n];
	for (int i = 0; i < n; ++i)
		testArr[i] = new int[n];
	
	int counter = 1;
	for (int i = 0; i < n; ++i)
	{
		for (int j = 0; j < n; j++)
		{
			testArr[i][j] = counter;
			counter++;
		}
	}
	testArr[2][3] = 0;
	testArr[0][5] = 0;

	//running func
	printNxN(testArr, n);
	arrZeroing(testArr, n);
	cout << "\n";
	printNxN(testArr, n);


	//delete array allocation
	for (int i = 0; i < n; ++i)
	{
		delete[] testArr[i];
	}
	delete[] testArr;
	*/

	/* 1.7 - Array Rotation
	int n=3;
	int** testArr= new int*[n];
	for (int i = 0; i < n; ++i)
		testArr[i] = new int[n];
	int counter = 1;
	for (int i = 0; i < n; ++i)
	{
		for (int j = 0; j < n; j++)
		{
			testArr[i][j] = counter;
			counter++;
		}
	}

	printNxN(testArr, n);
	rotateNxN(testArr, n);
	cout << "\n";
	printNxN(testArr, n);

	for (int i = 0; i < n; ++i)
	{
		delete testArr[i];
	}
	delete testArr;
	 */

	/* 1.6 - String Compression
	cout << stringCompression("bbadddieeeee");
	*/

	/* 1.5 
	string output = isOneEdit("bargl", "bargle") ? "goodie" : "noba";
	cout << output;
	*/

	/* 1.4
	//string output = isPalinPermuteFreq("diggledogrdogdigglet") ? "goodie" : "noba";
	//string output = isPalinPermuteFreqV2("diggledogdogdigglet") ? "goodie" : "noba";
	string output = isPalinPermuteBitVer("diggledogdogdigglet") ? "goodie" : "noba";
	cout << output;
	*/

	/* 1.3
	string textToAddHyp = "Mr John Denver    ";
	int trueLeng = 14;

	cout << textToAddHyp << "\n";
	replaceSpaces(textToAddHyp, trueLeng);
	cout << textToAddHyp;
	*/

	/* 1.2
	string permString1 = "yggoed";
	string permString2 = "deoggy";
	if (countPermuteMethod(permString1, permString2))
		cout << "GOOBY";
	else
		cout << "NO GOOBY";
	*/
	/* 1.1
	string testString = "blargleblargle";
	if (isAllUniqueChars(testString))
		cout << "IS UNIQUE";
	else
		cout << "DUPLICATE LETTERS";
	*/

	return 0;
}

/*--------------------- 1.8 ------------------------*/
void arrZeroing(int** arrToZero, int n)
{
	bool* row0s = new bool[n];
	bool* col0s = new bool[n];
	for (int i = 0; i < n; i++)
	{
		row0s[i] = false;
		col0s[i] = false;
	}

	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < n; j++)
		{
			if (arrToZero[i][j] == 0)
			{
				row0s[i] = true;
				col0s[j] = true;
			}
		}
	}

	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < n; j++)
		{
			if ((row0s[i] == true) || (col0s[j] == true))
			{
				arrToZero[i][j] = 0;
			}
		}
	}

	delete[] row0s;
	delete[] col0s;
	return;
}

/*--------------------- 1.7 ------------------------*/
void rotateNxN(int** arrToRot, int n)
{
	for (int layer = 0; layer < n / 2; layer++)
	{
		int first = layer;
		int last = n - 1 - layer;
		for (int i = first; i < last; i++)
		{
			int offset = i - first;
			int top = arrToRot[first][i];

			arrToRot[first][i] = arrToRot[last - offset][first];
			arrToRot[last - offset][first] = arrToRot[last][last - offset];
			arrToRot[last][last - offset] = arrToRot[i][last];
			arrToRot[i][last] = top;
		}
	}
}

void printNxN(int** arrPrint, int n)
{
	for (int i = 0; i < n; i++)
	{
		cout << "| ";
		for (int j = 0; j < n; j++)
		{
			cout << arrPrint[i][j] << " ";
		}
		cout << "|\n";
	}
}

/*--------------------- 1.6 ------------------------*/
string stringCompression(string text)
{
	int textIndex = 0;
	string resultString = "";
	while (textIndex < text.length()) {
		char subChar = text[textIndex];
		int subCharCount = 0;
		while (text[textIndex + subCharCount] == subChar)
		{
			subCharCount++;
		}
		resultString = resultString + subChar + to_string(subCharCount);
		textIndex += subCharCount;
	}
	if (text.length() >= resultString.length())
		return resultString;
	else
		return text;
}

/*--------------------- 1.5 ------------------------*/
bool isOneEdit(string text1, string text2)
{
	if (text1.length() == text2.length())
		return isOneReplace(text1, text2);
	else if (text1.length()== text2.length()+1)
		return isOneInsert(text1, text2);
	else if (text1.length()+1 == text2.length())
		return isOneInsert(text2, text1);
	else
		return false;
}

bool isOneReplace(string text1, string text2)
{
	bool diffFound = false;
	//checks for replace
	for (int i = 0; i < text1.length(); i++)
	{
		if (text1[i] != text2[i])
		{
			if (!diffFound)
				diffFound = true;
			else
				return false;
		}
	}
	return true;
}
bool isOneInsert(string text1, string text2) //checks if text1 is text2 w/ one insert
{
	int text1IndexOffset = 0;
	for (int i = 0; i < text2.length(); i++)
	{
		if ((text1[i + text1IndexOffset] != text2[i]))
		{
			if ((text1IndexOffset == 0) && (text1[i + 1] == text2[i]))
				text1IndexOffset = 1;
			else 
				return false;
		}
	}
	return true;
}

/*--------------------- 1.4 ------------------------*/
//Method 1 - Character frequency check
//creates charCount table array which it passes to subfunctions
//garbage - has magic num 'z'-'a' + 1 sprinkled throughout BAD but works
bool isPalinPermuteBitVer(string permString)
{
	int bitTracker = createBitVector(permString);
	return bitTracker == 0 || checkExactlyOneBitSet(bitTracker);
}

int createBitVector(string permString)
{
	int bitTracker = 0;
	for (int i = 0; i < permString.length(); i++)
	{
		int x = getCharNum(permString[i]);
		bitTracker = toggle(bitTracker, x);
	}
	return bitTracker;
}

int toggle(int bitTracker, int x)
{
	if (x < 0) return bitTracker;

	int mask = 1 << x;
	
	if ((bitTracker & mask) == 0)
		bitTracker = bitTracker | mask;
	else
		bitTracker = bitTracker & ~mask;
	
	return bitTracker;
}

bool checkExactlyOneBitSet(int bitTracker)
{
	return (((bitTracker) & (bitTracker - 1)) == 0);
}

bool isPalinPermuteFreqV2(string permString)
{
	int countOdd = 0;
	int* table = NULL;
	table = new int['z' - 'a' + 1];
	for (int i = 0; i < 'z' - 'a' + 1; i++)
	{
		table[i] = 0;
	}
	for (int i = 0; i < permString.length(); i++)
	{
		int x = getCharNum(permString[i]);
		if (x != -1) {
			table[x]++;
			if (table[x] % 2 == 1)
				countOdd++;
			else 
				countOdd--;
		}
	}
	return (countOdd <= 1);
}
bool isPalinPermuteFreq(string permString)
{
	int* table = NULL;
	table = new int['z' - 'a' + 1];
	for (int i = 0; i < 'z' - 'a' + 1; i++)
	{
		table[i] = 0;
	}
	buildCharFreq(permString, table);
	return checkMaxOneOdd(table);
}
//Builds character Frequenceies using the "getCharNum subfunc"
void buildCharFreq(string permString, int* arr)
{
	for (int x = 0; x < permString.length(); x++) {
		int y = getCharNum(permString[x]);
		if (y != -1)
			arr[y]++;
	}
}
//basically hashes 'a' to 'z' lowercase for an int array
int getCharNum(char c)
{
	if ('a' <= c && 'z' >= c)
		return (c - 'a');
	else
		return -1;
}
//checks characterFrequency array
bool checkMaxOneOdd(int* table)
{
	bool foundOdd = false;
	for (int i = 0; i < 'z' - 'a' + 1; i++)
	{
		if (table[i] % 2 == 1)
		{
			if (foundOdd)
				return false;
			else 
				foundOdd = true;
		}
	}
	return true;
}

/*--------------------- 1.3 ------------------------*/
void replaceSpaces(string& textToAddHyp, int trueLeng)
{
	int spaceCount = 0;
	for (int i = 0; i < trueLeng; i++) {
		if (textToAddHyp[i] == ' ') spaceCount++;
	}
	
	int index = trueLeng + spaceCount * 2;
	for (int i = trueLeng - 1; i >= 0; i--) {
		if (textToAddHyp[i] == ' ') {
			//textToAddHyp.replace(index - 3, 3, "%20");
			textToAddHyp[index - 1] = '0';
			textToAddHyp[index - 2] = '2';
			textToAddHyp[index - 3] = '%';
			index -= 3;
		}
		else {
			textToAddHyp[index - 1] = (char) textToAddHyp[i];
			index -= 1;
		}
	}
}


/*--------------------- 1.2 ------------------------*/
//Assumption whitespace matters & is preserved
bool sortingPermuteMethod(string permString1, string permString2)
{
	if (permString1.length() != permString2.length())
		return false;

	sort(permString1.begin(), permString1.end());
	sort(permString2.begin(), permString2.end());
	
	if (permString2 == permString1)
		return true;
	else
		return false;
}

bool countPermuteMethod(string permString1, string permString2, int charSetSize)
{
	//confirm length equivalence (obvi no permutation if != lengths)
	if (permString1.length() != permString2.length())
		return false;

	//make a letterCount array
	int* letterCount = NULL;
	letterCount = new int[charSetSize];
	for (int i = 0; i < charSetSize; i++) { letterCount[i] = 0; }

	//get letterCount for first string
	for (int i = 0; i < permString1.length(); i++) { letterCount[permString1[i]]++;}

	//subtract lettercounts, if below 0, obvi extra char in a set
	for (int i = 0; i < permString2.length(); i++) { 
		letterCount[permString2[i]]--; 
		if (letterCount[permString2[i]] < 0) {
			delete[] letterCount;
			return true;
		}
	}

	return true;

}

/*--------------------- 1.1 ------------------------*/
//naive assumption of valid charSetSize for s;
//basically uses a lazy ersatz hashmap
bool isAllUniqueChars(string s, int charSetSize){
	//sanity check via pigeonhole principle
	if (s.length() > charSetSize)
		return false;

	//boolean array for testing; dynamically sized for diff charsets
	bool* char_set = NULL;
	char_set = new bool[charSetSize];

	for (int i = 0; i < charSetSize; i++) { char_set[i] = false; }

	for (int i = 0; i < s.length(); i++)
	{
		if (char_set[s[i]]) {
			delete[] char_set;
			return false;
		}
		else
			char_set[s[i]]=true;
	}
	delete[] char_set;
	return true;
}
// Run program: Ctrl + F5 or Debug > Start Without Debugging menu
// Debug program: F5 or Debug > Start Debugging menu