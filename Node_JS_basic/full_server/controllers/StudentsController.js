import readDatabase from "../utils.js";

export default class StudentsController {
    static getAllStudents(req, res) {
        let responseText = 'This is the list of our students';
        const path = process.argv[2];
        readDatabase(path)
        .then((data) => {
            const sorteFields = Object.keys(data).sort();

            for (const field of sorteFields) {
                const students = data[field];
                const count = students.length
                const studentList = students.join(', ');
                responseText += `\nNumber of students in ${field}: ${count}. List: ${studentList}`;
            }
            res.status(200).send(responseText);
        })
        .catch(() => {
            res.status(500).send(`Cannot load the database`)
        });
    }

    static getAllStudentsByMajor(req, res) {
        const path = process.argv[2];
        const { major } = req.params;
        if( req.params.major !== 'CS' &&  req.params.major !== 'SWE'){
            return res.status(500).send('Major parameter must be CS or SWE');
        }
            readDatabase(path)
            .then((students) => {
            const studentList = students[major];
            res.status(200).send(`List: ${studentList.join(', ')}`);
            })
        .catch(() => {
            res.status(500).send('Cannot load the database');
         });
        }
}
