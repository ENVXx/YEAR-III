%% MCE 431 HW 5 %%
% Elias Newall-Vuillemot | 11/1/2025
clc; close all; clear all;
%% Question 5.7 (a)
sysa = tf([1, 3], [1, 12, 22, 20, 0]);
rlocus(sysa)
%% Question 5.7 (d)
sysD = tf([1, 7, 70, 204], [1, 14, 125, 850, 0, 0]);
rlocus(sysD);
%% Question 5.8 (b)
sysB = tf([1, 2], [1, 10, -1, -10, 0]);
rlocus(sysB);
%% Question 5.8 (f)
sysf = tf([1],[1, 3, 3, -7]);
rlocus(sysf);

