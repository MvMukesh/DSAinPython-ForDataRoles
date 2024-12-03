"""
Author: https://www.linkedin.com/in/mukesh-manral/
"""
import unittest

from solutions.remove_nth_node_from_end_of_list import Solution
from solutions.remove_nth_node_from_end_of_list import Solution2
from solutions.utils.leetcode import list_to_listnode
from solutions.utils.leetcode import listnode_to_list


class TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test(self):
        head = list_to_listnode([1, 2, 3, 4, 5])
        n = 2
        expected_head = self.solution.removeNthFromEnd(head, n)
        expected = [1, 2, 3, 5]
        self.assertEqual(listnode_to_list(expected_head), expected)

    def test2(self):
        head = list_to_listnode([1, 2, 3, 4, 5])
        n = 1
        expected_head = self.solution.removeNthFromEnd(head, n)
        expected = [1, 2, 3, 4]
        self.assertEqual(listnode_to_list(expected_head), expected)

    def test3(self):
        head = list_to_listnode([1, 2])
        n = 2
        expected_head = self.solution.removeNthFromEnd(head, n)
        expected = [2]
        self.assertEqual(listnode_to_list(expected_head), expected)

    def test4(self):
        head = list_to_listnode([1])
        n = 1
        expected_head = self.solution.removeNthFromEnd(head, n)
        expected = []
        self.assertEqual(listnode_to_list(expected_head), expected)


class TestCase2(unittest.TestCase):
    def setUp(self):
        self.solution = Solution2()

    def test(self):
        head = list_to_listnode([1, 2, 3, 4, 5])
        n = 2
        expected_head = self.solution.removeNthFromEnd(head, n)
        expected = [1, 2, 3, 5]
        self.assertEqual(listnode_to_list(expected_head), expected)

    def test2(self):
        head = list_to_listnode([1, 2, 3, 4, 5])
        n = 1
        expected_head = self.solution.removeNthFromEnd(head, n)
        expected = [1, 2, 3, 4]
        self.assertEqual(listnode_to_list(expected_head), expected)

    def test3(self):
        head = list_to_listnode([1, 2])
        n = 2
        expected_head = self.solution.removeNthFromEnd(head, n)
        expected = [2]
        self.assertEqual(listnode_to_list(expected_head), expected)

    def test4(self):
        head = list_to_listnode([1])
        n = 1
        expected_head = self.solution.removeNthFromEnd(head, n)
        expected = []
        self.assertEqual(listnode_to_list(expected_head), expected)


if __name__ == '__main__':
    unittest.main()
