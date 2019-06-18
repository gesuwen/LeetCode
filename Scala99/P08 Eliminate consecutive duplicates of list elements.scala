// P08 (**) Eliminate consecutive duplicates of list elements.
//     If a list contains repeated elements they should be replaced with a
//     single copy of the element.  The order of the elements should not be
//     changed.
//
//     Example:
//     scala> compress(List('a, 'a, 'a, 'a, 'b, 'c, 'c, 'a, 'a, 'd, 'e, 'e, 'e, 'e))
//     res0: List[Symbol] = List('a, 'b, 'c, 'a, 'd, 'e)

object P08 {
  // def compress[A](ls: List[A]): List[A] = ls match {
  //   case Nil       => Nil
  //   case h :: tail => h :: compress(tail.dropWhile(_ == h))
  // }
  
  // def compressTail[A](ls: List[A]): List[A] = {
  //   def compressR(res: List[A], curr: List[A]): List[A] = curr match {
  //     case h :: tail => compressR(h :: res, tail.dropWhile(_ == h))
  //     case Nil => res.reverse
  //   }
  //   compressR(Nil, ls)
  // }
  
  def compressFun[A](ls: List[A]): List[A] = {
    ls.foldRight(List[A]()) {
      (h, r) => 
      if (r.isEmpty || r.head != h) h :: r
      else r
    }
  }
}

println(P08.compressFun(List('a, 'a, 'a, 'a, 'b, 'c, 'c, 'a, 'a, 'd, 'e, 'e, 'e, 'e)))