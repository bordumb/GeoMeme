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
