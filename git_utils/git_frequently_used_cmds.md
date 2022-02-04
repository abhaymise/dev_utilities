## To solve password authenitification problem
if you get a message , remote: Support for password authentication was removed on August 13, 2021. Please use a personal access token instead

Use My Account → Settings → Developer settings → Personal access tokens → Generate new token.
git remote set-url origin https://<token>@github.com/<username>/<repo>

This would enable every authentification to be done through the generated auth token
