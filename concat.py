filenames = ['./csv/pm2_5.csv',
            './csv/co.csv', 
            './csv/no2.csv',
            './csv/o3.csv',
            './csv/so2.csv']
with open('./csv/data.csv', 'w') as outfile:
    with open(filenames[0]) as infile:
        line_no = len(infile.readlines())  # Number of line in pm2.5 file
    with open('./csv/data.csv', 'w') as outfile:
        for i in range(line_no):
            for file in filenames:
                with open(file) as infile:
                    lines=infile.readlines()
                    if i >= len(lines): # Check if line exists
                        outfile.write("," + "null")
                        continue
                    line = lines[i].strip() # remove new line character
                    print(line)
                    if file == filenames[0]: 
                        outfile.write(line)
                    elif file == filenames[-1]:
                        outfile.write("," + line.split(",")[-1] + "\n")
                    else:
                        outfile.write("," + line.split(",")[-1])
                    