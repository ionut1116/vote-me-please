#include <array>
#include <iostream>
#include <fstream>

void LoadFile(std::array <std::string, 5> & aAllCategories) {
    std::ifstream inFile("/home/anthony/Development/CSCE361/Fall2019/Lab5/inFile.dat");
    int i = 0;
    std::string sLine;
    while (std::getline(inFile, sLine)) {
        //std::cout << sLine << std::endl;
        if (sLine == "") {
            //std::cout << "Pushing back: " << i << std::endl;
            aAllCategories.at(i) = sLine;
            i++;
        }
        else
        {
            if (i == 0) { // if first category
                aAllCategories.at(0) = sLine;
            } else {
                aAllCategories.at(i) = aAllCategories.at(i) + sLine + ",";
            }
        }
        if (i > 4) {
            std::cout << "Error trying to read > 5 categories from file." << std::endl;
            return;
        }
    }
}

int main() {
    
    }
    LoadFile(aAllCategories);
    return 0;
}