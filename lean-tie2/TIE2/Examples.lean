import TIE2.Catalog

namespace TIE2

-- Forbidden exponents: all should be false.

def dimT2 : Dim := { l := 0, t := 2, r := 0, v := 0, wb := 0, gr := 0 }
def dimTMinus2 : Dim := { l := 0, t := -2, r := 0, v := 0, wb := 0, gr := 0 }
def dimL4 : Dim := { l := 4, t := 0, r := 0, v := 0, wb := 0, gr := 0 }
def dimLMinus4 : Dim := { l := -4, t := 0, r := 0, v := 0, wb := 0, gr := 0 }
def dimR2 : Dim := { l := 0, t := 0, r := 2, v := 0, wb := 0, gr := 0 }
def dimRMinus2 : Dim := { l := 0, t := 0, r := -2, v := 0, wb := 0, gr := 0 }
def dimV2 : Dim := { l := 0, t := 0, r := 0, v := 2, wb := 0, gr := 0 }
def dimVMinus2 : Dim := { l := 0, t := 0, r := 0, v := -2, wb := 0, gr := 0 }
def dimWb2 : Dim := { l := 0, t := 0, r := 0, v := 0, wb := 2, gr := 0 }
def dimWbMinus2 : Dim := { l := 0, t := 0, r := 0, v := 0, wb := -2, gr := 0 }
def dimGr2 : Dim := { l := 0, t := 0, r := 0, v := 0, wb := 0, gr := 2 }
def dimGrMinus2 : Dim := { l := 0, t := 0, r := 0, v := 0, wb := 0, gr := -2 }

example : dimT2.admissibleB = false := by native_decide
example : dimTMinus2.admissibleB = false := by native_decide
example : dimL4.admissibleB = false := by native_decide
example : dimLMinus4.admissibleB = false := by native_decide
example : dimR2.admissibleB = false := by native_decide
example : dimRMinus2.admissibleB = false := by native_decide
example : dimV2.admissibleB = false := by native_decide
example : dimVMinus2.admissibleB = false := by native_decide
example : dimWb2.admissibleB = false := by native_decide
example : dimWbMinus2.admissibleB = false := by native_decide
example : dimGr2.admissibleB = false := by native_decide
example : dimGrMinus2.admissibleB = false := by native_decide

-- Allowed boundary cases: should be true.

def dimLMinus3 : Dim := { l := -3, t := 0, r := 0, v := 0, wb := 0, gr := 0 }
def dimL3 : Dim := { l := 3, t := 0, r := 0, v := 0, wb := 0, gr := 0 }
def dimVMinus1 : Dim := { l := 0, t := 0, r := 0, v := -1, wb := 0, gr := 0 }

example : dimLMinus3.admissibleB = true := by native_decide
example : dimL3.admissibleB = true := by native_decide
example : dimVMinus1.admissibleB = true := by native_decide

example : catalog254.length = 254 := by native_decide
example : catalog254.all (fun e => e.dim.admissibleB) = true := by native_decide

end TIE2
