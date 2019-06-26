// P03 (*) Find the Kth element of a list.
//     By convention, the first element in the list is element 0.
//
//     Example:
//     scala> nth(2, List(1, 1, 2, 3, 5, 8))
//     res0: Int = 2

object P03 {
  def nth[A](n: Int, ls: List[A]): A =
    if (n >= 0) ls(n)
    else throw new NoSuchElementException


  def nthRec[A](n: Int, ls: List[A]): A = (n, ls) match {
    case (0, h :: _ ) => h
    case (n, _ :: tail) => nthRec(n-1, tail)
    case (_, Nil) => throw new NoSuchElementException
  }
}


println(P03.nth(2, List(1, 1, 2, 3, 5, 8)))
println(P03.nth(0, List(1)))