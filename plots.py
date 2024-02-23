
from typing import List

import matplotlib.pyplot as plt
from datetime import datetime
def create_time_plt(name: str, timings: List[List[int]], vertical_line_x: datetime = None, vertical_line_msg: str = None):
    
    # print(timings);
    # print(type(vertical_line_x))

    plt.figure(figsize=(24, 12))
    x_values, y_values = zip(*timings)
    if vertical_line_x is not None:  
        plt.axvline(x=datetime.strptime(vertical_line_x, "%Y-%m-%d"), color='r', linestyle='--', label=vertical_line_msg)
        plt.text(vertical_line_x, max(y_values), vertical_line_msg, rotation=90, verticalalignment='bottom', ha='right')
    plt.title(name)
    plt.xlabel("Workflow Run Dates")
    plt.ylabel("Duration in Minutes")
    plt.scatter(x_values, y_values)
    print(type(x_values[1]))
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.legend()
    date_str = datetime.now().strftime("%d-%m-%Y")
    plt.savefig(f'./{name}-{date_str}')
    #plt.savefig(f'./{self.repo}-{name}-{date_str}')
