import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import os, json
from datetime import datetime

INPUT_FILE = "historicalPrices.json"
OUTPUT_IMAGE = "chart.png"
ASSETS = '/assets/'

def read_json_file(file_name, file_loc = ASSETS ):
    with open(os.path.join(file_loc, file_name), 'r') as f:
        return json.load(f)
    
def create_plot(json_data, columns_to_plot=['Close'],  xlabel='Date', 
                ylabel='Value', title='Historical Prices',  date_format='%b %Y', 
                xtick_rotation=45,  save_path=None, grid_style='--',
                grid_visibility: bool=False, yticks_count:int = None, xticks_month_interval:int = 1,  ):
    fig, ax = plt.subplots(figsize=(12, 8))

    dates = [datetime.strptime(item['Date'], "%Y-%m-%d") for item in json_data]
    
    for col in columns_to_plot:
        values = [item[col] for item in json_data]
        plt.plot(dates, values, label=col)

    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    
    xmin = dates[0]
    xmax = dates[-1]
    # print(xmin, '  ', xmax)
    x_len = (xmax - xmin).days

    if xticks_month_interval is not None and (x_len // 30) > 3:
        if xticks_month_interval < 12:
            ax.xaxis.set_major_locator(mdates.MonthLocator(interval=xticks_month_interval))
            ax.xaxis.set_major_formatter(mdates.DateFormatter(date_format)) 
        else:
            ax.xaxis.set_major_locator(mdates.YearLocator())
    plt.xticks(rotation=xtick_rotation)
    
    if yticks_count:
        ax.locator_params(axis='y', nbins=yticks_count)    

    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    
    if len(columns_to_plot) > 1:
        ax.legend()

    if grid_visibility:
        plt.grid(grid_visibility, linestyle=grid_style,)
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, dpi=300)  
        
    return fig  

if __name__ == '__main__':
    json_data = read_json_file(INPUT_FILE, '.')
    print('Ram Sita')
    create_plot(json_data)