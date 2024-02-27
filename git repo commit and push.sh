if [[ `git status --porcelain` ]]; then
		echo "changes present"
		git status --short
		echo ""
		git add .
		read -p "enter commit message and press [enter]: " commitmessage
		git commit -m"$commitmessage"
		git push
	else			
		echo "no change"
fi
