# Build stage
FROM node:20-alpine AS builder
WORKDIR /employee
COPY package*.json ./
RUN npm install --only=production
COPY . .

# Production stage
FROM node:20-alpine
WORKDIR /employee
COPY --from=builder /employee /employee
EXPOSE 3000
CMD ["node", "index.js"]
