// P11 (*) Modified run-length encoding.
//     Modify the result of problem P10 in such a way that if an element has no
//     duplicates it is simply copied into the result list.  Only elements with
//     duplicates are transferred as (N, E) terms.
//
//     Example:
//     scala> encodeModified(List('a, 'a, 'a, 'a, 'b, 'c, 'c, 'a, 'a, 'd, 'e, 'e, 'e, 'e))
//     res0: List[Any] = List((4,'a), 'b, (2,'c), (2,'a), 'd, (4,'e))

object P09 {
  def pack[A](ls: List[A]): List[List[A]] = {
    if (ls.isEmpty) List(List())
    else {
      val (packed, next) = ls span(_ == ls.head)
      if (next == Nil) List(packed)
      else packed :: pack(next)
    }
  }
}

object P10 {
  import P09.pack
  def encode[A](ls: List[A]): List[(Int, A)] = 
    pack(ls) map {e => (e.length, e.head)}
}

object P11 {
  import P10.encode
  def encode11[A](ls: List[A]): List[Any] = 
    encode(ls) map {t => if (t._1 == 1) t._2 else t}
}

println(P11.encode11(List('a, 'a, 'a, 'a, 'b, 'c, 'c, 'a, 'a, 'd, 'e, 'e, 'e, 'e)))