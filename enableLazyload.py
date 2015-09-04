import os

def injectImgClass(file):
    lines = []
    rewrite_lines = []
    rewrite_numbers = []
    new_lines = []
    count = 0
    with open(file, "r") as f:
        for line in f:
            if "<img" in line:
                if not "id=" in line:
                    print line
                    rewrite_lines.append(line)
                    rewrite_numbers.append(count)
            count = count + 1
            lines.append(line)

    if len(rewrite_lines) == 0:
        return False

    for line in rewrite_lines:
        sp = line.split("<img")
        new = sp[0] + '<img class="lazy img-responsive"' + sp[1]
        sp = new.split("src=")
        new = sp[0] + 'data-original=' + sp[1]
        new_lines.append(new)
        print new

    for i, num in enumerate(rewrite_numbers):
        lines[num] = new_lines[i]        

    with open(file, "w") as f:
        f.writelines(lines)

    return True

path = "../output"

for root, dirs, files in os.walk(path):
    for file in files:
        if os.path.splitext(file)[1] == ".html":
            if injectImgClass(os.path.join(root, file)):
                print os.path.join(root, file)
