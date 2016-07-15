Intro
============================
Setting up the login so you can actually test the app.  You got two ways of going about it.
Using ngrok, or using localhost.
You're going to end up using both (mostly the latter).
The localhost takes less time.  While ngrok allows you to actually test it on the app/share it.

You're still going to have to setup the django website, and make a user, and give yourself all of the permissions.
If you don't know how to do that, you should first look at the `setup.py` doc and if you still can't do maybe consider trying again.

Here is quick guide.
The main emphasis is that this method uses a custom file called ```kidenga.py```

1. Make sure you have ngrok running.
2. Goto the bin folder
3. type ./ngrok http 8000

Now you have the backend running, make sure not to close that window either, move it aside

1. To ionic serve
```python kidenga.py serve```

2. To upload to ionic view
```python kidenga.py view```


more indepth reading
https://ngrok.com/
https://www.npmjs.com/package/gulp-shell



The rest of this document explains the basic process of what kidenga.py does for you
====================================================================================

In constant.js you will see something similar to this.

    .constant('RemoteAPI', {
      url: 'http://kidenga.arl.arizona.edu'
    })
    
This is the line where it tells the app where to talk with the backend.
Depending on wether or not you are trying to do Ionic View or Ionic Serve this needs to be a different URL

```ionic serve:   url: 'http://localhost:8100/backend'```



```ionic view :   url: '<ngrok>'```

It can be a pain to constantly switch between theese two so kidenga.py is a simple script that does it for you.

Kidenga.py sends a curl request to http://localhost:4040/api/tunnels to grab your current tunnels.
Assuming you only have 1 instance of ngrok running it will grab the correct tunnel. If you are using multiple instances of ngrok this will NOT work.

after it grabs your local ngrok url it checks the paramaters you sent to the kidenga.py command.

```python kidenga.py view```


A. if sent the view command, it will call the following gulp command

```gulp view-and-upload --go <ngrok_url>```


This command replaces the line in ur constant.js with the ngrok server so that your mobile device can talk to your localhost

B. if sent the serve command, it will call the following gulp command

```gulp reset-and-view```

this command replaces whatever is your constant.js with just localhost:8100/backend. This will allow your computer to talk to your computer!

Thats basically it! yay.
