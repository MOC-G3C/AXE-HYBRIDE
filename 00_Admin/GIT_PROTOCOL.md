# 🐙 GIT OPERATIONAL PROTOCOL (MOC-G3C)

> **Objective:** Simple & clear synchronization of the Hybrid Axis.
> **Rule:** Always verify before pushing.

---

## 1. THE "ADD" STAGE (PREPARATION)
This command gathers all new and modified files in the folder.

`git add .`

> *Note: The "." means "everything in the current folder".*

---

## 2. THE "COMMIT" STAGE (VALIDATION)
This saves the changes locally with a message explaining what you did.

`git commit -m "Description of changes"`

> *Example: `git commit -m "Update Manifest and add new protocol"`*

---

## 3. THE "PUSH" STAGE (TRANSMISSION)
This sends everything to GitHub.

`git push`

---

## ⚡ QUICK COMBO (THE FULL CYCLE)
Use this single line to do everything at once (Add + Commit + Push):

`git add . && git commit -m "Update system" && git push`