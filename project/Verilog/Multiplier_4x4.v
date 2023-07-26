`timescale 1ns/10ps

`include "Adder_4.v"

module Multiplier_4x4 (Product,A,B);

input [3:0] A;
input [3:0] B;
output [7:0] Product;
wire w1;
wire [3:0] wire1;
wire [3:0] wire2;
wire [3:0] wire3;
wire [3:0] wire4;
wire [4:0] wire5;
wire [4:0] wire6;

and inst1(Product[0],A[0],B[0]);
and inst2(wire1[0],A[0],B[1]);
and inst3(wire1[1],A[0],B[2]);
and inst4(wire1[2],A[0],B[3]);
not inst5(w1,A[0]);
and inst6(wire1[3],A[0],w1);

and inst7(wire2[0],A[1],B[0]);
and inst8(wire2[1],A[1],B[1]);
and inst9(wire2[2],A[1],B[2]);
and inst10(wire2[3],A[1],B[3]);

Adder_4 inst11(wire5[3:0],wire5[4],wire1[3:0],wire2[3:0]);

and inst12(wire3[0],A[2],B[0]);
and inst13(wire3[1],A[2],B[1]);
and inst14(wire3[2],A[2],B[2]);
and inst15(wire3[3],A[2],B[3]);
or inst16(Product[1],wire5[0],wire5[0]);

Adder_4 inst17(wire6[3:0],wire6[4],wire5[4:1],wire3[3:0]);

and inst18(wire4[0],A[3],B[0]);
and inst19(wire4[1],A[3],B[1]);
and inst20(wire4[2],A[3],B[2]);
and inst21(wire4[3],A[3],B[3]);
or inst22(Product[2],wire6[0],wire6[0]);

Adder_4 inst23(Product[6:3],Product[7],wire6[4:1],wire4[3:0]);

endmodule
