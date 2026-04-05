/**
 * TreeNode Class
 * Represents a node in the binary search tree.
 */
class TreeNode {
    /**
     * @constructor
     * @param {number} key - The key used to identify the node.
     * @param {number} val - The value associated with the key.
     */
    constructor(key, val) {
        this.key = key;
        this.val = val;
        this.left = null;
        this.right = null;
    }
}

/**
 * TreeMap Class
 * Implements a Binary Search Tree Map which maps integer keys to integer values.
 */
class TreeMap {
    /**
     * Initializes an empty binary search tree map.
     */
    constructor() {
        this.root = null;
    }

    /**
     * Inserts a key-value pair into the tree.
     * @param {number} key - The key to insert.
     * @param {number} val - The value to associate with the key.
     * @returns {void}
     */
    insert(key, val) {
        let newNode = new TreeNode(key, val);
        if (this.root === null) {
            this.root = newNode;
            return;
        }

        let current = this.root;
        while (true) {
            if (key < current.key) {
                if (current.left === null) {
                    current.left = newNode;
                    return;
                }
                current = current.left;
            } else if (key > current.key) {
                if (current.right === null) {
                    current.right = newNode;
                    return;
                }
                current = current.right;
            } else {
                current.val = val;
                return;
            }
        }
    }

    /**
     * Fetches the value associated with a key.
     * @param {number} key - The key to fetch.
     * @returns {number} - The value associated with the key or -1 if not found.
     */
    get(key) {
        let current = this.root;
        while (current !== null) {
            if (key < current.key) {
                current = current.left;
            } else if (key > current.key) {
                current = current.right;
            } else {
                return current.val;
            }
        }
        return -1;
    }

    /**
     * Fetches the value associated with the smallest key.
     * @returns {number} - The value associated with the smallest key or -1 if tree is empty.
     */
    getMin() {
        let current = this.findMin(this.root);
        return current !== null ? current.val : -1;
    }

    /**
     * Utility function to find the node with the smallest key.
     * @param {TreeNode} node - The node to start from.
     * @returns {TreeNode} - The node with the smallest key.
     */
    findMin(node) {
        while (node && node.left !== null) {
            node = node.left;
        }
        return node;
    }

    /**
     * Fetches the value associated with the largest key.
     * @returns {number} - The value associated with the largest key or -1 if tree is empty.
     */
    getMax() {
        let current = this.root;
        while (current !== null && current.right !== null) {
            current = current.right;
        }
        return current !== null ? current.val : -1;
    }

    /**
     * Removes the node associated with a key.
     * @param {number} key - The key to remove.
     * @returns {void}
     */
    remove(key) {
        this.root = this.removeHelper(this.root, key);
    }

    /**
     * Utility function to recursively remove the node with a given key.
     * @param {TreeNode} curr - The current node.
     * @param {number} key - The key to remove.
     * @returns {TreeNode} - The updated node.
     */
    removeHelper(curr, key) {
        if (curr === null) {
            return null;
        }

        if (key > curr.key) {
            curr.right = this.removeHelper(curr.right, key);
        } else if (key < curr.key) {
            curr.left = this.removeHelper(curr.left, key);
        } else {
            if (curr.left === null) {
                return curr.right;
            } else if (curr.right === null) {
                return curr.left;
            } else {
                let minNode = this.findMin(curr.right);
                curr.key = minNode.key;
                curr.val = minNode.val;
                curr.right = this.removeHelper(curr.right, minNode.key);
            }
        }
        return curr;
    }

    /**
     * Fetches the keys in ascending order.
     * @returns {number[]} - An array containing keys in ascending order.
     */
    getInorderKeys() {
        let result = [];
        this.inorderTraversal(this.root, result);
        return result;
    }

    /**
     * Utility function for in-order traversal to fetch keys.
     * @param {TreeNode} root - The root node to start traversal.
     * @param {number[]} result - An array to store the keys.
     * @returns {void}
     */
    inorderTraversal(root, result) {
        if (root !== null) {
            this.inorderTraversal(root.left, result);
            result.push(root.key);
            this.inorderTraversal(root.right, result);
        }
    }
}
