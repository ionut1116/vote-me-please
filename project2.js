<code>&lt;html&gt;
&lt;head&gt;
&lt;script&gt;
function loadFile() {
  var file = document.getElementById("file").files[0];
  var reader = new FileReader();
  reader.onload = function(e) {
    var text = reader.result;
    var lines = text.split("\n");
    for(var i = 0;i&lt;lines.length;i++) {
      var cells = lines[i].split("\t");
      var table = document.getElementById("table");
      var row = table.insertRow(i);
      var cell1 = row.insertCell(0);
      var cell2 = row.insertCell(1);
      cell1.innerHTML = cells[0];
      cell2.innerHTML = cells[1];
    }
  }
  reader.readAsText(file);
}
&lt;/script&gt;
&lt;/head&gt;
&lt;body&gt;
&lt;input type="file" id="file" onchange="loadFile()"&gt;&lt;br&gt;&lt;br&gt;
&lt;table id="table"&gt;
&lt;tr&gt;
&lt;th&gt;Name&lt;/th&gt;
&lt;th&gt;Address&lt;/th&gt;
&lt;/tr&gt;
&lt;/table&gt;
&lt;/body&gt;
&lt;/html&gt;
</code>