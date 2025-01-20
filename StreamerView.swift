//
//  StreamerView.swift
//  GeoStreamingApp
//

import SwiftUI
import AVFoundation

struct StreamerView: View {
    @StateObject private var locationManager = LocationManager()
    @StateObject private var streamerVM = StreamerViewModel()

    var body: some View {
        VStack {
            Text("Streaming From: \(locationManager.currentCity), \(locationManager.currentCountry)")
                .padding()

            Button("Start Stream") {
                streamerVM.createStream(city: locationManager.currentCity,
                                        country: locationManager.currentCountry)
            }
            .padding()

            if let shareURL = streamerVM.streamURL {
                Text("Share this link:")
                Text(shareURL.absoluteString)
                    .foregroundColor(.blue)
                    .underline()
                    .padding()

                Button("Stop Stream") {
                    streamerVM.stopStream()
                }
                .padding()
            }
        }
        .navigationTitle("Streamer")
        .onAppear {
            requestPermissions()
        }
    }

    func requestPermissions() {
        AVCaptureDevice.requestAccess(for: .video) { granted in
            // handle
        }
        AVCaptureDevice.requestAccess(for: .audio) { granted in
            // handle
        }
    }
}

class StreamerViewModel: ObservableObject {
    @Published var streamURL: URL?

    func createStream(city: String, country: String) {
        // In real scenario, you'd call a backend API or direct AWS/Agora/etc. SDK here.
        // Let's simulate an API call:
        BackendAPI.createStream(city: city, country: country) { result in
            switch result {
            case .success(let url):
                DispatchQueue.main.async {
                    self.streamURL = url
                    // TODO: Start your actual streaming session here using your streaming SDK
                }
            case .failure(let error):
                print("Failed to create stream: \(error)")
            }
        }
    }

    func stopStream() {
        // Stop streaming in your SDK
        // Optionally update backend
        streamURL = nil
    }
}
