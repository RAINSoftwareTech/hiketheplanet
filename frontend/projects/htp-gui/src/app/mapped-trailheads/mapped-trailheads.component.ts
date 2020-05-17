import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-mapped-trailheads',
  templateUrl: './mapped-trailheads.component.html',
  styleUrls: ['./mapped-trailheads.component.css', '../app.component.css']
})
export class MappedTrailheadsComponent implements OnInit {
  isLoading$;
  isMobile;
  panelOpen = true;
  showMap = true;
  showList = false;

  constructor() { }

  ngOnInit() {
  }

}
