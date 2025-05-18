# 02 - Git Branching and Workflow

This document summarizes the key concepts and best practices I am learning related to managing Git branches and using an effective branching model.

---

## 1. What is a Branch?

A Git branch is a lightweight movable pointer to a commit. Branches allow parallel development, experimentation, and structured workflows without affecting the main codebase.

---

## 2. Main Branch Types

| Branch            | Purpose                                                        |
| ----------------- | -------------------------------------------------------------- |
| `main` / `master` | Production-ready code. Should always be deployable.            |
| `dev`             | Integration branch for features, testing, and internal review. |
| `feature/*`       | New isolated feature development branches.                     |
| `bugfix/*`        | Hotfixes or patches for known issues under development.        |
| `hotfix/*`        | Critical production fixes. Merged into `main` and `dev`.       |
| `release/*`       | Preparation for release: final fixes, versioning, packaging.   |

---

## 3. Branching Strategy

Using a structured model (e.g., Git Flow or GitHub Flow) improves collaboration and scalability:

### Git Flow (typical for complex projects):

1. Work on features in `feature/*` branches.
2. Merge them into `dev` when ready.
3. Create `release/*` when preparing a version.
4. Apply last-minute fixes and merge into `main` and `dev`.
5. Use `hotfix/*` directly from `main` for critical issues.

### GitHub Flow (simpler projects):

1. Work on feature branches from `main`.
2. Open a pull request as soon as the branch is pushed.
3. Review, test, and merge back to `main`.

---

## 4. Common Commands

```bash
# Create and switch to a new branch
git checkout -b feature/voice-activation

# List all branches
git branch

# Switch branches
git checkout dev

# Merge another branch into current
git merge feature/voice-activation

# Delete a merged local branch
git branch -d feature/voice-activation

# Push a new branch to remote
git push -u origin feature/voice-activation
```

---

## 5. Rebase vs Merge

| Aspect     | `merge`                       | `rebase`                           |
| ---------- | ----------------------------- | ---------------------------------- |
| History    | Preserves full commit history | Rewrites history linearly          |
| Conflicts  | Resolved once during merge    | Resolved during each commit replay |
| Simplicity | Easier for teams and reviews  | Cleaner history but more complex   |

**Rule of thumb:** Use `merge` in shared branches. Use `rebase` for cleaning local history before pushing.

---

## 6. Best Practices

* Name branches descriptively: `feature/login-ui`, `bugfix/null-pointer-fix`, etc.
* Keep branches small and focused.
* Rebase local branches before pushing to avoid unnecessary merge commits.
* Regularly clean up merged local branches.
* Avoid force-push on shared branches.

---

## 7. Resources

* [https://nvie.com/posts/a-successful-git-branching-model/](https://nvie.com/posts/a-successful-git-branching-model/)
* [https://www.atlassian.com/git/tutorials/comparing-workflows](https://www.atlassian.com/git/tutorials/comparing-workflows)
* [https://git-scm.com/docs/git-branch](https://git-scm.com/docs/git-branch)
* [https://learngitbranching.js.org/](https://learngitbranching.js.org/)
