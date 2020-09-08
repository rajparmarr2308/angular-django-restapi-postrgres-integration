import { Injectable } from '@angular/core';
import {HttpClient, HttpHeaders} from '@angular/common/http';
import {Observable} from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ApiService {
  
  baseurl='http://127.0.0.1:8000';
  httpHeaders=new HttpHeaders({'Content-Type':'application/json'});
  constructor(private http : HttpClient) { }
  getAllNames(): Observable <any> {
    return this.http.get(this.baseurl+'/data/',
    {headers:this.httpHeaders});
  }
  addData(i): Observable <any> {
    const body={fname:i.fname,lname:i.lname,
     email:i.email,phone:i.phone,
     adress1:i.adress1,adress2:i.adress2,city:i.city,
     state:i.state,zipcode:i.zipcode
    }
    return this.http.post(this.baseurl+'/data/',body,
    {headers:this.httpHeaders});
  }
}
