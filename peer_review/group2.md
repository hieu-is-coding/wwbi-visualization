# Question 2 suggestions

Question 1 is just too fundamental and seems quite obvious. Therefore, group 17 hopes to recommend some insights for investagating the orther question.

## 1. Normalization

In terms of normalization, there is a very simple way to normalize these values: converting all output to a common unit like Gigajoule. This should be consistent with your statistics since industrial CO_2 emissions are tremendous.

Another approach is to apply Z-scores within each commodity type. By accounting for differences in scale across commodities, you may identify outlier with abnormal emissions trend (weirdly high or unusual low).

## 2. Visualization choices

When exploring clustering results, interactive scatter plots are an initial good idea (I guess). However, since you have mentioned the use of Silhouette Score, why don't ultilize it in visualization ?  Silhouette Plots sure can evaluate clustering quality thorugh different choice of k-value. Anyways, the use of Altair, Bokeh, or Plotly to obtain dynamic visualizations is considerably promising.