def string_uncryption_main(collected_string):
    crypted_string = str(collected_string)
    uncryption_group = str()
    uncrypted_string = str()
    uncryption_group_list = list()

    uncryption_dictionary = {"aYz1": "A", "zC34": "B", "bQw2": "C", "nIu2": "Ç", "p34R": "D", "rS23": "E", "PiQ1": "E",
                             "cK23": "G", "zZx1": "Ğ", "xWe1": "H", "9eQx": "I", "pQ23": "İ", "Zz94": "J", "xJ67": "K",
                             "yVmN": "L", "LpR5": "M", "aEzQ": "N", "bP53": "O", "oF61": "Ö", "cCvQ": "P", "eEmQ": "R",
                             "pbQS": "S", "cQrR": "Ş", "cqR2": "T", "zCv2": "U", "1x2q": "Ü", "q2Q1": "V", "vQ3T": "Y",
                             "t2Qz": "Z", "iO21": "a", "aPq2": "b", "qPu2": "c", "ZcAp": "ç", "z23Q": "d", "bRst": "e",
                             "fxNY": "f", "lzR2": "g", "mpR6": "ğ", "tQ20": "h", "oX3R": "ı", "45Zv": "i", "3TbG": "j",
                             "gRf8": "k", "s0Tr": "l", "nQ85": "m", "b6Re": "n", "G8qV": "o", "Zrt2": "ö", "pRtB": "p",
                             "fF21": "r", "zQ4F": "s", "fY67": "ş", "oNm4": "t", "p832": "u", "Ty92": "ü", "p4fH": "v",
                             "hUtR": "y", "0Lhm": "z", "mJ5d": "0", "d8Wk": "1", "p6FB": "2", "tqRB": "3", "BBq8": "4",
                             "fJh6": "5", "iI8H": "6", "9TnB": "7", "BhJk": "8", "oLtN": "9", "TqV5": " "}

    uncryption_keys = list(uncryption_dictionary.keys())

    for letters_to_component in crypted_string:
        uncryption_group = uncryption_group + letters_to_component
        total_count = len(crypted_string)
        if total_count <= total_count:
            if len(uncryption_group) == 4:
                uncryption_group_list.append(uncryption_group)
                uncryption_group = ""
        else:
            break

    for groups_to_uncryption in uncryption_group_list:
        if groups_to_uncryption in uncryption_keys:
            uncrypted_group = uncryption_dictionary[groups_to_uncryption]
            uncrypted_string = uncrypted_string + uncrypted_group
        else:
            continue

    return uncrypted_string


def string_uncryption_password_main(collected_string, collected_password):
    crypted_string = str(collected_string)
    main_password = str(collected_password)

    uncryption_group = str()
    uncrypted_string = str()
    uncryption_group_list = list()
    crypted_password = str()
    crypted_main_password = "A9B8"
    cryption_letter_list_for_main_password = list()

    uncryption_dictionary = {"aYz1": "A", "zC34": "B", "bQw2": "C", "nIu2": "Ç", "p34R": "D", "rS23": "E", "PiQ1": "E",
                             "cK23": "G", "zZx1": "Ğ", "xWe1": "H", "9eQx": "I", "pQ23": "İ", "Zz94": "J", "xJ67": "K",
                             "yVmN": "L", "LpR5": "M", "aEzQ": "N", "bP53": "O", "oF61": "Ö", "cCvQ": "P", "eEmQ": "R",
                             "pbQS": "S", "cQrR": "Ş", "cqR2": "T", "zCv2": "U", "1x2q": "Ü", "q2Q1": "V", "vQ3T": "Y",
                             "t2Qz": "Z", "iO21": "a", "aPq2": "b", "qPu2": "c", "ZcAp": "ç", "z23Q": "d", "bRst": "e",
                             "fxNY": "f", "lzR2": "g", "mpR6": "ğ", "tQ20": "h", "oX3R": "ı", "45Zv": "i", "3TbG": "j",
                             "gRf8": "k", "s0Tr": "l", "nQ85": "m", "b6Re": "n", "G8qV": "o", "Zrt2": "ö", "pRtB": "p",
                             "fF21": "r", "zQ4F": "s", "fY67": "ş", "oNm4": "t", "p832": "u", "Ty92": "ü", "p4fH": "v",
                             "hUtR": "y", "0Lhm": "z", "mJ5d": "0", "d8Wk": "1", "p6FB": "2", "tqRB": "3", "BBq8": "4",
                             "fJh6": "5", "iI8H": "6", "9TnB": "7", "BhJk": "8", "oLtN": "9", "TqV5": " "}

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

    uncryption_keys = list(uncryption_dictionary.keys())

    string_or_pasword = 0

    for letters_to_append_for_main_password_cryption in main_password:
        cryption_letter_list_for_main_password.append(letters_to_append_for_main_password_cryption)

    for letters_to_cryption_in_cryption_letter_list in cryption_letter_list_for_main_password:
        if letters_to_cryption_in_cryption_letter_list in cryption_keys:
            crypted_letter = cryption_dictionary[letters_to_cryption_in_cryption_letter_list]
            crypted_main_password = crypted_main_password + crypted_letter

    for letters_to_component in crypted_string:
        uncryption_group = uncryption_group + letters_to_component
        total_count = len(crypted_string)
        if total_count <= total_count:
            if len(uncryption_group) == 4:

                if uncryption_group == "A9B8":
                    string_or_pasword = 1

                if string_or_pasword == 0:
                    uncryption_group_list.append(uncryption_group)
                    uncryption_group = ""
                else:
                    crypted_group = uncryption_group
                    crypted_password = crypted_password + crypted_group
                    uncryption_group = ""
        else:
            string_or_pasword = 0
            break

    if crypted_main_password == crypted_password:
        for groups_to_uncryption in uncryption_group_list:
            if groups_to_uncryption in uncryption_keys:
                uncrypted_group = uncryption_dictionary[groups_to_uncryption]
                uncrypted_string = uncrypted_string + uncrypted_group
            else:
                continue
    else:
        uncrypted_string = "PASSWORDS DOESNT MATCH"

    print(crypted_main_password)
    print(crypted_password)
    return uncrypted_string
