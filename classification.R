library(caret)

setwd("/Users/kianamac/Documents/GitHub/uspermvisaproject/")
#setwd("~/HXRL/Github/uspermvisaproject/")

  
  #=========================== Reading files ===============================#  
 
  data <- read.csv("clean_data.csv", sep = ',' , header = TRUE)
  
  anyNA(data)
  
  smp_siz <- floor(0.7*nrow(data)) 
  train_ind <- sample(seq_len(nrow(data)),size = smp_siz, replace = FALSE)  # Randomly identifies the rows equal to sample size ( defined in previous instruction) from  all the rows of Smarket dataset and stores the row number in train_ind
  training <- data[train_ind,] #creates the training dataset with row numbers stored in train_ind
  testing <- data[-train_ind,]
  
  #=================================== Define models=======================# 
  trctrl <- trainControl(method = "repeatedcv", number = 10, repeats = 1, search="random", sampling = "smote")
  metric <- "Accuracy"
  DT_model <- train(case_status~., data = training, method = "rpart", metric = metric,trControl=trctrl,tuneLength = 10)
  Naive_model <- train(case_status~., data = training, method = "naive_bayes",trControl = trctrl)
  RF_model <- train(case_status~., data = training, method = "rf", metric = metric, trControl = trctrl)
  SVM_model <- train(case_status~., data = training, method = "svm", metric = metric,trControl=trctrl)
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
  write.table(results_DT,paste(file,"_DT.txt",sep = ""),sep = "\t", row.names = FALSE)
  write.table(results_NB,paste(file,"_NB.txt",sep = ""),sep = "\t", row.names = FALSE)
  write.table(results_RF,paste(file,"_RF.txt",sep = ""),sep = "\t", row.names = FALSE)
  write.table(results_svm,paste(file,"_svm.txt",sep = ""),sep = "\t", row.names = FALSE)
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
  

