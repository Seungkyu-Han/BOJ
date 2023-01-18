# [Gold II] Boggle - 11521 

[문제 링크](https://www.acmicpc.net/problem/11521) 

### 성능 요약

메모리: 2164 KB, 시간: 0 ms

### 분류

백트래킹(backtracking), 브루트포스 알고리즘(bruteforcing), 깊이 우선 탐색(dfs), 그래프 이론(graphs), 그래프 탐색(graph_traversal), 문자열(string)

### 문제 설명

<p>Boggle is a game in which 16 dice with letters on each side are placed into a 4x4 grid. Players then attempt to find words using letters from adjacent dice. You must write a program to find words from letters in a Boggle-like grid.</p>

<p>When forming a word, each letter must be adjacent in the grid (horizontally, vertically, or diagonally) to the previous letter, and each grid position (not necessarily each letter) may only appear once in each word.</p>

<p>In normal Boggle, every side of each die contains a single letter with one exception. No side has the letter q by itself; instead, the 2 letters qu appear together. Similarly, when the letter q appears in one of the grids in this problem's Boggle variant, it should be treated as qu.</p>

### 입력 

 <p>Input consists of a dictionary of words followed by several letter grids.</p>

<p>The first line contains an integer W (1 <= W <= 200) indicating the number of words in the dictionary. Each of the following W lines contains a string of 1 to 25 lowercase ASCII letters (a - z) representing a unique word in the dictionary.</p>

<p>The dictionary is followed by 1 or more letter grids. Each begins with a line containing an integer D (2 <= D <= 8) indicating the size of that grid (square of size D x D) or 0 (zero) indicating end of input. The following D lines each contain D lowercase ASCII letters (a - z); each line represents a row in the grid.</p>

### 출력 

 <p>For each grid, output consists of the following:</p>

<ul>
	<li>A line for each dictionary word that was found in the grid, sorted alphabetically.</li>
	<li>A line containing a dash (-).</li>
</ul>

