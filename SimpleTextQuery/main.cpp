#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <fstream>
#include <sstream>
#include<memory>
#include<cctype>
#include<clocale>

using namespace std;
/*
* Ex12.28
* Date:2015.7.14
*/

int main()
{
    ifstream inFile("test.txt");
    using LineNo = vector< string> :: size_type;
    LineNo lineNo(0);
    map<string, set< LineNo>> result;
    shared_ptr< vector< string> > input;

    for(string line; getline(inFile, line);++lineNo){
        input -> push_back(line);
        istringstream line_stream(line);
        for( string text, word; line_stream >> text; word.clear()){
            remove_copy_if(text.begin(), text.end(), back_inserter(word), ispunct);
            result[word].insert(lineNo);
        }
    }

    string word;
    cout << " Plz enter the word you want to query: " << endl;
    cin >> word;
    auto found = result.find(word);
    if( found != result.end()){
        cout <<  word << "  occurs " << found -> second.size() << (found -> second.size() > 1 ? "times" : "time") << endl;
        for( auto i : found -> second){
            cout << "\t( line " << i + 1 <<  ")" << input -> at(i) << endl;
        }
    } else cout << word << "occurs 0 times" << endl;
    return 0;
}
