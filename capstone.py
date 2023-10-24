import pandas as dan
import plotly.express as ex

frame = dan.read_csv("info.csv")
figu = ex.line(frame, x = "date", y = "cases", color = "country")
figu.show()