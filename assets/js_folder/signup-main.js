occupations_central_list = {
    CentralGovernmentContract: "Central-Government-Contract",
    CentralGovernmentRegular: "Central-Government-Regular",
    CentralGovernmentRetired: "Central-Government-Retired",
    PrivateEmployeeRegular: "Private-Employee-Regular",
    PrivateEmployeeContract: "Private-Employee-Contract",
    SelfEmployement: "Self-Employement",
    DailyWageEmployee: "Daily-Wage-Employee"
}

//Variables defined
const organization = document.querySelector('#organization');
const organizationpr = document.querySelector('#organizationpr');
const organizationList = document.querySelector('#organisations-list');
const stateList = document.querySelector('#state-select');
const centralList = document.querySelector('#central-select');
const privateList = document.querySelector('#private-select');
const othersList = document.querySelector('#other-select');
const occupation = document.querySelector('#occupation');
const office = document.querySelector('#office_level');
const departmentslist = document.querySelector('#departments-list');
const departmentslist1 = document.querySelector('#departments-list1');
const departmentslist2 = document.querySelector('#departments-list2');
const departmentslist3 = document.querySelector('#departments-list3');
const departmentslist4 = document.querySelector('#departments-list4');
const departmentslist5 = document.querySelector('#departments-list5');
const departmentslist6 = document.querySelector('#departments-list6');
const departmentslist7 = document.querySelector('#departments-list7');
const departmentslist8 = document.querySelector('#departments-list8');
const departmentslist9 = document.querySelector('#departments-list9');
const departmentslist10 = document.querySelector('#departments-list10');
const departmentslist11 = document.querySelector('#departments-list11');
const departmentslist12 = document.querySelector('#departments-list12');
const departmentslist13 = document.querySelector('#departments-list13');
const departmentslist14 = document.querySelector('#departments-list14');
const departmentslist15 = document.querySelector('#departments-list15');
const departmentslist16 = document.querySelector('#departments-list16');
const departmentslist17 = document.querySelector('#departments-list17');
const departmentslist18 = document.querySelector('#departments-list18');
const departmentslist19 = document.querySelector('#departments-list19');
const departmentslist20 = document.querySelector('#departments-list20');
const departmentslist21 = document.querySelector('#departments-list21');
const departmentslist22 = document.querySelector('#departments-list22');
const departmentslist23 = document.querySelector('#departments-list23');
const departmentslist24 = document.querySelector('#departments-list24');
const departmentslist25= document.querySelector('#departments-list25');
const departmentslist26 = document.querySelector('#departments-list26');
const departmentslist27 = document.querySelector('#departments-list27');
const departmentslist28 = document.querySelector('#departments-list28');
const anantapurConstList = document.querySelector('#anantapur_constituency-list');
const chitoorConstList = document.querySelector('#chitoor_constituency-list');
const eastGodavariConstList = document.querySelector('#east_godavari_constituency-list');
const gunturConstList = document.querySelector('#guntur_constituency-list');
const kadapaConstList = document.querySelector('#kadapa_constituency-list');
const krishnaConstList = document.querySelector('#krishna_constituency-list');
const kurnoolConstList = document.querySelector('#kurnool_constituency-list');
const nelloreConstList = document.querySelector('#nellore_constituency-list');
const prakasamConstList = document.querySelector('#prakasam_constituency-list');
const srikakulamConstList = document.querySelector('#srikakulam_constituency-list');
const vishakapatnamConstList = document.querySelector('#vishakhapatnam_constituency-list');
const vizianagaramConstList = document.querySelector('#vizianagaram_constituency-list');
const westGodavariConstList = document.querySelector('#west_godavari_constituency-list');
const district = document.querySelector('#district');
const mandalList = document.querySelector('#mandalList');
const panchayath = document.querySelector('#panchayathList');
const village = document.querySelector('#v-list');
const officeLocation = document.querySelector('#office-location');


const two = document.querySelector('#two');
organization.style.display = "none";
organizationList.style.display = "none";
departmentslist.style.display = "none";
departmentslist1.style.display = "none";
departmentslist2.style.display = "none";
departmentslist3.style.display = "none";
departmentslist4.style.display = "none";
departmentslist5.style.display = "none";
departmentslist6.style.display = "none";
departmentslist7.style.display = "none";
departmentslist8.style.display = "none";
departmentslist9.style.display = "none";
departmentslist10.style.display = "none";
departmentslist11.style.display = "none";
departmentslist12.style.display = "none";
departmentslist13.style.display = "none";
departmentslist14.style.display = "none";
departmentslist15.style.display = "none";
departmentslist16.style.display = "none";
departmentslist17.style.display = "none";
departmentslist18.style.display = "none";
departmentslist19.style.display = "none";
departmentslist20.style.display = "none";
departmentslist21.style.display = "none";
departmentslist22.style.display = "none";
departmentslist23.style.display = "none";
departmentslist24.style.display = "none";
departmentslist25.style.display = "none";
departmentslist26.style.display = "none";
departmentslist27.style.display = "none";
departmentslist28.style.display = "none";
office.style.display = "none";
organizationList.style.display = "none";
stateList.style.display = "none";
centralList.style.display = "none";
privateList.style.display = "none";
othersList.style.display = "none";
anantapurConstList.style.display = 'none';
chitoorConstList.style.display = 'none';
eastGodavariConstList.style.display = 'none';
gunturConstList.style.display = 'none';
kadapaConstList.style.display = 'none';
krishnaConstList.style.display = 'none';
kurnoolConstList.style.display = 'none';
nelloreConstList.style.display = 'none';
prakasamConstList.style.display = 'none';
srikakulamConstList.style.display = 'none';
vishakapatnamConstList.style.display = 'none';
vizianagaramConstList.style.display = 'none';
westGodavariConstList.style.display = 'none';
district.style.display = "none";
mandalList.style.display = "none";
panchayath.style.display = "none";
village.style.display = "none";
officeLocation.style.display = 'none';

function districtFilter() {
    district.addEventListener('input', function () {
        if (this.value === 'Anantapuramu') {
            anantapurConstList.style.display = 'initial';

        } else if (this.value === 'Chittoor') {
            chitoorConstList.style.display = 'initial';
        } else if (this.value === 'East-Godavari') {
            eastGodavariConstList.style.display = 'initial';
        } else if (this.value === 'Guntur') {
            gunturConstList.style.display = 'initial';
        } else if (this.value === 'Kadapa') {
            kadapaConstList.style.display = 'initial';

        } else if (this.value === 'Krishna') {
            krishnaConstList.style.display = 'initial';

        } else if (this.value === 'Kurnool') {
            kurnoolConstList.style.display = 'initial';

        } else if (this.value === 'Nellore') {
            nelloreConstList.style.display = 'initial';

        } else if (this.value === 'Prakasam') {
            prakasamConstList.style.display = 'initial';

        } else if (this.value === 'Srikakulam') {
            srikakulamConstList.style.display = 'initial';

        } else if (this.value === 'Visakhapatnam') {
            vishakapatnamConstList.style.display = 'initial';

        } else if (this.value === 'Vizianagaram') {
            vizianagaramConstList.style.display = 'initial';

        } else if (this.value === 'West-Godavari') {
            westGodavariConstList.style.display = 'initial';

        } else {
            prakasamConstList.style.display = 'none';
            nelloreConstList.style.display = 'none';
            kurnoolConstList.style.display = 'none';
            krishnaConstList.style.display = 'none';
            kadapaConstList.style.display = 'none';
            gunturConstList.style.display = 'none';
            srikakulamConstList.style.display = 'none';
            vishakapatnamConstList.style.display = 'none';
            westGodavariConstList.style.display = 'none';
            vizianagaramConstList.style.display = 'none';
            eastGodavariConstList.style.display = 'none';
            anantapurConstList.style.display = 'none';
            chitoorConstList.style.display = 'none';
        }


    });
}


//Occupations Filter
occupation.addEventListener('input', function () {
// console.log(this.value.replaceAll("-",""));
    if (this.value === 'STATE') {
        stateList.style.display = "initial";
        stateList.addEventListener('input', function () {
            if (this.value !== '') {
                organizationList.style.display = "initial";
                organizationList.addEventListener('input',function (){
                    if(this.value != ""){
                        if(this.value==='Agriculture-And-Co-Operation'){
                            departmentslist.style.display='initial';
                        }
                        else if(this.value ==='Animal-Husbandry-And-Fisheries'){
                            departmentslist1.style.display='initial';
                        }
                        else if(this.value ==='Backward-Classes-Welfare'){
                            departmentslist2.style.display='initial';
                        }
                        else if(this.value ==='Consumer-Affairs-Food-Civil-Supplies'){
                            departmentslist3.style.display='initial';
                        }
                        else if(this.value ==='Department-For-Women-Children-Disabled-And-Senior-Citizens'){
                            departmentslist4.style.display='initial';
                        }
                        else if(this.value ==='Environmentforestsscience-And-Technology'){
                            departmentslist5.style.display='initial';
                        }
                        else if(this.value ==='Finance'){
                            departmentslist6.style.display='initial';
                        }
                        else if(this.value ==='General-Administration'){
                            departmentslist7.style.display='initial';
                        }else if(this.value ==='Healthmedical-Family-Welfare'){
                            departmentslist8.style.display='initial';
                        }
                        else if(this.value ==='Higher-Education'){
                            departmentslist9.style.display='initial';
                        }
                        else if(this.value ==='Home'){
                            departmentslist10.style.display='initial';
                        }
                        else if(this.value ==='Housing'){
                            departmentslist11.style.display='initial';
                        } else if(this.value ==='Industries-And-Commerce'){
                            departmentslist12.style.display='initial';
                        }
                        else if(this.value ==='Information-Technologyelectronics-Communications'){
                            departmentslist13.style.display='initial';
                        }
                        else if(this.value ==='Energy'){
                            departmentslist14.style.display='initial';
                        }
                        else if(this.value ==='Minorities-Welfare'){
                            departmentslist15.style.display='initial';
                        }
                        else if(this.value ==='Municipal-Administration-Urban-Development'){
                            departmentslist16.style.display='initial';
                        }
                        else if(this.value ==='Panchayat-Raj-And-Rural-Development'){
                            departmentslist17.style.display='initial';
                        }
                        else if(this.value ==='Planning'){
                            departmentslist18.style.display='initial';
                        }
                        else if(this.value ==='Public-Enterprises'){
                            departmentslist19.style.display='initial';
                        }else if(this.value ==='Revenue'){
                            departmentslist20.style.display='initial';
                        }
                        else if(this.value ==='School-Education'){
                            departmentslist21.style.display='initial';
                        }
                        else if(this.value ==='Department-Of-Skills-Development-And-Training'){
                            departmentslist22.style.display='initial';
                        }else if(this.value ==='Social-Welfare'){
                            departmentslist23.style.display='initial';
                        }else if(this.value ==='Transportroads-And-Buildings'){
                            departmentslist24.style.display='initial';
                        }else if(this.value ==='Water-Resources'){
                            departmentslist25.style.display='initial';
                        }
                        else if(this.value ==='Youth-Advancementtourism-And-Culture'){
                            departmentslist26.style.display='initial';
                        }
                        else if(this.value ==='Labourfactoriesboilers-Insurance-Medical-Services-Department'){
                            departmentslist27.style.display='initial';
                        }
                        else if(this.value ==='Law'){
                            departmentslist28.style.display='initial';
                        }



                    }
                    else{
                        departmentslist.style.display = "none";
                        departmentslist1.style.display = "none";
                        departmentslist2.style.display = "none";
                        departmentslist3.style.display = "none";
                        departmentslist4.style.display = "none";
                        departmentslist5.style.display = "none";
                        departmentslist6.style.display = "none";
                        departmentslist7.style.display = "none";
                        departmentslist8.style.display = "none";
                        departmentslist9.style.display = "none";
                        departmentslist10.style.display = "none";
                        departmentslist11.style.display = "none";
                        departmentslist12.style.display = "none";
                        departmentslist13.style.display = "none";
                        departmentslist14.style.display = "none";
                        departmentslist15.style.display = "none";
                        departmentslist16.style.display = "none";
                        departmentslist17.style.display = "none";
                        departmentslist18.style.display = "none";
                        departmentslist19.style.display = "none";
                        departmentslist20.style.display = "none";
                        departmentslist21.style.display = "none";
                        departmentslist22.style.display = "none";
                        departmentslist23.style.display = "none";
                        departmentslist24.style.display = "none";
                        departmentslist25.style.display = "none";
                        departmentslist26.style.display = "none";
                        departmentslist27.style.display = "none";
                        departmentslist28.style.display = "none";
                    }
                })



                office.style.display = "initial";
                office.addEventListener('input', function () {
                    if (this.value !== '') {
                        if (this.value === 'State-Headquarters') {
                            officeLocation.style.display = 'initial';
                        } else if (this.value.replaceAll("-", "") === "DistrictHeadquarters") {
                            district.style.display = "initial";
                        } else if (this.value.replaceAll("-", "") === "ConstituencyHeadquarters") {
                            district.style.display = "initial";
                            district.addEventListener('input', districtFilter())
                        } else if (this.value.replaceAll("-", "") === "MandalHeadquarters") {


                            district.style.display = "initial";
                            mandalList.style.display = "initial";
                            district.addEventListener('input', districtFilter())
                        } else if (this.value.replaceAll("-", "") === "PanchayatHeadquarters") {

                            district.style.display = "initial";
                            mandalList.style.display = "initial";
                            panchayath.style.display = "initial";
                            district.addEventListener('input', districtFilter())
                        } else if (this.value.replaceAll("-", "") === "VillageHeadquarters") {

                            district.style.display = "initial";
                            mandalList.style.display = "initial";
                            panchayath.style.display = "initial";
                            village.style.display = "initial";
                            district.addEventListener('input', districtFilter())

                        } else {
                            officeLocation.style.display = 'none';

                            district.style.display = "none";
                            mandalList.style.display = "none";
                            panchayath.style.display = "none";
                            village.style.display = "none";
                        }
                    } else {
                        officeLocation.style.display = 'none';
                    }
                })

            } else {

                district.style.display = "none";
                mandalList.style.display = "none";
                panchayath.style.display = "none";
                village.style.display = "none";
                departmentslist.style.display = "none";
                organizationList.style.display = "none";
                office.style.display = "none";
            }
        });


    } else if (this.value === 'CENTRAL') {
        centralList.style.display = "initial";
        centralList.addEventListener('input', function () {
            if (this.value !== '') {
                organization.style.display = "initial";
            } else {
                organization.style.display = "none";
            }
        });
    } else if (this.value === 'PRIVATE') {
        privateList.style.display = "initial";
        privateList.addEventListener('input', function () {
            if (this.value !== '') {
                organization.style.display = "initial";
            } else {
                organization.style.display = "none";
            }
        });
    } else if (this.value === 'OTHERS') {
        othersList.style.display = "initial";
        organizationpr.style.display = "initial"

    } else {
        stateList.style.display = "none";
        centralList.style.display = "none";
        privateList.style.display = "none";
        othersList.style.display = "none";
        organizationpr.style.display = "none"
    }

});


const scaling = document.querySelector('.scaling');


scaling.addEventListener('hover', function (event) {
    event.style.fontSize = "130%";

});
