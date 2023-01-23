# Airbnb_rating_prediction
Created a machine learning model which can predict the 7 different categories of rating for Airbnb in Dublin. The different ratings are : review_scores_rating, review_scores_accuracy, review_scores_cleanliness,review_scores_checkin,review_scores_communication,review_scores_location,review_scores_value

The dataset was taken from : http://insideairbnb.com/get-the-data/.Only the data for Airbnb's in Dublin were considered for this project. Two different csv's were used. The listing csv has information related to the property and the owner. The review csv has the listing id and reviews in multiple languages.

Data preprocessing was done wherein categorical columns were encoded, unnecesaary columns were dropped, missing values had to be taken care of etc. 

Since the reviews were in languages other than English as well, they were first converted to English using googletrans api. Polarity analysis was done using VADER for few textual columns. Addtional features were added using TFIDF approach.

Lasso and kNN regression were used as the two machine learning algorithms and both the models performed well with an MSE of 0.02 for Lasso model and 0.022 for kNN model.
