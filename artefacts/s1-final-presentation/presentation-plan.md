# Outline
## Section 1 (Introduction)
#### Introduction
- Who are we, who are you?
#### Background
- Definitions (This sort of leads into motivation)
	- What is re-identification (I think it would be good to put a big quoted definition on the screen and break it down for the definition of de-identification and re-identification)
	- how do we prevent re-identification = What is de-identification
	- The issues with de-identification
		- This term is also sometimes referred to as anonymisation, in Australia we call it that because it is defined as such in legislation. In Europe they use anonymisation, these may be used interchangeable in our presentation.
		- How de-identification is a balance between being de-identified and retaining the utility of the research dataset 
	- Motivations For the project/why it is a difficult project
	- Discuss the high level challenges and why there is a need for a system like this 
#### Requirements
- Requirement groups (The Current Ones)
- Highlight the most important requirements 

## Section 2 (The Process)
### Sprint 1 (Project Setup/Project Management)
#### Overview/Objective (Show Gantt Chart)
- Project Management at the Beginning
	- Gantt Chart (We should structure this section around the Gantt chart)
		- At the beginning of each sub section of section we should show the Gantt chart and highlight where we are up to at this point in the project
	- Explain the initial plan for the project
	- Kanban board 
		- Contacted course coordinator to activate it and it was promptly added
#### Challenges
- First Challenge with the Project (Keep short don't sound like you are complaining/bitching)
	- Group member 3 is uncontactable
	- Discuss the issues
		- Difficulties organising meetings as they give conflicting availabilities
		- Not attending meetings
		- Difficulty getting into contact with them 
		- Time wasted using multiple meaning in order to contact this individual
#### Progress/Result
- Still unsure about the final group member
	- Working under the assumption they will not participate
- Started researching/literature reviewing collecting papers about de-identification

### Sprint 2-3 (Elicitation)
#### Overview/Objective
- Requirements Elicitation Stage of the Project
	- How was the elicitation conducted
	- This spanned up to the third meeting
		- Requirements were discussed in the first meeting
			- Web-based
		- Requirements were reviewed in the second meeting
			- We determine there is already a tool that ARX already fulfils the requirements of client and we also say that adding to ARX might be a good direction for the project (We might put the ARX section in the middle of this)
			- We send messages on slack saying as such
		- Presentation in the third meeting
	- The content for this section should be in the proposal
	- Should discuss each of our contributions to this
		- Max: Investigated ARX, and the CSIRO framework
		- Vinay: Created own lit review using other papers

- Our Understanding of the Project at this point in time
	1. Web App
	2. Users upload their research dataset
	3. There are risk analysis tools implemented using the ARX API
	4. There are de-identification tools implemented using the ARX API
	5. Managers of researchers can see these 

- ARX (What is it, why is it important to this project)
	- ARX is an open-source tool for de-identification that was created by researchers in Germany
	- It can be used as a tool, a library, or a desktop application
	- It features risk assessments
	- Automated de-identification
	- Graphs and assessments about a data sets utility
	- it also has many studies and has been recognised by the EU
	- It fulfils most of the requirements we had at that time.
#### Challenges
- The second meeting not web-based, there is clearly a misunderstanding between our two clients
#### Progress/Result
- Technical Decisions made for the Project
	- Most if not all of our technical decision will come back to haunt us
	- Java Spring Boot with Maven
		- Why: Max has experience with it, used it in his internship
		- Why: ARX is a Java library and we want to be able to leverage its features
	- MongoDB

### Sprint 4 (Starting Development) (Holiday Break week)
#### Overview/Objective (Gannt Chart)
- The first sprint of the project. This sprint will focus predominantly on making sure that the infrastructure is in place for development. The issues in the sprint will include the following categories, creating development containers to prevent issues with developers developing on different system, setting up the web framework, and creating a continuous integration pipeline.
	- Issues worked on
		- Max
			- Set up backend, using spring boot
				- Max has previous experience working with Spring boot through his internship so he is working on that.
				- Had some issues that I had not encountered before
				- Included add ARX as a dependency
			- Continuous integration pipeline with GitHub actions for the back-end
				- Never set this up before and GitHub actions was initially disabled. Fortunately another group had about it already so when it actually came to implement it had been activated for all of our repos
			- Database migration management
				- Flyaway this is when I discover that we are going to have to upload data sets that could have an unknown schema, flyaway is for relational data bases, I haven't worked with NOSQL databases before determine not to use
		- Vinay
			- Front-end framework with react
			- Dev-container (This was specified in the workshop)
				- Issues with the dev container as we had chosen to use Intelij Ultimate as it is free for students and we had used Ruby Mine in the previous semester which is essentially just InteliJ for Ruby
					- The IDE did not have support for dev containers
					- however we had very few issues not using a dev container

### Sprint 5 (Further Development)
#### Overview/Objective
- The second sprint will be focussing on implementing the core functionality of the project and producing User Interface (UI) diagrams to present to the client.
- Uploading CSV data sets, this will give the user one option for uploading their data sets for de-identification.
	- Specifying data types (sensitive, identifying, etc.), this allows the user to specify the significance of each data column and will affect de-identification and risk.
	- Specifying de-identification parameters, this allows the user to specify limits parameters that are used for de-identification.
	- De-identifying data base on the parameters.
	- UI diagrams for, uploading data, risk assessments report pages, utility report pages, de-identification specification
- Issues Worked On
	- Max
		- De-identification Configuration
		- Fixing the ARX dependency as I had not configured it correctly
		- Creating the endpoint for uploading data sets
			- Adding mongoDB
	- Vinay
		- Adding the ability to delete uploaded research datasets
		- Created Figma Designs for the front-end
#### Challenges
- significant set back due to incorrect requirements
- Challenge: we were four weeks into development, sprint one was our best time to do this because we had the most free time
- Challenge: many technical decisions were made based on incorrect requirements
#### Progress/Result
- Solution: Adjusting the scope to be much more conservative.
- New scope: Focus on de-identification questions and UI design, rather than implementation, these things can be changed much more quickly, leave implementation to next semester.
- We discovered the issues in the requirements through our initial designs in Figma so we decided to invest significantly more time into using this tool to ensue the product was what the client wanted

### Sprint 6
#### Overview/Objective
- Due to issues that occurred during the requirements gathering process sprint 3 will focus on changing the direction of the project. It was discovered at the sprint 2 meeting that the clients did not want an application that required users to upload their data. We had invested much of our development time into solving issues related to uploading datasets that were not in known formats and automatically de-identitfying these datasets using a tool called ARX. These challenges informed some of our technical decisions such as choosing to use Spring Boot and MongoDB.
	- In this sprint we will focus on producing an interactive demo application using Figma so that we can pivot our effort in future if the product is not as they envisioned. We will also produce a set of questions to help de-identify the data and create a python script that runs a basic version of the decision making framework.
	- Issues worked on
		- Max
			- Back to the literature review
			- De-identification questions
			- Update requirements documentation
		- Vinay
			- Back to the literature review
			- Figma layout design
			- Adding questions to figma
#### Challenges
- Talk about some of the clients comments in from the recording
#### Progress/Results
- Changes made to the figma document
- Questions updated to make them more clear

## Section 3
- Presentation of Results
	- Run through of the questions
	- Generated report for a combination of the questions
	- Figma prototype 

### The plan going forward
- Re-assessment of technologies for the project
- Implementing the front and backend for the website designed in Figma
