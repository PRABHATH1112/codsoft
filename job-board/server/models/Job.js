const mongoose = require('mongoose');

const jobSchema = new mongoose.Schema({
  title: String,
  company: String,
  location: String,
  description: String,
  salary: Number,
});

module.exports = mongoose.model('Job', jobSchema);
