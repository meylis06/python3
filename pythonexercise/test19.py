from sys import argv

script, filename= argv

metin= open(filename)

print(f"And here we go. {filename}")

print(metin.read())
