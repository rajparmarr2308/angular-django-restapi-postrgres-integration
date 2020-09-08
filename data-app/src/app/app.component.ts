import { Component } from '@angular/core';
import { ApiService } from './api.service';
// import { error } from 'console';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
  providers:[ApiService]
})
export class AppComponent {
  names=[{state:'gujarat'},{state:'mumbai'}];
  selectedData;
  
 
  constructor(private api : ApiService){
    this.getNames();      
    this.selectedData={
      id:-1,
      fname:'',
      lname:'',
      email:'',
      phone:'',
      adress1:'',
      adress2:'',
      city:'',
      state:'',
      zipcode:'',
}
  }
  getNames = () => {
       this.api.getAllNames().subscribe(
         data => {
           console.log(data);
           this.names=data;
         },
         error => {
           console.log(error);
         }
       );
  }

  addData = () =>{
    this.api.addData(this.selectedData).subscribe(
      data => {
        console.log(data);
        this.names.push(data);
      },
      error => {
        console.log(error);
      }
    );
  }
}
