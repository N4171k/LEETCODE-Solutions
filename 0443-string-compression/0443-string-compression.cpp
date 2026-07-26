class Solution {
public:
    int compress(vector<char>& chars) {
        int l = 0, r = 0, n = chars.size(), count = 1;
        string temp = "";

        while(r < chars.size()-1){
            if(chars[r] == chars[r+1])
            count++, r++;
            else{
                temp += chars[r];
                if (count > 1) temp += to_string(count);

                int i = 0;
                while(i < temp.size()){
                    chars[l++] = temp[i++];
                }
                temp = "", r++, count = 1;
            }
        }

        if(count > 1){
            temp += chars[r];
            temp += to_string(count);
            int i = 0;
            while(i < temp.size()){
                chars[l++] = temp[i++];
            }
        }else chars[l++] = chars[r];

        while(r-- >= l)
        chars.pop_back();

        return chars.size();
    }
};