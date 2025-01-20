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
