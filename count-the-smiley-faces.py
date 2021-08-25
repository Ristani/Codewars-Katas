"""
Given an array (arr) as an argument complete the function countSmileys that should
return the total number of smiling faces.

Rules for a smiling face:

Each smiley face must contain a valid pair of eyes. Eyes can be marked as : or ;
A smiley face can have a nose but it does not have to. Valid characters for a nose are - or ~
Every smiling face must have a smiling mouth that should be marked with either ) or D
No additional characters are allowed except for those mentioned.

Valid smiley face examples: :) :D ;-D :~)
Invalid smiley faces: ;( :> :} :]

Example
countSmileys([':)', ';(', ';}', ':-D']);       // should return 2;
countSmileys([';D', ':-(', ':-)', ';~)']);     // should return 3;
countSmileys([';]', ':[', ';*', ':$', ';-D']); // should return 1;

Note
In case of an empty array return 0. You will not be tested with invalid
input (input will always be an array). Order of the face (eyes, nose, mouth)
elements will always be the same.
"""

def count_smileys(arr):
    # Defaults results to 0 if no smileys in array.
    res = 0
    # Check each string in the array.
    for s in arr:
        # Length of 2 has no nose, :) ;D.
        if len(s) == 2 and s[0] in [":", ";"] and s[-1] in [")", "D"]:
            # Count it.
            res += 1
        # Length of 3 has a nose, ;~) :-D.
        elif len(s) == 3 and s[0] in [":", ";"] and s[1] in ["-", "~"] and s[-1] in [")", "D"]:
            # Count it.
            res += 1
    # Return number of smileys.
    return res
