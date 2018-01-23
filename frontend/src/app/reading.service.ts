import { HttpClient } from '@angular/common/http';
import { Injectable, isDevMode } from '@angular/core';
import { Observable } from 'rxjs/Observable';
import { catchError, map, tap } from 'rxjs/operators';

import { Reading } from './reading'

@Injectable()
export class ReadingService {
  private readingsUrl = 'api/readings/'

  constructor(private http: HttpClient) { 
  	if(isDevMode()) {
  		this.readingsUrl = 'http://127.0.0.1:8000/api/readings/'
  	}
  }

  getReadings(): Observable<Reading[]> {
  	return this.http.get<Reading[]>(this.readingsUrl)
  	  .pipe(
  	  	tap(readings => console.log(readings))
  	  	)
  }

}
