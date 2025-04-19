/* login.css */

body {
  margin: 0;
  padding: 0;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  background: linear-gradient(to right, #6a11cb, #2575fc);
  color: #333;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
}

.login-container {
  background-color: #fff;
  padding: 2.5rem 3rem;
  border-radius: 12px;
  box-shadow: 0 0 20px rgba(0, 0, 0, 0.2);
  width: 100%;
  max-width: 400px;
  box-sizing: border-box;
}

.login-container h2 {
  text-align: center;
  margin-bottom: 1.5rem;
  color: #444;
}

ul {
  list-style-type: none;
  padding: 0;
  margin-bottom: 1rem;
}

ul li a {
  text-decoration: none;
  color: #2575fc;
  font-weight: bold;
}

label {
  display: block;
  margin: 10px 0 5px;
  font-weight: 500;
}

input[type="radio"] {
  margin-right: 8px;
}

.form-group {
  margin-bottom: 1rem;
}

.form-control {
  width: 100%;
  padding: 0.6rem 0.8rem;
  border: 1px solid #ccc;
  border-radius: 6px;
  font-size: 1rem;
  transition: border 0.3s ease;
}

.form-control:focus {
  border-color: #2575fc;
  outline: none;
  box-shadow: 0 0 5px rgba(37, 117, 252, 0.3);
}

.btn {
  width: 100%;
  padding: 0.7rem;
  border: none;
  border-radius: 6px;
  background-color: #2575fc;
  color: white;
  font-size: 1rem;
  cursor: pointer;
  transition: background 0.3s ease;
}

.btn:hover {
  background-color: #1e63d0;
}

.messages {
  margin-top: 1rem;
  padding: 0.8rem;
  background-color: #ffe6e6;
  border-left: 4px solid red;
  border-radius: 6px;
}

.hidden {
  display: none;
}
