"use client";
import React, { useEffect, useState } from 'react';

import { ChristianCalendar } from "../components/christian-calendar";

export default function Home() {
  const [visiblePredgovor, setVisiblePredgovor] = useState<Boolean>(true);
  const [predgovor, setPredgovor] = useState<string>('');
  const title = 'ОХРИДСКИ ПРОЛОГ'
  const hidePredgovor = () => setVisiblePredgovor(false);

  useEffect(() => {
    fetch(`http://127.0.0.1:8000/forewords`,
    {
      method: 'GET',
      headers: {
        Accept: 'application/json',
      },
    })
    .then(response => response.json())
    .then(data => {
      console.log(data)
      setPredgovor(data[0].text)
    })
    .catch(error => {
      console.log(error)
    });
  });
  
  return (
    <main className="flex min-h-screen flex-col items-center justify-between p-24">
      <div className="z-10 w-full max-w-5xl items-center justify-between font-mono text-sm lg:flex">
        <h1>{ title }</h1>
       { visiblePredgovor && <p>{ predgovor }</p>}
        <div>
          <ChristianCalendar onDateSelected={hidePredgovor}/>
        </div>
      </div>
    </main>
  )
}
