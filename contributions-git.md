# Git and Github

This section has the guidelines we use to keep consistency across our different
Git repositories and Github projects.

## Start coding

If you're looking where to start, you can check the issues with the
`good first issue` label. Other labels will be used that may be more related to
the projects themselves, so don't hesitate to get in touch with the developers
if you need more guidance on how to start contributing to our projects.

## Proposing new features

If you want to propose a new feature (e.g adding a package) or do a big change
in the architecture it is highly recommended to open an issue first to discuss
it with the community.

## Authoring PRs

These are general guidelines for making PRs/commits easier to review:

 * Commits should be atomic and self-contained. Divide logically separate changes
   to separate commits. This principle is best explained in the the Linux Kernel
   [submitting patches][linux-sep-changes] guide.

 * Commit messages should explain the intention, _why_ something is done. This,
   too, is best explained in [this section][linux-desc-changes] from the Linux
   Kernel patch submission guide.

 * Commit titles (the first line in a commit) should be meaningful and describe
   _what_ the commit does.

 * Don't add code you will change in a later commit (it makes it pointless to
   review that commit), nor create a commit to add code an earlier commit should
   have added. Consider squashing the relevant commits instead.

 * It's not important to retain your development history when contributing a
   change. Use `git rebase` to squash and order commits in a way that makes them easy to
   review. Keep the final, well-structured commits and not your development history
   that led to the final state.

 * Consider reviewing the changes yourself before opening a PR. It is likely
   you will catch errors when looking at your code critically and thus save the
   reviewers (and yourself) time.

 * Use the PR's description as a "cover letter" and give the context you think
   reviewers might need. Use the PR's description to explain why you are
   proposing the change, give an overview, raise questions about yet-unresolved
   issues in your PR, list TODO items etc.

PRs which follow these rules are easier to review and merge.

[linux-sep-changes]: https://www.kernel.org/doc/html/v4.17/process/submitting-patches.html#separate-your-changes
[linux-desc-changes]: https://www.kernel.org/doc/html/v4.17/process/submitting-patches.html#describe-your-changes

### Commit Format

```
<area>: <description of changes>

Detailed information about the commit message goes here
```

Both the title and the body of the commit message shoud not exceed
72 characters in length. i.e. Please keep the title length under 72
characters, and the wrap the body of the message at 72 characters.

Separate the title and the body by 1 empty line.

Use the [imperative mood](https://chris.beams.io/posts/git-commit/#imperative)
for the title, and don't add a period at the end.

For the commit's message body, a period should come at the end of each
sentence (unless the line is not a regular sentence, e.g. code).

Here is an example of commit messages:

Good:
```
app-shells/bash: update ebuild to 5.3

Gentoo upstream has unmasked bash 5.3 and declared it stable.
This change updates the component to use the latest upstream ebuild.
```

Bad:
```
Update bash

Updated bash to the latest one.
```
