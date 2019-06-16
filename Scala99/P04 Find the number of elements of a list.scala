// P04 (*) Find the number of elements of a list.
//     Example:
//     scala> length(List(1, 1, 2, 3, 5, 8))
//     res0: Int = 6

object P04 {
  def length[A](ls: List[A]): Int = ls.length

  // def lengthRec[A](ls: List[A]): Int = ls match {
  //   case Nil => 0
  //   case _ :: tail => 1 + lengthRec(tail)
  // }

  // def lengthTailRec[A](res: Int, ls: List[A]): Int = ls match {
  //   case Nil => res
  //   case _ :: tail => lengthTailRec(res + 1, ls)
  // }

  def lengthFunctional[A](ls: List[A]): Int = ls.foldLeft(0) {
    (c, _) => c + 1
  }
}


// test case
println(P04.length(List(1, 1, 2, 3, 5, 8)))
println(P04.length(List()))
