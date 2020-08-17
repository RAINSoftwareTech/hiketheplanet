import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-menu',
  templateUrl: './menu.component.html',
  styleUrls: ['./menu.component.css']
})
export class MenuComponent implements OnInit {
  user$;

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
