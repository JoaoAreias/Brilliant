/*
	Calculates the maximum area in a histogram
*/

#include <bits/stdc++.h>

using namespace std;

vector<int> parse(const string &str);
int maxArea(const vector<int> &hist);

int main(){
	vector<int> input;
	string input_str;
	while(getline(cin, input_str)){
		input = parse(input_str);
		printf("%d\n", maxArea(input));
	}

	return 0;
}

vector<int> parse(const string &str){
	vector<int> tokens;

	string::size_type start = 0;
	string::size_type end = 0;

	while((end = str.find(" ", start)) != string::npos){
		tokens.push_back(stoi(str.substr(start, end-start), nullptr));
		start = end + 1;
	}
	tokens.push_back(stoi(str.substr(start), nullptr));

	return tokens;
}

int maxArea(const vector<int> &hist){
	stack<int> s;
	int max_area=0, tp, area_with_top, size;
	size = hist.size();
	
	int i=0;
	while(i < size){
		if(s.empty() || hist[i] >= hist[s.top()])
			s.push(i++);
		else{
			tp = s.top();
			s.pop();

			area_with_top = hist[tp]*(s.empty() ? i: i - s.top() - 1);
			if(max_area < area_with_top)
				max_area = area_with_top;
		}
	}

	while(!s.empty()){
		tp = s.top();
		s.pop();

		area_with_top = hist[tp]*(s.empty() ? i : i-s.top()-1);
		if(max_area < area_with_top)
			max_area = area_with_top;
	}
	return max_area;
}