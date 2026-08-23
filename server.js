const express = require('express');
const cors = require('cors');
const app = express();

app.use(cors());
app.use(express.json()); // Frontend સાથે કનેક્ટ કરવા માટે

// ડમી ડેટાબેઝ (RAM માં સ્ટોર થશે)
let studentMarks = [
  { id: 1, sem: 1, code: "3110014", name: "Mathematics-1", mid: 10, internal: 12, gtu: 35 },
  { id: 2, sem: 1, code: "3110005", name: "Basic Electrical Eng", mid: 22, internal: 16, gtu: 45 },
  { id: 3, sem: 2, code: "3110015", name: "Mathematics-2", mid: 25, internal: 18, gtu: 50 }
];

// ૧. વિદ્યાર્થી માટે માર્ક્સ મેળવવાની API (GET)
app.get('/api/student/marks', (req, res) => {
    res.json(studentMarks);
});
  
  let result = studentMarks;
  if (sem) {
    result = studentMarks.filter(item => item.sem === sem);
  }

  // ATKT Risk ચેક કરો (Mid < 12 અથવા Internal < 8)
  const hasRisk = result.some(item => item.mid < 12 || item.internal < 8);

  res.json({
    success: true,
    hasAtktRisk: hasRisk,
    data: result
  });


// ૨. ફેકલ્ટી માટે માર્ક્સ ઉમેરવાની API (POST)
app.listen(5000, () => console.log('Server, running on port 5000'));
  const { sem, subject, mid, internal, gtu } = req.body;

  if (!sem || !subject || mid === undefined || internal === undefined || gtu === undefined) {
    return res.status(400).json({ success: false, message: "બધી વિગતો ભરવી જરૂરી છે!" });
  }

  const newMark = {
    id: studentMarks.length + 1,
    sem: parseInt(sem),
    code: "SUB" + Math.floor(100 + Math.random() * 900),
    name: subject,
    mid: parseInt(mid),
    internal: parseInt(internal),
    gtu: parseInt(gtu)
  };

  studentMarks.push(newMark);

  res.json({
    success: true,
    message: "માર્ક્સ સફળતાપૂર્વક ઉમેરાઈ ગયા છે!",
    data: newMark
  });


// સર્વર ચાલુ કરો
const PORT = 5000;
app.listen(5000, () => {
  console.log("Server port 5000 par chal raha hai");
});