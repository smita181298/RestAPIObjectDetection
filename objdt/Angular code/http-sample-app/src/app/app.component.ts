import {Component, OnInit} from '@angular/core';
import {Observable} from "rxjs/Observable";
import {HttpClient, HttpEventType, HttpHeaders, HttpParams, HttpRequest} from "@angular/common/http";
import * as _ from 'lodash';


interface Course {
    description: string;
    courseListIcon: string;
    iconUrl: string;
    longDescription: string;
    url: string;
}


@Component({
    selector: 'app-root',
    templateUrl:"app.component.html",
    styleUrls:["app.component.css"]

})
export class AppComponent implements OnInit {


    constructor(private http: HttpClient) {

    }
    fileToUpload:any;
    gettingit:any = false;
    values:any;
        image_path:any;
        imageSrc:any;
        variable = 0;
    ngOnInit() {

       


    }

   

    httpPostExample(event: any) {

        if (event.target.files && event.target.files[0]) {
        const file = event.target.files[0];

        const reader = new FileReader();
        reader.onload = e => this.imageSrc = reader.result;

        reader.readAsDataURL(file);
    }
   this.variable = 1;
                this.gettingit = true;

         let filesystem =  event.target.files;
        this.fileToUpload = filesystem.item(0);
        let formData:FormData = new FormData();
        formData.append("file", this.fileToUpload, this.fileToUpload.name);
         // console.log(formData);
        this.http.post("http://127.0.0.1:5000/getImageDetails", formData).subscribe((val) => {
                this.values = val;
                this.gettingit = false;
            console.log(val)
        });

    }



   


}