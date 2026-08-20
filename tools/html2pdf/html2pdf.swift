import Cocoa
import WebKit
let args = CommandLine.arguments
let inURL = URL(fileURLWithPath: args[1]); let outPath = args[2]
let app = NSApplication.shared
app.setActivationPolicy(.prohibited)
let W: CGFloat = 560
class D: NSObject, WKNavigationDelegate {
  func webView(_ w: WKWebView, didFinish n: WKNavigation!) {
    DispatchQueue.main.asyncAfter(deadline: .now()+0.5) {
      w.evaluateJavaScript("document.documentElement.scrollHeight") { r, _ in
        let h = CGFloat((r as? Double) ?? 2000) + 40
        w.frame = NSRect(x: 0, y: 0, width: W, height: h)
        DispatchQueue.main.asyncAfter(deadline: .now()+0.7) {
          let cfg = WKPDFConfiguration(); cfg.rect = NSRect(x: 0, y: 0, width: W, height: h)
          w.createPDF(configuration: cfg) { res in
            switch res {
            case .success(let data): try? data.write(to: URL(fileURLWithPath: outPath)); FileHandle.standardError.write("ok \(Int(h))\n".data(using: .utf8)!); exit(0)
            case .failure(let e): FileHandle.standardError.write("fail \(e)\n".data(using: .utf8)!); exit(1)
            }
          }
        }
      }
    }
  }
}
let d = D()
let wv = WKWebView(frame: NSRect(x: 0, y: 0, width: W, height: 800))
wv.navigationDelegate = d
let win = NSWindow(contentRect: NSRect(x: 0, y: 0, width: W, height: 800), styleMask: [.borderless], backing: .buffered, defer: false)
win.contentView = wv
wv.loadFileURL(inURL, allowingReadAccessTo: inURL.deletingLastPathComponent())
DispatchQueue.main.asyncAfter(deadline: .now()+30) { FileHandle.standardError.write("timeout\n".data(using: .utf8)!); exit(3) }
app.run()
