import socket

# encrypt = {
#
# }
# import random
# letters = "abcdefghijklmnopqrstuvwxyz1234567890"
#
# def GenerateRandomString(letter, dict):
#
#     GeneratedString = "".join([random.choice(letters) for i in range(6)])
#     if GeneratedString in dict.values():
#         GeneratedString(letter, dict)
#     else:
#         dict[letter] = GeneratedString
#
# for i in letters:
#     GenerateRandomString(i, encrypt)
#
# print(encrypt)

# encryption = {'a': 'cgxmr5', 'b': 'p61ksb', 'c': 'vy7y2i', 'd': '85qyp6', 'e': 'mrwtv1', 'f': 'ld26qd', 'g': 'y7azjm',
#               'h': 'cssr8c', 'i': 'b6u3cq', 'j': 'h3hoy3', 'k': 'j8iyt6', 'l': 'fuyqvm', 'm': 'mp2qd4', 'n': 'm2yfka',
#               'o': 'gkm63u', 'p': 'vv75k4', 'q': 'pjgcpp', 'r': 'n0qvhu', 's': 'uk4nc9', 't': '5eebui', 'u': 'ulvvmn',
#               'v': 'lne008', 'w': '7gewba', 'x': 'krgjkm', 'y': '0vtpbz', 'z': 'cjvu39', '1': 'o1xf3q', '2': 'r9t7qi',
#               '3': '5isjif', '4': '9rpugk', '5': 'ffxb83', '6': 'xd325a', '7': 'rw5wfl', '8': 'ha7t44', '9': 'ak5a6r',
#               '0': '621qv1', " ": " "}
#
# new = {}
#
# for key, value in encryption.items():
#     new[value] = key
#
# print(new)
#
# string ="abcdefghijklmnopqrstuvwxyz1234567890"
# for i in string:
#     print(f"if event.key == pygame.K_{i}:\n\treturn str('{i}')")

print(socket.gethostbyname(socket.gethostname()))