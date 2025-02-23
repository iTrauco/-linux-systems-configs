echo "alias 2ssh=\"print -z 'gcloud compute ssh rtmp-relay-vm-dev --zone us-central1-a'\"" >> ~/.zshrc && exec zsh
echo "alias zinit='source ~/.zshrc'" >> ~/.zshrc

if [ -f "$HOME/.zshrc" ]; then
  echo 'alias pyup="python3 -m venv venv && source venv/bin/activate"' >> "$HOME/.zshrc"
  exec zsh
else
  echo 'alias pyup="python3 -m venv venv && source venv/bin/activate"' >> "$HOME/.bashrc"
  exec bash
fi