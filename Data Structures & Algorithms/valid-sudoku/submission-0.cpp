class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        int rows[9] = {}, cols[9] ={}, boxes[9] = {};
        for(int r = 0; r < 9; r++){
            for(int c = 0; c < 9; c++){
                if(board[r][c] == '.') continue;
                int d = board[r][c] - '0';
                int b = (r/3)*3 + (c/3);
                int bit = 1 << d;
                if(rows[r] & bit) return false;
                if(cols[c] & bit) return false;
                if(boxes[b] & bit) return false;
                rows[r] |= bit;
                cols[c] |= bit;
                boxes[b] |= bit;
            
            }
        }
       return true;
    }
};
