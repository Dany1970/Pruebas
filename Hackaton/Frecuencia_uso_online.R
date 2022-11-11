library(readxl)
datos1 <- read_excel("Universidad Digital 4.0 (respuestas).xlsx", 
                                                  sheet = "frecuencia tramites online")
ggplot(data = datos1,  aes(x = Frecuencia, fill = as.factor(Frecuencia))) +
  geom_histogram(binwidth = 1) + 
  xlab("Trámites online") +
  ylab("Frecuencia") +
  ggtitle("Frecuencia de uso de trámites en línea: 1. Nunca a 5. Siempre") +
  labs(fill = "Frecuencia") +
  theme_minimal()
