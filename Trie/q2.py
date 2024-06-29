"""
Trie is an efficient information retrieval data structure. This data structure is used to store Strings and search strings, String stored can also be deleted. Given a Trie root for a larger string super and a string key, delete all the occurences of key in the Trie.

Example 1:

Input:
N = 8
super = "the a there answer any by bye their" 
key = "the" 
 

Your Task:

Complete the function deleteKey() to delete the given string key.The String key if exists in the larger string super, must be deleted from Trie root. The larger string super contains space separated small strings. And if the string is deleted successfully than 1 will be printed.
If any other string other than String A is deleted, you will get wrong answer.

 

Constraints:
1≤ T ≤200
1≤ N, |A| ≤20
"""

class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEndOfWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, key):
        node = self.root
        for char in key:
            index = ord(char) - ord('a')
            if not node.children[index]:
                node.children[index] = TrieNode()
            node = node.children[index]
        node.isEndOfWord = True
    
    def search(self, key):
        node = self.root
        for char in key:
            index = ord(char) - ord('a')
            if not node.children[index]:
                return False
            node = node.children[index]
        return node is not None and node.isEndOfWord
    
    def deleteKey(self, key):
        node = self.root
        # Check if key is in the Trie
        for char in key:
            index = ord(char) - ord('a')
            if not node.children[index]:
                print(0)
                return
            node = node.children[index]
        
        # Mark the last node as not end of word
        node.isEndOfWord = False
        
        # Function to perform deletion from Trie
        def delete_helper(node, key, depth):
            if depth == len(key):
                return
            
            index = ord(key[depth]) - ord('a')
            child_node = node.children[index]
            
            if child_node:
                delete_helper(child_node, key, depth + 1)
                # After recursion, check if the child node can be deleted
                if not any(node.children):
                    node.children[index] = None
        
        # Iterate through all words in super and delete occurrences of key
        super_words = super.split()
        for word in super_words:
            if word == key:
                delete_helper(self.root, key, 0)
        
        # After deletion, check if key is still present in Trie
        if self.search(key):
            print(0)
        else:
            print(1)

# Driver Code
if __name__ == '__main__':
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        super_str = input().strip()
        key = input().strip()
        
        trie = Trie()
        words = super_str.split()
        
        for word in words:
            trie.insert(word)
        
        trie.deleteKey(key)
