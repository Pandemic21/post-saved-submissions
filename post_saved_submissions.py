import praw

USERNAME=""
PASSWORD=""
SUBREDDIT_NAME=""

r = praw.Reddit("Post saved submissoins /u/Pandemic21")
subreddit = r.get_subreddit(SUBREDDIT_NAME)
r.login(USERNAME,PASSWORD,disable_warning="True")
user = r.get_redditor(USERNAME)

for saved in r.user.get_saved():
	if type(saved) is praw.objects.Submission: 
		r.submit(subreddit,saved.title,url=saved.permalink)
