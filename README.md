# Twitter PMI		
- - -        

This is a script I threw together for a Math Assignment, inspired by [burrsettles'](https://github.com/burrsettles) article: [On "Geek" Versus "Nerd"](http://slackprop.wordpress.com/2013/06/03/on-geek-versus-nerd/).

The paper I wrote is stored in the repo as `paper.pdf` and is [downloadable](https://github.com/AndrewSB/TwitterPMI/blob/master/paper.pdf?raw=true). You're allowed to use it freely with citations. Also, I'd love to see what you end up making with the research, corpus, or script, so (you don't have to, but I'd love it)  drop me line with a link to what you made after you're done.

##How the program works     

###Data Collection
You supply a search term and a corpus of tweets and the program returns a csv with the PMI Scores (if you're reading this, I'm assuming you know what [PMI](http://en.wikipedia.org/wiki/PMI) is) based on a twitter data. My data was a directory of text files aquired from [here](http://www.illocutioninc.com/Corpora/). The script then runs PMI on the term and returns it in csv, formatted:      
`String` | `PMI Score`      

If you're planning to review the code, I'd start with `runall.py` which gives an overview of the project and a 'trigger' that runs the entire package.
 

###Get a Working CSV (Spreadsheet readable)
Once you run the 'Data Collection' part you'll have a file called `formattedOutput.csv`, that will have the words and their corresponding PMI Score of the word and the `target word` you chose in `driver.py`. If you are planning to compare the PMI's of *more* than one target word, you'll need to run the data collection more than once (changing the target word in `driver.py`).         
Once you have all of your PMI scores, stored in different CSV files, you can use `MergeCSV.py` to combine your CSV's using a dictionary - Trust me - It'll look good.      
Sidenote: My `MergeCSV.py` is for **two** CSV's, if you're going to do more you'll have to alter the script a little bit.


###Plot the data
I liked burrsettles' [plot](http://slackprop.files.wordpress.com/2013/06/plot-hires.pdf), so I tried to make something as close to his as I could. The `RLog` file can be opened in a text editor and its basically just the commands you'll need to create a plot (assuming you've narrowed down the hundereds of thousands of entries you had in your earlier CSV to maybe 100 or less) of a two-axes (two target words) PMI plot using the [statistical programming package R](http://www.r-project.org/).          

Example: *#to be added*
