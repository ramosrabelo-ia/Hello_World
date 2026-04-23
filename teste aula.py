import pandas as pd
import sweetviz as sv

#Com um data frame simples
alturas = [150, 160, 165, 170, 175, 180, 185, 210, 156, 173, 188, 170, 168, 167]
df = pd.DataFrame(alturas, columns=["Altura (cm)"])
print(df)
#Sweetviz
report = sv.analyze(df)
report.show_html("sweetviz_report.html")
print("EDA report generated: sweetviz_report.html")

#com o dataframe de carro
df = pd.read_csv("Cars Data.csv")

report = sv.analyze(df)
report.show_html("sweetviz_car_report.html")
print("EDA report generated: sweetviz_report.html")