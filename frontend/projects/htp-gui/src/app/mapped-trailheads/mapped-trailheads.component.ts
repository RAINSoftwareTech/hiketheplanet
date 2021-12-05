import { BreakpointObserver } from '@angular/cdk/layout';
import { Component, OnInit } from '@angular/core';

import { Observable } from 'rxjs';

import { TrailheadListService } from 'lib-hikes';

@Component({
  selector: 'app-mapped-trailheads',
  templateUrl: './mapped-trailheads.component.html',
  styleUrls: ['./mapped-trailheads.component.css', '../app.component.css']
})
export class MappedTrailheadsComponent implements OnInit {
  isLoading$?: Observable<boolean>;
  isMobile = true;
  panelOpen = true;
  showMap = true;
  showList = false;

  constructor(private breakpointObserver: BreakpointObserver,
              private trailheads: TrailheadListService) { }

  ngOnInit() {
    this.breakpointObserver.observe('(max-width: 599px)').subscribe(result => {
      this.isMobile = result.matches;
    });
    this.isLoading$ = this.trailheads.getLoadingStatus();
  }

  togglePanel() {
    this.panelOpen = !this.panelOpen;
  }

  showMobileMap() {
    this.showMap = true;
    this.showList = false;
  }

  showMobileList() {
    this.showList = true;
    this.showMap = false;
  }

}
