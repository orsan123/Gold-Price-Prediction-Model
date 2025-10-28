<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Gold Price Prediction Web App</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: #333;
            background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
            min-height: 100vh;
        }
        
        .container {
            max-width: 1000px;
            margin: 0 auto;
            padding: 20px;
        }
        
        header {
            text-align: center;
            margin-bottom: 40px;
            padding: 30px 0;
            background: white;
            border-radius: 15px;
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        }
        
        h1 {
            color: #2c3e50;
            font-size: 2.5em;
            margin-bottom: 10px;
        }
        
        .tagline {
            color: #7f8c8d;
            font-size: 1.2em;
            margin-bottom: 20px;
        }
        
        .badges {
            display: flex;
            justify-content: center;
            gap: 10px;
            margin-bottom: 20px;
        }
        
        .badge {
            background: #3498db;
            color: white;
            padding: 5px 15px;
            border-radius: 20px;
            font-size: 0.9em;
            font-weight: bold;
        }
        
        .badge.python { background: #3776ab; }
        .badge.flask { background: #000000; }
        .badge.ml { background: #e74c3c; }
        
        .section {
            background: white;
            margin-bottom: 30px;
            padding: 30px;
            border-radius: 15px;
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        }
        
        h2 {
            color: #2c3e50;
            border-bottom: 3px solid #3498db;
            padding-bottom: 10px;
            margin-bottom: 20px;
            display: inline-block;
        }
        
        .steps {
            display: grid;
            gap: 20px;
        }
        
        .step {
            display: flex;
            align-items: flex-start;
            gap: 15px;
        }
        
        .step-number {
            background: #3498db;
            color: white;
            width: 30px;
            height: 30px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: bold;
            flex-shrink: 0;
        }
        
        .step-content {
            flex: 1;
        }
        
        code {
            background: #2c3e50;
            color: #ecf0f1;
            padding: 15px;
            border-radius: 8px;
            display: block;
            margin: 10px 0;
            font-family: 'Courier New', monospace;
            overflow-x: auto;
        }
        
        .file-structure {
            background: #34495e;
            color: #ecf0f1;
            padding: 20px;
            border-radius: 8px;
            font-family: 'Courier New', monospace;
            line-height: 1.8;
        }
        
        .folder {
            color: #3498db;
            font-weight: bold;
        }
        
        .file {
            color: #ecf0f1;
            margin-left: 20px;
        }
        
        .features-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
            margin-top: 20px;
        }
        
        .feature {
            text-align: center;
            padding: 20px;
            background: #f8f9fa;
            border-radius: 10px;
            border-left: 4px solid #3498db;
        }
        
        .feature-icon {
            font-size: 2em;
            margin-bottom: 10px;
        }
        
        .tech-stack {
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
            margin-top: 15px;
        }
        
        .tech-item {
            background: #ecf0f1;
            padding: 8px 15px;
            border-radius: 20px;
            font-size: 0.9em;
        }
        
        .note {
            background: #fff3cd;
            border-left: 4px solid #ffc107;
            padding: 15px;
            margin: 20px 0;
            border-radius: 0 8px 8px 0;
        }
        
        footer {
            text-align: center;
            margin-top: 40px;
            padding: 20px;
            color: #7f8c8d;
            border-top: 1px solid #bdc3c7;
        }
        
        @media (max-width: 768px) {
            .container {
                padding: 10px;
            }
            
            h1 {
                font-size: 2em;
            }
            
            .section {
                padding: 20px;
            }
            
            .features-grid {
                grid-template-columns: 1fr;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>Gold Price Prediction Web App</h1>
            <p class="tagline">A simple Flask web application that predicts gold prices using machine learning</p>
            <div class="badges">
                <span class="badge python">Python</span>
                <span class="badge flask">Flask</span>
                <span class="badge ml">Machine Learning</span>
            </div>
        </header>

        <section class="section">
            <h2>🚀 Quick Start</h2>
            <div class="steps">
                <div class="step">
                    <div class="step-number">1</div>
                    <div class="step-content">
                        <h3>Install Requirements</h3>
                        <code>pip install flask pandas joblib prophet</code>
                    </div>
                </div>
                
                <div class="step">
                    <div class="step-number">2</div>
                    <div class="step-content">
                        <h3>Run the Application</h3>
                        <code>python app.py</code>
                    </div>
                </div>
                
                <div class="step">
                    <div class="step-number">3</div>
                    <div class="step-content">
                        <h3>Access the Application</h3>
                        <p><strong>URL:</strong> http://127.0.0.1:5000</p>
                        <p><strong>Login:</strong> username: <code>admin</code>, password: <code>admin</code></p>
                    </div>
                </div>
            </div>
        </section>

        <section class="section">
            <h2>📁 Project Structure</h2>
            <div class="file-structure">
                <div class="folder">gold-price-app/</div>
                <div class="file">app.py</div>
                <div class="folder">model/</div>
                <div class="file">prophet_model.pkl</div>
                <div class="folder">data/</div>
                <div class="folder">raw/</div>
                <div class="file">gold_and_usdx.csv</div>
                <div class="folder">processed/</div>
                <div class="file">forecast.csv</div>
                <div class="folder">templates/</div>
                <div class="file">login.html, home.html, index.html, forecast.html, about.html</div>
                <div class="folder">static/</div>
                <div class="file">CSS files and assets</div>
            </div>
        </section>

        <section class="section">
            <h2>✨ Features</h2>
            <div class="features-grid">
                <div class="feature">
                    <div class="feature-icon">🔐</div>
                    <h3>Secure Login</h3>
                    <p>Simple authentication system</p>
                </div>
                <div class="feature">
                    <div class="feature-icon">📈</div>
                    <h3>Price Predictions</h3>
                    <p>Get gold price forecasts</p>
                </div>
                <div class="feature">
                    <div class="feature-icon">📊</div>
                    <h3>Data Visualization</h3>
                    <p>Interactive charts and graphs</p>
                </div>
                <div class="feature">
                    <div class="feature-icon">📅</div>
                    <h3>Date-based Forecasts</h3>
                    <p>Select specific dates for predictions</p>
                </div>
            </div>
        </section>

        <section class="section">
            <h2>🛠️ Technologies Used</h2>
            <div class="tech-stack">
                <span class="tech-item">Flask</span>
                <span class="tech-item">Python</span>
                <span class="tech-item">Facebook Prophet</span>
                <span class="tech-item">Pandas</span>
                <span class="tech-item">Joblib</span>
                <span class="tech-item">HTML/CSS</span>
                <span class="tech-item">JavaScript</span>
            </div>
        </section>

        <div class="note">
            <strong>Note:</strong> This application is for educational and demonstration purposes only. 
            Gold price predictions are based on historical data and should not be considered as financial advice.
        </div>

        <footer>
            <p>Gold Price Prediction Web App &copy; 2024</p>
            <p>For support, please open an issue in the repository.</p>
        </footer>
    </div>
</body>
</html>
