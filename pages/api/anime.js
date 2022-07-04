import prisma from "../../lib/prisma"

export default async(req, res) =>{
  if(req.method !== "POST"){
    return res.status(405).json({ message: "Method Not Allowed" })
  }

  try{
    const anime = JSON.parse(req.body)
    const savedAnime = await prisma.anime.create({ data: anime })
    res.status(200).json(savedAnime)
  } catch(err){
    res.status(400).json({ message: 'Something Went Wrong'})
  }
}