# 03 - Git Merge Conflicts and Resolution

This document explains what merge conflicts are, why they occur, and how to resolve them effectively in a collaborative Git workflow.

---

## 1. What is a Merge Conflict?

A merge conflict happens when Git cannot automatically reconcile differences between two branches during a merge or rebase operation. This usually occurs when:

* Two branches modify the same lines of a file.
* A file is deleted in one branch but modified in the other.

Git stops and asks the user to resolve the conflict manually.

---

## 2. How Git Shows Conflicts

When a conflict occurs, Git marks the file and inserts conflict markers:

```txt
<<<<<<< HEAD
current branch's code
=======
incoming branch's code
>>>>>>> incoming-branch
```

You must choose or combine both sections, then remove the markers.

---

## 3. Steps to Resolve a Merge Conflict

```bash
# 1. Attempt to merge
git merge feature/voice-activation

# 2. Git reports conflict
# 3. Open the file and resolve the conflict manually

# 4. After editing, mark as resolved
git add conflicted_file.py

# 5. Complete the merge
git commit
```

If using rebase:

```bash
# During rebase
git rebase main
# Fix conflicts, then:
git add file
# Continue rebase
git rebase --continue
```

---

## 4. Useful Commands

```bash
# Abort a conflicted merge
git merge --abort

# Abort a conflicted rebase
git rebase --abort

# See unresolved files
git status
```

---

## 5. Tools for Conflict Resolution

* **VS Code**: built-in conflict resolver.
* **Meld** / **KDiff3** / **Beyond Compare**: graphical merge tools.
* **GitKraken** / **Sourcetree**: GUI Git clients with visual resolution.

Set default merge tool:

```bash
git config --global merge.tool meld
git mergetool
```

---

## 6. Best Practices

* Pull and rebase regularly when working on shared branches.
* Keep branches short-lived and focused.
* Communicate with collaborators about shared files.
* Use feature flags to avoid long-running branches.
* Prefer rebasing on top of updated `dev` before merging.

---

## 7. Resources

* [https://git-scm.com/docs/git-merge](https://git-scm.com/docs/git-merge)
* [https://www.atlassian.com/git/tutorials/using-branches/merge-conflicts](https://www.atlassian.com/git/tutorials/using-branches/merge-conflicts)
* [https://www.git-tower.com/learn/git/ebook/en/command-line/advanced-topics/merge-conflicts](https://www.git-tower.com/learn/git/ebook/en/command-line/advanced-topics/merge-conflicts)
* [https://www.gitkraken.com/learn/git/problems/git-merge-conflict](https://www.gitkraken.com/learn/git/problems/git-merge-conflict)
