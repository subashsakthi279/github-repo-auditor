# 🔍 GitHub Repo Auditor

A lightweight Python Command-Line Interface (CLI) tool that interacts with the public GitHub REST API to fetch and display repository data for any given user.

This project demonstrates core DevOps scripting skills, including API integration, JSON data parsing, error handling, and the use of command-line arguments for automation.

## 🚀 Features
* **REST API Integration:** Makes dynamic `GET` requests to the GitHub API using the `requests` library.
* **CLI Automation:** Accepts target usernames as command-line arguments (`sys.argv`), making it suitable for automated pipeline execution.
* **Intelligent Parsing:** Extracts and formats specific JSON data points (Repository Name, URL, Description) while ignoring unnecessary payload data.
* **Robust Error Handling:** Gracefully catches and reports missing users (HTTP 404) and missing command-line arguments.

## 🛠️ Tech Stack
* **Language:** Python 3
* **Libraries:** `requests`, `sys`, `json`
* **Concepts:** RESTful APIs, CLI Tooling

---

## 💻 How to Run Locally

**1. Clone the repository:**
```bash
git clone [https://github.com/subashsakthi279/github-repo-auditor.git](https://github.com/subashsakthi279/github-repo-auditor.git)
cd github-repo-auditor
