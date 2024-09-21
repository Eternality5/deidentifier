# SA Health De-identification Framework

## Directory Guide
- artefacts
    - deidentification-questions
        - The current itteration of the de-identification questions used in the survey.
    - figma-prototyping
        - Contains each draft of the Figma prototype for version control.
    - reflections
        - Contains the weekly reflection sorted by semester and group member.
    - s1-final-presntation
        - Contains artefacts from the creation of the semester 1 final presentation, including workload split and plan.

## Figma Prototype

Figma is a popular cloud-based design and prototyping tool used by designers, product teams, and developers to create interactive prototypes, design interfaces, and collaborate on design projects. With its powerful features and intuitive interface, Figma has gained widespread popularity in the design community.

#### **Why Figma?**

Using Figma for prototyping offers several benefits:

**Interactive Prototyping**: Figma enables the creation of interactive prototypes with realistic transitions, animations, and user interactions. Designers can define clickable areas, hotspots, and transitions between screens to simulate the user experience and test usability. This helps stakeholders and clients better understand the functionality and flow of the final product.

**Developer-Friendly Specs and Handoff**: Figma provides tools for developers to inspect design elements and generate design specifications. Developers can access measurements, colors, and assets, making the handoff process smoother and reducing the need for lengthy explanations or design meetings.

**Version History and Design Iterations**: Figma maintains a comprehensive version history, allowing designers to review and restore previous iterations of their designs. This feature is particularly useful when exploring different design options or reverting to earlier versions of the prototype.

Contained in `/artefacts/figma-prototyping` and
link to figma prototyping: [Figma Prototype](https://www.figma.com/proto/sAdybb8vfgy2OI3doweown/SERP-MVP?page-id=23%3A77&node-id=37-1504&starting-point-node-id=29%3A270)

## Development
### Setup
1. Ensue that you python3 install in your development environment https://www.python.org/
2. Install dependencies for the repo
   ```python -m pip install -r requirements.txt```
3. Generate static files, these are required to run tests
   ```python deidentifier/manage.py collectstatic```
4. Run database migrations
   ```python deidentifier/manage.py migrate```
5. Load the questions from into the database
```python loaddata.py```
6. To launch the server for development run
```python deidentifier/manage.py runserver```

#### Environment Variables

- If you are using Intellij to run your code you will need to set your environment variables, for development
  will need to set `DJANGO_SETTINGS_MODULE=deidentifier.settings.development`, do not use these
  settings for deployment.

### Loading Survey Questions
If you add a new page to the survey questions ensure that you add the fixtures file to the loaddata.py script so that can be automatically loaded in.

The loaddata.py script is a simple script for loading in the fixtures needed for the website to function. The questions
can be loaded in manually using the command ```python manage.py loaddata {{filename}}``` You don't need to add the path
to the filename, Django should be able to find the file. Don't try and run this command through Intellij,
it doesn't work because the script does not use an absolut path.
