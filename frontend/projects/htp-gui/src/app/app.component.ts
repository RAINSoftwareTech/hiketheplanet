/*
copyright (c) 2020 RAIN Software Technologies, LLC.
All rights reserved
..codeauthor::Fable Turas <fable@rainsoftware.tech>

 */
import { Component } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'htp-gui';
  isMap: boolean;

  constructor(private router: Router,) {
      this.isMap = router.isActive('', {paths: 'exact', queryParams: 'exact', fragment: 'ignored', matrixParams: 'ignored'});
  }
}
