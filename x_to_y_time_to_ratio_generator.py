with open(input("Enter results.txt full path: "),"r") as resultstxt, open("xy.txt","w") as xytxt:
    for i in resultstxt.readlines()[1:]:# first line is hint, skipping it
        xytxt.write(f"{float(i.split('|')[1])},{float(i.split('|')[-1])}\n")

