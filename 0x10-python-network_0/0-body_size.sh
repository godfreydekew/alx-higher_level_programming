#!/bin/bash
#Displays the length of the content
curl -s http://$1 | wc -c
