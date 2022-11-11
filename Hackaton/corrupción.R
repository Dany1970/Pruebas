library(readxl)
datos <- read_excel("Indice de percepcion de corrupcion.xlsx")
ggplot(data = datos, aes(x=Año, y=Indice, group = País, colour =País )) + 
  geom_line()  + 
  geom_point( size=2, shape=21, fill="white") + 
  theme_minimal()
