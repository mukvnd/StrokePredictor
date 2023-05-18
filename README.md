# StrokePredictor

According to the World Health Organization (WHO), stroke ranks as the second leading cause of death worldwide, accounting for approximately 11% of total deaths. Understanding the factors that contribute to an individual's likelihood of experiencing a stroke is essential in preventing its occurrence. Factors such as gender, age, hypertension, heart disease, marital status, work type, residence, average glucose level, body mass index (BMI), smoking status, and prior history of stroke play significant roles. By recognizing and addressing these risk factors, we can work towards reducing the incidence of stroke and safeguarding public health.


## Parameters
1) Age
2) Gender
3) Type of work (Private, Government, Self-employed etc.) 
4) Body Mass Index, a measure of body fat based on height and weight, used to assess whether a person's weight is healthy in relation to their height.
5) Average glucose level of the individual
6) Past history with heart condition/disease
7) Past history with hypertension, a condition where the force of blood against artery walls is consistently too high
8) Residencial type, whether the individual lives in an urban or a rural area
9) Smoking status, whether the individual currently smokes/used to smoke/never smoked

##Insights
- EDA and feature engineering performed using imputations and encodings.
- The model was extensively trained on the above features.
- Class imbalance resulted in the introduction of stratified k fold cross validation.
- Used a variety of ML algos, including logistic regression, random forest, kmeans, lightgbm, xgboost and catboost.
- Tuned the hyperparameters involced with RandomSearchCV to improve the model.
- Exported the model and prepared a flask-based back end to support the model.
