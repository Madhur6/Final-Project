# CAPSTONE - TheGoodNote (TGN)

**Demo video:** [https://youtu.be/_JwRIB4dgoU](https://youtu.be/O4CIRFtA5rc?si=qa_ed73VxRXMGzjy)

## Description

Welcome to TheGoodNote (TGN)!

This is my Final Project for the course CS50’s Web Programming with Python and JavaScript. It is built with Django, HTML, CSS, JavaScript, Python & Bootstrap.

The main concept of this app is to enable users to create and organize their notes efficiently. I came up with this idea because I often found myself struggling to keep track of my thoughts, ideas, and important information scattered across various platforms and devices. TheGoodNote aims to provide a centralized and user-friendly platform for managing all your notes.

## Distinctiveness and Complexity

I believe my project satisfies the distinctiveness and complexity requirements because it has nothing in common with the other course projects. In fact, in the course, we built:

- A Google search clone
- A project similar to Wikipedia that enables us to create an article with a markdown system and edit it.
- A bid auction website
- A SPA (single page app) - mail app
- A network app similar to Twitter in which we can create/like a post, edit our own post, and follow/unfollow people.

My project is a note-taking app that allows users to create, edit, organize, and delete notes. It is nowhere close to any of the other projects. This is for the distinctiveness.

About the complexity requirements, my project utilizes Django on the backend and JavaScript on the frontend. It is also mobile responsive, as shown in the demo video.

## Pages:

### 1. Home Page

When logged in, you are redirected to this page. Here, you will see a demo of our app. You can create a new note by clicking on the "Projects" button at the top left corner. You can also view, your profile directly from this page by clicking on your username on the top left corner.

### 2. Dashboard Page

When logged in, you are redirected to this page. Here, you will see a list of your notes. You can create a new note by clicking on the "+Add Project" button at the top left corner. You can also view or delete your notes directly from this page.

### 3. Note Detail Page

On this page, you can view the full content of a note. You can also edit the note by clicking on the "Edit" button.


## Folder Structure
- `core/`: Django app folder containing the main app logic.
- `project/`: Django app folder containing the project app logic.
- `userprofile/`: Django app folder containing the userprofile app logic.
- `templates/`: HTML templates for the app's pages.
- `static/`: Static files such as CSS styles.


## File Structure

The main folder called `TheGoodNote` contains 2 folders:

### The first one is our Django project called `finalproject` as well:

```plaintext
finalproject
 ┣ __pycache__
 ┃ 
 ┣ __init__.py
 ┣ asgi.py
 ┣ settings.py
 ┣ urls.py
 ┗ wsgi.py
```

**Files modified in this folder and what they contain:**
- **`settings.py`**: All of the settings of our Django project, our app installed, and our custom configuration.
- **`urls.py`**: All of the paths for our app, including the admin panel and our app called `notes`.


### The 1st one is our app called 'core':

```plaintext
core
 ┣ __pycache__
 ┃ 
 ┣ migrations
 ┃ ┣ __pycache__
 ┃ 
 ┣ static
 ┃ ┗ core
 ┃    ┗ css
 ┃       ┗ styles.css
 ┣ templates
 ┃ ┗ core
 ┃    ┣ change_password.html
 ┃    ┣ contact.html
 ┃    ┣ index.html
 ┃    ┣ layout.html
 ┃    ┣ login.html
 ┃    ┣ password_reset.html
 ┃    ┣ password_reset_complete.html
 ┃    ┣ password_reset_confirm.html
 ┃    ┣ password_reset_done.html
 ┃    ┣ plans.html
 ┃    ┣ privacy.html
 ┃    ┣ register.html
 ┃    ┣ terms.html
 ┃    ┗ user-manual.html
 ┣ __init__.py
 ┣ admin.py
 ┣ apps.py
 ┣ models.py
 ┣ serializers.py
 ┣ tests.py
 ┣ urls.py
 ┗ views.py
```

Files modified in this folder and what they contain:

- **migrations folder**: Contains every migration we do every time we bring a change to our models, database.
- **static/notes folder**: Contains our CSS and JavaScript files.
  - **styles.css**: This is our stylesheet in which we write all of our CSS for the design of the app.
  - **scripts.js**: This file contains JavaScript functions that add interactivity to the app.
- **templates/notes folder**: Contains all of our HTML templates.
  - **index.html**: The main page template.
  - **layout.html**: The base template.
  - **login.html**: The login page template.
  - **register.html**: The registration page template.
- **admin.py**: This is where we register our models into our admin panel.
- **apps.py**: Config file for the app.
- **models.py**: This file contains all of our models.
- **serializers.py**: This file contains all of our serialized models.
- **tests.py**: File in which we can write all of our tests for our app.
- **views.py**: This file contains all of our views.
- **urls.py**: This file contains all the URLs created for our app core, including:
  - Home page: `''` (index)
  - Login page: `'login'`
  - Logout page: `'logout'`
  - Registration page: `'register'`
  - Change password page: `'change_password'`
  - Password reset: `'password_reset'`
  - Password reset done: `'password_reset_done'`
  - Password reset confirm: `'password_reset_confirm'`
  - Password reset complete: `'password_reset_complete'`
  - Plans page: `'plans'`
  - Privacy page: `'privacy'`
  - Terms page: `'terms'`
  - Contact page: `'contact'`
  - User manual page: `'user_manual'`


### The 2nd one is our app called 'userprofile':

```plaintext
userprofile
 ┣ __pycache__
 ┃ 
 ┣ migrations
 ┃ ┣ __pycache__
 ┃ 
 ┣ static
 ┃ ┗ userprofile
 ┃    ┣ css
 ┃    ┃ ┗ styles.css
 ┃    ┗ js
 ┃       ┗ edit_profile.js
 ┣ templates
 ┃ ┗ userprofile
 ┃    ┣ change_password.html
 ┃    ┣ contact.html
 ┃    ┣ index.html
 ┃    ┣ layout.html
 ┃    ┣ login.html
 ┃    ┣ password_reset.html
 ┃    ┣ password_reset_complete.html
 ┃    ┣ password_reset_confirm.html
 ┃    ┣ password_reset_done.html
 ┃    ┣ plans.html
 ┃    ┣ privacy.html
 ┃    ┣ register.html
 ┃    ┣ terms.html
 ┃    ┗ user-manual.html
 ┣ __init__.py
 ┣ admin.py
 ┣ apps.py
 ┣ models.py
 ┣ serializers.py
 ┣ tests.py
 ┣ urls.py
 ┗ views.py
```

**Files modified in this folder and what they contain:**

- **migrations folder**: Contains every migration we do every time we bring a change to our models, database.
- **static/userprofile folder**: Contains our CSS and JavaScript files.
  - **css/styles.css**: This is our stylesheet where we write all of our CSS for the design of the app.
  - **js/edit_profile.js**: JavaScript file for editing user profiles.

- **templates/userprofile folder**: Contains all of our HTML templates.
  - **change_password.html**: The change password page template.
  - **contact.html**: The contact page template.
  - **index.html**: The main page template.
  - **layout.html**: The base template.
  - **login.html**: The login page template.
  - **password_reset.html**: The password reset page template.
  - **password_reset_complete.html**: The password reset complete page template.
  - **password_reset_confirm.html**: The password reset confirm page template.
  - **password_reset_done.html**: The password reset done page template.
  - **plans.html**: The plans page template.
  - **privacy.html**: The privacy page template.
  - **register.html**: The registration page template.
  - **terms.html**: The terms page template.
  - **user-manual.html**: The user manual page template.

- **admin.py**: This is where we register our models into our admin panel.
- **apps.py**: Config file for the app.

- **urls.py**: Contains URL patterns for the userprofile app. It includes:
  - URL pattern for user profile view: `'<int:user_id>/'`
  - URL pattern for edit profile view: `'edit_profile'`

- **models.py**: This file contains models related to the userprofile app. It includes:
  - UserProfile: Model representing user profiles. Fields include user, name, date of birth, about, country, and image.

- **forms.py**: Contains forms related to the userprofile app. It includes:
  - CreateUserProfileForm: Form for creating or updating user profiles. Fields include name, date of birth, about, country, and image.

- **views.py**: Contains views for userprofile-related functionality. It includes:
  - user_profile: View for displaying user profile information.
  - edit_profile: View for editing user profile information.


 
### The 3rd one is our app called 'project':

```plaintext
project
├── forms.py
├── migrations
│   └── ...
├── models.py
├── static
│   └── project
│       ├── css
│       │   └── styles.css
│       └── js
│           ├── post.js
│           ├── edit_post.js
│           └── upload_image.js
├── templates
│   └── project
│       ├── detail_post.html
│       ├── edit_post.html
│       ├── paginator.html
│       ├── post.html
│       ├── projects.html
│       ├── upload_image.html
│       └── upload_image_edit.html
├── urls.py
└── views.py

```

**Files modified in this folder and what they contain:**

- **migrations folder**: Contains every migration we do every time we bring a change to our models, database.
- 
- **templates/project**:
  - detail_post.html
  - edit_post.html
  - paginator.html
  - post.html
  - projects.html
  - upload_image.html
  - upload_image_edit.html

- **static/project/css**:
  - styles.css

- **static/project/js**:
  - post.js
  - edit_post.js
  - upload_image.js

- **forms.py**:
  Contains forms related to the project app. It includes:
  - PostForm: Form for creating or updating posts. Fields include title and content.
  - ImageUploadForm: Form for uploading images.

- **models.py**:
  This file contains models related to the project app. It includes:
  - Project: Model representing projects. Fields include user, title, and created_at.
  - Post: Model representing posts. Fields include project, title, content, created_at, last_modified, and status.
  - Img: Model representing images.

- **views.py**:
  Contains views for project-related functionality. It includes:
  - projects: View for displaying projects.
  - delete_project: View for deleting a project.
  - post: View for creating a new post.
  - upload_image: View for uploading images.
  - detail_post: View for displaying post details.
  - edit_post: View for editing a post.
  - upload_image_edit: View for uploading images while editing a post.
  - get_temporary_image_url: View for generating temporary image URLs.
  - get_image: View for retrieving images.
  - get_temporary_image_url_edit: View for generating temporary image URLs for editing.
  - get_image_edit: View for retrieving images for editing.
  - get_image_detail_post: View for retrieving images for the detail post.
  - delete_images: View for deleting images.
  - markdown: Helper function to convert markdown content to HTML.



## Scope for Future Developement:

We invite developers from all backgrounds and skill levels to contribute to the future development of TheGoodNote (TGN). 
Whether you're passionate about front-end design, back-end development, user experience, or documentation, there are numerous opportunities to make a meaningful impact on the project.

- **Utilization of Nginx for Serving Static Media:**
  - Nginx, a high-performance web server, can be utilized in conjunction with Google Cloud Platform to efficiently serve static media files, such as Markdown documents, HTML templates, and MathJax libraries.
  -  By configuring Nginx as a reverse proxy server, TheGoodNote can offload the task of serving static content from the application server, improving overall performance and reducing server load.

- **LoadBalancing and Auto-Scaling:**
  - Implementing load balancing and auto-scaling capabilities with Google Cloud Load Balancer enables TheGoodNote to distribute incoming traffic across multiple instances of the application deployed on GCP.
  - Load balancers can intelligently route requests to the most available and least loaded instances, ensuring optimal performance and high availability. Additionally, auto-scaling policies can be configured to automatically provision or de-provision instances based on predefined metrics, such as CPU utilization or request latency, allowing TheGoodNote to dynamically scale resources up or down in response to changing demand.
 
- **A-I Driven feature:**
  - TheGoodNote's future development could include AI-driven features to enhance user productivity and experience. These features may involve natural language processing for document analysis and search, predictive analytics for personalized suggestions, smart formatting assistance, contextual help, and automated document summarization.

- **Support for graphs/charts/bar-graphs:**
  - Integration of libraries like mermaid(or create our own logic for graphs) is going to be very usefull for users, As they won't be relying on some other app for adding graphs to their documents.
  - Having access to graphs will give user more power and control over their notes, Then having to upload images of graphs every time user needs a graph


## VISION:

Our vision for TheGoodNote (TGN) is to create a versatile and intuitive Markdown editor that empowers users to effortlessly create, collaborate on, and share documents and notes. We aim to provide a platform where users can seamlessly transition from ideas to polished content, leveraging the simplicity of Markdown syntax combined with powerful features for mathematical expressions, real-time collaboration, and streamlined editing.



## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/your-repository.git

2. **Navigate to the Project Directory:**
   ```bash
   cd your-repository

3. **Create a Virtual Environment:**
   ```bash
   python -m venv venv

4. **Activate the Virtual Environment:**

   - On Windows:
     ```bash
     venv\Scripts\activate
     ```

   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```


5. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt

6. **Run Migrations:**
   ```bash
   python manage.py makemigrations network/app-name
   python manage.py migrate

7. **Run the Development Server:**
   ```bash
   python manage.py runserver

8. **Access the App:**
   Open your web browser and navigate to http://127.0.0.1:8000/.



## Usage

### Project Creation:

- Create projects effortlessly using TGN's intuitive interface.

### Image Upload:

- Upload images to your projects with ease, enhancing your content with visual elements.

### Image URL Copy:

- Copy the URLs of uploaded images for easy sharing and embedding within your content.

### Markdown Editing:

- Utilize the TGN interface to edit Markdown content seamlessly.

### Use TGN Manual:

- The user manual for TGN aims to empower users with the knowledge and skills they need to make the most of the application

### Autocomplete Feature:

- Enjoy the autocomplete feature for HTML tags and MathJax expressions, ensuring error-free formatting.

---
<br>

## Credits

- Project idea and implementation provided by the developer of TGN - Madhur ([linkedin](https://www.linkedin.com/in/madhur-pandey-ba5255241/)).

## Acknowledgments

I'd like to express my appreciation to the CS50 staff and community for their guidance and support during the CS50 course.


## Contributing

Feel free to contribute to the development of this app! Fork the repository, make your changes, and submit a pull request.

## License

This project is licensed under the MIT License.
