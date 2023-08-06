import { ChristianCalendar } from "./christian-calendar";

export default async function Home() {
  const title = 'ОХРИДСКИ ПРОЛОГ'
  const response = await fetch(`http://127.0.0.1:8000/forewords`,
  {
    method: 'GET',
    headers: {
      Accept: 'application/json',
    },
  });

  const forewordsText = (await response.json()) as Foreword[];
  // console.log(forewordsText)
  return (
    <main className="flex min-h-screen flex-col items-center justify-between p-24">
      <div className="z-10 w-full max-w-5xl items-center justify-between font-mono text-sm lg:flex">
        <h1>{ title }</h1>
        <p>{ forewordsText[0].text }</p>
        <div>
          <ChristianCalendar />
        </div>
      </div>
    </main>
  )
}
