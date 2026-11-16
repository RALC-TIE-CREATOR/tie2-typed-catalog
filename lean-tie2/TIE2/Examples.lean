import TIE2.Catalog

namespace TIE2

def dimTMinus2 : Dim := { l := 0, t := -2, r := 0, v := 0, wb := 0, gr := 0 }
def dimL4 : Dim := { l := 4, t := 0, r := 0, v := 0, wb := 0, gr := 0 }
def dimR2 : Dim := { l := 0, t := 0, r := 2, v := 0, wb := 0, gr := 0 }

example : dimTMinus2.admissibleB = false := by native_decide
example : dimL4.admissibleB = false := by native_decide
example : dimR2.admissibleB = false := by native_decide

example : catalog254.length = 254 := by native_decide
example : catalog254.all (fun e => e.dim.admissibleB) = true := by native_decide

end TIE2
