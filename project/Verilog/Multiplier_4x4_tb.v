`timescale 1ns/10ps

module Multiplier_4x4_tb;

reg [3:0] A;
reg [3:0] B;
wire [7:0] Product;


Multiplier_4x4 UUT (Product,A[3:0],B[3:0]);

integer i;

initial
    begin
        $dumpfile("Multiplier_4x4_tb.vcd");
        $dumpvars(0,Multiplier_4x4_tb);

        A=4'b0000; B=4'b0000;
    end
initial
    begin
        for (i=0;i<256; i = i + 1)
            begin
                {B,A} = i;
                #10;
            end
    end

always @(Product)
$display("time =%0t \t A =%4b, B =%4b and Product =%8b",$time,A[3:0], B[3:0], Product[7:0]);

endmodule
