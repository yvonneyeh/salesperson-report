"""Generate sales report showing total melons each salesperson sold."""

def get_melons_sold_by_salesperson(filename):
    """ Return a dictionary of {salesperson_name : melons_sold}
    """
    mels_by_sales = {}  # create empty dictionary

# create context manager, open the file and call it "f"
# with = python closes file at the end of code block
    with open(filename) as f:   
        for line in f:      # loop through every line in the text file
            line = line.rstrip()    # strip whitespace on right side of lines
            
            # separate entries by vertical bar, create a list of data and unpack its values
            salesperson_name, total_dollars, melons_sold = line.split('|')  
            
            # salesperson = entries[0]    # 1st entry (index 0) is salesperson
            # melons = int(entries[2])    # 3rd entry (index 2) is melons, convert to integer

            if salesperson_name in mels_by_sales:      # if the person exists in the dictionary of salespeople
                mels_by_sales[salesperson_name] += int(melons_sold)   # add to salesperson's total melons sold

            else:
                mels_by_sales[salesperson_name] = int(melons_sold)     # if the person doesn't exist in the dictionary, add them
    return mels_by_sales

def print_sales_report(melons_sold_by_salesperson):
    """ Print a report of salespeople and the total number of melons they've sold

        Arguments:
            melons_sold_by_salesperson (dict) = {salesperson_name : melons_sold}
    """
    for salesperson_name, melons_sold in melons_sold_by_salesperson.items():
        print(f'{salesperson_name} sold {melons_sold} melons')


print_sales_report(get_melons_sold_by_salesperson('sales-report.txt'))