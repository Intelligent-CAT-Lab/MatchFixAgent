
/// SKEL HEAD BEGIN
function user_check_type(obj, _type) {
    if (typeof obj === 'object' && !Array.isArray(obj) && obj !== null && obj.hasOwnProperty("_class_name")) {
        if (String(_type).includes('function')) {
            for (let i of obj["_class_name"].split(";")) {
                if (i === String(_type).split(" ")[1].split("(")[0]) {
                    return true;
                }
            }
            return false;
        } else if (typeof _type === 'string') {
            for (let i of obj["_class_name"].split(";")) {
                if (i === _type) {
                    return true;
                }
            }
            return false;
        }
        else{
            return false;
        }
    } else {
        if (typeof _type === 'symbol') {
            if (_type.description === 'str' || _type.description === 'string') {
                return typeof obj === 'string';
            }
            if (_type.description === 'list' || _type.description === 'array') {
                return Array.isArray(obj);
            }
            if (_type.description === 'dict') {
                return obj.constructor === Object;
            }
            if (_type.description === 'int' || _type.description === 'number') {
                return Number.isSafeInteger(obj)  && obj !== 1e6;;
            }
            if (_type.description === 'float') {
                return typeof obj === 'number';
            }
            if (_type.description === 'bool' || _type.description === 'boolean') {
                return typeof obj === 'boolean';
            }
            if (_type.description === 'datetime') {
                return obj instanceof Date;
            }
            if (_type.description === 'time') {
                return obj instanceof Date && obj.getFullYear() === 1970 && obj.getMonth() === 0 && obj.getDate() === 1;
            }
            if (_type.description === 'date') {
                return obj instanceof Date && obj.getHours() === 0 && obj.getMinutes() === 0 && obj.getSeconds() === 0;
            }
            return false;
        }

        if (typeof _type === 'string') {
            if (_type === 'str' || _type === 'string') {
                return typeof obj === 'string';
            }
            if (_type === 'list' || _type === 'array') {
                return Array.isArray(obj);
            }
            if (_type === 'dict') {
                return obj.constructor === Object;
            }
            if (_type === 'int' || _type === 'number') {
                return Number.isSafeInteger(obj) && obj !== 1e6;
            }
            if (_type === 'float') {
                return typeof obj === 'number';
            }
            if (_type === 'bool' || _type === 'boolean') {
                return typeof obj === 'boolean';
            }
            if (_type === 'datetime') {
                return obj instanceof Date;
            }
            if (_type === 'time') {
                return obj instanceof Date && obj.getFullYear() === 1970 && obj.getMonth() === 0 && obj.getDate() === 1;
            }
            if (_type === 'date') {
                return obj instanceof Date && obj.getHours() === 0 && obj.getMinutes() === 0 && obj.getSeconds() === 0;
            }
            return false;
        }
        else return obj instanceof _type;
    }
}


function SkelClass(name) {
    let _class_var = {};
    _class_var._class_name = name;
    return _class_var;
}

/// SKEL HEAD END

function Node(param_0, param_1){
    function __init__(label, parent){
        /// --- BLOCK BEGIN 1
class_var.label = label;
class_var.parent = parent;
class_var.left = null;
class_var.right = null;    
        /// --- BLOCK END 1
    
    }
    
    var class_var = SkelClass('Node');
    class_var.__init__ = __init__;
    __init__(param_0, param_1);
    return class_var;
}


function BinarySearchTree(){
    function __init__(){
        /// --- BLOCK BEGIN 2
class_var.root = null;
return null;    
        /// --- BLOCK END 2
    
    }
    
    function empty(){
        /// --- BLOCK BEGIN 3
class_var.root = null;
return null;    
        /// --- BLOCK END 3
    
    }
    
    function is_empty(){
        /// --- BLOCK BEGIN 4
return class_var.root === null;    
        /// --- BLOCK END 4
    
    }
    
    function put(label){
        /// --- BLOCK BEGIN 5
class_var.root = class_var._put(class_var.root, label, null);    
        /// --- BLOCK END 5
    
    }
    
    function _put(node, label, parent){
        /// --- BLOCK BEGIN 6
        if (node === null) {
            node = new Node(label, parent);
        } else {
            if (label < node.label) {
                node.left = class_var._put(node.left, label, node);
            } else if (label > node.label) {
                node.right = class_var._put(node.right, label, node);
            } else {
                var msg = "Node with label " + label + " already exists";
                throw new Exception(msg);
            }
        }
        return node;    
        /// --- BLOCK END 6
    
    }
    
    function search(label){
        /// --- BLOCK BEGIN 7
return class_var._search(class_var.root, label);    
        /// --- BLOCK END 7
    
    }
    
    function _search(node, label){
        /// --- BLOCK BEGIN 8
        if (node === null) {
            var msg = "Node with label " + label + " does not exist";
            throw new Exception(msg);
        } else {
            if (label < node.label) {
                node = class_var._search(node.left, label);
            } else if (label > node.label) {
                node = class_var._search(node.right, label);
            }
        }
        return node;    
        /// --- BLOCK END 8
    
    }
    
    function remove(label){
        /// --- BLOCK BEGIN 9
var node = class_var.search(label);
if (node.right && node.left) {
    var lowest_node = class_var._get_lowest_node(node.right);
    lowest_node.left = node.left;
    lowest_node.right = node.right;
    node.left.parent = lowest_node;
    if (node.right) {
        node.right.parent = lowest_node;
    }
    class_var._reassign_nodes(node, lowest_node);
} else if (!node.right && node.left) {
    class_var._reassign_nodes(node, node.left);
} else if (node.right && !node.left) {
    class_var._reassign_nodes(node, node.right);
} else {
    class_var._reassign_nodes(node, null);
}    
        /// --- BLOCK END 9
    
    }
    
    function _reassign_nodes(node, new_children){
        /// --- BLOCK BEGIN 10
if (new_children !== null) {
    new_children.parent = node.parent;
}
if (node.parent !== null) {
    if (node.parent.right === node) {
        node.parent.right = new_children;
    } else {
        node.parent.left = new_children;
    }
} else {
    class_var.root = new_children;
}
return null;
    
        /// --- BLOCK END 10
    
    }
    
    function _get_lowest_node(node){
        /// --- BLOCK BEGIN 11
        var lowest_node;
        if (node.left) {
            lowest_node = class_var._get_lowest_node(node.left);
        } else {
            lowest_node = node;
            class_var._reassign_nodes(node, node.right);
        }
        return lowest_node;    
        /// --- BLOCK END 11
    
    }
    
    function exists(label){
        /// --- BLOCK BEGIN 12
try {
    class_var.search(label);
    return true;
} catch (exception) {
    return false;
}    
        /// --- BLOCK END 12
    
    }
    
    function get_max_label(){
        /// --- BLOCK BEGIN 13
if (class_var.root === null) {
    throw new Exception("Binary search tree is empty");
}
var node = class_var.root;
while (node.right !== null) {
    node = node.right;
}
return node.label;    
        /// --- BLOCK END 13
    
    }
    
    function get_min_label(){
        /// --- BLOCK BEGIN 14
if (class_var.root === null) {
    throw new Error("Binary search tree is empty");
}
var node = class_var.root;
while (node.left !== null) {
    node = node.left;
}
return node.label;
    
        /// --- BLOCK END 14
    
    }
    
    function inorder_traversal(){
        /// --- BLOCK BEGIN 15
return class_var._inorder_traversal(class_var.root);    
        /// --- BLOCK END 15
    
    }
    
    function* _inorder_traversal(node){
        /// --- BLOCK BEGIN 16
if (node !== null) {
    yield* class_var._inorder_traversal(node.left);
    yield node;
    yield* class_var._inorder_traversal(node.right);
}    
        /// --- BLOCK END 16
    
    }
    
    function preorder_traversal(){
        /// --- BLOCK BEGIN 17
return class_var._preorder_traversal(class_var.root);    
        /// --- BLOCK END 17
    
    }
    
    function* _preorder_traversal(node){
        /// --- BLOCK BEGIN 18
if (node !== null) {
    yield node;
    yield* class_var._preorder_traversal(node.left);
    yield* class_var._preorder_traversal(node.right);
}    
        /// --- BLOCK END 18
    
    }
    
    var class_var = SkelClass('BinarySearchTree');
    class_var.__init__ = __init__;
    class_var.empty = empty;
    class_var.is_empty = is_empty;
    class_var.put = put;
    class_var._put = _put;
    class_var.search = search;
    class_var._search = _search;
    class_var.remove = remove;
    class_var._reassign_nodes = _reassign_nodes;
    class_var._get_lowest_node = _get_lowest_node;
    class_var.exists = exists;
    class_var.get_max_label = get_max_label;
    class_var.get_min_label = get_min_label;
    class_var.inorder_traversal = inorder_traversal;
    class_var._inorder_traversal = _inorder_traversal;
    class_var.preorder_traversal = preorder_traversal;
    class_var._preorder_traversal = _preorder_traversal;
    __init__();
    return class_var;
}


function _get_binary_search_tree(){
    /// --- BLOCK BEGIN 19
var t = new BinarySearchTree();
    t.put(8);
    t.put(3);
    t.put(6);
    t.put(1);
    t.put(10);
    t.put(14);
    t.put(13);
    t.put(4);
    t.put(7);
    t.put(5);
    return t;

    /// --- BLOCK END 19

}

function test_put(){
    /// --- BLOCK BEGIN 20
t = new BinarySearchTree();
    if (!t.is_empty()) throw new Error('Assertion failed');

    t.put(8);

    if (t.root === null) throw new Error('Assertion failed');
    if (t.root.parent !== null) throw new Error('Assertion failed');
    if (t.root.label !== 8) throw new Error('Assertion failed');

    t.put(10);

    if (t.root.right === null) throw new Error('Assertion failed');
    if (t.root.right.parent !== t.root) throw new Error('Assertion failed');
    if (t.root.right.label !== 10) throw new Error('Assertion failed');

    t.put(3);

    if (t.root.left === null) throw new Error('Assertion failed');
    if (t.root.left.parent !== t.root) throw new Error('Assertion failed');
    if (t.root.left.label !== 3) throw new Error('Assertion failed');

    t.put(6);

    if (t.root.left.right === null) throw new Error('Assertion failed');
    if (t.root.left.right.parent !== t.root.left) throw new Error('Assertion failed');
    if (t.root.left.right.label !== 6) throw new Error('Assertion failed');

    t.put(1);

    if (t.root.left.left === null) throw new Error('Assertion failed');
    if (t.root.left.left.parent !== t.root.left) throw new Error('Assertion failed');
    if (t.root.left.left.label !== 1) throw new Error('Assertion failed');

    try {
        t.put(1);
    } catch (exception) {
        // Exception caught, do nothing
    }
    /// --- BLOCK END 20

}

function test_search(){
    /// --- BLOCK BEGIN 21
t = _get_binary_search_tree();

    node = t.search(6);
    if (node.label !== 6) throw new Error('Assertion failed');

    node = t.search(13);
    if (node.label !== 13) throw new Error('Assertion failed');

    try {
        t.search(2);
    } catch (exception) {
        // pass
    }
    /// --- BLOCK END 21

}

function test_remove(){
    /// --- BLOCK BEGIN 22
t = _get_binary_search_tree();

    t.remove(13);

    if (!(t.root !== null)) throw new Error("Assertion failed");
    if (!(t.root.right !== null)) throw new Error("Assertion failed");
    if (!(t.root.right.right !== null)) throw new Error("Assertion failed");
    if (!(t.root.right.right.right === null)) throw new Error("Assertion failed");
    if (!(t.root.right.right.left === null)) throw new Error("Assertion failed");

    t.remove(7);

    if (!(t.root.left !== null)) throw new Error("Assertion failed");
    if (!(t.root.left.right !== null)) throw new Error("Assertion failed");
    if (!(t.root.left.right.left !== null)) throw new Error("Assertion failed");
    if (!(t.root.left.right.right === null)) throw new Error("Assertion failed");
    if (!(t.root.left.right.left.label === 4)) throw new Error("Assertion failed");

    t.remove(6);

    if (!(t.root.left.left !== null)) throw new Error("Assertion failed");
    if (!(t.root.left.right.right !== null)) throw new Error("Assertion failed");
    if (!(t.root.left.left.label === 1)) throw new Error("Assertion failed");
    if (!(t.root.left.right.label === 4)) throw new Error("Assertion failed");
    if (!(t.root.left.right.right.label === 5)) throw new Error("Assertion failed");
    if (!(t.root.left.right.left === null)) throw new Error("Assertion failed");
    if (!(t.root.left.left.parent === t.root.left)) throw new Error("Assertion failed");
    if (!(t.root.left.right.parent === t.root.left)) throw new Error("Assertion failed");

    t.remove(3);

    if (!(t.root !== null)) throw new Error("Assertion failed");
    if (!(t.root.left.label === 4)) throw new Error("Assertion failed");
    if (!(t.root.left.right.label === 5)) throw new Error("Assertion failed");
    if (!(t.root.left.left.label === 1)) throw new Error("Assertion failed");
    if (!(t.root.left.parent === t.root)) throw new Error("Assertion failed");
    if (!(t.root.left.left.parent === t.root.left)) throw new Error("Assertion failed");
    if (!(t.root.left.right.parent === t.root.left)) throw new Error("Assertion failed");

    t.remove(4);

    if (!(t.root.left !== null)) throw new Error("Assertion failed");
    if (!(t.root.left.left !== null)) throw new Error("Assertion failed");
    if (!(t.root.left.label === 5)) throw new Error("Assertion failed");
    if (!(t.root.left.right === null)) throw new Error("Assertion failed");
    if (!(t.root.left.left.label === 1)) throw new Error("Assertion failed");
    if (!(t.root.left.parent === t.root)) throw new Error("Assertion failed");
    if (!(t.root.left.left.parent === t.root.left)) throw new Error("Assertion failed");
    /// --- BLOCK END 22

}

function test_remove_2(){
    /// --- BLOCK BEGIN 23
t = _get_binary_search_tree();

    t.remove(3);

    if (t.root === null) throw new Error('Assertion failed');
    if (t.root.left === null) throw new Error('Assertion failed');
    if (t.root.left.left === null) throw new Error('Assertion failed');
    if (t.root.left.right === null) throw new Error('Assertion failed');
    if (t.root.left.right.left === null) throw new Error('Assertion failed');
    if (t.root.left.right.right === null) throw new Error('Assertion failed');
    if (t.root.left.label !== 4) throw new Error('Assertion failed');
    if (t.root.left.right.label !== 6) throw new Error('Assertion failed');
    if (t.root.left.left.label !== 1) throw new Error('Assertion failed');
    if (t.root.left.right.right.label !== 7) throw new Error('Assertion failed');
    if (t.root.left.right.left.label !== 5) throw new Error('Assertion failed');
    if (t.root.left.parent !== t.root) throw new Error('Assertion failed');
    if (t.root.left.right.parent !== t.root.left) throw new Error('Assertion failed');
    if (t.root.left.left.parent !== t.root.left) throw new Error('Assertion failed');
    if (t.root.left.right.left.parent !== t.root.left.right) throw new Error('Assertion failed');
    /// --- BLOCK END 23

}

function test_empty(){
    /// --- BLOCK BEGIN 24
t = _get_binary_search_tree();
    t.empty();
    console.assert(t.root === null);
    /// --- BLOCK END 24

}

function test_is_empty(){
    /// --- BLOCK BEGIN 25
t = _get_binary_search_tree();
    if (t.is_empty()) throw new Error("Assertion failed");

    t.empty();
    if (!t.is_empty()) throw new Error("Assertion failed");
    /// --- BLOCK END 25

}

function test_exists(){
    /// --- BLOCK BEGIN 26
t = _get_binary_search_tree();

    console.assert(t.exists(6));
    console.assert(!t.exists(-1));
    /// --- BLOCK END 26

}

function test_get_max_label(){
    /// --- BLOCK BEGIN 27
t = _get_binary_search_tree();

    if (t.get_max_label() !== 14) {
        throw new Error('Assertion failed');
    }

    t.empty();

    try {
        t.get_max_label();
    } catch (exception) {
        // pass
    }
    /// --- BLOCK END 27

}

function test_get_min_label(){
    /// --- BLOCK BEGIN 28
t = _get_binary_search_tree();

    if (t.get_min_label() !== 1) {
        throw new Error('Assertion failed');
    }

    t.empty();

    try {
        t.get_min_label();
    } catch (exception) {
        // pass
    }
    /// --- BLOCK END 28

}

function test_inorder_traversal(){
    /// --- BLOCK BEGIN 29
t = _get_binary_search_tree();

    tmp = t.inorder_traversal();
    inorder_traversal_nodes = Array.from(tmp).map(i => i.label);
    console.assert(JSON.stringify(inorder_traversal_nodes) === JSON.stringify([1, 3, 4, 5, 6, 7, 8, 10, 13, 14]));
    /// --- BLOCK END 29

}

function test_preorder_traversal(){
    /// --- BLOCK BEGIN 30
t = _get_binary_search_tree();

    tmp = t.preorder_traversal();
    preorder_traversal_nodes = Array.from(tmp).map(i => i.label);
    console.assert(JSON.stringify(preorder_traversal_nodes) === JSON.stringify([8, 3, 1, 6, 4, 5, 7, 10, 14, 13]));
    /// --- BLOCK END 30

}

function binary_search_tree_example(){
    /// --- BLOCK BEGIN 31
t = new BinarySearchTree();
    t.put(8);
    t.put(3);
    t.put(6);
    t.put(1);
    t.put(10);
    t.put(14);
    t.put(13);
    t.put(4);
    t.put(7);
    t.put(5);

    console.log(
        `
            8
           / \\
          3   10
         / \\    \\
        1   6    14
           / \\   /
          4   7 13
           \\
            5
        `
    );

    console.log("Label 6 exists:", t.exists(6));
    console.log("Label 13 exists:", t.exists(13));
    console.log("Label -1 exists:", t.exists(-1));
    console.log("Label 12 exists:", t.exists(12));

    // Prints all the elements of the list in inorder traversal
    tmp = t.inorder_traversal()
    var inorder_traversal_nodes = Array.from(tmp).map(function(i) { return i.label; });
    console.log("Inorder traversal:", inorder_traversal_nodes);

    // Prints all the elements of the list in preorder traversal
    tmp = t.preorder_traversal()
    var preorder_traversal_nodes = Array.from(tmp).map(function(i) { return i.label; });
    console.log("Preorder traversal:", preorder_traversal_nodes);

    console.log("Max. label:", t.get_max_label());
    console.log("Min. label:", t.get_min_label());

    // Delete elements
    console.log("\nDeleting elements 13, 10, 8, 3, 6, 14");
    console.log(
        `
          4
         / \\
        1   7
             \\
              5
        `
    );
    t.remove(13);
    t.remove(10);
    t.remove(8);
    t.remove(3);
    t.remove(6);
    t.remove(14);

    // Prints all the elements of the list in inorder traversal after delete
    tmp = t.inorder_traversal()
    inorder_traversal_nodes = Array.from(tmp).map(function(i) { return i.label; });
    console.log("Inorder traversal after delete:", inorder_traversal_nodes);

    // Prints all the elements of the list in preorder traversal after delete
    tmp = t.preorder_traversal()
    preorder_traversal_nodes = Array.from(tmp).map(function(i) { return i.label; });
    console.log("Preorder traversal after delete:", preorder_traversal_nodes);

    console.log("Max. label:", t.get_max_label());
    console.log("Min. label:", t.get_min_label());

    /// --- BLOCK END 31

}

function test(){
    /// --- BLOCK BEGIN 32
binary_search_tree_example();
test_put();
test_search();
test_remove();
test_remove_2();
test_is_empty();
test_empty();
test_exists();
test_get_max_label();
test_get_min_label();
test_inorder_traversal();
test_preorder_traversal();

    /// --- BLOCK END 32

}

/// --- BLOCK BEGIN 0
test();
/// --- BLOCK END 0
