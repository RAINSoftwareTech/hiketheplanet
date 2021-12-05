import { CommonModule } from '@angular/common';
import { HttpClient, HttpClientModule } from '@angular/common/http';
import { APP_INITIALIZER, NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';

import { tap } from 'rxjs';

import { LibHikesModule } from 'lib-hikes';
import { LibMapModule } from 'lib-map';
import { LibSearchModule } from 'lib-search';
import { LibToolsModule } from 'lib-tools';
import { VendorsModule } from 'vendors';

import {environment} from '../environments/environment';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { FooterComponent } from './footer/footer.component';
import { HeaderComponent } from './header/header.component';
import { MappedTrailheadsComponent } from './mapped-trailheads/mapped-trailheads.component';
import { MenuComponent } from './menu/menu.component';


export function init_app(http: HttpClient) {
  const url = `${environment.baseAPIURL}/endpoints/`;
  const cacheOptions = {
    cacheKey: 'users:authUrls',
    cacheExpires: 5 * 24 * 60 * 60  // 5 days in seconds
  };
  // TODO: NEED TO HANDLE NO RESPONSE/FAILURE TO ALLOW VISUAL ELEMENTS TO LOAD WITH ERROR ALERT
  return () => {
    // @ts-ignore
    return http.get(url, {params: {cacheOptions}})
      .pipe(tap(urls => environment.baseUrls = urls));
  };
}

@NgModule({
  declarations: [
    AppComponent,
    HeaderComponent,
    FooterComponent,
    MappedTrailheadsComponent,
    MenuComponent
  ],
  imports: [
    HttpClientModule,
    BrowserModule,
    CommonModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    VendorsModule,
    LibMapModule,
    LibHikesModule,
    LibSearchModule,
    LibToolsModule,
    VendorsModule,
  ],
  providers: [
    {provide: APP_INITIALIZER, useFactory: init_app, deps: [HttpClient], multi: true},
    {provide: 'environment', useValue: environment},
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
