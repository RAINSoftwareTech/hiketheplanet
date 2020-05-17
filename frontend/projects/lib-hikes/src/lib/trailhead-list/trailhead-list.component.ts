import { Component, Input, OnInit } from '@angular/core';

@Component({
  selector: 'hikes-trailhead-list',
  templateUrl: './trailhead-list.component.html',
  styleUrls: ['./trailhead-list.component.css']
})
export class TrailheadListComponent implements OnInit {
  @Input() mobileView = false;

  constructor() { }

  ngOnInit() {
  }

}
