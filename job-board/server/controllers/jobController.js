const Job = require('/models/Job');

const getJobs = async (req, res) => {
  const jobs = await Job.find();
  res.json(jobs);
};

const addJob = async (req, res) => {
  const { title, company, location, description, salary } = req.body;
  const newJob = new Job({ title, company, location, description, salary });
  await newJob.save();
  res.json(newJob);
};

module.exports = { getJobs, addJob };
