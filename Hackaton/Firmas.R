library(readxl)
datos5 <- read_excel("Universidad Digital 4.0 (respuestas).xlsx", 
                                                  sheet = "Firmas")

porcentaje <- datos5 %>%
  group_by(Firmas) %>%
  count() %>%
  ungroup() %>%
  mutate(percentage=`n`/sum(`n`) * 100)

ggplot(porcentaje, aes(x=1, y=percentage, fill=Firmas)) +
         geom_bar(stat="identity") +
         geom_text(aes(label = paste0(round(percentage,1),"%")), 
                   position = position_stack(vjust = 0.5)) +
         coord_polar(theta = "y") + 
  ggtitle("Firmas diagitales y datos biométricos") +
         theme_void() + scale_fill_brewer(palette = "Blues")
