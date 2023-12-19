/*
 * @lc app=leetcode id=20 lang=golang
 *
 * [20] Valid Parentheses
 *
 * https://leetcode.com/problems/valid-parentheses/description/
 *
 * algorithms
 * Easy (40.27%)
 * Likes:    22863
 * Dislikes: 1591
 * Total Accepted:    4.1M
 * Total Submissions: 10.1M
 * Testcase Example:  '"()"'
 *
 * Given a string s containing just the characters '(', ')', '{', '}', '[' and
 * ']', determine if the input string is valid.
 *
 * An input string is valid if:
 *
 *
 * Open brackets must be closed by the same type of brackets.
 * Open brackets must be closed in the correct order.
 * Every close bracket has a corresponding open bracket of the same type.
 *
 *
 *
 * Example 1:
 *
 *
 * Input: s = "()"
 * Output: true
 *
 *
 * Example 2:
 *
 *
 * Input: s = "()[]{}"
 * Output: true
 *
 *
 * Example 3:
 *
 *
 * Input: s = "(]"
 * Output: false
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= s.length <= 10^4
 * s consists of parentheses only '()[]{}'.
 *
 *
 */

// @lc code=start
package main

import "fmt"

func isValid(s string) bool {
	resStack := []string{}
	validPairs := map[string]struct{}{
		"()": {},
		"[]": {},
		"{}": {},
	}

	openingBracket := map[rune]struct{}{
		'(': {},
		'[': {},
		'{': {},
	}

	for _, c := range s {
		if _, ok := openingBracket[c]; !ok {
			if len(resStack) == 0 {
				// fmt.Println(1)
				return false
			}
			poppedEl := resStack[len(resStack)-1]
			// fmt.Println(resStack)
			resStack = resStack[:len(resStack)-1]
			concatEl := fmt.Sprint(poppedEl + string(c))
			// fmt.Println(concatEl)
			// fmt.Println(resStack)
			if _, ok := validPairs[concatEl]; !ok {
				// fmt.Println(2)
				return false
			}
		} else {
			resStack = append(resStack, string(c))
		}
	}

	return len(resStack) == 0
}

// @lc code=end
