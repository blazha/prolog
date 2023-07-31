"use client";

import 'react-calendar/dist/Calendar.css';
import Calendar from 'react-calendar';

type ValuePiece = Date | null;

type Value = ValuePiece | [ValuePiece, ValuePiece];

export function ChristianCalendar() {
  return (
    <div>
      <Calendar onChange={onDateChanged} />
    </div>
  );
}

const onDateChanged = (value: Value) => {
  console.log("dan je " + (value as Date).getDate())
  console.log("mesec je " + ((value as Date).getMonth() + 1))
  const day = (value as Date).getDate();
  const month = (value as Date).getMonth() + 1;

  fetch(`http://127.0.0.1:8000/zitije/${month}/${day}`,
  {
    method: 'GET',
    headers: {
      Accept: 'application/json',
    },
  })
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => {
    console.log(error)
  });
}
