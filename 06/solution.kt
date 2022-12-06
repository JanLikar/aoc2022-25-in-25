import java.io.File

fun String.allCharsUnique(): Boolean = all(hashSetOf<Char>()::add)

fun main() {
    val input = File("input.txt").readText()

    // Start of packet marker
    val idx1 = input.windowed(4).indexOfFirst(String::allCharsUnique)
    println(idx1 + 4)

    // Start of message marker
    val idx2 = input.windowed(14).indexOfFirst(String::allCharsUnique)
    println(idx2 + 14)
}
