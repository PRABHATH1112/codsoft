const express = require('express');
const { getJobs, addJob } = require('../controllers/jobController');
const router = express.Router();

router.get('/jobs', getJobs);
router.post('/jobs', addJob);

module.exports = router;
