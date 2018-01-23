import { TestBed, inject } from '@angular/core/testing';

import { ReadingService } from './reading.service';

describe('ReadingsService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [ReadingService]
    });
  });

  it('should be created', inject([ReadingService], (service: ReadingService) => {
    expect(service).toBeTruthy();
  }));
});
