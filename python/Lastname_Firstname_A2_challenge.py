import numpy as np 

def is_sheet_usable(sheet):
    if type(sheet) != type(np.array([])):
        raise TypeError("Type of sheet is not numpy.ndarray")
    if sheet.shape != (100,100):
        raise ValueError("Shape of the sheet is not 100x100")
    values = np.unique(sheet)
    if len(values) > 2:
        raise ValueError("The sheet cntains values other than 0 and 1")
    if len(values) == 2 and ((0 not in values) or (1 not in values)):
        raise ValueError("The sheet cntains values other than 0 and 1")
    if len(values) == 1 and ((0 not in values) and (1 not in values)):
        raise ValueError("The sheet cntains values other than 0 and 1")
        
    if np.sum(sheet) > 8:
        return False
    
    for i in range(1,99):
        for j in range(1,99):
            subarray = sheet[i-1:i+2,j-1:j+2]
            if np.sum(subarray) > 4:
                return False
    return True
    
        
import pandas as pd
import os 

def combine_csv_files(directory, output_filename):
    list_of_dataframes = []
    for file in os.listdir(directory):
        if file.endswith('.csv'):
            try:
                df = pd.read_csv(directory+os.sep+file, index_col=('key'))
                list_of_dataframes.append(df)
            except:
                pass
    df_result = pd.concat(list_of_dataframes, axis=0)
    columns_to_be_dropped = []
    for column in df_result.columns:
        if df_result[column].isna().sum() > 0.5*len(df_result[column]):
            columns_to_be_dropped.append(column)
    df_result = df_result.drop(columns_to_be_dropped, axis='columns')
    df_result = df_result.sort_index(axis=1)
    df_result = df_result.sort_index(axis=0)
    df_result.to_csv(output_filename)
    
    
import matplotlib.pyplot as plt

def make_html_files():
    
    def create_html_template(name_of_dataset, previous, nextt, dataframe_html, image):
        if previous==None and nextt==None:
            template = f'<html><body>\n<h1>{name_of_dataset}</h1>\n{dataframe_html}\n<img src="{name_of_dataset}.png">\n</body></html>'
            return template
        if previous==None:
            template = f'<html><body>\n<h1>{name_of_dataset}</h1>\n<p>\nNext: <a href="{nextt}.html">{nextt}</a>\n</p>\n{dataframe_html}\n<img src="{name_of_dataset}.png">\n</body></html>'
            return template
        if nextt==None:
            template = f'<html><body>\n<h1>{name_of_dataset}</h1>\n<p>\nPrevious: <a href="{previous}.html">{previous}</a>\n</p>\n{dataframe_html}\n<img src="{name_of_dataset}.png">\n</body></html>'
            return template
        template = f'<html><body>\n<h1>{name_of_dataset}</h1>\n<p>\nPrevious: <a href="{previous}.html">{previous}</a>\nNext: <a href="{nextt}.html">{nextt}</a>\n</p>\n{dataframe_html}\n<img src="{name_of_dataset}.png">\n</body></html>'
        return template
    
    def save_plot_to_image(directory, name, df):
        for column in df.columns:
            plt.plot(df[column], label=column)
        plt.title(name)
        plt.legend()
        plt.savefig(directory+os.sep+name+'.png')
        plt.clf()
    
    directory = 'htmlplots'
    with open(directory+os.sep+'index.txt',mode='r') as index_file:
        files = index_file.read().splitlines()
        for i in range(len(files)):
            file = os.path.splitext(files[i])[0]
            df = pd.read_csv(directory+os.sep+files[i])
            save_plot_to_image(directory, file, df)
            df_html = df.to_html(index=False)
            template = ""
            if i == 0:
                if len(files) == 1:
                    template = create_html_template(file, None, None, df_html, file)
                else:
                    template = create_html_template(file, None, os.path.splitext(files[i+1])[0], df_html, file)
            elif i == len(files)-1:
                template = create_html_template(file, os.path.splitext(files[i-1])[0], None, df_html, file)
            else:
                template = create_html_template(file, os.path.splitext(files[i-1])[0], os.path.splitext(files[i+1])[0], df_html, file)
            with open(directory+os.sep+file+'.html',mode='w') as html_file:
                    html_file.write(template)