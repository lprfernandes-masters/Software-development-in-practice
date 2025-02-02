

# Git Commands
* git init => creates a git repo in the selected folder
* git add . => add all files in the folder to be tracked
* git status => check status of staging files  
* git commit -m "your commit message" => commit code
* git checkout -b nameOfBranch => to jump to branch x
* git branch => to see the active branch
* git remote add origin http://github.com/etc => adds the remote repo
* git push -u origin master => pushes to the remote called origin and to the branch master
* git revert <\hashcode of the commit> => reverts the identified commit.
* git pull or git pull origin master => to  
* git log => allows us to see all new commits 


TODO: KATAS Create a test repo, add files, commit them, create a feature branch with other file, commit them, and then create a pull request in git, and then merge both branches and delete the outstanding branch.


# Requirement Engineering

Requirements are presented into two levels of detail: User requirements and System requirements.


## User Requirements
It describes the services that the system should provide and the constraints under which it must operate. We don’t expect to see any level of detail, or what exactly the system will do, It’s more of generic requirements.

It’s usually written in a natural language and supplied by diagrams.


## System Requirements
Mean a more detailed description of the system services and the operational constraints such as how the system will be used and development constraints such as the programming languages.

This level of detail is needed by those who are involved in the system development, like engineers, system architects, testers, etc.


# Functional & Non-Functional Requirements
## Functional Requirements
It covers the main functions that should be provided by the system. When expressed as user requirements, they are usually described in an abstract way.

However, more specific functional system requirements describe the system functions, its inputs, processing; how it’s going to react to a particular input, and what’s the expected output.

## Non-Functional Requirements
These are the constraints on the functions provided by the system.

The constraints, like how many processes the system can handle (performance), what are the (security) issues the system needs to take care of such as SQL injections …

The rate of failure (reliability), what are the languages and tools that will be used (development), what are rules you need to follow to ensure the system operates within the law of the organization (legislative).


## Feasibility Report

Before getting started with the software, you need to make a study to identify whether the system is worth implementing and if it can be implemented under the current budget, technical skills, schedule, and if it does contribute to the whole organization objectives or not, etc.

# Requirements Elicitation

Describe the solution to be developed, including its functions, interfaces, design, and user experience. They’re usually formulated by the client or stakeholders.

Requirements elicitation is a complex process that consists of gathering, researching, defining, structuring, and clarifying a product’s requirements. It is an important step of the discovery phase of a project.

There are four types of requirements BAs usually handle during requirement elicitation:

1) Business requirements describe why a project is needed and how the company will benefit from it.
2) Stakeholder requirements capture the needs and expectations of stakeholders.
3) Solution requirements contain technical demands. They can be functional (describing what the system should do) and non-functional (describing the qualities the system should have).
4) Transition requirements define actions to be taken to transfer an organization from its current state to the desired state.

Key benefits:

* Establishes the precise scope of work and the budget.
* Avoids confusion during development. 
* Adds business value.
* Reveals hidden and assumed requirements.
* Allows for developing only relevant functionality


1) Preparing for elicitation - Collecting documentation needed and analyzing the current system (if exists). It usually includes:
* a description of the organization: business rules, structure, legal and regulatory requirements
* details of the project: solution analysis results, reports, or requirements prepared by other business analysts, technical and end user documentation of the existing system, manuals, instructions, tutorials for users and employees
* marketing materials: market research, competitor analysis, materials used to promote the solution

To speed up the study, the ba usually ask the client to provide a SME.

Analyzing stakeholder roles - apply the RACI (Responsible, Accountable, Consult, Inform) matrix to identify the role of each stakeholder. 

Then prepare use case and process flow diagrams and then prepare stakeholders for elicitation (choosing the most appropriate means of communication, scheduling periodic meetings if necessary, defining which information is needed)

2) Eliciting software requirements - happens during a series of meetings with various stakeholders. During these meetings, a business analyst has several tasks.
* Define requirements for the development team and stakeholders
* Manage the elicitation
* Document discussions
* Follow up with participants



3) Finalizing the elicitation - make sure that each of these questions is answered for each requirement:

* Why? - Why should the requirement be implemented, what problem does it solve, and what benefits does it provide?
* What? - What is the exact meaning of the requirement, what are the business rules, and what are the compliance or other requirements?
* How? - What are the possible ways to implement the requirement and what are the possible obstacles (outdated or insecure technologies, network limitations, etc.)?
* When? - How urgent is the requirement and how should it be prioritized?



## Elicitation techniques

* Interview
* Survey or questionnaire
* Interface analysis
* User interface (UI) analysis
* Documentation analysis
* Requirements workshop
* Brainstorm
* Focus groups
* Prototyping



# Conda

Creating environments
    
    conda create -n <env-name>

    //and to add packages
    conda create -n myEnvironment python numpy pandas

Listing environments

    conda info --envs

Change active environment back to default

    conda activate

Install packages

    conda install matplotlib

