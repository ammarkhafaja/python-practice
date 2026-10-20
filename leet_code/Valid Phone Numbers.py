# Read from the file file.txt and output all valid phone numbers to stdout.
file=open ("file1.txt","r")
for line in file:
    line = line.strip()
    if line in ("(---) ---/----", "---/----/----"):
        print(line)
