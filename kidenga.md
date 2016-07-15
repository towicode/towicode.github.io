Intro
============================
Setting up the login so you can actually test the app.  You got two ways of going about it.
Using ngrok, or using localhost.
You're going to end up using both (mostly the latter).
The localhost takes less time.  While ngrok allows you to actually test it on the app/share it.

You're still going to have to setup the django website, and make a user, and give yourself all of the permissions.
If you don't know how to do that, you should first look at the `setup.py` doc and if you still can't do it ask a staffer for help ;).

ONTO THE CONTENT!

1. Make sure you have ngrok running.
2. Goto the bin folder
3. type ./ngrok http 8000

Now that you have ngrok open make sure to not close that window, move it aside

1. Goto your BCF src folder.
2. Run the server by doing ```python manage.py runserver```

Now you have the backend running, make sure not to close that window either, move it aside

1. To ionic serve
```python kidenga.py serve```

2. To upload to ionic view
```python kidenga.py view```





The rest of this document explains the basic process of what kidenga.py does for you
====================================================================================

Run the application using ```ionic serve```
Go to the app.js and you'll see

    .constant('RemoteAPI', {
      url: 'http://kidenga.arl.arizona.edu'
    })

Then you want to install [ngrok](https://github.com/inconshreveable/ngrok).

Please type 
    
    ngrok http 8000
    
If that for whatever reason doesn't work there is a ngrok executable in the bin folder
    
    ```./ngrok http
    
Then open up a new console (just keep the ngrok running)

Go to the app.js and you'll see

    .constant('RemoteAPI', {
      url: 'http://kidenga.arl.arizona.edu'
    })

so you want to change the 

    url: 'http://kidenga.arl.arizona.edu'

to 

    url: <whatever your ngrok link is>

Replace whatever your ngrok link is, with whatever your ngrok link is, make sure to remove the `<>`

you can now 

    ionic upload

At this point if you run into problems, just delete the `ionic.project` file and run `ionic upload` again.

If you haven't made an ionic account, [Here you go](http://www.ionic.io/).

In order to actually see the app, you're going to have to download the ionic view app on your phone.

Then open the app, login, and the app should be there with the same id as the id in the `ionic.project` file.

You can now also 
    
    ionic share <insert person's email to share with>

Make sure that you remember to actually share the credentials on your local (django) site to the person you share with.

if you're curious, the url here is used in the AuthenticationService

    .service('AuthenticationService', function($q, $http, $state, RemoteAPI, $ionicPopup, $cookies, $ionicHistory) {
      var service = {
        user: undefined,
        login: function(email, password) {
          return $http.post(RemoteAPI.url + '/api/non-netid-login', {

and replaces the `RemoteAPI.url` and queries that specific api endpoint!
[Django Rest Framework Documentation!](http://www.django-rest-framework.org/)
