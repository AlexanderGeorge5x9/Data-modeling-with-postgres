<div class="_15vzQlp3FJ8f94suLiPCPf ureact-markdown "><h1 id="schema-for-song-play-analysis">Schema for Song Play Analysis</h1>
<p>Using the song and log datasets, you'll need to create a star schema optimized for queries on song play analysis. This includes the following tables.</p>
<h4 id="fact-table">Fact Table</h4>
<ol>
<li><strong>songplays</strong> - records in log data associated with song plays i.e. records with page <code>NextSong</code>  <ul>
<li><em>songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent</em></li>
</ul>
</li>
</ol>
<h4 id="dimension-tables">Dimension Tables</h4>
<ol start="2">
<li><strong>users</strong> - users in the app<ul>
<li><em>user_id, first_name, last_name, gender, level</em></li>
</ul>
</li>
<li><strong>songs</strong> - songs in music database<ul>
<li><em>song_id, title, artist_id, year, duration</em></li>
</ul>
</li>
<li><strong>artists</strong> - artists in music database<ul>
<li><em>artist_id, name, location, latitude, longitude</em></li>
</ul>
</li>
<li><strong>time</strong> - timestamps of records in <strong>songplays</strong> broken down into specific units<ul>
<li><em>start_time, hour, day, week, month, year, weekday</em></li>
</ul>
</li>
</ol>
</div>
<div><div class="index--container--2OwOl"><div class="index--atom--lmAIo layout--content--3Smmq"><div class="ltr"><div class="_15vzQlp3FJ8f94suLiPCPf ureact-markdown "><h1 id="project-template">Project Template</h1>
<p>To get started with the project, go to the workspace on the next page, where you'll find the project template files. You can work on your project and submit your work through this workspace. Alternatively, you can download the project template files from the Resources folder if you'd like to develop your project locally.</p>
<p>In addition to the data files, the project workspace includes six files:</p>
<ol>
<li><code>test.ipynb</code> displays the first few rows of each table to let you check your database.</li>
<li><code>create_tables.py</code> drops and creates your tables. You run this file to reset your tables before each time you run your ETL scripts.</li>
<li><code>etl.ipynb</code> reads and processes a single file from <code>song_data</code> and <code>log_data</code> and loads the data into your tables. This notebook contains detailed instructions on the ETL process for each of the tables.</li>
<li><code>etl.py</code> reads and processes files from <code>song_data</code> and <code>log_data</code> and loads them into your tables. You can fill this out based on your work in the ETL notebook.</li>
<li><code>sql_queries.py</code> contains all your sql queries, and is imported into the last three files above.</li>
<li><code>README.md</code> provides discussion on your project.</li>
</ol>
</div></div><span></span></div><span></span></div></div>