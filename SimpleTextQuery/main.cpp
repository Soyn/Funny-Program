#include<iostream>
#include "SimpleTextQuery.h"

using namespace std;


TextQuery :: TextQuery(ifstream& is) : file(new vector< string>)
{
    for(string text,word; getline(is, text);word.clear()){
        file ->push_back(text);
        int n = file ->size() - 1;
        istringstream line(text);
        while(line >> word){      //read each word in every line
            auto &lines =   wm[word]; //lines refer to shared_ptr<set<line_no>>
            if(!lines)   //if lines is null allocate a new set
                lines.reset(new set<line_no>);
            lines -> insert(n); //insert the line number
        }
    }
}
QueryResult  TextQuery :: query(const string &sought) const{
    //if sought is not found,a point refers to this set will return
    static shared_ptr<set< line_no>> nodata( new set<line_no>);
    auto loc = wm.find(sought);
    if (loc == wm.end())
        return QueryResult(sought, nodata, file); // not found
    else
        return QueryResult(sought, loc -> second, file);
}

string make_plural(size_t ctr, const string &word, const string &ending)
{
    return (ctr > 1) ? word + ending : word;
}
ostream& Print(ostream& os, const QueryResult &qr)
{
    os << qr.sought << " occurs " << qr.lines -> size() << "  " << make_plural(qr.lines -> size(), "time", "s") << endl;
    //print the line the sought occurs
    for( auto num: *qr.lines)
        os << "\t(line  " << num + 1 << ")" << *(qr.file ->begin() + num) << endl;
    return os;
}

void runQueries( ifstream &infile)
{
    TextQuery tq(infile); //save file and create query-map
    do{
        cout << "enter word to look for, or q to quit: ";
        string s;
        if( !(cin >> s) || s == "q") break;
        Print(cout, tq.query(s)) << endl;
    }while(true);
}
int main()
{
    ifstream infile("test.txt");
    runQueries(infile);
    return 0;
}
