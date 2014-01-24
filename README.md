# Twitter PMI		
- - -        

This is a script I threw together over a weekend for a math project, inspired by [burrsettles'](https://github.com/burrsettles) article: [On "Geek" Versus "Nerd"](http://slackprop.wordpress.com/2013/06/03/on-geek-versus-nerd/).

You supply a search term and a corpus of tweets and the program returns a csv with the PMI Scores (if you're reading this, I'm assuming you know what [PMI](http://en.wikipedia.org/wiki/PMI) is) based on a twitter data. My data was a directory of text files aquired from [here](http://www.illocutioninc.com/Corpora/). The script then runs PMI on the term and returns it in formatted csv, form: `String` | `PMI Score`