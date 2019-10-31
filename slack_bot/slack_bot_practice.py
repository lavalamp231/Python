#!/usr/bin/env python
import os
import slack


client = slack.WebClient(token=os.environ['SLACK_API_TOKEN'])

response = client.chat_postEphemeral(
    channel='#random',
    text="Hello world!",
    user="puppetchatbot")
