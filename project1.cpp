

#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

int main()

{

ifstream infile;

infile.open("filename.txt");

string line;

vector<string> names;

while (infile >> line)

{

names.push_back(line);

}

infile.close();

cout << "Please enter a criteria: " << endl;

string criterion;

cin >> criterion;

cout << "Please enter a name: " << endl;

string name;

cin >> name;

int index = 0;

for (int i = 0; i < names.size(); i++)

{

if (names[i] == name)

{

index = i;

break;

}

}

ofstream outfile;

outfile.open("filename.txt",ios::app);

outfile << criterion << "," << index << endl;

out
