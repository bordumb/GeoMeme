#!/bin/bash

# Define base project folder
PROJECT_NAME="GeoMeme"
BASE_DIR="$PWD/$PROJECT_NAME"

# Create folder structure
echo "Creating project structure..."
mkdir -p $BASE_DIR/{Models,Views/{Components},ViewModels,Services,Utilities,Assets.xcassets,Preview\ Content}

# Create Info.plist (App Config)
cat <<EOF > $BASE_DIR/Info.plist
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>CFBundleDevelopmentRegion</key>
    <string>$(PRODUCT_NAME)</string>
    <key>CFBundleDisplayName</key>
    <string>$PROJECT_NAME</string>
    <key>CFBundleExecutable</key>
    <string>\$(EXECUTABLE_NAME)</string>
    <key>UILaunchStoryboardName</key>
    <string>LaunchScreen</string>
</dict>
</plist>
EOF

# Create GeoMemeApp.swift (Entry Point)
cat <<EOF > $BASE_DIR/GeoMemeApp.swift
import SwiftUI

@main
struct GeoMemeApp: App {
    var body: some Scene {
        WindowGroup {
            ContentView()
        }
    }
}
EOF

# Create ContentView.swift (Root View)
cat <<EOF > $BASE_DIR/Views/ContentView.swift
import SwiftUI

struct ContentView: View {
    var body: some View {
        NavigationView {
            VStack {
                Text("Welcome to GeoMeme!")
                    .font(.largeTitle)
                NavigationLink("Start Streaming", destination: StreamerView())
            }
            .padding()
        }
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}
EOF

# Create StreamerView.swift
cat <<EOF > $BASE_DIR/Views/StreamerView.swift
import SwiftUI

struct StreamerView: View {
    @StateObject private var viewModel = StreamerViewModel()

    var body: some View {
        VStack {
            Text("Streaming from: \(viewModel.location)")
            Button("Start Streaming") {
                viewModel.startStreaming()
            }
        }
        .padding()
        .onAppear {
            viewModel.updateLocation()
        }
    }
}

struct StreamerView_Previews: PreviewProvider {
    static var previews: some View {
        StreamerView()
    }
}
EOF

# Create StreamerViewModel.swift
cat <<EOF > $BASE_DIR/ViewModels/StreamerViewModel.swift
import Foundation
import CoreLocation

class StreamerViewModel: ObservableObject {
    @Published var location: String = "Unknown"

    func updateLocation() {
        // Simulate location retrieval
        self.location = "San Francisco, CA"
    }

    func startStreaming() {
        print("Streaming started!")
    }
}
EOF

# Create Models
cat <<EOF > $BASE_DIR/Models/Stream.swift
import Foundation

struct Stream: Identifiable {
    let id: String
    let title: String
    let location: String
    let viewerCount: Int
    let streamURL: URL
}
EOF

cat <<EOF > $BASE_DIR/Models/User.swift
import Foundation

struct User: Identifiable {
    let id: String
    let username: String
    let avatarURL: URL?
}
EOF

# Create Services
cat <<EOF > $BASE_DIR/Services/BackendAPI.swift
import Foundation

class BackendAPI {
    static func fetchStreams() async throws -> [Stream] {
        // Simulate fetching streams from a backend
        return [
            Stream(
                id: "1",
                title: "Mountain Adventure",
                location: "Denver, CO",
                viewerCount: 120,
                streamURL: URL(string: "https://example.com/stream1")!
            )
        ]
    }
}
EOF

cat <<EOF > $BASE_DIR/Services/LocationManager.swift
import Foundation
import CoreLocation

class LocationManager: NSObject, CLLocationManagerDelegate {
    private let manager = CLLocationManager()
    var onLocationUpdate: ((String) -> Void)?

    override init() {
        super.init()
        manager.delegate = self
        manager.requestWhenInUseAuthorization()
        manager.startUpdatingLocation()
    }

    func locationManager(_ manager: CLLocationManager, didUpdateLocations locations: [CLLocation]) {
        guard let location = locations.last else { return }
        let geocoder = CLGeocoder()
        geocoder.reverseGeocodeLocation(location) { placemarks, error in
            guard let placemark = placemarks?.first, error == nil else { return }
            let city = placemark.locality ?? "Unknown City"
            let country = placemark.country ?? "Unknown Country"
            self.onLocationUpdate?("\(city), \(country)")
        }
    }
}
EOF

# Create Utilities
cat <<EOF > $BASE_DIR/Utilities/Config.swift
import Foundation

enum Config {
    static let apiBaseURL = "https://api.geomeem.com"
}
EOF

cat <<EOF > $BASE_DIR/Utilities/Extensions.swift
import SwiftUI

extension Color {
    static let primaryColor = Color("PrimaryColor")
}
EOF

# Create Preview Content
cat <<EOF > $BASE_DIR/Preview\ Content/PreviewData.swift
import Foundation

let mockStream = Stream(
    id: "1",
    title: "Mock Stream",
    location: "New York, NY",
    viewerCount: 100,
    streamURL: URL(string: "https://example.com/stream")!
)
EOF

# Feedback
echo "Project setup complete at $BASE_DIR"
