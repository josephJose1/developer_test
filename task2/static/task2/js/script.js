var behavior = false
var nColumn = 0

function sortTable(n) {
  console.log("WE ARE HERE!!")
    var table, rows, switching, i, x, y, shouldSwitch,dir, switchcount=0;
    table = document.getElementById("myTable");
    switching = true;
    //other var
    var tableFoot, rowFoot, myVar

    /*parse value from html*/
    n=parseInt(n)
    //extract datatype from tfoot
    tableFoot = document.getElementById("mytfoot");
    rowFoot = tableFoot.rows;
    myVar = rowFoot[0].getElementsByTagName("TD")[n-1]
    //console.log(myVar.textContent)
    // Set the sorting direction to ascending:
    dir = "asc";
    /*Make a loop that will continue until
    no switching has been done:*/
    while (switching) {
      //start by saying: no switching is done:
      switching = false;
      rows = table.rows;
      /*Loop through all table rows (except the
      first, which contains table headers):*/
      for (i = 1; i < (rows.length - 2); i++) {
        //start by saying there should be no switching:
        shouldSwitch = false;
        /*Get the two elements you want to compare,
        one from current row and one from the next:*/
        x = rows[i].getElementsByTagName("TD")[n-1];
        y = rows[i + 1].getElementsByTagName("TD")[n-1];
        /*check if the two rows should switch place:
        based on the direction, asc or desc: */
        if(myVar.textContent === 'number' || myVar.textContent === 'integer'){
          if (dir == "asc") {
            if (Number(x.innerHTML) > Number(y.innerHTML)) {
              //if so, mark as a switch and break the loop:
              shouldSwitch = true;
              break;
            }
          } else if (dir == "desc") {
            if (Number(x.innerHTML) < Number(y.innerHTML)) {
              //if so, mark as a switch and break the loop:
              shouldSwitch = true;
              break;
            }
          }
        }
        else if(myVar.textContent === 'string'){
          if (dir == "asc") {
            if (x.innerHTML.toLowerCase() > y.innerHTML.toLowerCase()) {
              // If so, mark as a switch and break the loop:
              shouldSwitch = true;
              break;
            }
          } else if (dir == "desc") {
            if (x.innerHTML.toLowerCase() < y.innerHTML.toLowerCase()) {
              // If so, mark as a switch and break the loop:
              shouldSwitch = true;
              break;
            }
          }
        }
      }
      if (shouldSwitch) {
        /*If a switch has been marked, make the switch
        and mark that a switch has been done:*/
        rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
        switching = true;
        // Each time a switch is done, increase this count by 1:
        switchcount ++;
      } else {
        /* If no switching has been done AND the direction is "asc",
        set the direction to "desc" and run the while loop again. */
        if (switchcount == 0 && dir == "asc") {
          dir = "desc";
          switching = true;
        }
      }
    }
  }
  /*filter and search */
function myFunction() {
  //test
  console.log("in my function")

  // Declare variables
  var input, filter, table, tr, td, i, txtValue;
  input = document.getElementById("myInput2");
  filter = input.value.toUpperCase();
  table = document.getElementById("myTable");
  tr = table.getElementsByTagName("tr");

  // Loop through all table rows, and hide those who don't match the search query
  for (i = 0; i < tr.length; i++) {
    td = tr[i].getElementsByTagName("td")[3];
    if (td) {
      txtValue = td.textContent || td.innerText;
      if (txtValue.toUpperCase().indexOf(filter) > -1) {
        tr[i].style.display = "";
      } else {
        tr[i].style.display = "none";
      }
    }
  }
}

function myFunctionFilter() {
    // Declare variables
    var input, filter, table, tr, td, i;
    input = document.getElementById("myInput2");
    filter = input.value.toUpperCase();
    table = document.getElementById("myTable");
    tr = table.getElementsByTagName("tr");
    th = table.getElementsByTagName("th");
    
     //depend of selection
    // Loop through all table rows and cols, and hide those who don't match the search query
    for (i = 0; i < tr.length; i++) {
      if (behavior===false){
        console.log("searching by all")
        for(j = 0; j< th.length; j++){
          td = tr[i].getElementsByTagName("td")[j];
          if (myFunctionCatchTd(td,tr,input,i)){
            break
          }
        }
      }else{
        td = tr[i].getElementsByTagName("td")[nColumn];//column 0, seach by id
        console.log("searching by column")
        myFunctionCatchTd(td,tr,input,i)
      }
    }
  }

function myFunctionCatchTd(td,tr,input,i) {
    var txtValue
    filter = input.value.toUpperCase();
    if (td) {
      txtValue = td.textContent || td.innerText;
      if (txtValue.toUpperCase().indexOf(filter) > -1) {
        tr[i].style.display = "";
        return true
      } else {
        tr[i].style.display = "none";
        return false
      }      
    
  }
}
function myFun(n){
  var b, opts, txt1, opts, current
  b = document.querySelector("select");
  opts = b.getElementsByTagName("option")
  current = opts[n]

  //verifier 
  myVerifier(n)

  //verify that elements doesn't has attribute selected
  if(!current.hasAttribute("selected")){
    for(var j=0;j< opts.length;j++){
      if(opts[j].hasAttribute("selected")){ 
        opts[j].removeAttribute("selected")
        current.setAttribute("selected","")
        break
      }
    }
  }
  opts[n].textContent
  input = document.getElementById("myInput2");
  txt1 = "Search by "
  input.setAttribute("placeholder", txt1.concat(" ", String(opts[n].textContent)));
}

function myVerifier(n){
  if(n!=0){
    behavior = true
    console.log("Here we are",n)
    nColumn = n-1
  }
  else{
    behavior = false
  }
}