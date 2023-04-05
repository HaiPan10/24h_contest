const dateBook = document.getElementById("date-book")
dateBook.addEventListener("change", function() {
  let dateBookInfo = document.getElementById("date-book-info")
  dateBookInfo.value = dateBook.value
})

const selectCaHoc = document.getElementById("select-ca-hoc")
function changeSelectedTime(gioBatDau, gioKetThuc){
  console.log("hello world")
  let startTime = document.getElementById("start-time-book")
  let endTime = document.getElementById("end-time-book")
  startTime.value = Date.parse(gioBatDau)
  endTime.value = Date.parse(gioKetThuc)
}