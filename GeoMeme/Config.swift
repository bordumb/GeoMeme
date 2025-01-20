//
//  Config.swift
//  GeoStreamingApp
//
//  A single place to manage secret keys or environment variables.
//  In iOS, you can set environment variables in Xcode’s scheme to read them at runtime
//  or you can embed them in build settings (.xcconfig). This example
//  is just to illustrate reading them from ProcessInfo or using placeholders.
//

import Foundation

class Config {
    static let shared = Config()

    private init() {}

    // For local dev, set an environment variable in Xcode or in your shell:
    //   export MY_API_KEY="mySuperSecretKey"
    //   Then read it like this:
    var apiKey: String {
        ProcessInfo.processInfo.environment["MY_API_KEY"] ?? ""
    }

    // Similarly for other secrets:
    var streamingURL: String {
        ProcessInfo.processInfo.environment["STREAMING_URL"] ?? ""
    }

    // Etc.
}
