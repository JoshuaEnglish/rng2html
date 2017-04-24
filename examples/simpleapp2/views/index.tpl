% rebase('base.tpl', title="SimpleApp")
<header class="w3-container w3-padding-32" style="padding-left:32px">
  <h1 class="w3-xlarge w3-padding-16">Address Book</h1>
  <p>A address book Web App in a wxPython Window</p>
</header>
<div class="w3-container w3-padding-32" style="padding-left:32px">

% include('addresses.tpl', addressBook=addressBook)


</div>



