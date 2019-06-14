// P02 (*) Find the last but one element of a list.
//     Example:
//     scala> penultimate(List(1, 1, 2, 3, 5, 8))
//     res0: Int = 5

object P02 {
  def penultimate[A](ls: List[A]): A = 
  if (ls.isEmpty) throw new NoSuchElementException
  else ls.init.last
  
  def penultimateRec[A](ls: List[A]): A = ls match {
    case h :: _ :: Nil => h
    case _ :: tail => penultimateRec(tail)
    case _ => throw new NoSuchElementException
  }
}

// Test cases
println(P02.penultimate(List(1, 1, 2, 3, 5, 8)))

println(P02.penultimate(List(5, 8)))

println(P02.penultimate(List(8)))
