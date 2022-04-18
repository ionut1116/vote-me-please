#include <fstream>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main()
{
    ifstream inFile;
    inFile.open("inFile.dat");

    string category;
    getline(inFile, category);

    vector<string> people;
    string person;
    while (getline(inFile, person))
    {
        people.push_back(person);
    }

    inFile.close();

    while (true)
    {
        cout << "Vote for your favorite " << category << "!" << endl;
        for (int i = 0; i < people.size(); i++)
        {
            cout << i+1 << ". " << people[i] << endl;
        }

        cout << people.size()+1 << ". Exit" << endl;

        int vote;
        cin >> vote;

        if (vote == people.size()+1)
        {
            break;
        }
        else if (vote > 0 && vote <= people.size())
        {
            cout << "You voted for " << people[vote-1] << "!" << endl;
        }
        else
        {
            cout << "Invalid vote." << endl;
        }
    }

    return 0;
}