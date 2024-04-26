# TheGoodNote (TGN)

## Distinctiveness and Complexity

Welcome to TheGoodNote (TGN)! TGN is a straightforward and efficient Markdown editor that simplifies Markdown editing and collaboration. It focuses on converting Markdown to HTML seamlessly, integrating MathJax for mathematical expressions, and providing a hassle-free experience for users.

#### Video Tutorial: [Watch the tutorial](https://www.youtube.com/watch?v=dQw4w9WgXcQ)

# Description

### Tech Stack

TheGoodNote (TGN) is built using a robust tech stack to ensure reliability, performance, and scalability. Here are some key components of the tech stack:

- **Python Django:** TheGoodNote is powered by Django, a high-level Python web framework that promotes rapid development and clean, pragmatic design.

- **Markdown:** Markdown is used as the primary syntax for text formatting in TGN, providing users with a simple and intuitive way to structure their content.

- **MathJax:** TGN integrates MathJax for rendering mathematical expressions using LaTeX syntax, enhancing the application's utility for users dealing with mathematical content.

- **HTML/CSS/JavaScript:** TGN utilizes standard web technologies such as HTML, CSS, and JavaScript to create a responsive and user-friendly interface for Markdown editing and collaboration.

- **SQLite:** TheGoodNote uses SQLite as its default database engine, providing a lightweight and easy-to-use solution for storing and retrieving data.

### MathJax Integration via CDN

TheGoodNote (TGN) seamlessly integrates MathJax for rendering mathematical expressions using LaTeX syntax. Here's how MathJax is integrated via CDN (Content Delivery Network):

1. **Include MathJax Script:**
   MathJax is included in the application using a script tag that references the MathJax CDN. This script tag is typically placed in the HTML template(s) where mathematical content is expected to be rendered.

   ```html
   <script src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/MathJax.js?config=TeX-AMS_CHTML"></script>
This script tag loads MathJax from the CDN and configures it to render mathematical expressions using the TeX and AMS extensions in CommonHTML format.
<br>

### Autocomplete Feature with JavaScript

TheGoodNote (TGN) incorporates an autocomplete feature for HTML tags and MathJax expressions, enhancing the user experience with error-free formatting. Here's how it works:

1. **HTML Tag Autocomplete:**
   - When a user types an opening HTML tag (e.g., `<div>`), TGN detects it and automatically inserts the corresponding closing tag (e.g., `</div>`) after the caret position.
   - The autocomplete feature ensures that HTML tags are properly paired, reducing the risk of syntax errors.
   - The autocomplete function also takes into account scenarios where attributes are included in the opening tag, ensuring consistent formatting.
   
2. **MathJax Expression Autocomplete:**
   - For mathematical expressions enclosed within double dollar signs (`$$`), TGN provides autocomplete functionality to insert the closing double dollar signs automatically.
   - When a user types the opening `$$` for a MathJax expression, TGN detects it and adds the closing `$$` after the caret position, allowing for seamless input of mathematical content.
   - This autocomplete feature streamlines the process of writing mathematical expressions, improving efficiency and accuracy.

3. **Copy URL Feature:**
   - TGN includes a feature to copy the URL of uploaded images, enhancing the sharing and embedding of images within the content.
   - Users can select an uploaded image and click the "Copy URL" button to copy the image URL to the clipboard.
   - The "Copy URL" button provides visual feedback upon successful copying, with an icon change to indicate completion.

4. **LocalStorage Integration:**
   - To improve user experience, TGN stores form data in the browser's localStorage before navigating to upload images.
   - When the user returns to the form, TGN populates the form fields with the stored data, allowing users to resume editing seamlessly.
   - Upon saving the post, TGN clears the localStorage to maintain data integrity and privacy.

By leveraging JavaScript, TheGoodNote (TGN) delivers a robust autocomplete feature that enhances productivity and ensures error-free formatting for HTML tags, MathJax expressions, and image URLs.
<br>



## TGN Overview
 TheGoodNote (TGN) stands as a straightforward and efficient Markdown editor, addressing the complexities often associated with Markdown editing and collaboration.
 It focuses on simplifying the Markdown conversion process to HTML, integrating MathJax for mathematical expressions, and providing a hassle-free experience for users.
## Features

- **TheGoodNote Interface:**
  - Provides a unified environment for Markdown editing.
  - The interface of TheGoodNote (TGN) is designed to provide users with a seamless and intuitive experience. It offers a clean and clutter-free workspace, allowing users to focus on their Markdown editing tasks without distractions.
  - TGN’s interface is user-friendly and accessible, catering to both novice and experienced users. With its sleek design and responsive layout, TGN ensures
a comfortable and efficient Markdown editing experience for all users

- **TGN Manual:**
    - The user manual for TheGoodNote (TGN) serves as a comprehensive guide to help users maximize their experience with the application. It covers a wide range of topics, from basic navigation and Markdown syntax to advanced editing techniques and customization options.
    - The manual begins with an introduction to TGN, providing an overview of its features, functionalities, and benefits. It then delves into the basics of Markdown, explaining its syntax and conventions in a clear and concise manner. Users are introduced to TGN's interface and navigation tools, guiding them through the various components of the application and how to utilize them effectively.
    - As users progress through the manual, they learn about TGN's advanced features, such as MathJax integration and Using HTML with MD syntax. Detailed instructions and examples are provided to help users understand how to leverage these features to enhance their Markdown editing workflow.
  
    - Overall, the user manual for TGN aims to empower users with the knowledge and skills they need to make the most of the application. Whether users are new to Markdown editing or experienced professionals, the manual serves as a valuable resource for unlocking the full potential of TGN and achieving their editing goals.

- **Use Markdown Syntax within HTML Tags:**
  - Allows the usage of Markdown syntax within HTML tags, combining Markdown's flexibility with HTML's power.
  - You can use Markdown syntax within HTML tags to combine the flexibility of Markdown with the power of HTML. This feature allows you to create rich content with ease.
  - To use Markdown syntax inside HTML tags, follow these steps:
    <br>
       – 1). Start with an HTML tag, such as &lt;center&gt;. <br>
       – 2). Leave the first line empty after the HTML tag. <br>
       – 3). Write your Markdown content, such as headings, lists, or emphasis, on subsequent lines. <br>
       – 4). End with the corresponding closing HTML tag, such as &lt;/center&gt;. <br>


- **MathJax Integration:**
  - Includes mathematical expressions, equations, and formulas within notes, documents, or messages.
  - TGN provides support for rendering mathematical content using LaTeX syntax. You can include mathematical expressions, equations, and formulas seamlessly within your notes, documents, or messages.
  - To use the math feature, enclose your mathematical content with double dollar signs (`$$`) like this, This will render the mathematical expression beautifully within your content. Here are a few key points to remember:
    <br>
       – 1). Enclose all mathematical content with double dollar signs (`$$`).. <br>
       – 3). Use LaTeX syntax for writing mathematical expressions. <br>
       – 4). Ensure that your LaTeX code is well-formed to avoid rendering issues. <br>

- **Safer Image Uploads:**
  - Ensure secure access to uploaded images, we employ tokens and digital signatures in generating URLs. This security measure prevents unauthorized access to your images and enhances data integrity.
  - It’s another layer of protection that ensures your content remains safe.

- **Real Time Preview:**
  - In TheGoodNote, we harness the power of Marked.js to enrich Markdown support in the frontend, providing users with a seamless editing experience coupled with a **real-time preview** feature on the right side. Marked.js facilitates an efficient process for rendering Markdown content into HTML instantly, ensuring that users can compose, visualize, and edit their documents in Markdown syntax with immediate feedback.
  - This integration of technologies guarantees a streamlined and user-friendly writing experience, where changes made in Markdown are dynamically reflected as HTML in real time, enhancing productivity and workflow efficiency.

- **Autocomplete Feature:**
  - Autocomplete feature tailored for HTML tags and MathJax expressions.

- **Simple to Use:**
  - Prioritizes simplicity, efficiency, and real-time collaboration.
  - Features streamlined Markdown conversion, real-time HTML preview, and user-centric design.


## Project's Limitations:

- **Dependency on External Services:**
  - The project relies on various external services and libraries, such as third-party APIs and frameworks. Any changes or disruptions in these services could directly impact the functionality and performance of the project, leading to potential downtimes or reduced feature availability.

- **Internet Connectivity:(Need for Native App Developement)**
  - TheGoodNoteheavily relies on internet connectivity for real-time collaboration and content synchronization.
  - Users with limited or unstable internet connections may experience disruptions in their editing sessions or encounter difficulties accessing certain features of the app.


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

## Folder Structure
- `core/`: Django app folder containing the main app logic.
- `project/`: Django app folder containing the project app logic.
- `userprofile/`: Django app folder containing the userprofile app logic.
- `templates/`: HTML templates for the app's pages.
- `static/`: Static files such as CSS styles.

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
