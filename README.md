## Instagram Scraper

Hi There!

In this repository, you will find a simple Python script to scrape Instagram posts from any public account. 

Just install the requirements and follow the steps below. Hope it can help you. 

---
---

First, to download posts and its associated images from a public Instagram account, run the code below. You need to pass, besides the user account name, the date ranges you want to grab the files. Make sure to pass all the required arguments in the correct format.

```python
python src/scraping.py -since 2023-12-15 -until 2024-1-1 -user <user_account>
```

Once the files were downloaded, to make our lives easier, navigate (``` cd <user_account>``` for Unix-based systems) to the folder where the files were stored --- here it will always be the user account name --- and execute the command below.  

```python
python ../src/preprocessing.py -output ../test.csv
```

It will generate a .csv file where you will find the publication content, associated image path, and the publication date. 


Finally, you can build a .txt file from the CSV running the following script. << **IMPORTANT** >> If you executed the previous command, navigate back to the last folder (``` cd ..```).

It will output a .txt file containing all posts' descriptions, separated by a header, which is the post's publication date. 

```python
python src/csv_to_txt.py -input_file test_file.csv -output test_result.txt
```