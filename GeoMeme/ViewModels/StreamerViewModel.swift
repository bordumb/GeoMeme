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
