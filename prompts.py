youtube_title_generator_prompt = """\
I want you to act as a viral YouTube title creator.
Think of titles that are catchy and attention-grabbing,
and will encourage people to click and watch the video.
The titles should be short, concise, and direct. They should also be creative and clever.
Try to come up with titles that are unexpected and surprising. Do not use titles that are too generic,
or titles that have been used too many times before. My video is about {topic}. """



youtube_thumbmail_generator_prompt = """I want you to act as a viral YouTube thumbnail
creator. Think of thumbnails that are catchy and attention-grabbing,
and will encourage people to click and watch the video. I will provide you with 10 Titles, and you will suggest thumbnails for each
describe what is in the thumbnail very well and be as detailed as you can, so desginers can understnad and create. Here are the titles {user_titles}."""


youtube_script_generator_prompt = """Act as a professional YouTube video script writer
and create an engaging script for a {minutes} minute video.
Think outside the box and come up with a creative, witty,
and captivating script that people would be interested in watching and sharing.
Utilize techniques to generate more engagement in the narration script. 
Create a timeline and stick to it for up to {minutes} minutes
of spoken narration.

THE Topic IS: [{topic}]"""


tweet_from_youtube_prompt = """Act as if you're a social media expert. 
Give me a 10 tweet thread based on the follwing youtube transcript: {youtube_transcript}. 
The thread should be optimised for virality and contain 
hashtags and emoticons. Each tweet should not exceed 280 characters in length."""