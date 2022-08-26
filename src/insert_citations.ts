import { PrismaClient } from "@prisma/client";

const citations = require("../data/processed/citations.json");

const prisma = new PrismaClient();

async function main() {
	for (const citation of citations) {
		const uploadedCitation = await prisma.citation.create({
			data: {
				...citation,
			},
		});
		console.log(`Inserted citation ${uploadedCitation.id}`);
	}
}

main()
	.then(async () => {
		await prisma.$disconnect();
	})
	.catch(async (e) => {
		console.error(e);
		await prisma.$disconnect();
		process.exit(1);
	});
