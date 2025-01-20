//
//  ViewerView.swift
//  GeoStreamingApp
//

import SwiftUI
import AVKit

struct ViewerView: View {
    let city: String
    let country: String
    let streamURL: URL

    var body: some View {
        VStack {
            Text("\(city), \(country)")
                .font(.headline)
                .padding()

            VideoPlayer(player: AVPlayer(url: streamURL))
                .onAppear {
                    // Auto-play the video
                    AVPlayer(url: streamURL).play()
                }
                .aspectRatio(contentMode: .fit)
        }
        .navigationTitle("Viewing Stream")
    }
}
