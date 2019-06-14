// P01 (*) Find the last element of a list.
//     Example:
//     scala> last(List(1, 1, 2, 3, 5, 8))
//     res0: Int = 8

// The start of the definition of last should be
//     def last[A](l: List[A]): A = ...
// The `[A]` allows us to handle lists of any type.

object P01 {
  def last[A](ls: List[A]): A = ls.last
  
  def lastRec[A](ls: List[A]): A = ls match {
    case h :: Nil => h
    case _ :: tail => lastRec(tail)
    case _ => throw new NoSuchElementException
  }
}

// Test cases
println(P01.last(List(1, 1, 2, 3, 5, 8)))

println(P01.last(List(1)))

println(P01.last(List()))
