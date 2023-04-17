# Commit Reference

In this document, you will find helpful tips on how to write better commit messages to enhance your collaboration and code management. Clear and effective commit messages are essential for efficient collaboration among team members and for maintaining a clean codebase.

## Commit Structure

The commit should follow the instruction below:

### 1. Tag

The commit should contain a tag that indicates the type of change made.

**Types:**

**feature:**		  [a new feature]

**fix:**	  		  [bug fix]

**refactor:** 	  [code restructuring]

**test:** 		    [test-related changes]

**doc:** 		      [documentation updates]

**style:** 			  [code formatting]

**perf:** 			  [improve performance]

**config:** 		  [change the configuration file]

**security:** 		[improve securiy]

**revert:** 		  [undo or revert previous changes]
	
**Note** - always use lower-case while using tags.

### 2. Commit Message

Each commit message should be simple, focused, and contain a single logical 
change.

**Example:**

**bad**

“updated the login controller, fixed a bug in the registration service, and made some minor styling changes.”

**good**

“add validation filter to the request message in the login stage.”

**Note** - the message should start with a verb in the present tense.

### 3. Body

If the change is complex, add additional information in the commit message 
body.

**Example:**

**header**

“add validation to the request message in the login stage”

**body**

“Previously, the login stage did not validate the request message, which could result in errors and security vulnerabilities. This commit adds validation to the request message to ensure that it contains all required fields and is in the correct format. With this improvement, we can improve the reliability and security of our login functionality.”

**Note** - for clearer and better understanding, the body should be grammatically correct.

### 4. Metadata

Include relevant metadata in your commit message such as issue references.

**Types:**

**related**

“This commit is related to #666 issue.”

**fix**

“Fix #999 issue.”

## Sample

```
fix: add validation filter to the request message in the login stage.

Previously, the login stage did not validate the request message, which could result in errors and security…

Fix #696 issue.
```

When writing commit messages, it is important to keep in mind that your teammates are also working on the same codebase. To ensure efficient collaboration, always provide clear and concise descriptions of your changes and their purpose. Avoid using shitty grammar or assuming that others are aware of what the **f** you are doing. By writing informative and easily understandable commit messages, you can facilitate better teamwork and help to maintain a clean and organized codebase.

“unknown”
