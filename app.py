import chat_gpt_api as gpt
import prompts as pr


#step 1: Enter a Topic
user_topic = input("Please enter your video topic: ")
user_minutes = input("Please enter your video length (in minutes): ")

#step 2: Generate 10 Catchy Title Ideas
titles_prompt = pr.youtube_title_generator_prompt.format(topic=user_topic)
titles = gpt.basic_generation(titles_prompt)
print("Titles Ideas: ")
print("----------------")
print(titles)
print("----------------")

#step 3: Generate Catchy Thumbnail Ideas
thumbnail_prompt = pr.youtube_thumbmail_generator_prompt.format(user_titles=titles)
thumbnails = gpt.basic_generation(thumbnail_prompt)
print("Thumbnail Ideas: ")
print("----------------")
print(thumbnails)
print("----------------")

#step 4: script
script_prompt = pr.youtube_script_generator_prompt.format(minutes=user_minutes,topic=user_topic)
script = gpt.basic_generation(script_prompt)
print("Suggested Script: ")
print("----------------")
print(script)
print("----------------")

#step 5: Into a twitter thread
tweet_prompt = pr.tweet_from_youtube_prompt.format(youtube_transcript=script)
tweet = gpt.basic_generation(tweet_prompt)
print("Twitter Thread: ")
print("----------------")
print(tweet)
print("----------------")
