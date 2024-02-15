## Instagram Scraper

Hi There!

In this repository, you will find a simple Python Script to scrape Instagram posts from any public account. 

Just install the requirements and follow the steps. Hope it can help you. 

First, to download images posts from a public Instagram account, run the code below. You need to pass, besides the user account name, the date range you want to grab the files. Make sure to pass all required arguments in the correct format.

```python
python src/scraping.py -since 2023-12-15 -until 2024-1-1 -user <user_account>
```

Once the files was downloaded, go make our lives easier, navigate (```cd <user_account>``` for Unix-based systems) to the folder the files was stored --- here it will always be the user account name --- and execute the command below.  

It will generate a .csv file where you will find the publication content, associated image path, and the publication date. 


```python
python ../src/preprocessing.py -output ../test.csv
```

Finally, you can build a .txt file from the csv running the following script. << **IMPORTANT** >> if you executed previous command, navigate back last folder (```cd ..```).

It will output a .txt file containing all post's descripiton separated by a HEADER which is the post' publication date. 

```python
python src/csv_to_txt.py -input_file test_file.csv -output test_result.txt
```

