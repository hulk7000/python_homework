#dev 合并到 staging
git fetch origin && git checkout staging && git pull origin staging && git merge origin/dev && git push origin staging

#staging 合并到 uat
git fetch origin && git checkout uat && git pull origin uat && git merge origin/staging && git push origin uat

#uat 合并到 prod
git fetch origin && git checkout prod && git pull origin prod && git merge origin/uat && git push origin prod

#基于原有分支代码到新的分支
git fetch origin && git checkout -b staging origin/dev && git push -u origin staging

git fetch origin && git checkout -b uat origin/staging && git push -u origin uat

git fetch origin && git checkout -b prod origin/uat && git push -u origin prod