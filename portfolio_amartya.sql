-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Sep 23, 2023 at 11:26 AM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `portfolio_amartya`
--

-- --------------------------------------------------------

--
-- Table structure for table `contacts_form`
--

CREATE TABLE `contacts_form` (
  `sno` int(11) NOT NULL,
  `name` text NOT NULL,
  `email` varchar(50) NOT NULL,
  `subject` text NOT NULL,
  `message` text NOT NULL,
  `datetime` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `contacts_form`
--

INSERT INTO `contacts_form` (`sno`, `name`, `email`, `subject`, `message`, `datetime`) VALUES
(1, 'NA', 'na@gmail.com', 'NA', 'NA', '2023-09-21 18:15:08'),
(13, 'Amartya Dey', 'amartyadey24@gmail.com', 'test3', 'testing 3', '2023-09-22 15:01:30'),
(23, 'Amartya Dey', 'amartyadey24@gmail.com', 'Hello', 'Check Gmail Security Alerts: Sometimes, Gmail might block sign-in attempts from new or unfamiliar apps. Check your Gmail inbox or spam folder for security alerts from Google. If you find any, follow the instructions to allow access to your Flask app.', '2023-09-22 16:38:14'),
(24, 'Amartya Dey', 'amartyadey24@gmail.com', 'Unlock Captcha', 'If you\'re still having issues, it\'s possible that Google has detected suspicious activity and blocked access. You can try unlocking your Google account by visiting this link: https://accounts.google.com/DisplayUnlockCaptcha. After unlocking, try running your Flask app again.', '2023-09-22 16:38:14'),
(25, 'Amartya Dey', 'amartyadey24@gmail.com', 'Unlock Captcha', 'If you\'re still having issues, it\'s possible that Google has detected suspicious activity and blocked access. You can try unlocking your Google account by visiting this link: https://accounts.google.com/DisplayUnlockCaptcha. After unlocking, try running your Flask app again.', '2023-09-22 16:49:17'),
(26, 'Amartya Dey', 'amartyadey24@gmail.com', 'Unlock Captcha', 'If you\'re still having issues, it\'s possible that Google has detected suspicious activity and blocked access. You can try unlocking your Google account by visiting this link: https://accounts.google.com/DisplayUnlockCaptcha. After unlocking, try running your Flask app again.', '2023-09-22 16:49:17'),
(27, 'Amartya Dey', 'amartyadey24@gmail.com', 'Hello', 'ff', '2023-09-22 17:21:16'),
(28, 'Amartya Dey', 'amartyadey24@gmail.com', 'fffff', 'fcsdfsdvfsdvsdvfsdsd', '2023-09-22 18:28:20'),
(29, 'Amartya Dey', 'amartyadey24@gmail.com', 'Check this out', 'db = SQLAlchemy(app)\r\n\r\n\r\nclass Contacts(db.Model):\r\n    sno = db.Column(db.Integer, primary_key=True)\r\n    name = db.Column(db.String(80), nullable=False)\r\n    phone_num = db.Column(db.String(12), nullable=False)\r\n    msg = db.Column(db.String(120), nullable=False)\r\n    date = db.Column(db.String(12), nullable=True)\r\n    email = db.Column(db.String(20), nullable=False)\r\n\r\n@app.route(\"/\")\r\ndef home():', '2023-09-22 18:34:24'),
(30, 'Amartya Dey', 'amartyadey24@gmail.com', 'Check this out', 'db = SQLAlchemy(app)\r\n\r\n\r\nclass Contacts(db.Model):\r\n    sno = db.Column(db.Integer, primary_key=True)\r\n    name = db.Column(db.String(80), nullable=False)\r\n    phone_num = db.Column(db.String(12), nullable=False)\r\n    msg = db.Column(db.String(120), nullable=False)\r\n    date = db.Column(db.String(12), nullable=True)\r\n    email = db.Column(db.String(20), nullable=False)\r\n\r\n@app.route(\"/\")\r\ndef home():', '2023-09-22 18:36:41'),
(31, 'Amartya Dey', 'amartyadey24@gmail.com', 'Check this out', 'db = SQLAlchemy(app)\r\n\r\n\r\nclass Contacts(db.Model):\r\n    sno = db.Column(db.Integer, primary_key=True)\r\n    name = db.Column(db.String(80), nullable=False)\r\n    phone_num = db.Column(db.String(12), nullable=False)\r\n    msg = db.Column(db.String(120), nullable=False)\r\n    date = db.Column(db.String(12), nullable=True)\r\n    email = db.Column(db.String(20), nullable=False)\r\n\r\n@app.route(\"/\")\r\ndef home():', '2023-09-22 18:37:16'),
(32, 'John', 'amartyadey24@gmail.com', 'tikki', 'kha le bhai', '2023-09-22 18:39:36'),
(33, 'John', 'amartyadey24@gmail.com', 'tikki', 'kha le bhai', '2023-09-22 18:42:11'),
(34, 'John', 'amartyadey24@gmail.com', 'tikki', 'kha le bhai', '2023-09-22 18:42:45');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `contacts_form`
--
ALTER TABLE `contacts_form`
  ADD PRIMARY KEY (`sno`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `contacts_form`
--
ALTER TABLE `contacts_form`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=35;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
