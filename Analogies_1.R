library(ggplot2)
library(corrgram)

# importo los datos desde un csv
datos <-  read.csv("Data/CSV/Analogies_1.csv", header = TRUE)

# Gráficos sencillos
boxplot(datos$X.Women..valores., data=datos, main="+ women - men", col=rainbow(10, alpha=0.2))
boxplot(datos$X.Men..valores., data=datos, main="+ men - women", col=rainbow(10, alpha=0.2))
boxplot(datos$X.Japan..valores, data=datos, main="+ japan - tokio", col=rainbow(10, alpha=0.2))
boxplot(datos$X.Tokio..valores., data=datos, main="+ tokio - japan", col=rainbow(10, alpha=0.2))

boxplot(datos$X.Women..valores., datos$X.Men..valores., datos$X.Japan..valores, 
        datos$X.Tokio..valores.,  data=datos, main="", col=rainbow(10, alpha=0.2),
        main="Cuatro distribuciones",
        names=c("+ women - men", "+ men - women", "+ japan - tokio", "+ tokio - japan"))

# + women - men
datos_mujeres <- datos$X.Women..valores.
# + men - women
datos_hombres <- datos$X.Men..valores.
# + japan - tokio
datos_japan <- datos$X.Japan..valores.
# + tokio - japan
datos_tokio <-  datos$X.Tokio..valores.

summary(datos_mujeres)
summary(datos_hombres)
summary(datos_japan)
summary(datos_tokio)
# observemos lo parecidas que son las medias

qplot(datos_mujeres, geom="histogram") 
qplot(datos_hombres, geom="histogram")
qplot(datos_japan, geom="histogram")
qplot(datos_tokio, geom="histogram")



# Correlaciones:
# =============

datos_numericos <- data.frame(datos_mujeres, datos_hombres, datos_japan, datos_tokio)

corrgram(datos_numericos, order=TRUE, lower.panel=panel.shade,
         upper.panel=NULL, text.panel=panel.txt,
         main="")
