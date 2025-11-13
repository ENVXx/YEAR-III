%% Nusselt Number Calculator: MCE 414 LAB 4
% Elias Newall-Vuillemot 11/12/2025
clc; close all; clear;
%% Setup Parameters
OD = 1.5 * 0.0254;
ID = 1.25 * 0.0254;
L = 7.375 * 0.0254;
rho_air = .8;
%% Experimental Values Import
DATA = importdata('lab4data.csv');
%% Calcs
As_Cyl = pi * (0.5 * (OD^2 + ID^2) + OD * L);
CALCS = [];
% v_inf calcs
CALCS = [CALCS; sqrt(DATA.data(1, :) .* 2 .* (rho_air))];
% Power calcs
CALCS = [CALCS; DATA.data(2, :) .* DATA.data(3, :)];
% T_film calcs
CALCS = [CALCS;0.5 .* (DATA.data(4, :) + DATA.data(5, :)) + 273.15];
% nhu_film calcs
CALCS = [CALCS;(1.04E-10).*(CALCS(3,:).^2) + (3.228E-8) .* CALCS(3,:)...
    - 3.136E-6];
% Prandlt calcs
CALCS = [CALCS;(1.940E-4).*CALCS(3,:) + 0.7673];
% Reynolds number calcs
CALCS = [CALCS;(CALCS(1,:) .* OD) ./ CALCS(4,:)];
% K film calcs
CALCS = [CALCS;(7.64E-5) * CALCS(3,:) + 3.27E-3];
% make a table
CALCS = array2table(CALCS',"VariableNames",["v_inf", "Power", "T_Film", ...
    "nhu_film", "Pr_film", "Re_d", "k_Film"], "RowNames",["200 RPM",...
    "300 RPM", "400 RPM", "500 RPM", "600 RPM"]);
% Nusselt, h, & q Number calcs
a = [0.193, 0.304, 0.158, 0.164, 0.15];
b = [0.618, 0.59, 0.66, 0.638, 0.638];
shapeNames = ["Cylinder", "Diamond", "Square", "Flat-Hex", "Point-Hex"];
for i = 1:length(a)
    Nu = a(i) * power(CALCS.Re_d, b(i)) .* power(CALCS.Pr_film,(1/3));
    % Nusselt
    CALCS = addvars(CALCS, Nu, ...
        NewVariableNames=strcat(shapeNames(i),"_Nusselt"));
    % h
    h = (CALCS{:, end} .* CALCS.k_Film)./OD;
    CALCS = addvars(CALCS, h ...
        , NewVariableNames=strcat(shapeNames(i),"_h"));
    % q
    q = CALCS{:, end} .* As_Cyl .* (CALCS.T_Film - 293.15);
    CALCS = addvars(CALCS, q, NewVariableNames=strcat(shapeNames(i),"_q"));
end






