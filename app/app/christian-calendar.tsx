"use client";
import React, { useState } from 'react';
import 'react-calendar/dist/Calendar.css';
import Calendar from 'react-calendar';

type ValuePiece = Date | null;

type Value = ValuePiece | [ValuePiece, ValuePiece];

export function ChristianCalendar() {
  const [zitije, setZitije] = useState<Zitije | null>(null);

  const onDateChanged = (value: Value) => {
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
    .then(data => {
      console.log(data as Zitije)
      setZitije(data as Zitije)
    })
    .catch(error => {
      console.log(error)
    });
  }

  return (
    <div>
      <Calendar onChange={onDateChanged} />
      { zitije?.sveci }
      { zitije?.stihovi }
      { zitije?.rasudjivanje }
      { zitije?.sozercanje }
      { zitije?.beseda }
    </div>
  );
}


