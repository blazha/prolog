export default function Home() {
  let text = "";

  fetch('http://127.0.0.1:8000/forewords')
    .then(results => results.json())
    .then(data => {
      console.log(data[0].text)
    });

  return (
    <main className="flex min-h-screen flex-col items-center justify-between p-24">
      <div className="z-10 w-full max-w-5xl items-center justify-between font-mono text-sm lg:flex">
        
      </div>
    </main>
  )
}
