import { CommonModule } from '@angular/common';
import { NgModule } from '@angular/core';

import { VendorsModule } from 'vendors';

import { HikeComponent } from './hike/hike.component';
import { LibHikesComponent } from './lib-hikes.component';
import { TrailheadListComponent } from './trailhead-list/trailhead-list.component';
import { TrailheadComponent } from './trailhead/trailhead.component';



@NgModule({
  declarations: [
    LibHikesComponent,
    TrailheadComponent,
    HikeComponent,
    TrailheadListComponent
  ],
  imports: [
    CommonModule,
    VendorsModule
  ],
  exports: [LibHikesComponent, TrailheadListComponent]
})
export class LibHikesModule { }
