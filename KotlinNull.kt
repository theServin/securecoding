fun greet(user: String?){
    println(user?.let { "Hello, $it!" } ?: "Hello, Guest!")
}