#!/usr/bin/env python
import os
import slack

#token = "xoxp-584011496384-586393602788-813872384884-5049873a932ae064eb91f1fb391a0d79"

client = slack.WebClient(token=os.environ['SLACK_API_TOKEN'])

response = client.chat_postEphemeral(
    channel='#random',
    text="Hello world!",
    user="puppetchatbot")