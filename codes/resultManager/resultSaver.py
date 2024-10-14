import pandas as pd
import os

class ResultSaver:
    def __init__(self, save_folder_path):
        self.save_folder_path = save_folder_path

    def save(self, df, file_name, flag):
        if flag == 'excel':
            file_path = os.path.join(self.save_folder_path, f"{file_name}.xlsx")
            df.to_excel(file_path, index=False)
        elif flag == 'csv':
            file_path = os.path.join(self.save_folder_path, f"{file_name}.csv")
            df.to_csv(file_path, index=False, encoding = "cp949")
        else:
            raise