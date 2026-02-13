import React, { useState } from 'react';
import './App.css';

function App() {
  const [showModal, setShowModal] = useState(false);
  const [showActivityModal, setShowActivityModal] = useState(false);

  // Sample data for activities
  const activities = [
    { id: 1, date: '2026-02-13', type: 'Running', duration: '30 min', distance: '5 km', calories: 250 },
    { id: 2, date: '2026-02-12', type: 'Cycling', duration: '45 min', distance: '15 km', calories: 320 },
    { id: 3, date: '2026-02-11', type: 'Swimming', duration: '60 min', distance: '2 km', calories: 400 },
    { id: 4, date: '2026-02-10', type: 'Yoga', duration: '40 min', distance: '-', calories: 150 },
  ];

  // Sample data for leaderboard
  const leaderboard = [
    { rank: 1, name: 'Alice Johnson', team: 'Team Alpha', points: 1250, activities: 45 },
    { rank: 2, name: 'Bob Smith', team: 'Team Beta', points: 1180, activities: 42 },
    { rank: 3, name: 'Carol White', team: 'Team Gamma', points: 1050, activities: 38 },
    { rank: 4, name: 'David Brown', team: 'Team Alpha', points: 980, activities: 35 },
    { rank: 5, name: 'Eve Davis', team: 'Team Beta', points: 920, activities: 33 },
  ];

  // Sample data for workout suggestions
  const workouts = [
    { id: 1, name: 'Morning Run', difficulty: 'Medium', duration: '30 min', category: 'Cardio' },
    { id: 2, name: 'HIIT Training', difficulty: 'Hard', duration: '25 min', category: 'Strength' },
    { id: 3, name: 'Yoga Flow', difficulty: 'Easy', duration: '45 min', category: 'Flexibility' },
  ];

  // Sample data for teams
  const teams = [
    { id: 1, name: 'Team Alpha', members: 12, totalPoints: 5420 },
    { id: 2, name: 'Team Beta', members: 10, totalPoints: 4950 },
    { id: 3, name: 'Team Gamma', members: 11, totalPoints: 4680 },
  ];

  const getRankClass = (rank) => {
    if (rank === 1) return 'leaderboard-gold';
    if (rank === 2) return 'leaderboard-silver';
    if (rank === 3) return 'leaderboard-bronze';
    return '';
  };

  const getDifficultyBadge = (difficulty) => {
    if (difficulty === 'Easy') return 'success';
    if (difficulty === 'Medium') return 'warning';
    if (difficulty === 'Hard') return 'danger';
    return 'secondary';
  };

  return (
    <div className="App">
      {/* Bootstrap Navigation */}
      <nav className="navbar navbar-expand-lg navbar-light bg-light">
        <div className="container-fluid">
          <a className="navbar-brand" href="#home">
            <img src="/logo.png" alt="OctoFit Logo" className="logo-image" />
            OctoFit Tracker
          </a>
          <button
            className="navbar-toggler"
            type="button"
            data-bs-toggle="collapse"
            data-bs-target="#navbarNav"
            aria-controls="navbarNav"
            aria-expanded="false"
            aria-label="Toggle navigation"
          >
            <span className="navbar-toggler-icon"></span>
          </button>
          <div className="collapse navbar-collapse" id="navbarNav">
            <ul className="navbar-nav ms-auto">
              <li className="nav-item">
                <a className="nav-link active" aria-current="page" href="#dashboard">
                  Dashboard
                </a>
              </li>
              <li className="nav-item">
                <a className="nav-link" href="#activities">
                  Activities
                </a>
              </li>
              <li className="nav-item">
                <a className="nav-link" href="#leaderboard">
                  Leaderboard
                </a>
              </li>
              <li className="nav-item">
                <a className="nav-link" href="#teams">
                  Teams
                </a>
              </li>
              <li className="nav-item">
                <a className="nav-link" href="#profile">
                  Profile
                </a>
              </li>
            </ul>
            <img src="/nos-logo.png" alt="NOS Logo" className="nos-logo-navbar" />
          </div>
        </div>
      </nav>

      {/* Main Content */}
      <div className="main-content">
        <div className="container">
          {/* Bootstrap Headings */}
          <h1 className="text-center mb-4 text-white">Welcome to OctoFit Tracker</h1>
          <p className="text-center text-white mb-5">
            Track your fitness journey, compete with friends, and achieve your goals!
          </p>

          {/* Stats Cards */}
          <div className="row mb-4">
            <div className="col-md-3 mb-3">
              <div className="card stat-card">
                <div className="stat-value">1,250</div>
                <div className="stat-label">Total Points</div>
              </div>
            </div>
            <div className="col-md-3 mb-3">
              <div className="card stat-card">
                <div className="stat-value">45</div>
                <div className="stat-label">Activities</div>
              </div>
            </div>
            <div className="col-md-3 mb-3">
              <div className="card stat-card">
                <div className="stat-value">12.5</div>
                <div className="stat-label">Hours</div>
              </div>
            </div>
            <div className="col-md-3 mb-3">
              <div className="card stat-card">
                <div className="stat-value">8,500</div>
                <div className="stat-label">Calories</div>
              </div>
            </div>
          </div>

          {/* Activities Section with Bootstrap Table */}
          <div className="row mb-4">
            <div className="col-12">
              <div className="card">
                <div className="card-header d-flex justify-content-between align-items-center">
                  <h3 className="mb-0">Recent Activities</h3>
                  <button
                    className="btn btn-light btn-sm"
                    onClick={() => setShowActivityModal(true)}
                  >
                    <i className="bi bi-plus"></i> Add Activity
                  </button>
                </div>
                <div className="card-body">
                  <div className="table-responsive">
                    <table className="table table-striped table-hover">
                      <thead>
                        <tr>
                          <th>Date</th>
                          <th>Type</th>
                          <th>Duration</th>
                          <th>Distance</th>
                          <th>Calories</th>
                          <th>Actions</th>
                        </tr>
                      </thead>
                      <tbody>
                        {activities.map((activity) => (
                          <tr key={activity.id}>
                            <td>{activity.date}</td>
                            <td>{activity.type}</td>
                            <td>{activity.duration}</td>
                            <td>{activity.distance}</td>
                            <td>{activity.calories}</td>
                            <td>
                              <button className="btn btn-sm btn-info me-2">View</button>
                              <button className="btn btn-sm btn-warning me-2">Edit</button>
                              <button className="btn btn-sm btn-danger">Delete</button>
                            </td>
                          </tr>
                        ))}
                      </tbody>
                    </table>
                  </div>
                </div>
              </div>
            </div>
          </div>

          {/* Leaderboard Section with Bootstrap Table */}
          <div className="row mb-4">
            <div className="col-12">
              <div className="card">
                <div className="card-header">
                  <h3 className="mb-0">🏆 Leaderboard</h3>
                </div>
                <div className="card-body">
                  <div className="table-responsive">
                    <table className="table table-striped table-hover">
                      <thead>
                        <tr>
                          <th>Rank</th>
                          <th>Name</th>
                          <th>Team</th>
                          <th>Points</th>
                          <th>Activities</th>
                          <th>Actions</th>
                        </tr>
                      </thead>
                      <tbody>
                        {leaderboard.map((user) => (
                          <tr key={user.rank}>
                            <td>
                              <span className={`leaderboard-rank ${getRankClass(user.rank)}`}>
                                {user.rank}
                              </span>
                            </td>
                            <td>{user.name}</td>
                            <td>{user.team}</td>
                            <td><strong>{user.points}</strong></td>
                            <td>{user.activities}</td>
                            <td>
                              <a href="#profile" className="btn btn-sm btn-primary">
                                View Profile
                              </a>
                            </td>
                          </tr>
                        ))}
                      </tbody>
                    </table>
                  </div>
                </div>
              </div>
            </div>
          </div>

          {/* Teams Section with Bootstrap Table */}
          <div className="row mb-4">
            <div className="col-12">
              <div className="card">
                <div className="card-header d-flex justify-content-between align-items-center">
                  <h3 className="mb-0">Teams</h3>
                  <button className="btn btn-light btn-sm" onClick={() => setShowModal(true)}>
                    <i className="bi bi-plus"></i> Create Team
                  </button>
                </div>
                <div className="card-body">
                  <div className="table-responsive">
                    <table className="table table-striped table-hover">
                      <thead>
                        <tr>
                          <th>Team Name</th>
                          <th>Members</th>
                          <th>Total Points</th>
                          <th>Actions</th>
                        </tr>
                      </thead>
                      <tbody>
                        {teams.map((team) => (
                          <tr key={team.id}>
                            <td><strong>{team.name}</strong></td>
                            <td>{team.members}</td>
                            <td>{team.totalPoints}</td>
                            <td>
                              <button className="btn btn-sm btn-success me-2">Join</button>
                              <button className="btn btn-sm btn-info">View</button>
                            </td>
                          </tr>
                        ))}
                      </tbody>
                    </table>
                  </div>
                </div>
              </div>
            </div>
          </div>

          {/* Workout Suggestions with Bootstrap Cards */}
          <div className="row mb-4">
            <div className="col-12">
              <h2 className="text-white mb-3">💪 Suggested Workouts</h2>
            </div>
            {workouts.map((workout) => (
              <div className="col-md-4 mb-3" key={workout.id}>
                <div className="card">
                  <div className="card-body">
                    <h5 className="card-title">{workout.name}</h5>
                    <p className="card-text">
                      <span className={`badge bg-${getDifficultyBadge(workout.difficulty)} me-2`}>
                        {workout.difficulty}
                      </span>
                      <span className="badge bg-secondary">{workout.category}</span>
                    </p>
                    <p className="card-text">
                      <strong>Duration:</strong> {workout.duration}
                    </p>
                    <button className="btn btn-primary w-100">Start Workout</button>
                  </div>
                </div>
              </div>
            ))}
          </div>
        </div>
      </div>

      {/* Bootstrap Modal for Creating Team */}
      {showModal && (
        <div
          className="modal show d-block"
          tabIndex="-1"
          style={{ backgroundColor: 'rgba(0,0,0,0.5)' }}
        >
          <div className="modal-dialog modal-dialog-centered">
            <div className="modal-content">
              <div className="modal-header">
                <h5 className="modal-title">Create New Team</h5>
                <button
                  type="button"
                  className="btn-close btn-close-white"
                  onClick={() => setShowModal(false)}
                  aria-label="Close"
                ></button>
              </div>
              <div className="modal-body">
                {/* Bootstrap Form */}
                <form>
                  <div className="mb-3">
                    <label htmlFor="teamName" className="form-label">
                      Team Name
                    </label>
                    <input
                      type="text"
                      className="form-control"
                      id="teamName"
                      placeholder="Enter team name"
                    />
                  </div>
                  <div className="mb-3">
                    <label htmlFor="teamDescription" className="form-label">
                      Description
                    </label>
                    <textarea
                      className="form-control"
                      id="teamDescription"
                      rows="3"
                      placeholder="Describe your team"
                    ></textarea>
                  </div>
                  <div className="mb-3">
                    <label htmlFor="teamGoal" className="form-label">
                      Team Goal
                    </label>
                    <select className="form-control" id="teamGoal">
                      <option>Weight Loss</option>
                      <option>Muscle Gain</option>
                      <option>General Fitness</option>
                      <option>Competition</option>
                    </select>
                  </div>
                </form>
              </div>
              <div className="modal-footer">
                <button
                  type="button"
                  className="btn btn-secondary"
                  onClick={() => setShowModal(false)}
                >
                  Cancel
                </button>
                <button type="button" className="btn btn-primary">
                  Create Team
                </button>
              </div>
            </div>
          </div>
        </div>
      )}

      {/* Bootstrap Modal for Adding Activity */}
      {showActivityModal && (
        <div
          className="modal show d-block"
          tabIndex="-1"
          style={{ backgroundColor: 'rgba(0,0,0,0.5)' }}
        >
          <div className="modal-dialog modal-dialog-centered">
            <div className="modal-content">
              <div className="modal-header">
                <h5 className="modal-title">Log Activity</h5>
                <button
                  type="button"
                  className="btn-close btn-close-white"
                  onClick={() => setShowActivityModal(false)}
                  aria-label="Close"
                ></button>
              </div>
              <div className="modal-body">
                {/* Bootstrap Form */}
                <form>
                  <div className="mb-3">
                    <label htmlFor="activityType" className="form-label">
                      Activity Type
                    </label>
                    <select className="form-control" id="activityType">
                      <option>Running</option>
                      <option>Cycling</option>
                      <option>Swimming</option>
                      <option>Yoga</option>
                      <option>Weight Training</option>
                    </select>
                  </div>
                  <div className="mb-3">
                    <label htmlFor="duration" className="form-label">
                      Duration (minutes)
                    </label>
                    <input
                      type="number"
                      className="form-control"
                      id="duration"
                      placeholder="30"
                    />
                  </div>
                  <div className="mb-3">
                    <label htmlFor="distance" className="form-label">
                      Distance (km)
                    </label>
                    <input
                      type="number"
                      className="form-control"
                      id="distance"
                      placeholder="5.0"
                      step="0.1"
                    />
                  </div>
                  <div className="mb-3">
                    <label htmlFor="activityDate" className="form-label">
                      Date
                    </label>
                    <input
                      type="date"
                      className="form-control"
                      id="activityDate"
                    />
                  </div>
                </form>
              </div>
              <div className="modal-footer">
                <button
                  type="button"
                  className="btn btn-secondary"
                  onClick={() => setShowActivityModal(false)}
                >
                  Cancel
                </button>
                <button type="button" className="btn btn-primary">
                  Save Activity
                </button>
              </div>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}

export default App;
