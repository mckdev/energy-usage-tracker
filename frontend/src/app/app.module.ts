import { HttpClientModule } from '@angular/common/http';
import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { FlexLayoutModule } from '@angular/flex-layout';

import { AppComponent } from './app.component';
import { ReadingsComponent } from './readings/readings.component';

import { ReadingService } from './reading.service'


@NgModule({
  declarations: [
    AppComponent,
    ReadingsComponent
  ],
  imports: [
    FlexLayoutModule,
    BrowserModule,
    HttpClientModule
  ],
  providers: [ReadingService],
  bootstrap: [AppComponent]
})
export class AppModule { }
