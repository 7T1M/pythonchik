from string_formatter import StringFormatter

formatter = StringFormatter()

str = "fhfh fjdfjfdj djfwkfjsjfdsf iwdfjwif jfjf dskfsdfsfj kfsl"

print(formatter.delete_words(str,5))

str1 = "password123 djfdifj3dof"

print(formatter.swap_digits(str1))

str2 = "kwefimfwmfwimfiwmfiwmf dkdcmkd"

print(formatter.split_for_every_symbol(str2))

str3 = "fjfldvm vmbngh vnmbf cmvn gbj kl o"

print(formatter.sort_for_word_len(str3))

str4 = "hello this is example how to sort the word in alphabetical manner"

print(formatter.sort_for_lexicographic(str4))

