//
//  ContentView.swift
//  GeoStreamingApp
//

import SwiftUI

struct ContentView: View {
    var body: some View {
        NavigationView {
            VStack {
                Text("Geo Streaming App")
                    .font(.largeTitle)
                    .padding()
                Text("Welcome!")
                    .font(.subheadline)
            }
            .navigationTitle("Home")
        }
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}
