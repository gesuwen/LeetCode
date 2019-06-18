// P05 (*) Reverse a list.
//     Example:
//     scala> reverse(List(1, 1, 2, 3, 5, 8))
//     res0: List[Int] = List(8, 5, 3, 2, 1, 1)

object P05 {
  def reverse[A](ls: List[A]): List[A] = ls.reverse
  
  // def reverseRec[A](ls: List[A]): List[A] = ls match {
  //   case Nil => Nil
  //   case h :: tail => reverseRec(tail) ::: List(h)
  // }
  
  // def reverseTail[A](ls: List[A]): List[A] = {
  //   def reverseR(res: List[A], curr: List[A]): List[A] = curr match {
  //     case Nil => res
  //     case h :: tail => reverseR(h :: res, tail)
  //   }
  //   reverseR(Nil, ls)
  // }
  
  def reverseFun[A](ls: List[A]): List[A] = ls.foldLeft(List[A]()) {
      (r, h) => h :: r
    }
}

println(P05.reverse(List(1, 1, 2, 3, 5, 8)))