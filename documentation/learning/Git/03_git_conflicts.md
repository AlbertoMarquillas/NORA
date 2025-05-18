# 03 - Git Merge Conflicts

This document explains what merge conflicts are, why they happen, and how to resolve them efficiently.

---

## 1. What is a Merge Conflict?

A merge conflict occurs when Git cannot automatically reconcile differences between two branches. This usually happens when two branches modify the same line in a file or when one branch deletes a file that another branch modifies.

---

## 2. Common Scenarios

* Two branches edit the same line in the same file.
* One branch deletes a file modified in another branch.
* File renaming or movement combined with modifications.

---

## 3. Conflict Markers

When a conflict occurs, Git marks the problematic area like this:

```text
<<<<<<< HEAD
code from current branch
=======
code from incoming branch
>>>>>>> feature/new-feature
```

You must choose one version, merge them manually, or write a new resolution.

---

## 4. Resolution Steps

1. Run `git status` to locate conflicting files.
2. Open each file and look for conflict markers `<<<<<<<`, `=======`, `>>>>>>>`.
3. Edit the file to resolve the conflict manually.
4. Once resolved, mark the file as resolved:

   ```bash
   git add <filename>
   ```
5. Commit the resolution:

   ```bash
   git commit
   ```

---

## 5. Abort or Retry

If you want to abort the merge and return to the previous state:

```bash
git merge --abort
```

To retry after fixing manually:

```bash
git add .
git commit
```

---

## 6. Tools for Resolving Conflicts

* Visual Studio Code (shows conflict sections clearly).
* GitKraken, SourceTree (graphical interfaces).
* `git mergetool` (CLI-based tool that integrates with difftools).

---

## 7. Best Practices

* Pull often from main branches to reduce divergence.
* Communicate with teammates about file ownership.
* Avoid long-lived branches.
* Keep changes small and focused.

---

## 8. Resources

* [https://www.git-scm.com/docs/git-merge](https://www.git-scm.com/docs/git-merge)
* [https://www.atlassian.com/git/tutorials/using-branches/merge-conflicts](https://www.atlassian.com/git/tutorials/using-branches/merge-conflicts)
* [https://docs.github.com/en/get-started/using-git/resolving-merge-conflicts](https://docs.github.com/en/get-started/using-git/resolving-merge-conflicts)
