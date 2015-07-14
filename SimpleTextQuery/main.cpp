#include<sstream>
#include<algorithm>
#include "Ex12.27.h"

/*
* the Simple text query
* Date:2015.7.14
*/
using namespace std;

TextQuery :: TextQuery(ifstream &ifs) : input(new vector<string>){
    LineNo lineNo(0);
    for( string line, getline(ifs, line); ++lineNo){
        input -> push_back(line);
        istringstream line_stream(line);
        for( string text, word; line_stream >> text; word.clear()){
            //remove the punctation of the word(such as:  word,   )
            remove_copy_if(text.begin(), text.end(), back_inserter(word), ispunct());

            //read the word and the line number
            auto &nos = result[word];

            if(!nos) nos.reset(new set<lineNo>);  // if the word doesn't exsit
            nos -> insert(LineNo);
        }
    }
}

QueryResult TextQuery :: query(const string& str) const {
    static shared_ptr<set<LineNo> > nodate(new set<LineNo>);
    auto found = result.find(str);
    if( found == result.end() ) return QueryResult( str, nodate, input);
    else return QueryResult( str, found -> second, input);
}

ostream print(ostream &out, const QueryResult &qr){
    out << qr.word << "  occurs  " << qr.nos -> size() << (qr.size() > 1 ? " times" : " time") << endl;
    for( auto i : *qr.nos)
        out << "\t(line )" << i + 1 << ")   " << qr.input ->at(i) << endl;
    return out;
}
