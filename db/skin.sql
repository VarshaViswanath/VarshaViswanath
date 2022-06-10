-- phpMyAdmin SQL Dump
-- version 5.1.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 11, 2022 at 06:40 AM
-- Server version: 10.4.22-MariaDB
-- PHP Version: 7.4.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `skin`
--

-- --------------------------------------------------------

--
-- Table structure for table `dpic`
--

CREATE TABLE `dpic` (
  `id` int(11) NOT NULL,
  `tit` varchar(150) NOT NULL,
  `pic` varchar(150) NOT NULL,
  `st` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `dpic`
--

INSERT INTO `dpic` (`id`, `tit`, `pic`, `st`) VALUES
(1, 'aneesh babu', 'ISIC_0024707.jpg', 0),
(2, 'test', 'ISIC_0010889.jpg', 0),
(3, '45', 'ISIC_0024411.jpg', 0),
(4, 'abc', 'ISIC_0024432.jpg', 0);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `dpic`
--
ALTER TABLE `dpic`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `dpic`
--
ALTER TABLE `dpic`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
