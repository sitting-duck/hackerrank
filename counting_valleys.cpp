// not working at this point in time, code runs but answer is not good
//

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
    int currentStep, valleys = 0;
    char currentStepChar[2] = {0, 0};

    std::cout << "steps: " << steps << std::endl;
    std::cout << "currentStep: " << currentStep << std::endl;
    for(int i = 0; i < steps; i++) {
        std::cout << "currentStep: " << currentStep << std::endl;
        if(i < steps && currentStep == 0) {
            std::cout << "got the zero" << " i: " << i << std::endl;
            std::cout << "next step is: " << path[++i] << std::endl;
            std::cout << "less than steps: " << (i < steps) << std::endl;
            bool equals = path.compare(++i, 1, std::string("D"));
            //std::cout << "next step equals D: " << (path.compare(++i, 1, std::string("D"))) << std::endl;
            //std::cout << "equals: " << std::string::compare(path[++i], "D") <<
            currentStepChar[0] = path[++i];
            std::cout << "currentStepChar: " << currentStepChar << std::endl;
            std::cout << "equals: " << strcasecmp(currentStepChar, "D") << std::endl;
        }

        if(i < steps && currentStep == 0 && path[++i] == 'D') {
            std::cout << "increment valleys" << std::endl;
            valleys++;
        }

        std::cout << "path[i]: " << path[i] << std::endl;
        if(path[i] == 'D') {
            currentStep--;
        } else if(path[i] == 'U') {
            currentStep++;
        }
    }
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

