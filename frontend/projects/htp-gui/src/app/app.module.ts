import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';

import { LibHikesModule } from 'lib-hikes';
import { LibMapModule } from 'lib-map';
import { LibSearchModule } from 'lib-search';
import { LibToolsModule } from 'lib-tools';
import { VendorsModule } from 'vendors';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { FooterComponent } from './footer/footer.component';
import { HeaderComponent } from './header/header.component';
import { MappedTrailheadsComponent } from './mapped-trailheads/mapped-trailheads.component';
import { MenuComponent } from './menu/menu.component';

@NgModule({
  declarations: [
    AppComponent,
    HeaderComponent,
    FooterComponent,
    MappedTrailheadsComponent,
    MenuComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    VendorsModule,
    LibMapModule,
    LibHikesModule,
    LibSearchModule,
    LibToolsModule,
    VendorsModule,
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
