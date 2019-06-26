// P18 (**) Extract a slice from a list.
//     Given two indices, I and K, the slice is the list containing the elements
//     from and including the Ith element up to but not including the Kth
//     element of the original list.  Start counting the elements with 0.
//
//     Example:
//     scala> slice(3, 7, List('a, 'b, 'c, 'd, 'e, 'f, 'g, 'h, 'i, 'j, 'k))
//     res0: List[Symbol] = List('d, 'e, 'f, 'g)

object P18 {
  def slice[A](start: Int, end: Int, ls: List[A]): List[A] =
  (start, end, ls) match {
    case (_, _, Nil) => Nil
    case (_, e, _) if e <= 0         => Nil
    case (s, e, h :: tail) if s <= 0 => h :: slice(0, e-1, tail)
    case (s, e, h :: tail)           => slice(s-1, e-1, tail)
  }

  def sliceTail[A](start: Int, end: Int, ls: List[A]): List[A] = {
    def sliceR[A](count: Int, curr: List[A], res: List[A]): List[A] =
      (count, curr) match {
        case (_, Nil) => res.reverse
        case (c, h :: tail) if end <= c => res.reverse
        case (c, h :: tail) if start <= c => sliceR(c+1, tail, h :: res)
        case (c, _ :: tail) => sliceR(c+1, tail, res)
      }
    sliceR(0, ls, Nil)
  }

  def sliceTail2[A](start: Int, end: Int, ls: List[A]): List[A] = {
    def sliceR[A](count: Int, curr: List[A], res: List[A]): List[A] = {
      if (curr.isEmpty || count >= end) res.reverse
      else sliceR(count + 1, curr.tail,
        if (count >= start) curr.head :: res
        else res)
    }
    sliceR(0, ls, Nil)
  }

  def sliceFun[A](start: Int, end: Int, ls: List[A]): List[A] = {
    ls drop start take (end - (start max 0))
  }
}

println(P18.slice(3, 7, List('a, 'b, 'c, 'd, 'e, 'f, 'g, 'h, 'i, 'j, 'k)))
println(P18.sliceTail(3, 7, List('a, 'b, 'c, 'd, 'e, 'f, 'g, 'h, 'i, 'j, 'k)))
println(P18.sliceTail2(3, 7, List('a, 'b, 'c, 'd, 'e, 'f, 'g, 'h, 'i, 'j, 'k)))
println(P18.sliceFun(3, 7, List('a, 'b, 'c, 'd, 'e, 'f, 'g, 'h, 'i, 'j, 'k)))
