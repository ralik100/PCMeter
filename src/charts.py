import pandas as pd
import log_parser
import matplotlib.pyplot as plt



def to_chart():
    plt.style.use("seaborn-v0_8")
    data=log_parser.log_parser("log.txt")

    df=pd.DataFrame(data)
    df["Time"]=pd.to_datetime(df["Time"])
    print(df)
    df.set_index("Time", inplace=True)
    df_wide = df.pivot(index="Time", columns="metric", values="usage")
    df_wide.plot()

    plt.title("Usage", fontsize=20)
    plt.xlabel("Time", fontsize=15)
    plt.ylabel("Usage in percent", fontsize=15)

    plt.grid(True, linestyle="--", alpha=0.6)
    plt.legend(loc="upper left")

    plt.xticks(rotation=45)
    plt.show()


to_chart()

