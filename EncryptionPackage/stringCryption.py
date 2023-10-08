def string_cryption_main(collected_string):
    main_string = str(collected_string)
    crypted_string = str()
    cryption_letter_list = list()

    cryption_dictionary = {"A": "aYz1", "B": "zC34", "C": "bQw2", "Ç": "nIu2", "D": "p34R", "E": "rS23", "F": "PiQ1",
                           "G": "cK23", "Ğ": "zZx1", "H": "xWe1", "I": "9eQx", "İ": "pQ23", "J": "Zz94", "K": "xJ67",
                           "L": "yVmN", "M": "LpR5", "N": "aEzQ", "O": "bP53", "Ö": "oF61", "P": "cCvQ", "R": "eEmQ",
                           "S": "pbQS", "Ş": "cQrR", "T": "cqR2", "U": "zCv2", "Ü": "1x2q", "V": "q2Q1", "Y": "vQ3T",
                           "Z": "t2Qz", "a": "iO21", "b": "aPq2", "c": "qPu2", "ç": "ZcAp", "d": "z23Q", "e": "bRst",
                           "f": "fxNY", "g": "lzR2", "ğ": "mpR6", "h": "tQ20", "ı": "oX3R", "i": "45Zv", "j": "3TbG",
                           "k": "gRf8", "l": "s0Tr", "m": "nQ85", "n": "b6Re", "o": "G8qV", "ö": "Zrt2", "p": "pRtB",
                           "r": "fF21", "s": "zQ4F", "ş": "fY67", "t": "oNm4", "u": "p832", "ü": "Ty92", "v": "p4fH",
                           "y": "hUtR", "z": "0Lhm", "0": "mJ5d", "1": "d8Wk", "2": "p6FB", "3": "tqRB", "4": "BBq8",
                           "5": "fJh6", "6": "iI8H", "7": "9TnB", "8": "BhJk", "9": "oLtN", " ": "TqV5"}

    cryption_keys = list(cryption_dictionary.keys())

    for letters_to_append in main_string:
        cryption_letter_list.append(letters_to_append)

    for letters_to_cryption in cryption_letter_list:
        if letters_to_cryption in cryption_keys:
            crypted_letter = cryption_dictionary[letters_to_cryption]
            crypted_string = crypted_string + crypted_letter
        else:
            continue

    return crypted_string


def string_cryption_password_main(collected_string, collected_password):
    main_string = str(collected_string)
    main_password = str(collected_password)

    count = 0
    crypted_string = str()
    cryption_letter_list = list()
    cryption_letter_list_for_password = list()

    cryption_dictionary = {"A": "aYz1", "B": "zC34", "C": "bQw2", "Ç": "nIu2", "D": "p34R", "E": "rS23", "F": "PiQ1",
                           "G": "cK23", "Ğ": "zZx1", "H": "xWe1", "I": "9eQx", "İ": "pQ23", "J": "Zz94", "K": "xJ67",
                           "L": "yVmN", "M": "LpR5", "N": "aEzQ", "O": "bP53", "Ö": "oF61", "P": "cCvQ", "R": "eEmQ",
                           "S": "pbQS", "Ş": "cQrR", "T": "cqR2", "U": "zCv2", "Ü": "1x2q", "V": "q2Q1", "Y": "vQ3T",
                           "Z": "t2Qz", "a": "iO21", "b": "aPq2", "c": "qPu2", "ç": "ZcAp", "d": "z23Q", "e": "bRst",
                           "f": "fxNY", "g": "lzR2", "ğ": "mpR6", "h": "tQ20", "ı": "oX3R", "i": "45Zv", "j": "3TbG",
                           "k": "gRf8", "l": "s0Tr", "m": "nQ85", "n": "b6Re", "o": "G8qV", "ö": "Zrt2", "p": "pRtB",
                           "r": "fF21", "s": "zQ4F", "ş": "fY67", "t": "oNm4", "u": "p832", "ü": "Ty92", "v": "p4fH",
                           "y": "hUtR", "z": "0Lhm", "0": "mJ5d", "1": "d8Wk", "2": "p6FB", "3": "tqRB", "4": "BBq8",
                           "5": "fJh6", "6": "iI8H", "7": "9TnB", "8": "BhJk", "9": "oLtN", " ": "TqV5"}

    cryption_keys = list(cryption_dictionary.keys())

    for letters_to_append_for_password in main_password:
        cryption_letter_list_for_password.append(letters_to_append_for_password)

    for letters_to_append in main_string:
        cryption_letter_list.append(letters_to_append)

    for letters_to_cryption in cryption_letter_list:
        if letters_to_cryption in cryption_keys:
            crypted_letter = cryption_dictionary[letters_to_cryption]
            crypted_string = crypted_string + crypted_letter
        else:
            continue

    for letters_to_add_crypted_password in cryption_letter_list_for_password:
        if letters_to_add_crypted_password in cryption_keys:
            crypted_password_letter = cryption_dictionary[letters_to_add_crypted_password]
            if count == 0:
                crypted_string = crypted_string + "A9B8" + crypted_password_letter
                count = count + 1
            else:
                crypted_string = crypted_string + crypted_password_letter

    return crypted_string
