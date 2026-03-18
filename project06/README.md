# Introduction
In this project we use a Neighbor-joining (NJ) algorithm to create a phylogenetic tree based on 20 HIV-1 reverse transcriptase sequences. The NJ method constructs a tree based off of a distance matrix that represents how similar two sequences are to eahc other. The NJ algorithm iteratively joins "neighbors" to internal nodes based on how closely related they are to each other and all other members of the distance matrix. It starts by operating on the most closely related neighbors, connecting them to an internal node, removing them from the distance matrix, and then adding the internal node to the distance matrix. It does this iteratively until all that is left is a 2x2 matrix from which it can connect the final neighbors in the distance matrix. The result of this algorithm is a newick string representation of the phylogenetic tree which can be plotted to create a final tree.

** Note ** Both neighbour_joining.py and project06.ipynb do the same things, as long as the class data, smithwaterman.py, and distance_matrix.py are in your directory both files should have the same functionality.
# Pseudocode

```
Neighbour joining algorithm

INITIALISATION STEP

I. Make a working copy of distance matrix so original is not modified where D is copy of distance_matrix
II. Make a copy of labels containing sequenceIDs
III. Set n to be the number of sequences which is the length of column or length of row in the distance matrix
IV. Each sequence starts as its own newick string and this dict grows into the full tree as merges happen
    newick_nodes = {}
    The Dictionary structure
    key   = the node name (sequence ID used in the matrix)
    value = the newick string for that node and everything below if the key were to be an internal node
        The newick string contains
        1. leaf names      — the sequence IDs
        2. branch lengths  — the limb lengths like 11.0, 2.0
        3. brackets        — showing which nodes are grouped together
    for each label in labels:
        newick_nodes[label] = label
    # result: {"DM1": "DM1", "DM2": "DM2", ...}
V.  counter = 0 # counter increments each iteration so internal node name is always unique

ITERATION STEP
    while n > 2:

        1. Calculate row sum which is sum of each row in D matrix for every node
        # Sum every row in D matrix
        # row_sums[i] = total distance from node i to all others
        row_sums = array of size n
        for each node i from 0 to n-1:
            row_sums[i] = sum of all values in row i of D matrix

        2. Fill in Q matrix in which for one cell two row sums are used as for every pair in (i,j):
        # Create empty n×n Q matrix
        Q = zeros(n, n)
        # Fill every cell using two rows at a time
        for each i from 0 to n-1:
            for each j from 0 to n-1:
                if i != j:
                    Q(i,j) = (n-2) * D[i][j] - row_sums[i] - row_sums[j]
        #set diagonal so it is never picked as minimum


        3. Find the closet neighbour(i,j) which is the most negative number in the Q matrix
        where (i,j)  represents the position of minimum value in Q matrix

        4. Calculate the limb length to internal node k using distance matrix
        r_i = row_sums[i] # Calculates how far is i from everyone
        r_j = row_sums[j] # Calculates how far is j from everyone
          (a). Split distance evenly in halves
            half_dist = D[i][j] / 2
          (b). Correction for global position
            # if r_i > r_j then i is further from everyone than j
            # so di gets bigger pushing j closer to k
            # if r_i == r_j then correction is 0 — split evenly distances to k
            correction = (r_i - r_j) / (2 * (n-2))
          (c). Calculate branch length from i to internal node k
            di = half_dist + correction
          (d). Calculate branch length from j to internal node k using whatever distance is left after di
            dj = D[i][j] - di

        5. When internal node (k) is found
        (a). Get the existing newick strings for i and j
        newick_i = newick_nodes[labels[i]]
        newick_j = newick_nodes[labels[j]]

        (b). Build newick string for k combining i and j
        # wrap them together into one newick string for k
        # format: (left_subtree:length, right_subtree:length)
        new_newick = "(" + newick_i + ":" + di + "," + newick_j + ":" + dj + ")"

        6. Compute distances from new node k to all remaining nodes x
        # calculate how far x remaining nodes is from the new internal node k
            new_distances = []
            for each x from 0 to n-1:
                if x != i and x != j:
                 # average the distances through i and j
                # minus D[i][j] to remove double counting
                d_kx = (D[i][x] + D[j][x] - D[i][j]) / 2
                new_distances.append(d_kx)

        7. Rebuild matrix without i and j and with k added:
        (a). Collect indices of all nodes except i and j
        keep = [all indices from 0 to n-1 except i and j]

        (b). Generate unique name for new internal node
        # counter increments each iteration so name is always unique
        counter   = counter + 1
        new_label = f"internal_node_{counter}"

        (c). Build new smaller matrix from kept rows and columns
        # size goes from n×n to (n-1)×(n-1)
        new_D = D[keep rows][keep columns]

        (d). Expand by 1 row and 1 column for new node k
        expanded = zeros(n-1, n-1)
        expanded[0:n-2][0:n-2] = new_D

        (e). Fill in k's distances to all remaining nodes
        for each index x from 0 to len(new_distances)-1:
            expanded[last_row][x] = new_distances[x]
            expanded[x][last_col] = new_distances[x]

        (f). Update labels — remove i and j, add k
        new_labels = [labels[x] for x in keep] + [new_label]

        (g). Update newick nodes dict
        # remove i and j entries, add k entry
        new_newick_nodes = {labels[x]: newick_nodes[labels[x]] for x in keep}
        new_newick_nodes[new_label] = new_newick

        (h). Update everything for next iteration
        D  = expanded
        labels  = new_labels
        newick_nodes =  new_newick_nodes
        n  = n - 1

TERMINATION STEP
# only two nodes left so we can connect directly
# no Q matrix needed as only one pair remains
    final_dist = D[0][1]
    # get newick strings for last two nodes
    n0 = newick_nodes[labels[0]]
    n1 = newick_nodes[labels[1]]
    # split final distance evenly between both sides
    # because there is no correction possible with only 2 nodes

    # The newick_string containing the tree graph
    return newick_string

Key things in the algorithm

newick_nodes dict is the tree
— each merge wraps two entries into one newick string
— by termination it contains the full tree string

k internal node is created from DM1 (i) and DM2 (j)
— k enters the matrix as a single node
— matrix is now: [k, DM3, DM4]

— newick_nodes = {
    "k":   "(DM1:11.0,DM2:2.0)",
    "DM3": "DM3",
    "DM4": "DM4"
}

D is always a square matrix
— starts n×n
— shrinks by 1 each iteration

row_sums must be recomputed every iteration
— matrix changes each time so old row sums are out of date
```

# Successes
We communicated our progress along the way and shared resources that helped us understand the algorithm better.  We were able to print out the distance matrix from the 20 sequences which helped us in implementing the neighbor joining algorithm. We walked through each step of the process together and successfully ran the neighbor joining algorithm.

# Struggles
The neighbor joining overall was a little bit confusing especially the part of getting to know what the Q matrix does and trying to implement it in the algorithm was a little bit of a challenge for all of us.

# Personal Reflections
## Group Leader
Connor Crawford - This weeks algorithm was the most conceptually difficult for me to understand. I had a hard time understanding the purpose of creating the q-matrix based off the distance matrix. Furthermore, I struggled to understand how we use the q-matrix to update the distance matrix, and how any of that helped us figure out the distances properly. Thankfully Thu Thu was on top of it this week and had great pseudocode and resources for us to go off. Eventually I came to the understanding that values in the q-matrix represent adjusted distances based off of how far away two sequences are from each other and how far away each sequences is from every other sequence in the matrix. These adjusted distances can be used to pick the most closely related sequence in any given iteration, whose distaces to an internal parent node can be calculated based off 1. how far away they are from each other and 2. how far away they are from every other sequence relative to one another.

## Other member
Fardina Tabassum- This project was tricky to figure out, mostly because it took me a while to figure out that the algorithm we were doing in class was different from what we were to implement for this project. Due to having a hectic week, I was unable to dedicate as much time to this project, but my teammates really helped me catch up to speed and broke down the entire algorithm step by step which greatly helped with my understanding. I was a bit glad that we got to reuse some of the logic from the previous project such as the Smith-Waterman so I was not completely lost but I did have a hard time understanding how we go from a distance matrix to a Q matrix and the calculation behind it but after meeting with my teammates I was able to gain much more clarity about the concept.

Thu Thu Han - For this week, I started working on the algorithm a little bit earlier as I felt really behind during class and could not understand the lecture content. I struggled really bad to grasp the whole picture as there was a lot of information to take in and to consider. But pieces started to come together eventually and the main part of the neighbor joining algorithm which only takes two nodes per iteration really helped me understand the algorithm overall as I was able to visualize what the final graph should look like. I think this week was when I made most of my personal development as well. I was able rewrite the draft diagram I had to pseudocode working with dictionaries and matrices and I learned different ways to utilize NumPy module and they were so helpful in this algorithm. Moreover understanding the Q matrix and the calculation it does to find neighbor was also was a huge factor in implementing the algorithm. I think being able to visualize each step along the way really helped in the long run as I implemented the code. 

# Generative AI Appendix
No AI use in this project.
