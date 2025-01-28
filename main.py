from src.dtw_lab.lab1 import read_csv_from_google_drive, visualize_data, calculate_statistic, clean_data

if __name__ == '__main__ ':
    df = read_csv_from_google_drive ( '1eKiAZKbWTnrcGs3bqdhINo1E4rBBpglo ')
    print(df)
    df = clean_data ( df )
    visualize_data ( df )
    print ( f'The mean value for the charge left percentage is{ calculate_statistic( 'mean ',df[' Charge_Left_Percentage '])}')
