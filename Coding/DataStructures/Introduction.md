# What is Data Structures ?
A data structure is a method of organizing data to facilitate its use and manipulation. It involves storing data in a particular format. To illustrate this concept, let's consider an example:

Suppose you want to buy an ice cream and you go to a stall to make a purchase. What you encounter is a queue of people waiting for their turn to buy an ice cream. As soon as a person receives their ice cream, they leave the queue from the beginning, and someone new who wants to buy an ice cream enters the queue from the end. In this scenario:

Each person waiting in the queue represents a single data entity.
The way data (people) enters and exits the queue defines the properties of a particular data structure.

## Types of Data Structures
Data structures are mainly classified into two types:

### Linear Data Structures
Linear data structures are those in which data is organized sequentially, one after another, much like the queue at the ice cream stall. Common linear data structures include:

Array: An array is a fixed-size, ordered collection of elements of the same data type, accessible by their indices. Arrays are efficient for direct access but less flexible in terms of resizing.

Linked List: A linked list is a dynamic data structure consisting of nodes, where each node contains data and a reference (or pointer) to the next node. Linked lists are flexible in size and useful for insertions and deletions.

Stack: A stack is a linear data structure following the Last-In-First-Out (LIFO) principle. It's commonly used for managing data in a way that the most recently added item is the first to be removed.

Queue: A queue adheres to the First-In-First-Out (FIFO) principle, where the first item added is the first to be removed. It's frequently used for tasks like task scheduling.

ArrayList: Similar to arrays, ArrayLists are dynamic arrays, allowing for resizing as needed. They combine some advantages of both arrays and linked lists.

### Non-Linear Data Structures
Non-linear data structures are those in which data is organized in a non-sequential manner, similar to the arrangement of leaves on a tree. Common non-linear data structures include:

Trees: Trees are hierarchical data structures with a root node and child nodes, forming a branching structure. Examples include binary trees, binary search trees, and balanced trees like AVL and Red-Black trees.

Graphs: Graphs consist of nodes (vertices) and edges connecting them. They model complex relationships and networks. Graphs can be directed or undirected, and edges can have weights.

Tries: Tries are tree-like data structures used for efficient key-based data storage and retrieval. They are commonly used in dictionaries and autocomplete systems.