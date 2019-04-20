library(caret)
library(rpart.plot)
library(rpart)

setwd("/Users/kianamac/Documents/GitHub/uspermvisaproject/")
#setwd("~/HXRL/Github/uspermvisaproject/")
#=========================== Reading files ===============================#  
 
  data <- read.csv("Final_data.csv", sep = ',' , header = TRUE)
  
  anyNA(data)
  
  # smp_siz <- floor(0.7*nrow(data)) 
  # train_ind <- sample(seq_len(nrow(data)),size = smp_siz, replace = FALSE)  # Randomly identifies the rows equal to sample size ( defined in previous instruction) from  all the rows of Smarket dataset and stores the row number in train_ind
  set.seed(1234)
  train_ind <- sample(1:nrow(data),0.5*nrow(data))
  training <- data[train_ind,] #creates the training dataset with row numbers stored in train_ind
  testing <- data[-train_ind,]
  training$case_status <- as.factor(training$case_status)
  
#=================================== Define models=======================# 
  # trctrl <- trainControl(method = "cv", number = 10, search="random")
  metric <- "Accuracy"
  DT_model <- rpart(case_status~., data = training, cp =0.2)
  Naive_model <- train(case_status~., data = training, na.action = na.pass, method = "naive_bayes")
  RF_model <- train(case_status~., data = training,na.action = na.pass, method = "rf", metric = metric)
  SVM_model <- train(case_status~., data = training, na.action = na.pass, method = "svm", metric = metric)
  #=================================== Visualizations of tree based methods=======================# 
  rpart.plot(DT_model,box.palette = "RdBu",shadow.col = "gray", nn =TRUE)
  Importance.RF <- varImp(RF_model)
  plot(Importance.complete, top = 10)
#============================ Predict using the test data=================#
  DT_predict <- predict(DT_model, newdata = testing)
  Naive_predict <-predict(Naive_model, newdata = testing)
  RF_predict <- predict(RF_model, newdata = testing)
  svm_predict <- predict(SVM_model,newdata=testing)
#========================== construct the confusion matrix===============#
  cm_DT <- confusionMatrix(DT_predict,testing$case_status)
  cm_Naive <- confusionMatrix(Naive_predict,testing$case_status)
  cm_RF <- confusionMatrix(RF_predict,testing$case_status)
  cm_svm <- confusionMatrix(svm_predict,testing$case_status)
#============================ output files============================================
  # write.table(results_DT,paste(file,"_DT.txt",sep = ""),sep = "\t", row.names = FALSE)
  # write.table(results_NB,paste(file,"_NB.txt",sep = ""),sep = "\t", row.names = FALSE)
  # write.table(results_RF,paste(file,"_RF.txt",sep = ""),sep = "\t", row.names = FALSE)
  # write.table(results_svm,paste(file,"_svm.txt",sep = ""),sep = "\t", row.names = FALSE)
#============================ output confusion matrices================
  write.table(as.matrix(cm_Naive),paste(file,"Naive_ref.txt",sep = ""),sep = "\t")
  write.table(as.matrix(cm_Naive, what = "overall"),paste(file,"Naive_overall.txt",sep = ""),sep = "\t")
  write.table(as.matrix(cm_Naive, what = "classes"),paste(file,"Naive_cls.txt",sep = ""),sep = "\t")
  write.table(as.matrix(cm_DT),paste(file,"DT_ref.txt",sep = ""),sep = "\t")
  write.table(as.matrix(cm_DT, what = "overall"),paste(file,"DT_overall.txt",sep = ""),sep = "\t")
  write.table(as.matrix(cm_DT, what = "classes"),paste(file,"DT_cls.txt",sep = ""),sep = "\t")
  write.table(as.matrix(cm_RF),paste(file,"RF_ref.txt",sep = ""),sep = "\t")
  write.table(as.matrix(cm_RF, what = "overall"),paste(file,"RF_overall.txt",sep = ""),sep = "\t")
  write.table(as.matrix(cm_RF, what = "classes"),paste(file,"RF_cls.txt",sep = ""),sep = "\t")
  write.table(as.matrix(cm_RF),paste(file,"svm_ref.txt",sep = ""),sep = "\t")
  write.table(as.matrix(cm_RF, what = "overall"),paste(file,"svm_overall.txt",sep = ""),sep = "\t")
  write.table(as.matrix(cm_RF, what = "classes"),paste(file,"svm_cls.txt",sep = ""),sep = "\t")
  