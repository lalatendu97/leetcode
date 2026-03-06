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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        int s = 0;
        ListNode* res = new ListNode();
        ListNode* dummy = res;

        while (l1 != nullptr || l2 != nullptr or s != 0){
            
            if (l1 != nullptr){
                s += l1 -> val;
                l1 = l1 -> next;
            }

            if (l2 != nullptr){
                s += l2 -> val;
                l2 = l2 -> next;
            }

            res -> next = new ListNode(s % 10);
            s /= 10;
            res = res -> next;
        }
        return dummy -> next;
    }
};