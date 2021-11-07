import { CommonModule } from '@angular/common';
import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { RouterModule } from '@angular/router';

import { VendorsModule } from 'vendors';

import { HikeMinimalComponent } from './hike-minimal/hike-minimal.component';
import { HikeComponent } from './hike/hike.component';
import { TrailheadListComponent } from './trailhead-list/trailhead-list.component';
import { TrailheadComponent } from './trailhead/trailhead.component';



@NgModule({
  declarations: [
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
  exports: [TrailheadListComponent]
})
export class LibHikesModule { }
