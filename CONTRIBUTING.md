# Contributing to Phys_probl_F34567

Thank you for your interest in contributing to this repository. This project collects code and solutions for problems used in the Physics 101 course at TNTU. The project welcomes contributions that fix bugs, add or improve solutions, improve documentation, or add examples and tests.

This file explains the recommended GitHub workflow, coding and commit guidelines, and how maintainers will review contributions.

---

## Before you start

- Read the project README.md to learn how to run code and notebooks locally.
- Check existing issues and pull requests to avoid duplicating work.
- If you are fixing or extending a particular course problem, confirm which file or folder corresponds to that problem.

## Reporting issues

If you find a problem (a bug, missing data file, unclear solution, or broken notebook) please open a GitHub issue with:

- A short, descriptive title.
- A clear description of the problem and expected behavior.
- Steps to reproduce the problem (commands, notebook cell numbers, or inputs) and any error messages or stack traces.
- Your environment details when relevant (Python version, platform, major package versions).

If you are not a GitHub user you can still contact the repository maintainers by email (see the project page) or open an issue after creating a free GitHub account.

## How to contribute changes (recommended workflow)

We follow the common Fork -> Branch -> Pull Request workflow. If you are unfamiliar with GitHub, these steps are brief and linked to official documentation when useful.

1. Fork the repository
   - Click the "Fork" button on the repository page to create a copy under your account.
2. Clone your fork locally
   - git clone https://github.com/<your-username>/Phys_probl_F34567.git
   - cd Phys_probl_F34567
3. Create a feature branch
   - Use a descriptive branch name, for example:
     - fix/problem-12-typo
     - feat/problem-7-numerical-solution
     - docs/add-run-instructions
   - git checkout -b fix/problem-12-typo
4. Make your changes
   - Keep changes focused: one logical change per branch/PR.
   - Add or update tests or example notebooks when applicable.
5. Run tests and linters locally (if available)
   - If this repository includes tests or a requirements.txt, install dependencies and run the test suite before committing.
6. Commit with a clear message
   - Use present-tense, short summary and, if needed, a longer body:
     - Add solution for problem 12: damped oscillator
     - Fix: correct sign in problem 4 analytic derivation
   - Keep commits small and focused.
7. Push your branch to your fork
   - git push origin fix/problem-12-typo
8. Open a Pull Request (PR)
   - Go to your fork on GitHub and click "Compare & pull request".
   - Choose the target branch of the main repository (usually `main`).
   - In your PR description, explain what you changed and why; reference any related issue ("Fixes #123").

## Branching and naming

- Base new work on the repository default branch (usually `main`).
- Keep branch names short and descriptive: type/short-description (e.g., `feat/add-problem-5`, `fix/data-path`).

## Coding style and file structure

- Code: follow common Python best practices (PEP8) where applicable.
- Notebooks: keep notebooks runnable from top-to-bottom; clear the output before committing unless the output is needed for documentation.
- Place solutions and related data in a folder named consistently with the problem number or topic.
- Include a brief README or comments inside the problem folder explaining how to run scripts or notebooks if it is not obvious.

## Tests and examples

- If adding code that can be tested, include unit tests where reasonable and instructions so maintainers can run them.
- For notebooks, include a short example cell or instructions showing inputs and expected results.

## Pull request review process

- Maintainers will review PRs and may request changes. Please respond to review comments and push updates to the same branch.
- Small, well-documented PRs merge faster.
- When your PR is approved and CI checks (if any) pass, a maintainer will merge it.

## Continuous integration

- If the repository has CI configured, ensure your changes pass CI checks. If you need help interpreting CI failures, ask in the PR discussion.

## Licensing and contributor license

- By contributing, you agree that your contribution will be made under the same license as this repository (see LICENSE file). If you cannot accept that, do not submit a PR.

## Attribution and authorship

- Keep author information in files you add or update if it is meaningful. Use a short contributor line or git history records.

## Small contributions without GitHub

If you are not able to use GitHub but want to propose a change (typo fix, small script), you can:

- Send the patch or suggested change to a maintainer by email. Include the target filename, the exact change (a unified diff or the new file contents), and a short explanation.
- The maintainers will review and, if acceptable, they may apply the change and credit you in the commit message.

## Code of Conduct

Be respectful and constructive in discussions and reviews. If a formal Code of Conduct exists in this repository, follow it; otherwise default to GitHub's Community Guidelines.

## Who to contact

- The repository README or project page lists project maintainers. Use PR comments, issues, or the listed maintainer contact to ask questions about contributing.

---

Thank you for helping improve this collection of physics problem solutions. We appreciate clear, well-documented contributions that help other students and instructors.
