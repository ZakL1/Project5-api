# Shutter Api

This is the backend API for the Shutter web app, built using Django REST Framework. It handles data and functionality for user authentication, posts, comments, likes, and profiles.

 
### Existing Features

- __User Authentication__

  - Allows the frontend users to register. login, logout and save their information for future use


- __CRUD Posts__

  - Allows the frontend users to create, read, update and delete their own posts


- __Add, Delete Comments__

  - Allows the frontend users to add comments to posts or delete their own comments


- __Like, Unlike Posts__

  - Allows the frontend users to like and unlike posts 


- __CRUD Profile__

  - Allows the frontend users to create, read, update and delete their own profile


- __Cloudinary Image Upload__

  - Allows the frontend users uploads to be stored in cloudinary




## User Stories

- Link to me user stories - https://github.com/users/ZakL1/projects/4?query=sort%3Aupdated-desc+is%3Aopen

## Manual Testing 


-  __Creating a Post as an Authenticated User__
- Action: I logged into the API using /dj-rest-auth/login/ and copied the token.

- Test: Sent a POST request to /api/posts/ with a valid title, content, and image using Postman (with the token in headers).

- Expected Result: The new post appeared in the /api/posts/ list and returned status 201 CREATED.

- Result: Pass — post created successfully.


-  __Preventing Unauthenticated Post Creation__
-Action: Sent a POST request to /api/posts/ without logging in.

-Expected Result: The server should reject the request with 401 UNAUTHORIZED.

-Result: Pass — unauthenticated user was blocked from creating a post.


-  __Deleting a Comment as the Comment Owner__
- Action: Logged in, created a comment using /api/comments/, and then sent a DELETE request to that comment’s URL.

- Expected Result: The comment should be deleted and return 204 NO CONTENT.

- Result: Pass — deletion worked as expected.


-  __Editing a Profile Image__
- Action: Logged into /dj-rest-auth/login/, used /api/profiles/me/ with PUT to update the profile image with a Cloudinary URL.

- Expected Result: Profile should update and reflect new image URL.

- Result: Pass — image updated and visible in frontend.


## Automatic testing

- Did not have time to implement this

### Validator Testing 

- CSS
  - No errors were found when passing through the official [(Jigsaw) validator](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fvalidator.w3.org%2Fnu%2F%3Fdoc%3Dhttps%253A%252F%252Fcode-institute-org.github.io%252Flove-running-2.0%252Findex.html&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en#css)
- Javascript
  - No errors were found when passing through the official [ESLint validator](https://eslint.org/play/)

### Unfixed Bugs

- I installed whitenoise so that the deployed project had styles but couldn't get it working in time so sadly the api
has no css but still works perfectly fine

### Future features

- Add followers model and serializer
- Add full comment CRUD
- Add videos to posts model

## Deployment

- The site was deployed to GitHub pages. The steps to deploy are as follows: 
  - In the GitHub repository, navigate to the Settings tab 
  - From the source section drop-down menu, select the Master Branch
  - Once the master branch has been selected, the page will be automatically refreshed with a detailed ribbon display to indicate the successful deployment. 

1. **Ensure Build Output is Ready**

- Run the following command to create an optimized production build of your app:

  - Run this command in the terminal
  - npm run build
  - This will generate a `build/` folder containing all the necessary static files for deployment.

  - Install gunicorn in your django backend terminal by typing:
  - pip install gunicorn
  - pip freeze > requiremtns.txt

  - Now create a new file in the root directory called 'Procfile', no extensions
  - Add the follwing code to the file:
  - web: gunicorn your_project_name.wsgi



### 🌐 Deploying to Heroku

1. **Create a New App on Heroku**

   - Create a heroku account (if you don't have one)
   - Go to [Heroku Dashboard](https://dashboard.heroku.com/)
   - Click **"New" > "Create new app"**
   - Enter a name (e.g., `Shutter`)
   - Choose your region and click **Create app**

2. **Connect to GitHub**

   - In your Heroku app, go to the **Deploy** tab
   - Choose **GitHub** as the deployment method
   - Connect your GitHub account if prompted
   - Search for and connect the correct repository

3. **Set the Buildpack for Static Sites**

   - Go to the **Settings** tab in Heroku
   - Under **Buildpacks**, click **Add Buildpack**
   - Select:  python
   - Make sure it's listed above any other buildpacks

4. **Set Congif Vars**

   - Below the build packs select Reveal Config Vars
    and add the follwing (add the left text to the key 
    box and the right text to the value box):

    - ALLOWED_HOST = your-app-name.herokuapp.com
    - CLIENT_ORIGIN = https://your-frontend-domain.com
    - CLIENT_ORIGIN_DEV = http://localhost:3000
    - CLOUDINARY_URL = your-cloudinary-url
    - DISABLE_COLLECTSTATIC = 1
    - SECRET_KEY = your-django-secret-key

5. **Add Heroku Postgres Add-on**

   - In your Heroku app, go to the Resources tab
   - In the Add-ons section, search for Heroku Postgres
   - Select the free plan (e.g., Hobby Dev) and click Provision
   - Heroku will automatically add a DATABASE_URL config var to your app


### 🚀 Deploy the App

1. Go to the **Deploy** tab
2. Under **Manual deploy**, select your branch (e.g., `main`)
3. Click **Deploy Branch**

The live link can be found here - https://shutter-api-aad07b464590.herokuapp.com/


## Credits 

### Content 

- ChatGPT was used for some of the content and debugging help
- A big thank you to the code intitute tutor team for the help!

### Media

- All images are from google images
