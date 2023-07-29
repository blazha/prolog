"use client";

import 'react-calendar/dist/Calendar.css';
import Calendar from 'react-calendar';
import { useState } from 'react';

type ValuePiece = Date | null;

type Value = ValuePiece | [ValuePiece, ValuePiece];

export function ChristianCalendar() {
  return (
    <div>
      <Calendar {...commonProps} />
    </div>
  );
}

const commonProps = {
  onChange: (value: Value) => {
    console.log(value)
  },
}
