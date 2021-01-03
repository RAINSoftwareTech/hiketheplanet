import { CommonModule } from '@angular/common';
import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { RouterModule } from '@angular/router';

import { VendorsModule } from 'vendors';

import { HikeComponent } from './hike/hike.component';
import { LibHikesComponent } from './lib-hikes.component';
import { TrailheadListComponent } from './trailhead-list/trailhead-list.component';
import { TrailheadComponent } from './trailhead/trailhead.component';
import { HikeMinimalComponent } from './hike-minimal/hike-minimal.component';



@NgModule({
  declarations: [
    LibHikesComponent,
    TrailheadComponent,
    HikeComponent,
    TrailheadListComponent,
    HikeMinimalComponent
  ],
  imports: [
    CommonModule,
    VendorsModule,
    RouterModule,
    BrowserModule
  ],
  exports: [LibHikesComponent, TrailheadListComponent]
})
export class LibHikesModule { }
