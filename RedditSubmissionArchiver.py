#imports
import praw
import URLArchiver

#Properties
subredditName = "badlinguistics"
userAgent = "BadLinguisticsBot2: v0.1 by /u/nciacrkson"
reddit = praw.Reddit(user_agent=userAgent, site_name='Chomskydoz')
backlogOfSubmissions = 5 #The number of submissions that the bot should work through, set to at least 1

#Functions

#Script
reddit.refresh_access_information()
subreddit = reddit.get_subreddit(subredditName)
submissionStream = praw.helpers.submission_stream(reddit_session = reddit,
												  subreddit = subreddit,
												  limit = backlogOfSubmissions,
												  verbosity = 0)

for submission in submissionStream:
	print submission.url
	if submission.url != submission.permalink: #We ignore self-posts
		urlOfArchive = URLArchiver.archive(submission.url)
		if urlOfArchive is not None:#Ensure we received a url to archive
			commentText = "The link submitted with this post has been archived here: " + urlOfArchive
			#print commentText #Uncomment this line for testing
			submission.comment(commentText) #Comment out this line for testing
