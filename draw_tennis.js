var width = 800,
    height = 800,
    radius = 0.7 * Math.min(width, height) / 2,
    innerRadius = 0.2 * radius;

var pie = d3.layout.pie()
    .sort(null)
    .value(function(d) { return d.width; });

var tip = d3.tip()
  .attr('class', 'd3-tip')
  .offset([0, 0])
  .html(function(d) {
    return d.data.label + ":\n" + "total: <span style='color:orangered'>" + Math.round(d.data.win_lit) + "</span>"
            + "<br>" + "average/match: <span style='color:orangered'>" + Math.round(d.data.win_avg) + "</span>"
            + "<br>" + "percent: <span style='color:orangered'>" + Math.round(d.data.win_percent * 100) + "</span>";
  });

//lose_avg,name,win_avg,win_percent,win_lit,lose_lit,color
var arc = d3.svg.arc()
  .innerRadius(innerRadius)
  .outerRadius(function (d) { 
    return (radius - innerRadius) * (d.data.win_percent) + innerRadius; 
    //return (radius - innerRadius) * (d.data.score / 100.0) + innerRadius; 

  });

  var arcLabel = d3.svg.arc()
  .innerRadius(radius)
  .outerRadius(function (d) { 
    return (1.1 * radius); 
    //return (radius - innerRadius) * (d.data.score / 100.0) + innerRadius; 

  });

var outlineArc = d3.svg.arc()
        .innerRadius(innerRadius)
        .outerRadius(radius);

var outlineArcLabel = d3.svg.arc()
            .innerRadius(1.3 * radius)
            .outerRadius(1.3 * radius);


var outlineArcLabel = d3.svg.arc()
            .innerRadius(radius)
            .outerRadius(1.3 * radius);

var svg = d3.select("body").append("svg")
    .attr("width", width)
    .attr("height", height)
    .append("g")
    .attr("transform", "translate(" + width / 2 + "," + height / 2 + ")");

svg.call(tip);
d3.csv('aster_data.csv', function(error, data) {
//lose_avg,name,win_avg,win_percent,win_lit,lose_lit,color

  data.forEach(function(d) {
    d.name     =  d.name;
    d.lose_avg  = +d.lose_avg;
    d.win_avg  = +d.win_avg;
    d.color  =  d.color;
    d.win_percent = +d.win_percent;
    //d.width  = +d.weight;
    d.width  = 1;
    d.label  =  d.name;
    d.win_lit = +d.win_lit;
  });
  // for (var i = 0; i < data.score; i++) { console.log(data[i].id) }
  
  var path = svg.selectAll(".solidArc")
      .data(pie(data))
    .enter().append("path")
      .attr("fill", function(d) { return d.data.color; })
      .attr("class", "solidArc")
      .attr("stroke", "gray")
      .attr("d", arc)
      .on('mouseover', tip.show)
      .on('mouseout', tip.hide);

    var pathLabel= svg.selectAll(".solidArcLabel")
      .data(pie(data))
    .enter().append("path")
      .attr("fill", function(d) { return "#cccccc"; })
      .attr("class", "solidArc")
      .attr("stroke", "black")
      .attr("d", arcLabel);
      // .on('mouseover', tip.show)
      // .on('mouseout', tip.hide)


  var outerPath = svg.selectAll(".outlineArc")
      .data(pie(data))
    .enter().append("path")
      .attr("fill", "none")
      .attr("stroke", "gray")
      .attr("id", function(d,i){ return "label_"+ i;})
      .attr("class", "outlineArc")
      .attr("d", outlineArc);  

  var outerPathLabel = svg.selectAll(".outlineArcLabel")
      .data(pie(data))
      .enter().append("pathLabel")
      .attr("fill", "none")
      .attr("stroke", "black")
      .attr("class", "outlineArcLabel")
      .attr("id", "outerpathlabel")
      .attr("d", outlineArcLabel);  

  // calculate the weighted mean score
  // var score = 
  //   data.reduce(function(a, b) {
  //     //console.log('a:' + a + ', b.score: ' + b.score + ', b.weight: ' + b.weight);
  //     return a + (b.score * b.weight); 
  //   }, 0) / 
  //   data.reduce(function(a, b) { 
  //     return a + b.weight; 
  //   }, 0);

  svg.selectAll("labelText")
      .data(data)
        .enter()
        .append('text')
        .attr("x", 45)   //Move the text from the start angle of the arc
        .attr("dy", -8) //Move the text down
        .attr("class", "aster-label")
        .append('textPath')
        .attr('xlink:href', function(d,i){return "#label_" + i;})
        .text(function(d){ return d.label});

  svg.append("svg:text")
    .attr("class", "aster-score")
    .attr("dy", ".35em")
    .attr("text-anchor", "middle") // text-align: right
    .text("Winners VS Losers");

});