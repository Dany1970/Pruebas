library(readxl)
datos2 <- read_excel("Universidad Digital 4.0 (respuestas).xlsx", 
                                                  sheet = "Capacitación")
View(datos2)
ggplot(data = datos2, aes(x = Capacitación1 , y = Audience.Ratings..)) +
  geom_point(aes(color = Genre), size = 1, alpha = 0.7) +
  xlab('Género') +
  ylab('Puntuación de la Audiencia') +
  ggtitle('Puntuación de la Audiencia según el Género') +
  theme_minimal()