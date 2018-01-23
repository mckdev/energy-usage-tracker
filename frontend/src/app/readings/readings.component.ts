import { Component, OnInit } from '@angular/core';
import { Reading } from '../reading';
import { ReadingService } from '../reading.service'
import * as d3 from '../_d3';

@Component({
  selector: 'app-readings',
  templateUrl: './readings.component.html',
  styleUrls: ['./readings.component.css']
})
export class ReadingsComponent implements OnInit {
  readings: Reading[];

  usage_per_day: string;
  annual_estimation: string;
  price_per_kWh: number = 0.2323;

  constructor(private readingService: ReadingService) { }

  ngOnInit() {  
  	this.getReadings();
  }

  getReadings() {
  	this.readingService.getReadings()
  	  .subscribe(readings => {
        this.readings = readings;
        this.createGraph();
        this.usage_per_day = this.calculateUsagePerDay();
        this.annual_estimation = this.estimateAnnualUsage();
      })
  }

  createGraph() {
    let margin = {top: 20, right: 20, bottom: 30, left: 50},
        width = 960 - margin.left - margin.right,
        height = 500 - margin.top - margin.bottom;

    let x = d3.scaleTime().range([0, width]);
    let y = d3.scaleLinear().range([height, 0]);

    let xAxis = d3.axisBottom(x);
    let yAxis = d3.axisLeft(y);

    let line = d3.line<{date: Date, value: number}>()
      .x(function(d) { return x(d.date); })
      .y(function(d) { return y(d.value); });

    let svg = d3.select('div#graph').append('svg')
  	  .attr('width', width + margin.left + margin.right)
  	  .attr('height', height + margin.top + margin.bottom)
  	  .append('g')
  	  .attr('transform', 'translate(' + margin.left + ',' + margin.top + ')');
    
    let parseDate = d3.timeParse('%Y-%m-%d %H:%M:%S')

	this.readings.forEach(function(d) {
	  d.date = parseDate(d.date)
	});

	x.domain(d3.extent(this.readings, function(d) { return d.date }));
	y.domain(d3.extent(this.readings, function(d) { return d.value; }));

	svg.append("g")
	  .attr("class", "x axis")
	  .attr("transform", "translate(0," + height + ")")
	  .call(xAxis)
    .append("text")
    .text("Date")
    .style("text-anchor", "end")
    .attr("x", width)
    .attr("y", -6)

	svg.append("g")
	  .attr("class", "y axis")
	  .call(yAxis)
	  .append("text")
	  .attr("transform", "rotate(-90)")
	  .attr("y", 6)
	  .attr("dy", ".71em")
	  .style("text-anchor", "end")
	  .text("Reading value");	 

	svg.append("path")
	  .datum(this.readings)
	  .attr("class", "line")
	  .attr("d", line);	

  }

  treatAsUTC(date) {
    let result = new Date(date);
    result.setMinutes(result.getMinutes()) - result.getTimezoneOffset();
    return result;
  }

  daysBetween(startDate, endDate) {
    let difference =  Math.floor((endDate - startDate) / 86400000); 
    console.log(difference)
    return difference;
  }

  calculateUsagePerDay(): string {
  	let first_reading = this.readings[0]
  	let last_reading = this.readings[this.readings.length-1]
  	let daysBetween = this.daysBetween(first_reading.date, last_reading.date)
    let difference = this.calculateDifference(first_reading.value, last_reading.value)
  	return (Number(difference) / daysBetween).toFixed(1)
  }

  estimateAnnualUsage(): string {
  	return (Number(this.usage_per_day) * 365).toFixed(1)
  }

  calculateDifference(startValue, endValue): string {
  	return (endValue - startValue).toFixed(1)
  }	

  calculatePrice(usage): string {
    let net = usage * this.price_per_kWh
    let gross = net + (net * 0.19)
    return gross.toFixed(2)
  }

}
