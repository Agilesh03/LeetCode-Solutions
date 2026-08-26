class Solution {
    public int romanToInt(String s) {

        int result = 0;

        for (int i = 0; i < s.length(); i++) {

            int current = value(s.charAt(i));

            if (i + 1 < s.length()) {
                int next = value(s.charAt(i + 1));

                if (current < next) {
                    result -= current;
                } else {
                    result += current;
                }

            } else {
                result += current;
            }