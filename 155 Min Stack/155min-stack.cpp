class MinStack {
public:
    stack<int> r;
    stack<int> m;
    MinStack() {
        
    }
    
    void push(int val) {
        if (m.empty() || val <= m.top()) {m.push(val);}
        r.push(val);
    }
    
    void pop() {
        if (r.top() == m.top()){m.pop();}
        r.pop();
    }
    
    int top() {
        return r.top();
    }
    
    int getMin() {
        return m.top();
    }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(val);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */