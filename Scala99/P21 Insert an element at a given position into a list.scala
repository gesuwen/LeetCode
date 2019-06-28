// P21 (*) Insert an element at a given position into a list.
//     Example:
//     scala> insertAt('new, 1, List('a, 'b, 'c, 'd))
//     res0: List[Symbol] = List('a, 'new, 'b, 'c, 'd)

object P21 {
  def insertAt[A](e: A, pos: Int, ls: List[A]): List[A] =
    ls.take(pos) ++ List(e) ++ ls.drop(pos);

  def insertAt2[A](e: A, pos: Int, ls: List[A]): List[A] = ls.splitAt(pos) match {
    case (pre, post) => pre ::: e :: post
  }
}

println(P21.insertAt('new, 1, List('a, 'b, 'c, 'd)))
println(P21.insertAt2('new, 1, List('a, 'b, 'c, 'd)))