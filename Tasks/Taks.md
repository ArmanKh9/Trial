# Remaining Tasks

## AI Tasks

### Identifying the same object from multiple images

Same object needs to be identified by the AI from images that are potentially taken from a different distance, angle, and in different time. Siamese-CNN is a potential solution. The following method is under investigation as a potential solution:

#### Siamese network
Siamese network with two sets branches that each branch divides into three sub-branches: Each main branch takes three inputs through its sub-branches. Each sub-branch generates a vector after its feature extractors. The vectors of sub-branches will be combined by taking either average, max or min of the three. 
The combined vectors of each of the main branches will be concatenated and followed by multiple fully connected then a binary output layer for classification.
Three images that are fed to each of the main branch shall be of the same object.

![siamese concept](https://github.com/ArmanKh9/Trial/blob/master/Tasks/siamese_concept.jpg)



### Creating a training database for model training

Database must consist of similar images to those that the model will use for classification. The training data must have some detailed info such as specy. These detailed info must be determined later.

# Shelving
The work needs to be done through a kickstarter fund raise. The kickstarter money raise period is between 30 to 60 days. Many things need to be done before the fund raising period like video, company setup, bank account setup, tax arrangements, cost estimate and team setup. Also, it is very mportant to pursuade friends and family members to invest on your idea first for the kickstarter to pick up. 
Moreover, the fund raising period is probably the most busy time. The 30-60 days period is a 16 hours/day work period. In this period, you will need to answer tond of questions from kickstarter backers. This requires taking off work for a month at least. In case enough fund was raised, it will be new full time job.













