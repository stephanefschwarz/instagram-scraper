import pandas as pd

HEADER_LEN = 20
HEADER = "{markers} >>> {date} <<< {markers}\n\n"
BOTTOM_LINE = "\n"


def main():
    
    dataframe = pd.read_csv("arielle_posts.csv")
    
    with open("arielle_txt_posts.txt", "a") as file:
        
        for row in dataframe.itertuples():
            file.write(HEADER.format(markers="="*HEADER_LEN, date=row.post_date))
            file.write(row.post)
            file.write(BOTTOM_LINE)
            
        file.close()
    
    pass

if __name__ == "__main__":
    
    main()