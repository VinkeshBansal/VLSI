`timescale 1ns/10ps

`include "Full_Adder.v"

module Adder_4 (Sum, Carry, A, B);

input [3:0] A;
input [3:0] B;
output [3:0] Sum;
output Carry;
wire x1,x2,x3;

Half_Adder inst1(Sum[0],x1,A[0],B[0]);
Full_Adder inst2(Sum[1],x2,A[1],B[1],x1);
Full_Adder inst3(Sum[2],x3,A[2],B[2],x2);
Full_Adder inst4(Sum[3],Carry,A[3],B[3],x3);

endmodule
