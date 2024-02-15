import pandas as pd
import argparse

HEADER_LEN = 20
HEADER = "{markers} >>> {date} <<< {markers}\n\n"
BOTTOM_LINE = "\n"

def command_line_parsing():

    parser = argparse.ArgumentParser(description = __doc__)
    
    parser.add_argument('--input_file', '-input_file', 
                        dest='input_file', 
                        required=True,
                        help='Path to the .csv file you want to convert.',
                        default='./csv_output.csv')

    parser.add_argument('--output', '-output', 
                        dest='output', 
                        required=False,
                        help='Path where you want to store the .txt file will be generated and the txt file name.',
                        default='./txt_output.txt')
    
    return parser.parse_args()


def main():
    
    args = command_line_parsing()
    
    dataframe = pd.read_csv(args.input_file)
    
    with open(args.output, "a") as file:
        
        for row in dataframe.itertuples():
            file.write(HEADER.format(markers="="*HEADER_LEN, date=row.post_date))
            file.write(row.post)
            file.write(BOTTOM_LINE)
            
        file.close()
    
    pass

if __name__ == "__main__":
        
    main()