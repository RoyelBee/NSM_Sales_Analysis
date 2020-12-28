
def generate_layout():
    results = """ <!DOCTYPE html>
            <html>
            <head>
                <style>
                    table, th, td {
                        border: 1px solid black;
                        border-collapse: collapse;
                    }

                    table {
                        border: 1px solid black;
                        table-layout: fixed;
                        width: 20000px;
                    }

                    th, td {
                        border: 1px solid black;
                        width: 150px;
                        overflow: hidden;
                    }

                    .central{
                        text-align: center;
                    }

                    th.style1{
                        background-color: #e5f0e5;
                        padding-left: 2px;
                        padding-right: 5px;
                        text-align: right;
                    }
                    .style1{
                        padding-right: 3px;
                        text-align: right;


                    }
                    .number_style{
                        padding-right: 3px;
                        text-align: right;
                        font-size: 12px;   
                        height: 40px;
                    }

                    #number_style2{
                        padding-right: 3px;
                        text-align: right;
                        font-size: 10px;
                        height: 40px;   
                    }

                    .item_sl{
                        width: 60px !important; 
                        background-color: #e5f0e5;
                        padding-right: 3px;
                        text-align: center;
                    }
                    td.serial{
                        width: 60px !important;
                        padding-left: 5px;
                        text-align: center;
                        font-size: 12px;
                    }
                    serial1{
                        padding-left: 5px;
                        text-align: left;
                        font-size: 16px;
                    }
                    .sl_center{
                        padding-left: 5px;
                        text-align: center;
                        font-size: 12px;
                    }

                    #sss{

                        padding-left: 5px;
                        text-align: center;
                        font-size: 10px;
                    }
                    #ssstd{

                        padding-left: 3px;
                        padding-right: 3px;
                        text-align: right;
                        font-size: 10px;
                    }
                    #padding{

                        padding-left: 5px;
                        text-align: right;
                        font-size: 5px;
                    }

                    .serialno{
                        width: 30px !important;
                        padding-left: 5px;
                        text-align: center;
                        font-size: 12px;
                    }
                    .brand {
                        width: 70px !important;
                        background-color: #e5f0e5;
                        font-weight: bold;
                        color: black;
                        text-align: left;
                    }
                    .brandsl {
                        width: 30px !important;
                        background-color: #e5f0e5;
                        font-weight: bold;
                        color: black;
                        text-align: center;
                    }

                    .brandtd {
                        width: 50px !important;
                        text-align: left;
                        padding-left: 2px;
                        font-weight: bold;
                        font-size: 12px;
                        color: black;
                    }
                    .branch_name{
                        text-align: left;
                        padding-left: 2px;
                        font-weight: bold;
                        font-size: 14px;
                        color: black;
                    }

                    #btd {
                        width: 50px !important;
                        text-align: left;
                        padding-left: 2px;
                        font-weight: bold;
                        font-size: 12px;
                        color: black;
                    }

                    .brandtd1 {
                        width: 40px !important;
                        text-align: left;
                        padding-left: 2px;
                        font-weight: bold;
                        font-size: 14px;
                        color: black;

                    }
                    th.style2{
                        background-color: #faeaca;
                    }
                    .remaining{
                        background-color: #faeaca;
                        padding-left: 20px;
                    }
                    .sales_monthly_trend{
                     background-color: #faeaca;
                     padding-left: 20px;

                    }
                    .style3{
                        background-color: #f7e0b3;
                        padding-left: 5px;
                        padding-right: 2px;

                    }
                    td {
                        font-family: "Tohoma";
                        border: 1px solid gray;
                        font-size: 8px;

                    }
                    .branch_bg_color{
                        font-family: "Tohoma";
                        background-color: #a7c496;
                        padding-left: 5px;
                        color: black;
                        padding-right: 2px;
                        text-align: right;
                        font-size: 8px;

                    }
                    td.num_style {
                        text-align: right;
                        border: 1px solid gray;
                        padding-right: 5px;
                        font-size: 10px;
                    }
                    .color_style{
                        padding-left: 10px;
                        padding-top: 5px;
                        padding-bottom: 5px;
                        padding-right: 10px;
                        color: black;
                        width: 25%
                    }
                    .color_style{
                        width: 16.66%;
                        padding-left: 10px;
                        padding-top: 5px;
                        padding-bottom: 10px;
                        padding-right: 10px;
                        font-size: 14px;
                        font-weight: bolder;
                    }
                      .my_rotate {
                            color: red !important;
                      }
                    .nation_wide{

                        text-align: center;
                        padding-right: 2px;
                        border: 1px solid gray;
                        padding-left: 10px;
                        font-weight: bolder;
                        font-size: 12px;
                        color: black;
                    }
                    .description{
                        width: 900px !important;
                        background-color: #e5f0e5;
                        font-size: 12px;
                        color: black;
                    }
                    .description1{
                        width: 250px !important;
                        background-color: #e5f0e5;
                        font-size: 14px;
                        font-weight: bolder;
                        color: black;
                    }
                    .descriptionmain{
                        width: 250px !important;
                        font-size: 12px;
                        color: black;
                    }

                    #descriptionmain2{
                        width: 280px !important;
                        font-size: 10px;
                        color: black;
                    }

                    .y_desc_sales{
                        width: 250px !important;
                        font-size: 12px;
                        font-weight: bold;
                        color: black;
                    }

                    .grand_total{
                        font-size: 15px;
                        font-weight: bolder;
                        color: black;
                    }

                    .descriptiontd{
                        padding-left: 2px;
                        font-size: 14px;
                        font-weight: bolder;
                    }

                    .descriptionmastertd{
                        padding-left: 2px;
                        font-size: 9px;
                    }

                    .uom{
                        background-color: #e5f0e5;
                        font-size: 11px;
                        color: black;

                    }
                    .uom2{
                        text-align:right;
                        font-size: 10px;
                        color: black;
                    }
                    .uom3{
                        background-color: #faeaca;
                        text-align:right;
                        font-size: 11px;
                        color: black;
                    }


                    .my_margin{
                    margin-right: 220px;
                    color: #E5F0E5 !important;
                    }
                    th.avg_sales{
                        width: 500px !important;
                        background-color: #e5f0e5;
                        font-size: 12px;
                        color: black;
                    }
                     td.avg_sales{
                        width: 100% !important;
                        padding-left:5px;
                    }
                    .remarks{
                    padding-left: 1px;
                    padding-right: 1px;
                    text-align: right;
                    font-size: 10px;
                    }

                    .remarks1{
                    padding-left: 1px;
                    padding-right: 1px;
                    text-align: left;
                    font-size: 10px;
                    }
                    .remarks2{
                    padding-left: 1px;
                    padding-right: 1px;
                    text-align: left;
                    font-size: 12px;
                    }
                    .info{
                        background-color: #a9f2e7;
                        font-size: 13px;
                        text-align: left;
                        text-decoration-line: none;
                        color: black;

                    }

                    .banner{
                    width: 800px !important;
                    height: 200px !important;
                    border: 1px solid #0f6674;
                    }

                .float_left {
                    width: 50%;
                    float: left;
                }

                .colors{
                    background-color: #b7fff8;
                    text-align: center;
                    padding-left: 2px;
                    padding-right: 2px;

                }

            .branch_plant_color{
                background-color: antiquewhite;
                padding-left: 2px;
                padding-right: 2px;
            }


        </style>

            </head>
            <body>
                <img src="cid:dash" width="90%"> <br>

                </body>
            </html>
        """
    return results
