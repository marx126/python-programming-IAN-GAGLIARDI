# Classification accuracy
TP = 2
FP = 2
FN = 11
TN = 985
accuracy = (TP + TN) / (TP + TN + FP + FN)

print(f"The accuracy of this model is {accuracy}.")

# TP and TN are accurate predictions of the model, since they indicate that
# the model correctly predicted whether or not there is a fire.

# Thats why we need to divide the sum of TP and TN by all the possible results
# to know how accurate the model is.

# In my opinion, this is not a good model, since is very important to be 100%
# accurate when detecting something as important as a fire.