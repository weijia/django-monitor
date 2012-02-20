#!/bin/bash

git add .

echo Update Message:
read UpdateMessage
git commit -a -m "$UpdateMessage"
git push --all
