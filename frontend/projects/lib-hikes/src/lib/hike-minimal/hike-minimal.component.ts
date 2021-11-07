import { Component, Input, OnInit } from '@angular/core';

import { TrailheadHike } from 'lib-api-clients';

@Component({
  selector: 'hikes-hike-minimal',
  templateUrl: './hike-minimal.component.html',
  styleUrls: ['./hike-minimal.component.css']
})
export class HikeMinimalComponent implements OnInit {
  @Input() hike!: TrailheadHike;

  difficultyIcon: string;

  constructor() {
    this.difficultyIcon = `assets/images/${this.hike.difficulty.toLowerCase()}.png`;
  }

  ngOnInit(): void {
  }

}
