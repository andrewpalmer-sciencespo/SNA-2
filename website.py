import streamlit as st

st.title("SNA2 Final Project Website")
st.write("Andrew Palmer, Eli Press, Connor Fujita, Dhillon Grewal")

st.header("01. Our Network")

st.image("SNA Final PNGS/Fullnetwork.png",)
st.caption("Full Network of Collaborating Artists")

st.write("""
Our research explores the collaboration network behind Spotify’s weekly charting artists. The dataset includes **approximately 20,000 artists** whose songs appeared on the charts. 
To understand how collaboration might influence or reflect popularity, we expanded the network to incorporate **roughly 136,000 additional artists** who featured with at least one charting artist.

Together, this forms a collaboration web of **over 300,000 edges**, representing direct musical collaborations such as featured tracks or joint albums.

The dataset was sourced from **Kaggle**, a data platform operated by Google, and provided the foundation for our network analysis.
""")

st.subheader("Community Detection via Louvain Method")

st.write("""
To make sense of this massive network, we employed the **Louvain method**, a community detection algorithm that identifies clusters of densely connected nodes.
Initially, this method sorted the network into about **1,400 groups**, but many of these were extremely small or overlapping.

After refining the process, we distilled the network into **23 distinct subgroups**. These communities align closely with music genres, highlighting how artists cluster within genre-defined boundaries through collaboration.
""")
st.image("SNA Final PNGS/Louvain.png",)
st.caption("Louvain Method Community Detection")

st.header("02. Analysis")

st.subheader("The 23 Genre-Based Communities")

st.image("SNA Final PNGS/genres.png",)
st.caption("23 Genre-Based Communities")

st.write("""
Each of the 23 communities corresponds closely with a musical genre. Artists tend to collaborate within their genre groups, reinforcing established musical boundaries and cultural norms.
This genre-based clustering illustrates how stylistic identity remains a strong influence in the modern digital music landscape, even on a global platform like Spotify.
""")

st.subheader("Degree Centrality vs Artist Popularity")

st.write("""
Degree centrality measures how many direct connections an artist has within the network—i.e., the number of collaborations.
When comparing this measure to artist popularity on Spotify, we observed a **positive correlation**: artists with more collaborations generally had higher popularity scores.

However, this raises a critical question: **Does popularity drive collaborations, or do collaborations lead to popularity?**
The causality remains unclear. While the data shows a correlation, further statistical modeling is required to determine directionality.
""")

st.image("SNA Final PNGS/highestdegreenode.png",)
st.caption("Most Connected Artists")

st.subheader("Betweenness Centrality and Network Positioning")

st.image("SNA Final PNGS/connectivityvspop.png",)
st.caption("Connectivity vs Popularity")

st.write("""
Betweenness centrality identifies artists who serve as bridges between different communities—those who lie on the shortest paths between other artists.
Most artists in the dataset have a **betweenness centrality near zero**, meaning they operate within tightly knit groups and don’t connect across genres or cliques.

Only a **select number of highly popular artists** score high on betweenness, acting as central connectors between otherwise disconnected groups.
These artists hold a structurally important role in shaping cross-genre collaborations and trends.
""")



st.header("03. Key Findings and Interpretation")

st.write("""
Several key insights emerged from the data:

- There is a **positive relationship between the number of collaborations (degree centrality) and artist popularity**.
- Many of the **most popular artists had over 100 collaborators**, suggesting that broader network exposure contributes to fame and influence.
- **High betweenness centrality is rare**, and generally only associated with artists who are already highly popular.
- This implies that becoming a connector or influencer in the Spotify collaboration network is more likely a result of popularity, not a cause of it.
""")
st.image("SNA Final PNGS/degreevspop.png",)
st.caption("Degree Centrality vs Popularity")

st.image("SNA Final PNGS/betweeness.png",)
st.caption("Betweenness Centrality")

st.image("SNA Final PNGS/betweenessmegazoom.png",)
st.caption("Betweenness Centrality Zoomed In")

st.header("04. Broader Implications and Extensions")

st.subheader("Interpreting the Influence of Labels and Industry Structure")
st.write("""
Importantly, **all artists in the dataset are signed to major record labels**. These labels often coordinate collaborations and have extensive promotional power, influencing an artist’s network position and exposure.

This raises a critical question: **Are these patterns a reflection of organic popularity, or are they shaped by label-driven strategies and access to marketing infrastructure?**

If we were to include independent artists in the analysis, we might observe a very different structure—perhaps one with more isolated nodes and less centralized connectivity.

Our findings suggest that **network centrality may not be purely meritocratic**. Instead, it could be heavily influenced by strategic decisions made by record labels, raising important questions about access and inequality in the music industry.
""")

st.subheader("Related Research and Conceptual Foundations")
st.write("""
This project builds on previous academic research in music sociology and network theory:

- **Tobin South, Matthew Roughan, and Lewis Mitchell (2020)** studied critical shifts in **Eigenvector centrality** within Spotify networks, showing how genres like rap have gained influence over time.
- **David Hesmondhalgh, Ellis Jones, and Mark Taylor (2021)** explored how Spotify’s platform design reinforces existing industry hierarchies, limiting visibility for independent artists while amplifying those supported by major labels.

Together, these works highlight how **popularity, genre dominance, and centrality evolve**—and how platforms may reproduce structural inequalities under the guise of algorithmic fairness.
""")

st.markdown("---")
st.write("This project used data from Kaggle. The original presentation design was created with assets from Slidesgo, Flaticon, and Freepik.")