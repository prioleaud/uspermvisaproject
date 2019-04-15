library(readxl)
library(normalr)
library(cluster)

#setwd("~/Courses/STA6707/Project/")
setwd("/Users/kianamac/Documents/GitHub/uspermvisaproject/")
#=========================== Reading files ===============================#  

#data <- read.csv("clean_data.csv", sep = ',' , header = TRUE)
clustering <- function(data){
anyNA(data)

#=========================== Hierarchical Methods ===============================#  

#Single-Linkage
uspermvisa_sgl = agnes(data,diss = F, metric = "euclidean", stand = F, method = "single")
grp <- cutree(uspermvisa_sgl,k=3)
table(grp)

grp <- cutree(uspermvisa_sgl,k=4)
table(grp)

grp <- cutree(uspermvisa_sgl,k=5)
table(grp)

grp <- cutree(uspermvisa_sgl,k=6)
table(grp)

grp <- cutree(uspermvisa_sgl,k=7)
table(grp)

grp <- cutree(uspermvisa_sgl,k=8)
table(grp)

grp <- cutree(uspermvisa_sgl,k=9)
table(grp)

grp <- cutree(uspermvisa_sgl,k=10)
table(grp)

grp <- cutree(uspermvisa_sgl,k=11)
table(grp)

grp <- cutree(uspermvisa_sgl,k=12)
table(grp)

#Complete Linkage
uspermvisa_com = agnes(data,diss = F, metric = "euclidean", stand = F, method = "complete")
grp <- cutree(uspermvisa_com,k=3)
table(grp)

grp <- cutree(uspermvisa_com,k=4)
table(grp)

grp <- cutree(uspermvisa_com,k=5)
table(grp)

grp <- cutree(uspermvisa_com,k=6)
table(grp)

grp <- cutree(uspermvisa_com,k=7)
table(grp)

grp <- cutree(uspermvisa_com,k=8)
table(grp)

grp <- cutree(uspermvisa_com,k=9)
table(grp)

grp <- cutree(uspermvisa_com,k=10)
table(grp)

grp <- cutree(uspermvisa_com,k=11)
table(grp)

grp <- cutree(uspermvisa_com,k=12)
table(grp)

#Average
uspermvisa_avg = agnes(data,diss = F, metric = "euclidean", stand = F, method = "average")
grp <- cutree(uspermvisa_avg,k=3)
table(grp)

grp <- cutree(uspermvisa_avg,k=4)
table(grp)

grp <- cutree(uspermvisa_avg,k=5)
table(grp)

grp <- cutree(uspermvisa_avg,k=6)
table(grp)

grp <- cutree(uspermvisa_avg,k=7)
table(grp)

grp <- cutree(uspermvisa_avg,k=8)
table(grp)

grp <- cutree(uspermvisa_avg,k=9)
table(grp)

grp <- cutree(uspermvisa_avg,k=10)
table(grp)

grp <- cutree(uspermvisa_avg,k=11)
table(grp)

grp <- cutree(uspermvisa_avg,k=12)
table(grp)

x11()
plot(uspermvisa_sgl)
plot(uspermvisa_com)
plot(uspermvisa_avg)

#Divisive Method

uspermvisa_div = diana(data, diss = F, metric = "euclidean", stand = F)

plot(uspermvisa_div)

#=========================== Partitioning Methods ===============================#  

#K-Means
cl3 <- kmeans(data,3)
pca.uspermvisa <- princomp(scale(data))
plot(pca.uspermvisa$scores[,1:2],col=cl3$cluster,pch=cl3$cluster,main="K-Means: 3 Clusters")

cl4 <- kmeans(data,4)
pca.uspermvisa <- princomp(scale(data))
plot(pca.uspermvisa$scores[,1:2],col=cl4$cluster,pch=cl4$cluster,main="K-Means: 4 Clusters")

cl5 <- kmeans(data,5)
pca.uspermvisa <- princomp(scale(data))
plot(pca.uspermvisa$scores[,1:2],col=cl5$cluster,pch=cl5$cluster,main="K-Means: 5 Clusters")

cl6 <- kmeans(data,6)
pca.uspermvisa <- princomp(scale(data))
plot(pca.uspermvisa$scores[,1:2],col=cl6$cluster,pch=cl6$cluster,main="K-Means: 6 Clusters")

cl7 <- kmeans(data,7)
pca.uspermvisa <- princomp(scale(data))
plot(pca.uspermvisa$scores[,1:2],col=cl7$cluster,pch=cl7$cluster,main="K-Means: 7 Clusters")

cl8 <- kmeans(data,8)
pca.uspermvisa <- princomp(scale(data))
plot(pca.uspermvisa$scores[,1:2],col=cl8$cluster,pch=cl8$cluster,main="K-Means: 8 Clusters")

cl9 <- kmeans(data,9)
pca.uspermvisa <- princomp(scale(data))
plot(pca.uspermvisa$scores[,1:2],col=cl9$cluster,pch=cl9$cluster,main="K-Means: 9 Clusters")

cl10 <- kmeans(data,10)
pca.uspermvisa <- princomp(scale(data))
plot(pca.uspermvisa$scores[,1:2],col=cl10$cluster,pch=cl10$cluster,main="K-Means: 10 Clusters")

cl11 <- kmeans(data,11)
pca.uspermvisa <- princomp(scale(data))
plot(pca.uspermvisa$scores[,1:2],col=cl11$cluster,pch=cl11$cluster,main="K-Means: 11 Clusters")

cl12 <- kmeans(data,12)
pca.uspermvisa <- princomp(scale(data))
plot(pca.uspermvisa$scores[,1:2],col=cl12$cluster,pch=cl12$cluster,main="K-Means: 12 Clusters")

#PAM 
pam.uspermvisa.3 <- pam(data,k = 3)
clusplot(pam.uspermvisa.3)
plot(pam.uspermvisa.3)

pam.uspermvisa.3 <- pam(data,k = 4)
clusplot(pam.uspermvisa.4)
plot(pam.uspermvisa.4)

pam.uspermvisa.5 <- pam(data,k = 5)
clusplot(pam.uspermvisa.5)
plot(pam.uspermvisa.5)

pam.uspermvisa.6 <- pam(data,k = 6)
clusplot(pam.uspermvisa.6)
plot(pam.uspermvisa.6)

pam.uspermvisa.7 <- pam(data,k = 7)
clusplot(pam.uspermvisa.7)
plot(pam.uspermvisa.7)

pam.uspermvisa.8 <- pam(data,k = 8)
clusplot(pam.uspermvisa.8)
plot(pam.uspermvisa.8)

pam.uspermvisa.9 <- pam(data,k = 9)
clusplot(pam.uspermvisa.9)
plot(pam.uspermvisa.9)

pam.uspermvisa.10 <- pam(data,k = 10)
clusplot(pam.uspermvisa.10)
plot(pam.uspermvisa.10)

pam.uspermvisa.11 <- pam(data,k = 11)
clusplot(pam.uspermvisa.11)
plot(pam.uspermvisa.11)

pam.uspermvisa.12 <- pam(data,k = 12)
clusplot(pam.uspermvisa.12)
plot(pam.uspermvisa.12)
}

