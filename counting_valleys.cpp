#include <bits/stdc++.h>
#include <cstring>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);

/*
 * Complete the 'countingValleys' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts following parameters:
 *  1. INTEGER steps
 *  2. STRING path
 */

int countingValleys(int steps, string path) {
    int currentStep = 0;
    int valleys = 0;
    char currentStepChar[2] = {0, 0};
    char nextStepChar[2] = {0, 0};
    bool equalsD = -1;
    
    for(int i = 0; i < steps; i++) {
        std::cout << path[i];
        currentStepChar[0] = path[i];
        equalsD =  strcasecmp(currentStepChar, "D");
        
        if(equalsD == 0) {
            currentStep--;
        } else {
            currentStep++;
        }
        
        if(i==0 && currentStep == -1) {
            valleys++;
        }
        
        //std::cout << "char: " << currentStepChar << " i: " << path[i] << " equalsD: " << equalsD << "currStep: " << currentStep << std::endl;
        
        
        if(i < steps && currentStep == 0) {
            bool equals = path.compare(i+1, 1, std::string("D"));
            currentStepChar[0] = path[i+1];        
        }
        
        nextStepChar[0] = path[i+1];
        equalsD =  strcasecmp(nextStepChar, "D");
        if(i < steps && currentStep == 0 && equalsD == 0) {
            std::cout << "increment valleys" << std::endl;
            valleys++;
        }
    }
    std::cout << std::endl;
    
    // for(int i = 0; i < steps; i++) {
    //     currentStepChar[0] = path[i];
    //     //std::cout << "char: " << currentStepChar << " i: " << path[i] << std::endl;
    //     equalsD =  strcasecmp(currentStepChar, "D");
    //     if(equalsD == 0) {
    //         currentStep--;
    //     } else {
    //         currentStep++;
    //     }
        
    //     //std::cout << "currentStep: " << currentStep << "char: " << currentStepChar << std::endl;
        
    //     if(i < steps && currentStep == 0) {
    //         bool equals = path.compare(++i, 1, std::string("D"));
    //         currentStepChar[0] = path[++i];        
    //     }
        
    //     nextStepChar[0] = path[++i];
    //     equalsD =  strcasecmp(nextStepChar, "D");
    //     if(i < steps && currentStep == 0 && equalsD == 0) {
    //         std::cout << "increment valleys" << std::endl;
    //         valleys++;
    //     }
    // }
    return valleys;
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string steps_temp;
    getline(cin, steps_temp);

    int steps = stoi(ltrim(rtrim(steps_temp)));

    string path;
    getline(cin, path);

    int result = countingValleys(steps, path);

    fout << result << "\n";

    fout.close();

    return 0;
}

string ltrim(const string &str) {
    string s(str);

    s.erase(
        s.begin(),
        find_if(s.begin(), s.end(), not1(ptr_fun<int, int>(isspace)))
    );

    return s;
}

string rtrim(const string &str) {
    string s(str);

    s.erase(
        find_if(s.rbegin(), s.rend(), not1(ptr_fun<int, int>(isspace))).base(),
        s.end()
    );

    return s;
}
 
