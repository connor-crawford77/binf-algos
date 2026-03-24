# Introduction
The Burrows Wheel Transform is a transformation of a string into one with useful properties for run-length encoding and finding patterns of interest in the original string. The implmementation of the Burrows Wheel transform in this project does the following:

- Finds the BWT string by finding all cyclical rotations of the original string
- Finds the suffix array of a string
- Finds the BWT string from the suffix array
- Finds the count array, a dictionary that stores the number of characters lexicographically smaller than the set of characters in the string
- Finds the occurence array, a dictionary that stores the number of times a unique character in the string occurs up to each position in the BWT
- Uses the count array and occurence array the starting position of pattern matches in the original string
- Run length encodes and decodes the BWT string

# Pseudocode

```
BWT Transformation Function:
    Append '$' to the end of input string
    Initialise a list to store all cyclic rotations
    Loop through every index in the length of the string
      Take a substring from ind to end and concatenate it with substring from start to ind
      Store the rotation along with its index position in the list

    Sort the rotations lexicographically
    Initialise a string to store the transformed string
    Initialise a list for original indices

    Loop through each rotation in the sorted rotations list
      Pick the last character of the rotation
      Append the character to the transformed string
      Store the original index position in the original indices list

  Return transformed string and original indices

Suffix Array Function:
    Append '$' to the end of the string
    Initialise a list called suff
    Loop through every index in the length of the string
      If ind equals 0 (suffix starts at the last position)
        Suff ind becomes length of string - 1
      Else
        Suff ind becomes ind - 1
      Take out the suffix from that position till the end
      Store the suffix along with its starting position
    Sort the suffix list lexicographically
    Extract the starting positions from the sorted list
  Return the starting positions as a list

BWT from suffix array Function:
    Append '$' to the text
    Initialise a string called transform
    Loop through every index in suffix positions
      Pick the character just before the suffix begins (suffix - ind; character - text[ind-1])
      Append the character to transform
  Return the transform

Calculate counts Function:
    Count the frequency of each character using Counter and sort lexicographically
    Initialise the current count as 0
    Loop through each character in the sorted order
      Store the frequency of the character
      Assign current count (number of characters that occurred until then) as the count
      Add the stored frequency to current_count
  Return the count dict

Calculate occurences Function:
    Pick the unique alphabets(characters) from BWT string
    Initialise a 2D array with zeros where rows - alphabets columns - position in BWT string
    Create a mapping from each character to its row index
    Loop through each position and character in BWT string
      Add 1 to all the positions from index onwards in that character row
BWT Transformation Function:
    Append '$' to the end of input string
    Initialise a list to store all cyclic rotations
    Loop through every index in the length of the string
      Take a substring from ind to end and substring from start to end
      Store the rotation along with its index position in the list

  To sort the rotations lexicographically
    Initialise a string to store the transformed string
    Initialise a list for original indices

    Loop through each rotation in the sorted rotations list
      Pick the last character of the rotation
      Append the character to the transformed string
      Store the original index position in original indices list

  Return transformed string and original indices

Update Range function:

Take a character of interest from the query
To update the range of the pattern search
If the lower range is 0
    The new lower range is the value of the count of the character + 0 + 1
Else
    The new lower range is the value of the count of that character + the value of the occurence of that character at the lower - 1 position

The new upper range is the value of the count of the character + the value of the occurence of that character at the upper range position

Return the new lower and upper range values

Find Match Function:

lower = 0
upper = the length of the original string - 1

For each character in the reverse query sequence
    if the lower range is greater than the upper range break the loop

    lower range, upper range = update_range(lower, upper, count array, occurence array)

Once we've done one query of the loop and have come away with multiple matches we need to update the match indices with all matches

To do this
set an indicator, like i equal to the lower range
while that indicator is less than or equal to the upper range returned from the loop
    append the suffix array value of the indicator to a list of match indexes
    increment the indicator + 1

This will appropriately update list of matches with each match

Return the list of match indices that represent each start location of the match in the original string

Run Length Encode Function:

set a character count equal to 0
define the previous character as the first character in the bwt string

for each current character in the bwt string
    if the character doesn't equal the previous character
        add the previous character and it's count to the run length encode string
        set the character count to 0 again
    increment the character count by 1
    set the previous character to the current character

add the previous character and the character count to the run length encode string and return it


Run Length Decode Function:

for each set of two characters in the run length encode string
    the character is the first character of the set
    the count is the second character of the set
    add the character times the count to the decoded string

return the decoded string


```

# Successes
As a group we were able to walk through each function and write the code together. This made learning the algorithm and trouble shooting the functions much smoother. We often found that when one person was stuck, someone else had a perspective that helped us break through, and through bouncing perspectives off each other that's how we made the most progress on the project. Because we talked through the algorithm and coded together we were able to work through the project more quickly than we otherwise would have if we tried to divide it up or work on each part on our own.

# Struggles
The biggest hurdle we had was with the pattern matching portion of this project. At our first pass through we were able to get one to two patterns returned depending on if there were multiple, however, if there were any more than two our function wouldn't find them. The ultimate problem was that if we had a lower and upper range that were different from each other by the end of the for loop that meant there was still a search range with matches, but we weren't continuing to account for these matches. Our resolution to this was a while loop that updated the match indices from the suffix arrays so long as the lower range was less than or equal to the upper range returned from the query search.

# Personal Reflections
## Group Leader
Connor Crawford: I really enjoyed working through these functions with my group this week. I felt the most confusing part of the project for me was the pattern matching. Even now, even though I understand how the steps are working as we've implemented it, I still feel a little unsure about why it works and finds all the pattern matches. Despite this I felt like implementation went very smooth and my group members had really valuable perspectives that helped me understand this project.

## Other member
Aaronie Jersha Jenyfred: For this project, I feel the conceptual understanding was the hardest part. The overview of pseudocode that was given for eaach function really helped in navigating the algorithmic logic. This project also broadened my understanding of indexing and string operations. Also, debugging and brainstorming together as a group made the work real smooth. 

Nicholas Bottomley: The implementation was relatively straightforward once we were able to understand the conceptual parts. The pseudocode and slides from the lecture powerpoint were extremely useful for understanding what was happening. My groupmates helped fix any other confusion that I had during our group meetings. Overall, this project went very smoothly and we were able to successfully implement a working BWT and run-length encoding algorithm.

# Generative AI Appendix
Generative AI was not used in this project.
