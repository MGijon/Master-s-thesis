library(ggplot2)
library(corrgram)

# importo los datos desde un csv
datos <-  read.csv("Data/CSV/Analogies_Questions.csv", header = TRUE)

boxplot(datos$Who, datos$Why, datos$Where, datos$When, datos$What, datos$How, 
        datos$Whom,  data=datos, main="", col=rainbow(10, alpha=0.2),
        main="",
        names=c("+ Who - thing", "Why - thing", "Where - thing", "When - thing", "What - thing", "How - thing", "Whom - thing"))

summary(datos$Who)
summary(datos$Why)
summary(datos$Where)
summary(datos$When)
summary(datos$What)
summary(datos$How)
summary(datos$Whom)

# Correlaciones:
# =============

datos_numericos <-  data.frame(datos$Who, datos$Why, datos$Where, datos$When, datos$What, datos$How, datos$Whom)

corrgram(datos_numericos, order=TRUE, lower.panel=panel.shade,
         upper.panel=NULL, text.panel=panel.txt,
         main="")


