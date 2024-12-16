from remove_exclamation import remove

tests = ["Hi!", "Hi!!!", "!Hi", "!Hi!", "Hi! Hi!", "Hi", ""]
for test in tests:
    print(remove(test))