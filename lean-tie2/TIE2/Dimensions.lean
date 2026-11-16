namespace TIE2

structure Dim where
  l : Int
  t : Int
  r : Int
  v : Int
  wb : Int
  gr : Int
deriving Repr, DecidableEq

def inRangeB (x lo hi : Int) : Bool :=
  decide (lo ≤ x ∧ x ≤ hi)

def inUnitB (x : Int) : Bool :=
  decide (x = -1 ∨ x = 0 ∨ x = 1)

def Dim.admissibleB (d : Dim) : Bool :=
  inRangeB d.l (-3) 3 && inUnitB d.t && inUnitB d.r &&
  inUnitB d.v && inUnitB d.wb && inUnitB d.gr

inductive Kind
  | primitive
  | quantity
  | process
  | relation
  | candidate
deriving Repr, DecidableEq

inductive Tensor
  | scalar
  | vector
  | pseudovector
  | tensor
deriving Repr, DecidableEq

inductive Status
  | standard
  | etiqueta
  | bridge
  | candidate
deriving Repr, DecidableEq

structure Entry where
  id : String
  level : Nat
  expression : String
  unit : String
  dim : Dim
  kind : Kind
  tensor : Tensor
  status : Status
  source : String
deriving Repr

end TIE2
