from glob import glob
import pandas as pd
from datetime import datetime

DATE_FORMAT= '%Y-%m-%d_%H-%M-%S'
ROOT_FOLDER = ''#'./ariellepedrosa/'

def main():
    
    files = glob(ROOT_FOLDER + "*")    
    dataframe = pd.DataFrame({"file_name":files})
    
    dataframe["post_id"] = dataframe.file_name.apply(lambda file_name: file_name.split("_UTC")[0])
    dataframe["file_extention"] = dataframe.file_name.apply(lambda file_name: file_name.split(".")[1])
    
    
    # Removing video description
    txt_set = set(dataframe[dataframe.file_name.str.contains(".txt")].post_id)
    img_set = set(dataframe[dataframe.file_name.str.contains(".jpg")].post_id)
    
    symm_diff = txt_set.symmetric_difference(img_set)
    dataframe = dataframe[~dataframe.post_id.isin(symm_diff)]
    
    # Adding post's text to dataframe and date
    
    date_ = []
    post_ = []
    imgs_ = []
    meta_data_ = []
    
    for post_id in txt_set:
        
        try:
        
            date_.append(datetime.strptime(post_id, DATE_FORMAT))
            imgs_.append(dataframe.file_name[(dataframe.file_extention == 'jpg') & (dataframe.post_id == post_id)].to_list())
            # meta_data_.append(dataframe.file_name[(dataframe.file_extention == 'json') & (dataframe.post_id == post_id)].to_list())
            
            post_file = open(post_id + "_UTC.txt", "r")
            post = post_file.read()
            post_.append(post)
            
        except Exception as e:
            print('Error on file :: {}'.format(e))
            
    final_dataframe = pd.DataFrame({
        "post_id" : list(txt_set),
        "post_date" : date_,
        "post_images" : imgs_,
        # "meta_data" : meta_data_,
        "post" : post_
    })
    
    final_dataframe.sort_values(by="post_date", ascending=False, inplace=True)
    final_dataframe.to_csv('../arielle_posts.csv', index=False)
    
    


if __name__ == "__main__":
    
    main()