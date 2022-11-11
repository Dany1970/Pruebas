library(readxl)
datos <- read_excel("Universidad Digital 4.0 (respuestas).xlsx", 
                    sheet = "Distribución de la muestra")
View(Universidad_Digital_4_0_respuestas_)
ggplot(data = datos, aes(x = Categoría, fill = as.factor(Categoría))) +
  geom_bar() +
  xlab("categoría") +
  ylab("Cantidades") +
  ggtitle("Distribución de la muestra") +
  labs(fill = "Categorías") +
  theme_minimal()

