import { Component, Inject, Input, OnInit } from '@angular/core';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.css', '../app.component.css']
})
export class HeaderComponent implements OnInit {
  @Input() sideNav;
  user$;
  showUserLogin = false

  constructor(@Inject('environment') private env) { }

  ngOnInit() {
    this.showUserLogin = !!this.env.baseUrls.login;
  }

}
