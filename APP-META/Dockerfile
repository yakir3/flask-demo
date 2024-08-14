FROM go:1.22.0

# Set an environment variable
ENV APP /app
#ENV PROJECT_ENV prod
ENV EXPOSE_PORT 8080

#RUN groupadd -g 1001 -r app && useradd -r -u 1001 -g app app
#RUN mkdir $APP && chown app.app $APP
WORKDIR $APP

#COPY --chown=app:app . .
COPY . .
COPY APP-META/entrypoint.sh /bin/entrypoint.sh

EXPOSE ${EXPOSE_PORT}

#USER app
ENTRYPOINT ["/bin/entrypoint.sh"]
CMD ["debug"]
