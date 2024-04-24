import pandas as pd 
import plotly.express as px
df = pd.read_csv("train.csv")


for cols in df.columns:
    print(cols)


hist_region = px.histogram(df,x = "region_category")
#hist_region.show()

complaint_hist = px.histogram(df, x = "complaint_status")
#complaint_hist.show()

churn_avg_time_scatter = px.scatter(df,x = "avg_time_spent", y = "churn_risk_score")
churn_avg_time_scatter.show()

df_grouped = df.groupby("complaint_status")["churn_risk_score"].mean()
print(df_grouped)