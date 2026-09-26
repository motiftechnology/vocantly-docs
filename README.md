# Vocantly Documentation

Welcome to the Vocantly documentation repository — guides, SDK reference, and API reference for building on Vocantly.

This site is built with the [Mint](https://www.npmjs.com/package/mint) docs CLI and self-hosted as a static export on our own infrastructure at `docs.vocantly.com`, rather than on a hosted docs platform.

## Development

Install the docs CLI to preview your documentation changes locally:

```
npm i -g mint
```

Run the following command at the root of this repository, where `docs.json` is located:

```
mint dev
```

View your local preview at `http://localhost:3000`.

## Publishing changes

This site does not auto-deploy on push. To publish:

1. Push your changes to the default branch.
2. Run `./deploy.sh docs` from the main workspace to export a static build, strip the docs CLI's own platform branding, and sync it to the server.

See `scripts/rebrand-export.py` for what that stripping step does and why.

## Need help?

### Troubleshooting

- If your dev environment isn't running: run `mint update` to ensure you have the most recent version of the CLI.
- If a page loads as a 404: make sure you are running in a folder with a valid `docs.json`.

### Resources
- [Docs CLI documentation](https://mintlify.com/docs)
