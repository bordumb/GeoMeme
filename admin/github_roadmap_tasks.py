import requests

# ---- CONFIGURATION ---- #
GITHUB_TOKEN = ""
REPO_OWNER = "bordumb"  # Replace with your GitHub username
REPO_NAME = "GeoMeme"   # Replace with your repository name
BASE_URL = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}"
HEADERS = {
    "Authorization": f"Bearer {GITHUB_TOKEN}",
    "Accept": "application/vnd.github+json",
}

# Roadmap Data with Tasks for Each Issue
ROADMAP_TASKS = {
    "Build and release MVP": [
        "Define MVP feature set",
        "Create wireframes and UI designs",
        "Develop core app functionality",
        "Conduct internal testing",
        "Prepare for App Store submission",
    ],
    "Integrate live video streaming backend": [
        "Choose a video streaming provider (e.g., AWS IVS, Agora)",
        "Integrate SDK into the app",
        "Test live streaming functionality",
        "Optimize for low latency",
        "Implement error handling for streaming issues",
    ],
    "Implement geolocation tagging (City, Country)": [
        "Integrate Core Location framework",
        "Use reverse geocoding to get location",
        "Display city and country in UI",
        "Handle location permissions",
        "Test location accuracy across regions",
    ],
    "Create viewer interface for live streams": [
        "Design viewer UI",
        "Integrate video player",
        "Display streamer location in UI",
        "Add support for pause and playback controls",
        "Test stream playback for various internet speeds",
    ],
    "Launch on iOS App Store": [
        "Create App Store assets (screenshots, descriptions)",
        "Submit app for review",
        "Fix any issues from review feedback",
        "Go live on the App Store",
        "Monitor user reviews and initial feedback",
    ],
    "Introduce user profiles for streamers": [
        "Design profile page UI",
        "Enable profile editing",
        "Link profiles to streams",
        "Add profile picture upload functionality",
        "Test profile functionality for edge cases",
    ],
    "Implement real-time chat functionality": [
        "Choose a chat service provider",
        "Integrate chat SDK",
        "Enable chat in viewer interface",
        "Implement profanity filters and moderation",
        "Test real-time messaging for large-scale streams",
    ],
    "Create global map visualization for streams": [
        "Design map-based UI for live streams",
        "Integrate mapping library (e.g., MapKit, Google Maps)",
        "Plot active streams on the map",
        "Add click-to-watch functionality from the map",
        "Test map responsiveness for various zoom levels",
    ],
    "Collaborate with influencers for marketing": [
        "Identify potential influencer partners",
        "Reach out to influencers with collaboration proposals",
        "Plan promotional campaigns with influencers",
        "Monitor performance of influencer campaigns",
        "Iterate on marketing strategies based on campaign results",
    ],
    "Test viewer tipping feature": [
        "Design tipping interface for viewers",
        "Integrate payment gateway (e.g., Stripe, PayPal)",
        "Implement tipping notification for streamers",
        "Add analytics for tipping trends",
        "Test payment flow for errors and edge cases",
    ],
    "Gamify streaming with achievements": [
        "Define achievement criteria (e.g., 'Streamed from 5 cities')",
        "Design UI for achievements",
        "Integrate achievements into user profiles",
        "Notify users when they unlock an achievement",
        "Test gamification mechanics for usability",
    ],
    "Enable stream recording for streamers": [
        "Add recording toggle to streamer interface",
        "Save recorded streams to cloud storage",
        "Provide download functionality for recorded streams",
        "Notify streamers when recording is complete",
        "Test recording quality and storage limits",
    ],
    "Highlight top-rated streams in a global feed": [
        "Define criteria for top-rated streams (e.g., viewer count, ratings)",
        "Design UI for the global feed",
        "Implement sorting and filtering options for the feed",
        "Test global feed responsiveness",
        "Monitor performance of the feed for heavy usage",
    ],
    "Optimize streaming quality and reduce latency": [
        "Analyze current streaming performance",
        "Identify bottlenecks in streaming pipeline",
        "Implement adaptive bitrate streaming",
        "Test streaming quality on different network conditions",
        "Deploy updates to reduce latency",
    ],
    "Add analytics dashboard for streamers": [
        "Define key metrics for streamers (e.g., viewers, tips, location)",
        "Design UI for analytics dashboard",
        "Integrate analytics data into the app",
        "Add downloadable analytics reports",
        "Test dashboard performance for large datasets",
    ],
    "Translate the app into 10+ languages": [
        "Identify target languages based on user demographics",
        "Localize UI strings using translation services",
        "Handle text direction for right-to-left languages",
        "Test app layout for multilingual support",
        "Deploy language selection feature in settings",
    ],
    "Launch Android version of the app": [
        "Set up Android development environment",
        "Port core features from iOS to Android",
        "Optimize UI for Android devices",
        "Conduct beta testing on Android",
        "Launch app on Google Play Store",
    ],
    "Implement AI-powered recommendations for streams": [
        "Train AI model using user viewing data",
        "Integrate AI recommendations into the app",
        "Add personalization options for users",
        "Test AI accuracy for stream suggestions",
        "Monitor user engagement with recommendations",
    ],
    "Enable 360° live streaming for immersive experiences": [
        "Choose 360° camera integration solution",
        "Add 360° video support to the app",
        "Test streaming functionality with 360° cameras",
        "Optimize UI for 360° video navigation",
        "Monitor performance and viewer feedback for 360° streams",
    ],
    "Expand into partnerships with travel apps": [
        "Identify potential travel app partners",
        "Propose integration ideas (e.g., live tours, stream sharing)",
        "Collaborate on promotional campaigns",
        "Integrate travel app data into GeoCast",
        "Monitor partnership performance and user engagement",
    ],
    "Introduce custom alerts for specific locations or categories": [
        "Enable users to set location-based alerts",
        "Add category filtering for alerts",
        "Design UI for custom alert management",
        "Test alerts for real-time functionality",
        "Monitor user engagement with alerts",
    ],
}

# ---- FUNCTIONS ---- #

def get_issues():
    """
    Fetch all issues from the repository.
    """
    print("Fetching issues from repository...")
    url = f"{BASE_URL}/issues"
    response = requests.get(url, headers=HEADERS)
    if response.status_code == 200:
        issues = response.json()
        print(f"Fetched {len(issues)} issues.")
        return issues
    else:
        print(f"Failed to fetch issues: {response.json()}")
        exit(1)


def update_issue(issue_number, updated_body):
    """
    Update the body of an issue with new content.
    """
    print(f"Updating issue #{issue_number}...")
    url = f"{BASE_URL}/issues/{issue_number}"
    data = {"body": updated_body}
    response = requests.patch(url, headers=HEADERS, json=data)
    if response.status_code == 200:
        print(f"Issue #{issue_number} updated successfully.")
    else:
        print(f"Failed to update issue #{issue_number}: {response.json()}")


# ---- SCRIPT EXECUTION ---- #

if __name__ == "__main__":
    # Step 1: Fetch issues from the repository
    issues = get_issues()

    # Step 2: Update each issue with its tasks
    for issue in issues:
        title = issue["title"]
        issue_number = issue["number"]
        tasks = ROADMAP_TASKS.get(title)

        if tasks:
            # Create a markdown checklist from the tasks
            checklist = "\n".join([f"- [ ] {task}" for task in tasks])

            # Update the issue body with the checklist
            updated_body = f"{issue['body']}\n\n### Tasks:\n{checklist}"
            update_issue(issue_number, updated_body)
        else:
            print(f"No tasks found for issue '{title}'. Skipping.")
