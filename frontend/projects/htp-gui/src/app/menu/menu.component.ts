import { Component, OnInit } from '@angular/core';

import { Observable } from 'rxjs';

@Component({
  selector: 'app-menu',
  templateUrl: './menu.component.html',
  styleUrls: ['./menu.component.css']
})
export class MenuComponent implements OnInit {
  user$?: Observable<any>;

  userNavItems = [
    {title: 'Profile', route: '/profile'},
  ];

  hikeNavItems = [
    {title: 'Add New Trailhead', route: '/trailheads/'},
    {title: 'Add New Hike', route: '/hikes/'},
  ];

  constructor() { }

  ngOnInit() {
  }

}
