const userProfile = {
    name: "Omar",
    birthYear: 2007,
    isDeveloper: true,
    hobbies: ["Coding", "Football", "Gaming"]
};

function showProfile() {
    const currentYear = new Date().getFullYear();
    const age = currentYear - userProfile.birthYear;
    const months = age * 12;

    document.getElementById("profileInfo").textContent =
        `Name: ${userProfile.name}, Developer: ${userProfile.isDeveloper}`;
    document.getElementById("ageInfo").textContent =
        `Age: ${age}, Months: ${months}, Hobbies: ${userProfile.hobbies.length}`;

    console.log(userProfile);
    console.log("Age:", age, "Months:", months);
}

function showHobbies() {
    const list = document.getElementById("hobbiesList");
    list.innerHTML = "";

    userProfile.hobbies.forEach(function (hobby) {
        const item = document.createElement("li");
        item.textContent = hobby;
        list.appendChild(item);
    });
}

document.getElementById("profileForm").addEventListener("submit", function (event) {
    event.preventDefault();
    const name = document.getElementById("username").value.trim();
    const year = Number(document.getElementById("birthYear").value);

    if (name && year >= 1900 && year <= new Date().getFullYear()) {
        userProfile.name = name;
        userProfile.birthYear = year;
        showProfile();
    }
});

document.getElementById("addButton").addEventListener("click", function () {
    const input = document.getElementById("newItem");
    const hobby = input.value.trim();

    if (hobby) {
        userProfile.hobbies.push(hobby);
        input.value = "";
        showHobbies();
        showProfile();
    }
});

document.getElementById("removeButton").addEventListener("click", function () {
    if (userProfile.hobbies.length > 0) {
        userProfile.hobbies.pop();
        showHobbies();
        showProfile();
    }
});

showProfile();
showHobbies();
