# Network Simulations

Using Python, I followed instructions to simulate a social network and simulate some covariates for each individual in the network. Lastly I was tasked with taking a sample and computing its confidence interval to ultimately check if the values of beta1 and beta2 matched those that I had provided earlier. The steps are shown below:

My first task was to simulate the social nework. Setting an x and a y using two values taken from a normal distribution with an arbitrary mean and standard deviation, I plotted various points in a two dimensional graph to represent individuals in a network. 

I then proceeded to create a list of lists to represent a matrix which consisted of euclidean distances between any two points contained in the graph. When printed to console, looks like this:
```sh
[['0.0', '0.465990674635', '0.357202949064', '0.0133321569109', '0.388099356896'], ['0.465990674635', '0.0', '0.660109732204', '0.478682555747', '0.839541846968'], ['0.357202949064', '0.660109732204', '0.0', '0.357965940372', '0.332919926034'], ['0.0133321569109', '0.478682555747', '0.357965940372', '0.0', '0.377884098192'], ['0.388099356896', '0.839541846968', '0.332919926034', '0.377884098192', '0.0']]
```
Visually, it is not appealing but this matrix allows for fast access when requesting a euclidean distance between any two points. 

Next, I simulated edges by taking draws from a bernoulli distribution with probability: e^(euc_dist * a)/[1 + e^(euc_dist * a)]. The constant a is an arbitrary constant which controlls the overall expected tie frequency. Values of 1 contributed an edge between two given points and values of 0 signified no edge.

Plotting the edges in the graph resulted in a graph like the one below(50 individuals):

![Alt text](C:\Users\Lenovo\Documents\GitHub\network_simulations)



 


Markdown is a lightweight markup language based on the formatting conventions that people naturally use in email.  As [John Gruber] writes on the [Markdown site] [1]:

> The overriding design goal for Markdown's
> formatting syntax is to make it as readable
> as possible. The idea is that a
> Markdown-formatted document should be
> publishable as-is, as plain text, without
> looking like it's been marked up with tags
> or formatting instructions.

This text you see here is *actually* written in Markdown! To get a feel for Markdown's syntax, type some text into the left window and watch the results in the right.

### Version
3.0.2

### Tech

Dillinger uses a number of open source projects to work properly:

* [AngularJS] - HTML enhanced for web apps!
* [Ace Editor] - awesome web-based text editor
* [Marked] - a super fast port of Markdown to JavaScript
* [Twitter Bootstrap] - great UI boilerplate for modern web apps
* [node.js] - evented I/O for the backend
* [Express] - fast node.js network app framework [@tjholowaychuk]
* [Gulp] - the streaming build system
* [keymaster.js] - awesome keyboard handler lib by [@thomasfuchs]
* [jQuery] - duh

### Installation

You need Gulp installed globally:

```sh
$ npm i -g gulp
```

```sh
$ git clone [git-repo-url] dillinger
$ cd dillinger
$ npm i -d
$ mkdir -p public/files/{md,html,pdf}
$ gulp build --prod
$ NODE_ENV=production node app
```

### Plugins

Dillinger is currently extended with the following plugins

* Dropbox
* Github
* Google Drive
* OneDrive

Readmes, how to use them in your own application can be found here:

* plugins/dropbox/README.md
* plugins/github/README.md
* plugins/googledrive/README.md
* plugins/onedrive/README.md

### Development

Want to contribute? Great!

Dillinger uses Gulp + Webpack for fast developing.
Make a change in your file and instantanously see your updates!

Open your favorite Terminal and run these commands.

First Tab:
```sh
$ node app
```

Second Tab:
```sh
$ gulp watch
```

(optional) Third:
```sh
$ karma start
```

### Todo's

 - Write Tests
 - Rethink Github Save
 - Add Code Comments
 - Add Night Mode

License
----

MIT


**Free Software, Hell Yeah!**

[john gruber]:http://daringfireball.net/
[@thomasfuchs]:http://twitter.com/thomasfuchs
[1]:http://daringfireball.net/projects/markdown/
[marked]:https://github.com/chjj/marked
[Ace Editor]:http://ace.ajax.org
[node.js]:http://nodejs.org
[Twitter Bootstrap]:http://twitter.github.com/bootstrap/
[keymaster.js]:https://github.com/madrobby/keymaster
[jQuery]:http://jquery.com
[@tjholowaychuk]:http://twitter.com/tjholowaychuk
[express]:http://expressjs.com
[AngularJS]:http://angularjs.org
[Gulp]:http://gulpjs.com
