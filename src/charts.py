import pandas as pd
import log_parser
import matplotlib.pyplot as plt



def to_chart(log_file_path):
    plt.style.use("seaborn-v0_8")
    data=log_parser.log_parser(log_file_path)

    df=pd.DataFrame(data)
    print(df.columns)
    print(df.head())
    df["Time"]=pd.to_datetime(df["Time"])
    
    df_wide = df.pivot(index="Time", columns="Metric", values="Usage")
    df.set_index("Time", inplace=True)
    

    df_wide.plot()

    plt.title("Usage", fontsize=20)
    plt.xlabel("Time", fontsize=15)
    plt.ylabel("Usage in percent", fontsize=15)

    plt.grid(True, linestyle="--", alpha=0.6)
    plt.legend(loc="upper left")

    plt.xticks(rotation=45)
    plt.show()


to_chart("log.txt")

