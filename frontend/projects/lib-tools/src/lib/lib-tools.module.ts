import { NgModule } from '@angular/core';
import { LibToolsComponent } from './lib-tools.component';
import { PageNotFoundComponent } from './page-not-found/page-not-found.component';



@NgModule({
  declarations: [LibToolsComponent, PageNotFoundComponent],
  imports: [
  ],
  exports: [LibToolsComponent]
})
export class LibToolsModule { }
