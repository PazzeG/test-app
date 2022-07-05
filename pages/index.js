import Head from 'next/head';
import Anime from '../components/Anime';
import ClientOnly from '../components/ClientOnly'

export default function ClientSide(){
  return(
    <div className="container ">
      <Head>
        <title>
          Next App Test Tech
        </title>
      </Head>
      <main className="main w-screen h-screen">
        <ClientOnly>
          <Anime />
        </ClientOnly>
      </main>
    </div>
  )
}