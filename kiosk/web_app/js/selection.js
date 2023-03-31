/**
 * Method to open dialog containg details place with image
 * @param {*} name name of the place
 * @param {*} src src of the image
 */
function openDetailDialog(placeID, src) {
  //get the id and assign it to variable popup
  var popup = document.getElementById('openDetailPage');
  if (popup) { //if popup is true
    popup.style.display = "block"; // make it visible
  }
  $("#placeImage").attr('src', src);// remove the existing image src value and append new src value
  $("#placeName").empty().append(places[placeID].name); //updating name from the id
  $("#description").empty().append(places[placeID].description); //updating description from the id
}

/**
 * method to close the dialog box
 */
function closeDialog() {
  //get the id and assign it to variable popup
  var popup = document.getElementById('openDetailPage');
  if (popup) {//if popup is true
    popup.style.display = "none";//assign it to none & remove
  }
}

// values to display details about places
const places = [
  {
    "id": 1,
    "name": "ALAN SHEARER STATUE",
    "description": "The statue of Newcastle United hero Alan Shearer has been moved inside the boundaries of St James' Park. The 10ft (3m) statue was put up in 2016 on Barrack Road outside the grounds of the stadium",
    "review": "It was great game!"
  },
  {
    "id": 2,
    "name": "THE BACK PAGE",
    "description": "Store for sports and football memorabilia, including new, used and collectible books, CDs and DVDs.",
    "review": "They got nice collection"
  },
  {
    "id": 3,
    "name": "GRAINGER MARKET",
    "description": "Bustling market hall dating from 1835, featuring 80+ vendors selling produce, meat & vintage goods.",
    "review": "I buy everything from there"
  },
  {
    "id": 4,
    "name": "NQ64",
    "description": "NQ64 is now in Newcastle! Head into our neon paradise for retro arcade machines, retro consoles, amazing game themed cocktails, craft beers, lagers, alcohol free cocktails, wines, spirits and soft drinks. Open til late every night!",
    "review": "Place doesn't have wheelchair access"
  },
  {
    "id": 5,
    "name": "CROWS NEST",
    "description": "The Crows Nest is a vibrant pub located in the hustle and bustle of Newcastle-Upon-Tyne combining friendly service with a warm and inviting atmosphere.",
    "review": "Not bad!"
  },
  {
    "id": 6,
    "name": "LEAZES PARK",
    "description": "Public park with a fishing lake and boathouse, playground, tennis courts and a restored bandstand."
  }
]