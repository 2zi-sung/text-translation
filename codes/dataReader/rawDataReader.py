import pandas as pd
import os

class RawDataReader:
    def __init__(self, data_path):
        self.data_path = data_path
    
    def loadSingleRawData(self, filename):
        file_path = os.path.join(self.data_path, filename)

        if filename.endswith('.xlsx'):
            raw_data_df = pd.read_excel(file_path)
        elif filename.endswith('.csv'):
            raw_data_df = pd.read_csv(file_path)

        single_raw_data_df = [(raw_data_df, filename)]
        
        return single_raw_data_df
    
    def loadMultipleRawData(self):
        multiple_raw_data_df = []

        for file_name in os.listdir(self.data_path):
            if file_name.endswith('.xlsx') or file_name.endswith('.csv'):
                file_path = os.path.join(self.data_path, file_name)

                if file_name.endswith('.xlsx'):
                    raw_data_df = pd.read_excel(file_path)
                elif file_name.endswith('.csv'):
                    raw_data_df = pd.read_csv(file_path)

                multiple_raw_data_df.append((raw_data_df, file_name))

        return multiple_raw_data_df