// P16 (**) Drop every Nth element from a list.
//     Example:
//     scala> drop(3, List('a, 'b, 'c, 'd, 'e, 'f, 'g, 'h, 'i, 'j, 'k))
//     res0: List[Symbol] = List('a, 'b, 'd, 'e, 'g, 'h, 'j, 'k)

object P16 {
  def drop[A](N: Int, ls: List[A]): List[A] = {
    def dropR(c: Int, curr: List[A]): List[A] = (c, curr) match {
      case (_, Nil) => Nil
      case (1, _ :: tail) => dropR(N, tail)
      case (_, h :: tail) => h :: dropR(c-1, tail)
    }
    dropR(N, ls)
  }
  
  def dropFun[A](N: Int, ls: List[A]): List[A] =
    ls.zipWithIndex filter { v => (v._2 + 1) % N != 0} map {_._1}
    
    def dropTailRec[A](N: Int, ls: List[A]): List[A] = {
      def dropR(c: Int, curr: List[A], res: List[A]): List[A] = (c, curr) match {
        case (_, Nil) => res.reverse
        case (1, _ :: tail) => dropR(N, tail, res)
        case (_, h :: tail) => dropR(c - 1, tail, h :: res)
      }
      dropR(N, ls, Nil)
    }
}

println(P16.drop(3, List('a, 'b, 'c, 'd, 'e, 'f, 'g, 'h, 'i, 'j, 'k)))
println(P16.dropFun(3, List('a, 'b, 'c, 'd, 'e, 'f, 'g, 'h, 'i, 'j, 'k)))
println(P16.dropTailRec(3, List('a, 'b, 'c, 'd, 'e, 'f, 'g, 'h, 'i, 'j, 'k)))