import { ApolloProvider } from "@apollo/client";
import AnilistClient from "../http/AnilistClient";
import "../styles/globals.css"

export default function MyApp({Component, pageProps}){
    return(
        <ApolloProvider client={AnilistClient} >
            <Component {...pageProps} />
        </ApolloProvider>
    )
}