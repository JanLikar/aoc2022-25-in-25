object Solution {
    def main(args: Array[String]) = {
        val grid = io.Source.fromFile("input.txt")
            .getLines()
            .map((x: String) => x.toArray.map(_.asDigit))
            .toArray

        val coords = for (
            x <- 0 until grid(0).length;
            y <- 0 until grid.length)
            yield (x,y)

        def getHeight(coords: (Int, Int)): Int = coords match {
            case (x, y) => grid(y)(x)
        }

        def treeVisible(slice: Array[Int], height: Int) = {
            slice.forall(h => h < height)
        }

        val visibleCount = coords
            .map({ case (x, y) => (getSlices(grid, x, y), getHeight(x, y))})
            .filter({ case (slices, height) => slices.exists(treeVisible(_, height)) })
            .length

        val maxScore = coords
            .map({ case (x, y) => (getSlices(grid, x, y), getHeight(x, y))})
            .map({ case (slices, height) => slices.map(viewDistance(_, height))})
            .map(_.product)
            .max

        println(visibleCount)
        println(maxScore)
    }

    def getSlices(grid: Array[Array[Int]], x: Int, y: Int): Array[Array[Int]] = {
        val row = grid(y)
        val col = grid.map(e => e(x))

        Array(
            row.slice(0, x).reverse,
            row.drop(x + 1),
            col.slice(0, y).reverse,
            col.drop(y + 1),
        )
    }

    def viewDistance(slice: Array[Int], treeHeight: Int): Int = {
        slice
            .zipWithIndex
            .filter({ case (h, i) => h >= treeHeight })
            .map({ case (h, i) => i + 1 })
            .headOption
            .getOrElse(slice.length)
    }

}
