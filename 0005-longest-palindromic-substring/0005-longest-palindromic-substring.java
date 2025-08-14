class Solution {
    public String longestPalindrome(String s) {
        String longest = "";
         //s = "abba";
        s = s.replace("","#");
        for (int center = 0; center < s.length(); center++) {
//            String longestPair = getLongest(s, center, true);
//            if (longestPair.length() > longest.length()) {
//                longest = longestPair;
//            }
            String longestOdd = getLongest(s, center, false);
            if (longestOdd.length() > longest.length()) {
                longest = longestOdd;
            }
        }
        return longest.replace("#","");
    }

    private static String getLongest(String s, int center, boolean czyParzysty) {
        int ramie = 0;
        int centerLeft = center;
        int centerRight = centerLeft;
        if (czyParzysty) {
            centerRight++;
        }
        while (centerRight + ramie < s.length() && centerLeft - ramie >= 0) {
            char leftValue = s.charAt(centerLeft - ramie);
            char rightValue = s.charAt(centerRight + ramie);
            if (leftValue != rightValue) {
                break;
            }
            ramie++;
        }
        return s.substring(centerLeft - ramie + 1, centerRight + ramie );
    }


}