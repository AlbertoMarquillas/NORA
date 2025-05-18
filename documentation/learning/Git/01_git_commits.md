# 01 - Git and Clean Commits

This document gathers the best practices I am learning to use Git professionally, with a special focus on structured semantic commits.

---

## 1. Semantic Commits

Semantic commits follow a clear convention to structure messages and facilitate version control, history review, and changelog automation.

### 🧩 General Format

```
<type>[optional scope]: <short description>
```

**Example:**

```
feat(voice): add custom wake word detection
```

---

## 2. Common Types

| Type       | Description                                             |
| ---------- | ------------------------------------------------------- |
| `feat`     | New feature                                             |
| `fix`      | Bug fix                                                 |
| `docs`     | Documentation changes                                   |
| `style`    | Formatting (spaces, indentation, no functional changes) |
| `refactor` | Code refactoring without affecting external behavior    |
| `perf`     | Performance improvements                                |
| `test`     | Adding or modifying tests                               |
| `chore`    | Maintenance tasks (builds, scripts, dependencies)       |
| `build`    | Build system or packaging changes                       |
| `ci`       | Continuous integration and automation workflow changes  |

---

## 3. Best Practices

* **Use imperative tone.** Example: "add NFC module", not "added NFC module".
* **First line ≤ 72 characters.**
* **Write clear, specific, and task-focused messages.**
* **Avoid vague commits like "misc changes" or "update".**
* **Reference tasks or tickets if using Jira or similar.**

---

## 4. Commits with Breaking Changes

When a change breaks compatibility, it must be explicitly marked:

```
feat(api): remove /v1/status endpoint

BREAKING CHANGE: All clients must now use /v2/status instead.
```

---

## 5. Useful Tools

* **Commitizen (`cz`)**: CLI for guided commits.
* **Husky + Commitlint**: Enforce commit rules before pushing.
* **Conventional Changelog**: Automatically generates changelogs.

---

## 6. Real Examples in This Project

```
feat(frontend): add interaction button to landing page
fix(rtc): fix non-blocking read of register 0x0F
docs(gui): document possible states in FSM graph
```

---

## 7. Resources

* [https://www.conventionalcommits.org](https://www.conventionalcommits.org)
* [https://www.npmjs.com/package/commitizen](https://www.npmjs.com/package/commitizen)
* [https://typicode.github.io/husky](https://typicode.github.io/husky)
* [https://github.com/conventional-changelog/commitlint](https://github.com/conventional-changelog/commitlint)
