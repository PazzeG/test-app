import { ApolloProvider } from "@apollo/client";
import AnilistClient from "../http/AnilistClient";

export default function MyApp({Component, pageProps}){
    return(
        <ApolloProvider client={AnilistClient}>
            <Component {...pageProps}/>
        </ApolloProvider>
    )
}