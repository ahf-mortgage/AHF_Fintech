

// for loan above limit
// bps
const D7 = document.getElementById('D7').innerHTML
const E5 = "{{gci}}"
const E6 = document.getElementById('E6')
if (Number.parseFloat(D7) > 0) {
  E6.innerHTML = ` $\ ${(Number.parseFloat(E5) / Number.parseFloat(D7) * 10000).toLocaleString()}`
} else {
  E6.innerHTML = 0
}

// bps
const D8 = document.getElementById('D8').innerHTML
const E8 = document.getElementById('E8')
if (Number.parseFloat(D8) > 0) {
  E8.innerHTML = ` $\ ${(Number.parseFloat(E5) / Number.parseFloat(D8) * 10000).toLocaleString()}`
} else {
  E8.innerHTML = 0
}

// bps
const D9 = document.getElementById('D9').innerHTML
const E9 = document.getElementById('E9')
if (Number.parseFloat(D9) > 0) {
  E9.innerHTML = ` $\ ${(Number.parseFloat(E5) / Number.parseFloat(D9) * 10000).toLocaleString()}`
} else {
  E9.innerHTML = 0
}

// bps
const D10 = document.getElementById('D10').innerHTML
const E10 = document.getElementById('E10')
if (Number.parseFloat(D10) > 0) {
  E10.innerHTML = ` $\  ${(Math.round(Number.parseFloat(E5) / Number.parseFloat(D10) * 10000)).toLocaleString()}`
} else {
  E10.innerHTML = 0
}

// bps
const D11 = document.getElementById('D11').innerHTML


// loan amount
const E11 = document.getElementById('E11')
if (Number.parseFloat(D11) > 0) {
  // loan amount
  E11.innerHTML = ` $\  ${(Math.round(Number.parseFloat(E5) / Number.parseFloat(D11) * 10000)).toLocaleString()}`
} else {
  // loan amount
  E11.innerHTML = 0
}


// bps
const D12 = document.getElementById('D12').innerHTML
// loan amount
const E12 = document.getElementById('E12')
if (Number.parseFloat(D12) > 0) {
  // loan amount
  E12.innerHTML = ` $\  ${(Math.round(Number.parseFloat(E5) / Number.parseFloat(D12) * 10000)).toLocaleString()}`
} else {
  // loan amount
  E12.innerHTML = 0
}


// bps
const D13 = document.getElementById('D13').innerHTML
// loan amount
const E13 = document.getElementById('E13')
if (Number.parseFloat(D13) > 0) {
  // loan amount
  E13.innerHTML = ` $\  ${(Math.round(Number.parseFloat(E5) / Number.parseFloat(D13) * 10000)).toLocaleString()}`
} else {
  // loan amount
  E13.innerHTML = 0
}



// bps
const D14 = document.getElementById('D14').innerHTML
// loan amount
const E14 = document.getElementById('E14')
if (Number.parseFloat(D14) > 0) {
  // loan amount
  E14.innerHTML = ` $\  ${(Math.round(Number.parseFloat(E5) / Number.parseFloat(D14) * 10000)).toLocaleString()}`
} else {
  // loan amount
  E14.innerHTML = 0
}




const ahf_commission_amount = Number.parseFloat("{{ahf_commission_amount}}")
// AHF
const F7 = document.getElementById("F7")
F7.innerText = `${Math.round(D7 * ahf_commission_amount)}`

// AHF
const F8 = document.getElementById("F8")
F8.innerText = `${Math.round(D8 * ahf_commission_amount)}`

const F9 = document.getElementById("F9")
F9.innerText = `${Math.round(D9 * ahf_commission_amount)}`

// AHF
const F10 = document.getElementById("F10")
F10.innerText = `${Math.round(D10 * ahf_commission_amount)}`

// AHF
const F11 = document.getElementById("F11")
F11.innerText = `${Math.round(D11 * ahf_commission_amount)}`

// AHF
const F12 = document.getElementById("F12")
F12.innerText = `${Math.round(D12 * ahf_commission_amount)}`
// AHF
const F13 = document.getElementById("F13")
F13.innerText = `${Math.round(D13 * ahf_commission_amount)}`

// AHF
const F14 = document.getElementById("F14")
F14.innerText = `${Math.round(D14 * ahf_commission_amount)}`









// branch logic
const branch_commission_amount = Number.parseFloat("{{branch_commission_amount}}")
const G7 = document.getElementById("G7")
G7.innerText = `${Math.round(D7 * branch_commission_amount)}`

// Branch
const G8 = document.getElementById("G8")
G8.innerText = `${Math.round(D8 * branch_commission_amount)}`

// Branch
const G9 = document.getElementById("G9")
G9.innerText = `${Math.round(D9 * branch_commission_amount)}`

// Branch
const G10 = document.getElementById("G10")
G10.innerText = `${Math.round(D10 * branch_commission_amount)}`

// Branch
const G11 = document.getElementById("G11")
G11.innerText = `${Math.round(D11 * branch_commission_amount)}`

// Branch
const G12 = document.getElementById("G12")
G12.innerText = `${D12 * branch_commission_amount}`

// Branch
const G13 = document.getElementById("G13")
G13.innerText = `${D13 * branch_commission_amount}`

// Branch
const G14 = document.getElementById("G14")
G14.innerText = `${D14 * branch_commission_amount}`

// for loan below limit
// gci=   (comp_plan.Percentage * 100) * loan_break_point.loan_break_point / 10000 + comp_plan.Flat_Fee
// max = $B$7
//=IF($E$21*D23/10000+$B$3 < $B$7,$E$21*D23/10000+$B$3,$B$7)

const loan_below_limits_raw = "{{loan_below_limits}}"
const MAX_GCI = Number.parseFloat("{{comp_plan_for_lower_limit.MAX_GCI}}")

const loan_below_limits = JSON.parse(loan_below_limits_raw);
const comp_plan_percentage = Number.parseFloat("{{comp_plan_for_lower_limit.Percentage}}")




for (let num of loan_below_limits) {
  const D2 = document.getElementById(`D2_${num}`)
  const F2 = document.getElementById(`F2_${num}`)
  const H2 = document.getElementById(`H2_${num}`)
  let branch_share = 0
  let ahf_share = 0

  const gci_result = (comp_plan_percentage * 100) * num / 10000 + Number.parseFloat("{{comp_plan_for_lower_limit.Flat_Fee}}")
  const branch_amount = (Number.parseFloat("{{branch_amount}}") / 100)//Number.parseFloat("{{branch_commission_amount}}")
  const ahf_amount = 1 - (Number.parseFloat("{{branch_amount}}") / 100)

  if (gci_result < MAX_GCI) {
    D2.innerText = (gci_result).toLocaleString()
    branch_share = (gci_result * branch_amount)
    ahf_share = (gci_result * ahf_amount)
  }
  else {
    D2.innerText = MAX_GCI.toLocaleString()
    branch_share = MAX_GCI * branch_amount
    ahf_share = MAX_GCI * ahf_amount
  }
  F2.innerText = ahf_share.toLocaleString()
  H2.innerHTML = `<p class='font-bold'> ${branch_share.toLocaleString()} </p>`

}

