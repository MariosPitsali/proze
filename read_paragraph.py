with open("paragraph.txt", "r") as paragraph:
    contents = list(paragraph)
sentences = contents[0].split(".")
sent = []
for item in sentences:
    sent.append(item)
    
for i in range(len(sent)):
    print ("Another sentence:" + sent[i] + ".\n")