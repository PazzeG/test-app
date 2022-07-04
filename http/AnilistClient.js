import {ApolloClient, InMemoryCache} from "@apollo/client";

const AnilistClient = new ApolloClient({
  uri: 'https://graphql.anilist.co',
  cache: new InMemoryCache()
});

export default AnilistClient;