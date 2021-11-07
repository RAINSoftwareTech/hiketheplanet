import { Component, Inject, Input, OnInit } from '@angular/core';

import { MatSidenav } from '@angular/material/sidenav';

import { Observable } from 'rxjs';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.css', '../app.component.css']
})
export class HeaderComponent implements OnInit {
  @Input() sideNav!: MatSidenav;
  user$?: Observable<any>;
  showUserLogin = false;

  constructor(@Inject('environment') private env: {[key: string]: any}) { }

  ngOnInit() {
    this.showUserLogin = !!this.env.baseUrls.login;
  }

}
