import requests
import json

# ---- CONFIGURATION ---- #
GITHUB_TOKEN = ""
REPO_OWNER = "bordumb"  # Replace with your GitHub username
REPO_NAME = "GeoMeme"   # Replace with your repository name
BASE_URL = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}"
HEADERS = {
    "Authorization": f"Bearer {GITHUB_TOKEN}",
    "Accept": "application/vnd.github+json",
}

# Roadmap Data
ROADMAP = {
    "2025Q1": [
        "Build and release MVP",
        "Integrate live video streaming backend",
        "Implement geolocation tagging (City, Country)",
        "Create viewer interface for live streams",
        "Launch on iOS App Store",
    ],
    "2025Q2": [
        "Introduce user profiles for streamers",
        "Implement real-time chat functionality",
        "Create global map visualization for streams",
        "Collaborate with influencers for marketing",
        "Test viewer tipping feature",
    ],
    "2025Q3": [
        "Gamify streaming with achievements",
        "Enable stream recording for streamers",
        "Highlight top-rated streams in a global feed",
        "Attend travel and tech conferences for promotion",
        "Optimize streaming quality and reduce latency",
    ],
    "2025Q4": [
        "Implement branded partnerships for featured streams",
        "Launch pay-per-view marketplace for exclusive streams",
        "Add analytics dashboard for streamers",
        "Enable group streams for collaborative broadcasting",
        "Scale backend to handle a growing user base",
    ],
    "2026Q1": [
        "Add follower/following functionality",
        "Enable comments and reactions in real-time",
        "Create community hubs for popular locations",
        "Feature staff picks and trending streams",
        "Launch GeoCast merchandise store for branding",
    ],
    "2026Q2": [
        "Launch Android version of the app",
        "Release a web app for viewing and managing streams",
        "Translate the app into 10+ languages",
        "Localize app UI for right-to-left languages",
        "Partner with major global events like the Olympics",
    ],
    "2026Q3": [
        "Introduce streamer subscription tiers for monetization",
        "Expand into partnerships with travel apps like Lonely Planet",
        "Launch seasonal campaigns (e.g., cherry blossoms, holiday markets)",
        "Integrate with CDN providers for ultra-low latency",
        "Begin outreach to potential investors for Series A funding",
    ],
    "2026Q4": [
        "Implement AI-powered recommendations for streams",
        "Add smart translation for chat and captions",
        "Use computer vision to categorize streams by content type",
        "Tailor app homepage for personalized content discovery",
        "Introduce custom alerts for specific locations or categories",
    ],
    "2027Q1": [
        "Enable 360° live streaming for immersive experiences",
        "Integrate AR overlays for landmarks and stream details",
        "Collaborate with real estate companies for virtual property tours",
        "Partner with educational platforms for virtual field trips",
        "Develop tools for better moderation and content safety",
    ],
    "2027Q2": [
        "Expand server infrastructure to remote regions",
        "Optimize bandwidth usage with dynamic streaming quality",
        "Launch GeoCast Ambassador Program for streamers",
        "Collaborate with governments for tourism promotions",
        "Highlight GeoCast as a top innovator in live streaming tech",
    ],
    "2028Q1": [
        "Develop partnerships with satellite providers like Starlink",
        "Enable streaming from remote and offline areas",
        "Introduce blockchain-based stream authentication",
        "Host annual GeoCast Awards for top streamers",
        "Continue enhancing AR and VR capabilities for streams",
    ],
    "2028Q2": [
        "Launch GeoCast Originals featuring exclusive content",
        "Add green initiatives for sustainable streaming",
        "Expand into niche markets (e.g., real-time sports analysis)",
        "Collaborate with global non-profits for fundraising streams",
        "Implement advanced AI moderation for community safety",
    ],
    "2029Q1": [
        "Create a GeoCast API for third-party integrations",
        "Open up the platform for external developers",
        "Host hackathons to drive innovation in live streaming",
        "Enhance data analytics with predictive audience metrics",
        "Introduce gamification for viewers to boost engagement",
    ],
    "2030Q1": [
        "Make GeoCast a household name with a global ad campaign",
        "Introduce virtual shopping during live streams",
        "Create a GeoCast metaverse experience for VR users",
        "Expand into live-streaming professional events like conferences",
        "Strengthen security with advanced encryption protocols",
    ],
    "2031Q1": [
        "Develop autonomous drone integration for hands-free streaming",
        "Build offline-first capabilities for areas with limited connectivity",
        "Launch GeoCast-certified hardware for pro streamers",
        "Grow GeoCast’s community-driven funding initiatives",
        "Continue pushing the boundaries of AR and VR experiences",
    ],
    "2032Q1": [
        "Redefine streaming with holographic broadcasts",
        "Partner with AI companies for emotion-driven content",
        "Develop real-time language coaching through streams",
        "Introduce large-scale virtual events (concerts, festivals)",
        "Set the industry standard for immersive, geo-tagged streaming",
    ],
}

# ---- FUNCTIONS ---- #

# ---- FUNCTIONS ---- #

def create_label(label_name, color="0366d6", description="Roadmap milestone"):
    """
    Create a label in the repository.
    """
    print(f"Creating label: {label_name}")
    url = f"{BASE_URL}/labels"
    data = {
        "name": label_name,
        "color": color,  # Default GitHub blue
        "description": description,
    }
    response = requests.post(url, headers=HEADERS, json=data)
    if response.status_code == 201:
        print(f"Label '{label_name}' created successfully.")
    elif response.status_code == 422:
        print(f"Label '{label_name}' already exists.")
    else:
        print(f"Failed to create label '{label_name}': {response.json()}")


def create_issue(title, body, label_name):
    """
    Create an issue in the repository and assign a label.
    """
    print(f"Creating issue: {title}")
    url = f"{BASE_URL}/issues"
    data = {
        "title": title,
        "body": body,
        "labels": [label_name],  # Assign the label to the issue
    }
    response = requests.post(url, headers=HEADERS, json=data)
    if response.status_code == 201:
        issue_id = response.json()["id"]
        print(f"Issue '{title}' created successfully with ID: {issue_id}")
    else:
        print(f"Failed to create issue '{title}': {response.json()}")


# ---- SCRIPT EXECUTION ---- #

if __name__ == "__main__":
    # Step 1: Create labels
    for year_quarter in ROADMAP.keys():
        create_label(year_quarter, description=f"Tasks for {year_quarter}")

    # Step 2: Create issues and assign labels
    for year_quarter, tasks in ROADMAP.items():
        for task in tasks:
            create_issue(
                title=task,
                body=f"This task is part of the roadmap for {year_quarter}.",
                label_name=year_quarter,
            )

