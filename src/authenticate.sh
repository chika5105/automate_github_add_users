#!/bin/bash
#authenticate to github using Personal Identification Token

echo "Authenticating to Github with provided token credentials"
curl -i -u username:$TOKEN $OWNER_URL
echo "Authenticated To Github Successfully"
