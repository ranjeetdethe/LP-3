import time

# Naive String Matching Algorithm
def naive_string_matching(text, pattern):
    n = len(text)         # Length of the text
    m = len(pattern)      # Length of the pattern
    matches = []          # List to store the starting indices of matches

    # Loop through each position in the text
    for i in range(n - m + 1):
        # Check for pattern match at position i
        for j in range(m):
            if text[i + j] != pattern[j]:
                break
        else:
            # If the inner loop didn't break, we found a match
            matches.append(i)
    return matches

# Rabin-Karp Algorithm
def rabin_karp(text, pattern):
    n = len(text)         # Length of the text
    m = len(pattern)      # Length of the pattern
    d = 256               # Number of characters in the input alphabet
    q = 101               # A prime number
    p = 0                 # Hash value for the pattern
    t = 0                 # Hash value for the text
    h = 1                # The value of h will be "d^(m-1) % q"
    matches = []          # List to store the starting indices of matches

    # Precompute h = d^(m-1) % q
    for i in range(m - 1):
        h = (h * d) % q

    # Compute the hash value of the pattern and the first window of text
    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q

    # Slide the pattern over the text one by one
    for i in range(n - m + 1):
        # Check the hash values of the current window of text and pattern
        if p == t:
            # Check for characters one by one
            if text[i:i + m] == pattern:
                matches.append(i)

        # Calculate the hash value for the next window of text
        if i < n - m:
            t = (d * (t - ord(text[i]) * h) + ord(text[i + m])) % q

            # We might get negative value of t, converting it to positive
            if t < 0:
                t += q

    return matches

# Function to test both algorithms and measure performance
def test_string_matching():
    text = "ABABDABACDABABCABAB"  # Sample text
    pattern = "ABAB"              # Sample pattern

    # Testing Naive String Matching
    start_time = time.time()      # Start timing for Naive
    naive_matches = naive_string_matching(text, pattern)
    naive_time = time.time() - start_time  # Calculate time taken for Naive

    # Testing Rabin-Karp Algorithm
    start_time = time.time()      # Start timing for Rabin-Karp
    rabin_matches = rabin_karp(text, pattern)
    rabin_time = time.time() - start_time  # Calculate time taken for Rabin-Karp

    # Print results
    print("Naive String Matching Matches at Indices:", naive_matches)
    print("Time taken by Naive String Matching:", naive_time)
    print("Rabin-Karp Matches at Indices:", rabin_matches)
    print("Time taken by Rabin-Karp Algorithm:", rabin_time)

# Run the test
test_string_matching()

