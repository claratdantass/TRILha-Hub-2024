s = "egg" 
t = "add"

dict = {}
def isomorfic(s,t):
    if len(set(s)) != len(set(t)):
    # if the number of unique letters is diff, than this words cannot be isomorfic
    # the 'set' function takes off the repeated letters, only a unique version of that letter remains
        return False

    for i in range(len(s)):
        if s[i] not in dict:
            dict[s[i]] = t[i]
        elif dict[s[i]] != t[i]:
            return False 
    return True



