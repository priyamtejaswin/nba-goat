# nba-goat

To find the **greatest-of-all-time** using statistics. I have created this repository to explore different methods for estimating relative skill of NBA teams. I was inspired by [FiveThirtyEight.com's CARMElo system](https://projects.fivethirtyeight.com/2018-nba-predictions/). My aim is to dive-deep into every method, derive the update equations and discuss the pros and cons. I intend to cover the following methods:
1. Elo and common extensions.[DONE]
2. Assumed Density Filtering.[IN PROGRESS]
3. Expectation Propagation(given that this NBA data has already ocurred and can be used for batched inference.)
4. Extensions to EP(score difference).

The complexity of methods increases according to the [standard, universally accepted W3D difficulty rating system](http://agentpalmer.com/wp-content/uploads/2014/10/Setting-your-Wolfenstein-3D-Difficulty-Level.jpg). You have been warned.

### A note about the notebooks.

All the text is written in Markdown. To avoid rendering issues, I would recommend to view it on nbviewer using the links provided below. The 2nd cell of the notebooks contains some javascript which hides all the input code cells for a pleasant reading experience. If you're interested in the code, then please click on the **here** link in the 2nd cell. The code for generating the graphical models is in `scratch.ipynb`.

---

### 1. Elo:
https://nbviewer.jupyter.org/github/priyamtejaswin/nba-goat/blob/master/nb-elo_vanilla.ipynb
- [x] Tracking NBA franchises through changes in names and cities.
- [x] Explain Elo with its core assumptions and apply the vanilla Elo on nba data.
- [x] Extend the base model to account for score difference(mov-Elo).
- [x] Extend the base model to account for home-court advantage(hca-Elo).
- [x] Finish with interactive visualisation of Warriors and Bulls.
- [x] Discuss and segue to ADF and TrueSkill.

Scroll down to the last cell for an interactive visualisation for two of my favorite teams!

### 2. ADF:
https://nbviewer.jupyter.org/github/priyamtejaswin/nba-goat/blob/master/nb-adf_team.ipynb
- [x] Start by explaining the 2 core operations (convolution, greater-than).
- [x] Explain the clutter problem and the complexity involved with calculating the exact posterior.
- [x] Derive the parameter updates for the clutter problem using ADF.
- [x] Visualise the update procedure.
- [ ] Setup the skill estimation problem in context of ADF.
- [ ] Derive updates using ADF.
- [ ] Apply on NBA data.
- [ ] Compare against mov-Elo from previous notebook.

Scroll down to the last cell to view ADF in action while estimating the true mean in noise!

---

### TODOs

1. Add chart/figure/timeline **A brief history of nba franchises** detailing the change in names. Use the DataFrame or https://www.basketball-reference.com/teams/ for the actual data. For team names with abbreviations, parse http://www.apbr.org/abbreviations.html using the following regex: `/[A-Z]{3}\ \-\ [A-Za-z\ \-\\\/]+\([A-Z\ \\\-\/]+\)/g` .

2. Think of good examples to demonstrate strengths and weaknesses of the methods. Bulls got MJ, MJ left. Shaq left Lakers at their peak and then won again with the Heat in 2006. Warriors turnaround. Jason Kidd started with the Mavs, then the Nets, then the Mavs again.

3. Account for carry over performance after every season.
