#ifndef SIMPLETEXTQUERY_H_INCLUDED
#define SIMPLETEXTQUERY_H_INCLUDED

#include<memory>
#include <string>
#include<vector>
#include<map>
#include<set>
#include<algorithm>
#include <fstream>
#include <sstream>
#include<iostream>
/*
*@Breif:the head file of Ex12.30
*@Soyn
*/
using namespace std;

class QueryResult;

class TextQuery{
public:
    using line_no = vector<string> :: size_type;
    TextQuery(ifstream&);
    QueryResult query(const string&) const;
private:
    shared_ptr<vector<string> > file; //input file
    //creat the map from word to line number
    map<string, shared_ptr< set< line_no>>> wm;
};

class QueryResult{
friend ostream& print(ostream&, const QueryResult);
public:
using line_no = vector<string> :: size_type;
    QueryResult(string s, shared_ptr< set< line_no>> p, shared_ptr< vector<string>> f) : sought(s), lines(p), file(f){}

public:
    string sought ;// the word we want to query
    shared_ptr<set< line_no>> lines; //the line number the word occurs
    shared_ptr< vector< string> > file; //input file
};

#endif // SIMPLETEXTQUERY_H_INCLUDED
