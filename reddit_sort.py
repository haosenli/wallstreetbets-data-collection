"""
Elliot Liu
Haosen Li
This file contains the RedditSort class
"""
import praw


class RedditSort:
    def __init__(self, sub_name, praw_keys):
        """
        Takes in a subreddit name and a dictionary of credentials for PRAW.
        Instantiates a Reddit_Sort object.
        """
        self._reddit = praw.Reddit(client_id=praw_keys.pop('praw_client_id'),
                                   client_secret=praw_keys.pop(
                                       'praw_client_secret'),
                                   user_agent=praw_keys.pop('praw_user_agent'),
                                   username=praw_keys.pop('praw_username'),
                                   password=praw_keys.pop('praw_password'))
        self._subreddit = self._reddit.subreddit(sub_name)

    def get_submissions(self, post_limit):
        """
        Takes in a given post limit as an integer, returns a dictionary of
        submissions.
        """
        submissions = {}
        for submission in self._subreddit.new(limit=post_limit):
            post_title = submission.title.lower()
            submissions[post_title] = submission
        return submissions

    def get_comments(self, submissions):
        """
        Takes in a dictionary containing Reddit submission objects.
        Returns a list of comments.
        """
        comments = []
        for post in submissions.values():
            for top_level_comment in post.comments:
                if isinstance(top_level_comment, praw.models.MoreComments):
                    continue
                comments.append(top_level_comment.body)
        return comments