/*
3120. Count the Number of Special Characters I

You are given a string word. A letter is called special if it appears both in lowercase and uppercase in word.
Return the number of special letters in word.

Input: word = "aaAbcBC"
Output: 3

Explanation:
The special characters in word are 'a', 'b', and 'c'.
*/

#include <stdbool.h>

int numberOfSpecialChars(char* word) {

    bool lower[26] = {false};
    bool upper[26] = {false};

    for (int i = 0; word[i] != '\0'; i++) {
        char c = word[i];
        if (c >= 'a' && c <= 'z') {
            lower[c - 'a'] = true;
        } else if (c >= 'A' && c <= 'Z') {
            upper[c - 'A'] = true;
        }
    }
    int specials = 0;
    for (int i = 0; i<26;i++){
        if(lower[i] && upper[i])
            specials++;
    }
    return specials;
}