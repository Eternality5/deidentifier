# Final Report Plan

The report main part (i.e., excluding the appendix) should be 2cm margins all around, using 12-point font with double spacing.

I think before we start on this we should discuss how much work we think each task will take to make it more simple.

## I. INTRODUCTION (V)
Give an overview/background of the project and describe the main objective(s) of the project.  

- Most of this can be taken from the proposal, just needs to be refined to fit the current project better

## II. LITERATURE REVIEW (V)
You may have done further literature review after submitting the project proposal and/or you may have refined your literature review – this section can include that work and you can bring some parts (only important ones from the project proposal but you wouldn’t get marks for the previously assessed work) in the section. 

- Most of this could be take from the original report
- I think both of us have things to say about this secition
- Note from research proposal "more works could have been included regarding any other web based solution currently available for de-identification."
- I'm thinking Vinay if you can refine this section as you wrote it in the proposal and we did quite well in that an I can add some of the more information I've looked into

## III. PROJECT SPECIFICATION  (M)
Describe the functionality (both functional and non-functional) that your project aims to provide. In addition to that, explain whether you had to make any changes to the original requirements, and why.  

- This section could take the specification from the proposal
- Then a section would need to be written abou the changes
- "The functional and non-functional requirements provided are detailed and given in the proper format (ID, description, category etc.). However, the priority should also be assigned to the requirements."

## IV. SYSTEM DESIGN  (V)
This section should provide the overall design of your project. You should justify your main design choices and discuss other options you have considered. This section should contain UML diagram to illustrate your design.  

Sytem Design
System

Questions
- Presenting questions (

- Main design choices why did we pick the tech we used
	- We are changing our tech stack, lets say for the purpose of this we are using Django, why Django
		- Uses python
			- Both familiar with Python
			- Python works well with Machine Learning and data science
			- Has lots of good ML and DS libraries
		- Mature ecosystem, lots of libraries
		- It uses an opionated structure (MVT)
			- This keeps the strucure of the project consistent
		- It's full stack, (it is full stack right)
			- Don't have to deal with a connection between a front and a back end
			- application that is dempendent on another application
			- One language = less context switching = good
	- What else did we condsider when picking out a framework
		- Ruby on Rails, why not RoR?
			- Very similar
			- Big thing ML and DS libraries
			- Django Traction 
			- Vinay will probably be writing this and he wants to pick it
			- Rails scales better apparently, Ruby is on average faster than Python
			- I'm more familiar with Rails than Django
			- MVC architechture vs MVT, MVT could be considered simpler 
			- From experiecne user authentication can be quite easy with rails
		- Why not a stick with spring
			- Thymeleaf not very good
			- Have to manually implement database migration management
			- Manually implement database
			- connect database tables with models, this is done automatically

- Front-End first approach (V)
- UML System diagram (V)
- Update the sequece diagram (V)

## V. IMPLEMENTATION  (M)
This section provides an overview of the approach employed in developing our prototype for the system outlined in the System Design. It delves into the collaborative efforts of our team, encompassing task allocation, resolution of intellectual and technical challenges, utilization of software development techniques, meticulous testing procedures, proficient employment of GitHub, and communication within the team and with our client. As a disclaimer for this section some of what is talked about in this section will be refereing to the development of the project with its original scope, using the original achitechture, as development has not yet begun on the new system.

### Dividing Work
At the beginning of each two-week sprint, our team held a sprint planning meeting to divide the workload effectively. We started by defining a sprint goal, which was initially established during the project proposal but was subject to adjustments as per the evolving needs of our client. Once we had a clear overall goal, we further broke it down into individual issues which were achievable in one week. These issues were thoroughly discussed and assigned to team members. Our aim was to distribute the tasks in a way that minimized any potential blockers and ensured smooth progress. To evenly distribute the workload each person was assigned approximately two issues per sprint, allowing for an average of one issue to be completed per week.

### Problem Solving Techniques
To address the problems at hand, our team considered several techniques. We utilized pros and cons lists to systematically evaluate options, taking into account factors of varying significance to make well-informed decisions. Additionally, we found value in discussing problems with other groups, leveraging their perspectives and knowledge since our team was relatively small. Since we didn't have any non-disclosure agreements to worry about, we could freely engage in open discussions. Furthermore, we explored the use of generative AI to ask questions in a more human-like manner this was particularly effective for finding a solution for how to store research datasets that have unknowable data formats.

### Software development techniques
Our team trialed a number of software development techniques including, stand up meetings, sprints, Kanban boards, and pair programming.

Early on in the project we trialed a process similar to stand up meeting where we would send a stand up message on Discord. The stand up message was formatted as a response to the following questions, "What have you done this since your last message?", "What are we going to do before our next message?", and "Do you have any blockers". We chose to do these in the form of messages because our schedules are not very consisitent as would be the case with a full-time or part-time team. These messages had the advantage of keeping us accountable but we found it hard to stay consistant and oftern not much progress was made from day to day. Weekly or bi-weekly meeting lined up better with actual progress made. 

We effectively implemented sprints as a software development technique in our project. Setting up a main objective for each sprint served as a helpful guidepost, enabling us to track our progress and communicate effectively with others. The sprints ensured that our project stayed on course and met the desired goals. Regular meetings with the client played a vital role in this process, providing valuable insights and helping us make necessary adjustments. Overall, the use of sprints proved to be a beneficial approach, aiding in project management and enhancing collaboration with the client.

We successfully utilized Kanban Boards as a software development technique in our project. The boards provided a visual representation of our work, making it easy to see the tasks at hand and their respective statuses. This enabled us to quickly identify what needed to be done and allowed team members to take on additional tasks if they had available time. The Kanban Boards effectively facilitated task management and ensured a balanced workload distribution. While we are still in the process of evaluating the impact of implementing work in progress (WIP) limits, we found the overall use of Kanban Boards to be valuable in enhancing visibility and streamlining our workflow within the team.

We breifly utilised pair programming during the development portion of the project. Because our team is only two people we were well suited to this, it was a good chance for us to share skills such as Max teaching Vinay the basics of Spring Boot. This technique worked well but with only four weeks of real development time it is yet to be seen if it is well suited to out team.

### Testing
- Project was delayed so testing was limited to the few features implemented of the original design
	- The strategy isolate units as much as possible using dependency inversion, that way we could mock any of the services that a unit interacted with

### GitHub
- GitHub usage increased significantly during the second half of the project
- We wanted to be able to version control more parts of the project, so we could have an idea of where we were currently at with the project and having to make a pull request for this such as a work split artefact for a presentation or a plan for a presentation meant that thing were completed rather that being left in a half finished state.

### Communication Channels
- Slack was used for communication with the client between meetings and to share file such as requirements documentation and agenda with the client.
- Discord was used to communicate between myself and my team mate to give updates of the project.
	- Initially daily stand up messages were send including the following information
		- What we had done since the last message
		- What we were planning to do
		- If we had any road blocks
	- We also used it to share learning resources
	- Create to do lists for more informal work assignments 
	- And announce if there were pull requests that needed reviewing

## VI. DIVISION OF WORK (M)
Describe the division of work. This need not be a long story - just a brief statement of who did what. You may mention who has done what as you describe each section of the implementation, however it is always a good idea to have a section summarising the division of work.  

- "The progress and planning section contained the Gantt chart which clearly showed the planning for the project but in the Gantt chart individual contribution should also have been depicted."

## VII. REFLECTION (V)
Description of the final product you have produced, i.e., your overall achievement this semester. 
What have you implemented?
What have you not managed to implement? 
What were the difficulties: which did you manage to overcome, and how? 
What you have learnt this semester, and what possible changes you need to do next semester to improve? 

## REFERENCES  
The reference includes the reference or related materials you have used in your final report.  

## APPENDIX  
The appendix should could contain any additional resources you need to present, records of group meetings, who did what, and, if possible, amount of time spent by various group members on their contributions.

- Gantt chart (M)
- Division of work table (V)