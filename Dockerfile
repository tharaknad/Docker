FROM python:3.9-slim as base

WORKDIR /software

COPY . .



ENV NAME calculator

# Second stage using distroless image
FROM gcr.io/distroless/python3

WORKDIR /software

# Copy files from the 'base' stage to the current stage
COPY --from=base /software /software

CMD ["code.py"]

