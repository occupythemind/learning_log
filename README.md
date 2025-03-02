# follow this step to add and update a remote repository from a local one

gh repo create (To create a new repository or simply do that on thier github.com)

git init (To initialize a local repo)
git add . ( To add all file or replace '.' with the files or directory you wish to add)
git commit -m "<message>" (The commit message - changes description)

git remote add origin <repo_link> (The repo you created earlier, add it here)
git remote -v (To verify if the repository was added)
git push -u origin master (Replace 'master' with the branch name you used or you want to make changes with; it'll still work cause now
	the 2 repos have been linked, but you'll need to go to github, make a ull request, check for conflicts (If no conflict or you're okay with it) then merge.)Just like collaborators.


You already know that the branch name decides with name/ branch has the changes
you made. Don't be confused.

# To fetch and add latest updates on that repo
git fetch origin
git merge origin/master (Again, replace 'master' with your bracnch name)

You can easily achieve this 2 above by
	git pull origin master (replace branch name if not yours)

