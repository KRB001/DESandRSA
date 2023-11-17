def ascii_to_hex(message):
    result = ""
    if len(message) == 0:
        return result
    for char in message:
        result = result + str(format(ord(char), "x"))
    return result


def hex_to_binary(message):
    if len(message) == 0:
        return ""
    result = bin(int(message, 16))[2:].zfill(64)
    return result


def ascii_to_binary(message):
    temp = ascii_to_hex(message)
    return hex_to_binary(temp)