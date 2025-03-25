# Peer Review For Proposal - Group 17 

Thank you for sharing your proposal. Below are a few suggestions that we hope can help refine and strengthen your work:

## Question 1

Your first question is “How have the total emissions from major entities changed over the years, and what are the key trends across different commodities?”. While this is a solid starting point, the insights may be quite expected (e.g., emissions rising over time due to industrial growth). To make this question more impactful and policy-relevant, here are a few directions you could consider:

- Explore emission intensity (emissions per unit of production) to reveal how efficiently different commodities are produced over time.
- Disaggregate trends by parent_type (investor-owned, state-owned, nation-state) to explore whether different ownership structures have different emission profiles.
- Connect historical emissions to global policy milestones (e.g., the Kyoto Protocol, Paris Agreement) to explore cause-effect trends. Instead of just showing emissions rising, maybe you can try to identify moments of reduction or plateau, and explore why they happened? (e.g., shifts in commodity usage, policy changes, economic downturns).
- You can also try to highlight xontributions from top emitters. A Pareto-style analysis (e.g., are 20% of entities responsible for 80% of emissions?) could provide a compelling narrative for targeting interventions.

## Question 2

The second question is really promising to analyze and has the potential to uncover hidden patterns across industries and company types. Here are a few gentle suggestions to take it even further. 

To enhance your analysis, we suggest incorporating normalization techniques. Here are two simple yet effective approaches:
- Unit Standardization: Convert emissions into a common energy unit like Gigajoules (GJ). This helps maintain consistency, especially given the massive scale of industrial CO₂ emissions across different commodities.
- Z-score Normalization: Apply Z-score standardization within each commodity type. This approach adjusts for differences in scale and could help identify outliers or entities with unusually high or low emission trends.

Regarding visualization, since you mentioned using Silhouette Scores, you can consider including Silhouette Plots to justify your choice of cluster number (k-value). Also, we suggest leveraging interactive visualizations using Altair, Bokeh, or Plotly, especially for exploring multi-dimensional clusters and letting users filter by commodity, ownership type, etc.


Good luck and have fun with your project – we look forward to seeing your final work!
