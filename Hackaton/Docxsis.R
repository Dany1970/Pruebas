datos4<- read_excel("Universidad Digital 4.0 (respuestas).xlsx", 
                                                  sheet = "Documentación por sistema")
ggplot(data = datos4,  aes(x = Sistema,fill = as.factor(Sistema))) +
  geom_bar() +
  labs(fill = "") +
  theme_minimal()
