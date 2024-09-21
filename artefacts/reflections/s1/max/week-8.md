# Week 8 Reflection
*Maximilien Schuller – a1766887*

## What have you done for the project during the week individually?
Individually, my contributions to the project during the week included fixing ARX dependency issues and creating API CRUD endpoints for de-identification configurations which is information that is needed by 
ARX.

## What you plan to do for the project next week individually?
Next week, my individual plan for the project is to prioritize two key tasks. Firstly, I will revisit the literature review and focus on crafting clear and concise questions for de-identification. It is important to provide a sound rationale for each question, supported by relevant sources, including backlinks. This approach will ensure the questions are well-grounded and contribute to the project's overall quality.
Additionally, I will dedicate time to evaluating the existing source code and deciding regarding its suitability. I aim to determine whether it is beneficial to continue using the current codebase or explore the possibility of transitioning to a simpler framework. This evaluation is driven by the desire to streamline development efforts for potential future benefits. Detailed insights on the reasoning behind this decision will be shared in the subsequent section of this reflection.

## List the issue you encounter and give reasons if applicable.
Firstly, there were issues adding ARX as a dependency to the project as I had never added a dependency to a Maven project that wasn’t hosted on the Maven central repository. It took a long time to figure out how to do this as I could not find a source that explained it in a way that I could understand. I did however figure it out in the end.
Secondly there were massive changes to the requirements, we have been working for the past 4 or so week working on our current set of requirements which stated that we would have the user upload their data set to our application for automatic risk evaluation and de-identification. The whole reason our application was build in Java and Spring was so we could leverage the ARX de-identification tool which are Java tools. My group partner is not familiar with Java either, so it was a big investment for the team. Additionally, we selected MongoDB because we needed a document database to store research data sets. Both design decisions have been made redundant as we are not able to have research sets uploaded to our solution. Basically, brings the project back to the drawing board as we invested most of our time into solving these technical problems.

