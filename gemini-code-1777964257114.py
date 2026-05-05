<!DOCTYPE html>
<html>
<head>
    <title>BMS Smart Trader UI</title>
    <style>
        body {
            font-family: Arial;
            background: #f0f0f0;
        }
        .container {
            width: 90%;
            margin: auto;
        }
        .box {
            width: 30%;
            background: #fff;
            border: 1px solid #999;
            float: left;
            margin: 15px;
        }
        .header {
            background: linear-gradient(#3a5f0b, #1e3d05);
            color: white;
            padding: 8px;
            text-align: center;
            font-weight: bold;
        }
        table {
            width: 100%;
            border-collapse: collapse;
        }
        table, th, td {
            border: 1px solid #ccc;
        }
        th, td {
            padding: 6px;
            text-align: left;
        }
    </style>
</head>

<body>

<div class="container">

    <!-- Sales -->
    <div class="box">
        <div class="header">Sales</div>
        <table>
            <tr><th>SL</th><th>Caption</th><th>Amount</th></tr>
            <tr><td>1</td><td>Cash Sales</td><td>0</td></tr>
            <tr><td>2</td><td>Credit Sales</td><td>0</td></tr>
            <tr><td>3</td><td>Sales Return</td><td>0</td></tr>
        </table>
    </div>

    <!-- Purchase -->
    <div class="box">
        <div class="header">Purchase</div>
        <table>
            <tr><th>SL</th><th>Caption</th><th>Amount</th></tr>
            <tr><td>1</td><td>Cash Purchase</td><td>0</td></tr>
            <tr><td>2</td><td>Credit Purchase</td><td>0</td></tr>
            <tr><td>3</td><td>Purchase Return</td><td>0</td></tr>
        </table>
    </div>

    <!-- Accounts -->
    <div class="box">
        <div class="header">Accounts</div>
        <table>
            <tr><th>SL</th><th>Caption</th><th>Amount</th></tr>
            <tr><td>1</td><td>Receipt</td><td>0</td></tr>
            <tr><td>2</td><td>Payment</td><td>0</td></tr>
        </table>
    </div>

</div>

</body>
</html>
