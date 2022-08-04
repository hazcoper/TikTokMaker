
from grabComment import createSubmission, createReddit, grabTitle, grabMostLiked
from generateSpeech import generateAudio



url = "https://www.reddit.com/r/explainlikeimfive/comments/ue0par/eli5_what_did_edward_snowden_actually_reveal_abot/"
url = "https://www.reddit.com/r/explainlikeimfive/comments/6joszt/eli5_why_can_people_walk_many_miles_without/"

myReddit = createReddit()
mySubmission = createSubmission(url, myReddit)
myTitle = grabTitle(mySubmission)

commentList = grabMostLiked(mySubmission)

isTrue = True
counter = 0
while isTrue:
    print(commentList[counter].body)
    print()
    user = input("Next commnet? (no to stop)")
    if user == "no":
        isTrue = False
        break
    counter = counter + 1


generateAudio(myTitle, "title", True)
generateAudio(commentList[counter].body, "comment1", True)



# get the title url
# generate the title sound
# generate the title image
# ask for comment url, or to list comments
# generate comment sound
# generate comment image
# add it all to the video