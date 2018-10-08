# Pre-commit script to automatically update README
# To install, run ``mv .github/pre-commit-script .git/hooks/pre-commit && chmod u+x .git/hooks/pre-commit``
python src/doctree.py . >.github/example_output.md 
cat .github/base_README.md .github/example_output.md >.github/README.md 
echo "\`\`\`" >>.github/README.md
git add .github/
