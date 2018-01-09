# nba-goat

To find the **greatest-of-all-time** using statistics. I have created this repository to explore different methods for estimating relative skill of NBA teams. The complexity of methods increases according to the [standard, universally accepted W3D difficulty rating system](http://agentpalmer.com/wp-content/uploads/2014/10/Setting-your-Wolfenstein-3D-Difficulty-Level.jpg). You have been warned.

### Elo:
https://nbviewer.jupyter.org/github/priyamtejaswin/nba-goat/blob/master/nb-elo_vanilla.ipynb
- Vanilla elo. No bells and whistles.
- Adjusted elo. For margiv-of-victory(mov) and home-court-advantage(hca).

Scroll down to the last cell for an interactive visualisation for two of my favorite teams.

### ADF:
https://nbviewer.jupyter.org/github/priyamtejaswin/nba-goat/blob/master/nb-adf_team.ipynb
- Start by explaining the 2 core operations (convolution, greater-than).
- Explain the clutter problem, the complexity involved with calculating the exact posterior.
- Derive the parameter updates for the clutter problem using ADF.
- Setup skill inference.

### TODOs

1. Add chart/figure/timeline **A brief history of nba franchises** detailing the change in names. Use the DataFrame or https://www.basketball-reference.com/teams/ for the actual data. For team names with abbreviations, parse http://www.apbr.org/abbreviations.html using the following regex: `/[A-Z]{3}\ \-\ [A-Za-z\ \-\\\/]+\([A-Z\ \\\-\/]+\)/g` .

2. Think of good examples to demonstrate strengths and weaknesses of the methods. Bulls got MJ, MJ left. Shaq left Lakers at their peak and then won again with the Heat in 2006. Warriors turnaround. Jason Kidd started with the Mavs, then the Nets, then the Mavs again.

3. Account for carry over performance after every season.
