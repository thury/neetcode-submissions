class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<int> operands;

        for (const string& tok : tokens) {
            if (tok == "+" || tok == "-" || tok == "*" || tok == "/") {
                int right = operands.top();
                operands.pop();

                int left = operands.top();
                operands.pop();

                int result;

                if (tok == "+") {
                    result = left + right;
                } else if (tok == "-") {
                    result = left - right;
                } else if (tok == "*") {
                    result = left * right;
                } else {
                    result = left / right; // C++ truncates toward zero
                }

                operands.push(result);
            } else {
                operands.push(stoi(tok));
            }
        }

        return operands.top();
    }
};