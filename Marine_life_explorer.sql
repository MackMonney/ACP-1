CREATE TABLE MarineObservations (
    ObservationID INT PRIMARY KEY,
    AnimalName VARCHAR(50),
    AnimalGroup VARCHAR(50),
    EstimatedWeight DECIMAL(6,2),
    DepthObserved DECIMAL(5,2),
    ObservationDate DATE
);

INSERT INTO MarineObservations
VALUES
(1, 'Blue Whale', 'Mammal', 120000.00, 50.5, '2026-06-01'),
(2, 'Hammerhead Shark', 'Fish', 450.50, 120.0, '2026-06-02'),
(3, 'Giant Squid', 'Mollusk', 300.25, 600.5, '2026-06-03'),
(4, 'Dolphin', 'Mammal', 250.00, 35.2, '2026-06-04'),
(5, 'Sea Turtle', 'Reptile', 180.75, 20.0, '2026-06-05'),
(6, 'Clownfish', 'Fish', 1.20, 15.8, '2026-06-06'),
(7, 'Octopus', 'Mollusk', 35.50, 80.4, '2026-06-07'),
(8, 'Seal', 'Mammal', 220.30, 42.0, '2026-06-08');

SELECT DISTINCT AnimalGroup
FROM MarineObservations;

SELECT COUNT(*) AS TotalObservations
FROM MarineObservations;

SELECT COUNT(*) AS MammalCount
FROM MarineObservations
WHERE AnimalGroup = 'Mammal';

SELECT SUM(EstimatedWeight) AS TotalWeight
FROM MarineObservations;

SELECT AVG(DepthObserved) AS AverageDepth
FROM MarineObservations;

SELECT
    COUNT(*) AS TotalObservations,
    SUM(EstimatedWeight) AS TotalWeight,
    AVG(DepthObserved) AS AverageDepth
FROM MarineObservations;