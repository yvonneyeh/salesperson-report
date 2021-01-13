"""Generate sales report showing total melons each salesperson sold."""

# create empty lists for salespeople and melons sold
salespeople = [] 
melons_sold = []

# open the file and name it file
f = open('sales-report.txt')

# loop through every line in the text file
for line in f:
    line = line.rstrip()    # strip whitespace on right side of lines
    entries = line.split('|')   # create entries separated by vertical bar

    salesperson = entries[0]    # 1st entry (index 0) is salesperson
    melons = int(entries[2])    # 3rd entry (index 2) is melons, convert to integer

    if salesperson in salespeople:      # if the person exists in the list of salespeople
        position = salespeople.index(salesperson)   # the position is the index in the list

        melons_sold[position] += melons     # add 1 to melons_sold index postion every time you iterate
    else:
        salespeople.append(salesperson)     # if the person doesn't exist in the list, add them
        melons_sold.append(melons)          # same for melons sold


for i in range(len(salespeople)):           # for each number in the range of the length of the salespeople list
    print(f'{salespeople[i]} sold {melons_sold[i]} melons')     #print this statement
