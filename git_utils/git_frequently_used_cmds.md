## To solve password authenitification problem
if you get a message , remote: Support for password authentication was removed on August 13, 2021. Please use a personal access token instead

Use My Account → Settings → Developer settings → Personal access tokens → Generate new token.

git remote set-url origin https://<token>@github.com/<username>/<repo>

This would enable every authentification to be done through the generated auth token
  
## Undo a commit & redo
```
$ git commit -m "Something terribly misguided" # (0: Your Accident)
$ git reset HEAD~                              # (1)
[ edit files as necessary ]                    # (2)
$ git add .                                    # (3)
$ git commit -c ORIG_HEAD                      # (4)
```
- This command is responsible for the undo. It will undo your last commit while leaving your working tree (the state of your files on disk) untouched. You'll need to add them again before you can commit them again).

- Make corrections to working tree files.

- git add anything that you want to include in your new commit.

- Commit the changes, reusing the old commit message. reset copied the old head to .git/ORIG_HEAD; commit with -c ORIG_HEAD will open an editor, which initially contains the log message from the old commit and allows you to edit it. If you do not need to edit the message, you could use the -C option.
  
## To remove (not revert) a commit that has been pushed to the server, 
rewriting history with 
```git push origin master --force``` is necessary.
  
## error: src refspec master does not match any.
- Try git show-ref to see what refs you have. Is there a refs/heads/master?

> Due to the recent "Replacing master with main in GitHub" action, you may notice that there is a refs/heads/main. As a result, the following command may change from git push origin HEAD:master to git push origin HEAD:main

- You can try git push origin HEAD:master as a more local-reference-independent solution. This explicitly states that you want to push the local ref HEAD to the remote ref master (see the git-push refspec documentation).
