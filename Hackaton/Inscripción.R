library(readxl)
datos3<- read_excel("Universidad Digital 4.0 (respuestas).xlsx", 
                                                  sheet = "Inscripción Online")
View(datos3)
ggplot(data = datos3,  aes(x = Inscripcion,fill = as.factor(Inscripcion))) +
  geom_bar() +
  xlab("Inscripción online") +
  ylab("Frecuencia") +
  ggtitle("Trámite de inscripción totalmente online") +
  labs(fill = "Inscripcion") +
  theme_minimal()
