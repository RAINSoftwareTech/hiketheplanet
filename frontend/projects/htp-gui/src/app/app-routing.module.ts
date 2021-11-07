import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { HikeComponent, TrailheadComponent } from 'lib-hikes';
import { PageNotFoundComponent } from 'lib-tools';

import { MappedTrailheadsComponent } from './mapped-trailheads/mapped-trailheads.component';

const routes: Routes = [
  {path: 'trailheads/:trailhead-slug', component: TrailheadComponent},
  {path: 'hikes/:hike-slug', component: HikeComponent},
  {path: '', component: MappedTrailheadsComponent},
  {path: '**', component: PageNotFoundComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes, { relativeLinkResolution: 'legacy' })],
  exports: [RouterModule]
})
export class AppRoutingModule { }
