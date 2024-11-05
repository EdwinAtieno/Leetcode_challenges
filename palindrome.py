# class Solution(object):
#     def isPalindrome(self, s):
#         """
#         :type s: str
#         :rtype: bool
#         """
#         s = s.lower()
#         s = re.sub("[^a-z0-9]", "", s)
#         return s == s[::-1]
import matplotlib.pyplot as plt

timeline_data = {
    "Year": [2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024],
    "UK": [
        "National AI Strategy",
        "",
        "",
        "",
        "Education AI Report",
        "",
        "AI Approach",
        "",
    ],
    "US": [
        "",
        "",
        "",
        "AI Initiative",
        "",
        "AI Teaching Future",
        "",
        "Ed Tech Plan",
    ],
    "China": [
        "AI Development Plan",
        "",
        "AI Major",
        "",
        "",
        "",
        "AI Campaign",
        "AI Education Bases",
    ],
}

fig, ax = plt.subplots(figsize=(12, 6))

for country, events in timeline_data.items():
    if country == "Year":
        continue
    for i, event in enumerate(events):
        if event:
            ax.plot(
                timeline_data["Year"][i],
                0,
                marker="o",
                label=country if i == 0 else "",
            )
            ax.text(
                timeline_data["Year"][i],
                0.1
                if country == "UK"
                else (-0.1 if country == "US" else -0.2),
                event,
                ha="center",
                va="center",
                fontsize=9,
                bbox=dict(facecolor="white", alpha=0.6, edgecolor="black"),
            )

ax.set_xticks(timeline_data["Year"])
ax.set_yticks([])  # Hides the y-axis labels
ax.set_ylim(-0.5, 0.5)
ax.legend()
plt.title(
    "Timeline of AI Policy Developments in Higher Education (2014-2024)"
)
plt.show()

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        s = re.sub("[^a-z0-9]", "", s)
        return s == s[::-1]
