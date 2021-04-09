let package = Package(
    name: "myapp",
    targets: [
        Target(name: "App", dependencies: ["Module1", "Module2"]),
        Target(name: "Module1"),
        Target(name: "Module2")

    ],
    dependencies: [
        // Some external dependencies
    ],
    exclude: [
        // Excludes
    ]
)