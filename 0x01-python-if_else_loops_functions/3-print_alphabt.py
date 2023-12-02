  GNU nano 4.8                                                              2-print_alphabet.py                                                                         #!/usr/bin/python3
for i in range(ord('a'), ord('z') + 1):
	if i == 'q' or 'e':
	continue
        print("(:c)".format(i), end "")
