<div class="w3-container addressBook">
  
% for card in addressBook:

    <div class="w3-card"><p>{{card["name"]}}</p><p>{{card["email"]}}</p></div>
  
% end

</div>