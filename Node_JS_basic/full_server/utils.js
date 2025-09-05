const fs = require('fs').promises;

async function readDatabase(path) {
  try {
    const data = await fs.readFile(path, 'utf8');

    const lines = data
      .split('\n')
      .map((line) => line.trim())
      .filter((line) => line.length > 0);

    if (lines.length <= 1) {
      return {};
    }

    const header = lines[0];
    const rows = lines.slice(1);
    const cols = header.split(',').map((col) => col.trim().toLowerCase());

    const firstnameIndex = cols.indexOf('firstname');
    const fieldIndex = cols.indexOf('field');

    if (firstnameIndex === -1 || fieldIndex === -1) {
      throw new Error('Invalid CSV format: missing firstname or field column');
    }

    const result = {};

    for (const row of rows) {
      const cells = row.split(',').map((cell) => cell.trim());
      const firstname = cells[firstnameIndex];
      const field = cells[fieldIndex];

      if (!firstname || !field) continue;

      if (!result[field]) {
        result[field] = [];
      }

      result[field].push(firstname);
    }

    return result;
  } catch (error) {
    throw new Error('Cannot load the database');
  }
}

module.exports = readDatabase;
