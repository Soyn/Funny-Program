#ifndef SIMPLETEXTQUERY_H_INCLUDED
#define SIMPLETEXTQUERY_H_INCLUDED

#include<string>
#include<iostream>
#include<vector>
#include<set>
#include<map>
#include<fstream>
#include<memory>

using namespace std;
/*
*Simple TextQuery
*@Soyn
*Date:2015.7.14
*/

class QueryResult;
class TextQuery{
/*This class is to query text*/
public:
    using LineNo = vector<string> :: size_type;
    TextQuery(ifstream&);
    QueryResult query( const string& ) const;
private:
    shared_ptr< vector<string> > input;                       //input is a smart point which refers to a vector, and the element in vector refers to the line of the text
    map<string, shared_ptr< set<LineNo >>> result; //we can check the word in the map to see the line number
};

class QueryResult{
    /*this class is to show the result*/
public:
    friend ostream& print( ostream&, const QueryResult&);
    QueryResult(const string& s, shared_ptr<set<TextQuery::LineNo>> Set, shared_ptr< vector<string>> v) : word(s),input(v){}
private:
    string word;
    shared_ptr< set<TextQuery::LineNo>> nos;
    shared_ptr< vector<string>> input;
};

ostream& print(ostream& , const QueryResult);


#endif // SIMPLETEXTQUERY_H_INCLUDED
