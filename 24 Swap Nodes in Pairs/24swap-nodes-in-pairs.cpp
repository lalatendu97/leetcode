/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* swapPairs(ListNode* head) {
        if (head == nullptr){return nullptr;}
        vector<int> res;

        while (head != nullptr){
            res.push_back(head -> val);
            head = head -> next;
        }

        for (int i = 0; i + 1 < res.size(); i+=2){
            swap(res[i], res[i + 1]);
        }

        ListNode* x = new ListNode();
        ListNode* y = x;
        for (int i = 0; i < res.size(); i++){
            y -> next = new ListNode(res[i]);
            y = y -> next;
        }

        return x -> next;
    }
};