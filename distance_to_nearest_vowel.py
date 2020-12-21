def distance_to_nearest_vowel(txt):
    """Finds the distance of every letter from the closest vowel in string."""

    prev = float('-inf')
    ans = []
    for i, x in enumerate(txt):
        if x in 'aeiou': prev = i
    ans.append(i - prev)

    prev = float('inf')
    for i in range(len(txt) - 1, -1, -1):
        if txt[i] in 'aeiou': prev = i
    ans[i] = min(ans[i], prev - i)

    return ans
