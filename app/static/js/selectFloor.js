const dateBook = document.getElementById("date-book")
dateBook.addEventListener("change", function() {
  let dateBookInfo = document.getElementById("date-book-info")
  dateBookInfo.value = dateBook.value
})

// const selectCaHoc = document.getElementById("select-ca-hoc")
// selectCaHoc.addEventListener("change", function(){
//  getCaHoc(parseInt(this.value))
// })

window.onload = function(){
 getCaHoc(parseInt(1))
}


function getCaHoc(caHocId){
  fetch(`/api/get_ca_hoc/${caHocId}`, {
    method : "post",
    body : JSON.stringify({
      "id" : caHocId
    }),
    headers: {
      'Content-Type': 'application/json'
    }
  }).then(res => res.json()).then(data => {
    let startTime = document.getElementById("start-time-book")
    let endTime = document.getElementById("end-time-book")
    startTime.value = data.gio_bat_dau
    endTime.value = data.gio_ket_thuc
  })
}