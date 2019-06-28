// P22 (*) Create a list containing all integers within a given range.
//     Example:
//     scala> range(4, 9)
//     res0: List[Int] = List(4, 5, 6, 7, 8, 9)

object P22 {
  def rangeBuiltIn(start: Int, end: Int): List[Int] = List.range(start, end + 1)

  def rangeRec(start: Int, end: Int): List[Int] = {
    if (end < start) Nil
    else start :: rangeRec(start + 1, end);
  }

  def rangeTail(start: Int, end: Int): List[Int] = {
    def rangeR(end: Int, res: List[Int]): List[Int] = {
      if (end < start) res
      else rangeR(end - 1, end :: res)
    }
    rangeR(end, Nil)
  }

  def unfoldRight[A, B](s: B)(f: B => Option[(A, B)]): List[A] =
    f(s) match {
      case None => Nil
      case Some((r, n)) => r :: unfoldRight(n)(f)
    }

  def rangeFun(start: Int, end: Int): List[Int] =
    unfoldRight(start) {n =>
      if (n > end) None
      else Some((n, n+1))
    }
}

println(P22.rangeBuiltIn(4, 9))
println(P22.rangeRec(4, 9))
println(P22.rangeTail(4, 9))
println(P22.rangeFun(4, 9))