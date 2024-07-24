def hamming_encode(data):
    """
    Encodes the input data using Hamming code.
    """
    # Calculate the number of parity bits needed
    m = len(data)
    r = 0
    while 2**r < m + r + 1:
        r += 1

    # Initialize the encoded data
    encoded = [0] * (m + r)

    # Fill the data bits
    data_index = 0
    for i in range(len(encoded)):
        if (i + 1) & (i + 2) == 0:  # Check if the position is a power of 2 (parity bit position)
            continue
        encoded[i] = data[data_index]
        data_index += 1

    # Calculate the parity bits
    for i in range(r):
        parity = 0
        for j in range(1, len(encoded) + 1):
            if j & (2**i):
                parity ^= encoded[j - 1]
        encoded[2**i - 1] = parity

    return encoded

def hamming_decode(encoded):
    """
    Decodes the input Hamming encoded data.
    """
    # Calculate the number of parity bits
    r = 0
    while 2**r < len(encoded):
        r += 1

    # Calculate the syndrome
    syndrome = 0
    for i in range(r):
        parity = 0
        for j in range(1, len(encoded) + 1):
            if j & (2**i):
                parity ^= encoded[j - 1]
        syndrome += parity * (2**i)

    # If syndrome is non-zero, there is an error at the position indicated by syndrome
    if syndrome:
        encoded[syndrome - 1] ^= 1

    # Extract the data bits
    data = []
    data_index = 0
    for i in range(len(encoded)):
        if (i + 1) & (i + 2) != 0:  # Check if the position is not a power of 2 (parity bit position)
            data.append(encoded[i])

    return data

# Example usage
data = [1, 0, 1, 1]
encoded = hamming_encode(data)
print("Encoded data:", encoded)
decoded = hamming_decode(encoded)
print("Decoded data:", decoded)
