# -*- coding: utf-8 -*-
"""
Created on Fri May 18 12:29:22 2018

@author: HP
"""


import facebook as fb

# Facebook Graphic Explorer API user Access Token
access_token = "EAACEdEose0cBAEDLFX9srBiHhav5wIA46GsjHfjOyAOciQVqDYaNhlCaOQydKEWa8feYDmWLWmFD4zZANreDFSc3WOvvTqFEvRHVGR72Wkyk0Q60OLt6ImreZBl4RG1BIogvXIbz5dOyMk80jTZCVRroDlHZApr4sYsZAZAf08TWJwwtzipZBDzG4yuH54l5ZBgWgZB2Jjh3Q9gZDZD"

# Message to post as status on Facebook
status = "......"

# Authenticating
graph = fb.GraphAPI(access_token)

# Posting Status on your wall
post_id = graph.put_wall_post(status)


graph.put_photo(image=open('sample.jpg', 'rb'),
                message='Look at this cool photo!')




