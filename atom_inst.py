from dataclasses import dataclass
from typing import List, ClassVar

@dataclass
class Atom:
    ALL_ATOM: ClassVar[List['Atom']] = []
    name:str
    spot:list
    related_cost:list
    tool:list
    combine:list
    prevent:list
    postvent:list
    unit:list
    cant_consume:list
    damage_to_other:list
    damage_to_itself:list
    quality_adj_positive:list
    quality_adj_negative:list
    timing_amount_fluctuation:list
    near_person:list
    written_on:list
    repair:list

    animate:str
    def __post_init__(self):
        Atom.ALL_ATOM.append(self)
        if self.animate:
            pass

rape_target     = Atom("rape_target"    ,[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],"y")
sexual_interest = Atom("sexual_interest",[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],"y")
love_interest   = Atom("love_interest"  ,[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],"y")
child           = Atom("child"          ,[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],"y")
baby            = Atom("baby"           ,[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],"y")
dog             = Atom("dog"            ,[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],"y")
meat            = Atom("eat"            ,[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],"" )
vegetable       = Atom("vegetable"      ,[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],"" )
dildo           = Atom("dildo"          ,[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],"" )
fleshlight      = Atom("fleshlight"     ,[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],"" )
alcohol         = Atom("alcohol"        ,[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],"" )
sanitizer       = Atom("sanitizer"      ,[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],"" )
cardboard_box   = Atom("cardboard_box"  ,[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],"" )
house           = Atom("house"          ,[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],"" )
garbage         = Atom("garbage"        ,[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],"" )
corpse          = Atom("corpse"         ,[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],"" )

rape_target     .spot = ["dark alley", "night road", "courthouse"]
sexual_interest .spot = ["brothel", "tinder", "pediatrician's office"]
love_interest   .spot = ["pickup spot", "tinder", "marriage agency", "pediatrician's office"]
child           .spot = ["play area", "school", "lost child center", "orphanage"]
baby            .spot = ["play area", "orphanage", "stroller"]
dog             .spot = ["animal shelter", "dog house", "pet store", "veterinary clinic"]
meat            .spot = ["restaurant", "kitchen", "fridge", "grocery store", "ranch"]
vegetable       .spot = ["restaurant", "kitchen", "fridge", "grocery store", "farm field"]
sanitizer       .spot = ["sanitizer holder", "pharmacy", "entrance", "bathroom sink"]
alcohol         .spot = ["liqueur store", "wine cellar", "kitchen", "fridge", "bar", "nightclub", "brewery", "distillery"]
dildo           .spot = ["sex toy store", "bedroom", "toilet", "bedside drawer"]
fleshlight      .spot = ["sex toy store", "bedroom", "toilet", "bedside drawer"]
cardboard_box   .spot = ["storage room", "warehouse", "moving truck", "recycling center", "post office", "shipping department", "garage", "attic"]
house           .spot = ["residential area", "suburb", "neighborhood", "street", "real estate agency", "construction site", "architectural firm", "home improvement store"]
garbage         .spot = ["trash can", "landfill", "recycling bin", "dumpster", "waste management facility", "sewer", "drainage system", "garbage truck"]
corpse          .spot = ["morgue", "graveyard", "crime scene", "hospital", "funeral home", "burial site", "autopsy room", "cemetery"]

rape_target     .related_cost = ["bail", "legal fees"]
sexual_interest .related_cost = ["divorce alimony", "Wedding Expenses", "Date Expenses"]
love_interest   .related_cost = ["divorce alimony", "Wedding Expenses", "Date Expenses"]
child           .related_cost = ["Child support", "Kindergarten Fees"]
baby            .related_cost = ["Child support", "Kindergarten Fees"]
dog             .related_cost = ["vaccination fee", "dog food fee"]
meat            .related_cost = []
vegetable       .related_cost = []
sanitizer       .related_cost = []
alcohol         .related_cost = ["Liquor tax"]
dildo           .related_cost = []
fleshlight      .related_cost = []
cardboard_box   .related_cost = ["shipping cost", "storage fees", "recycling fees"]
house           .related_cost = ["mortgage payments", "property taxes", "maintenance costs", "utility bills", "homeowners insurance", "renovation expenses"]
garbage         .related_cost = []
corpse          .related_cost = []


rape_target     .tool = ["weapon", "sleeping pills"]
sexual_interest .tool = ["tinder"]
love_interest   .tool = ["tinder"]
meat            .tool = ["knife"]
vegetable       .tool = ["knife"]
child           .tool = []
baby            .tool = []
dog             .tool = []
sanitizer       .tool = []
alcohol         .tool = ["ID"]
dildo           .tool = []
fleshlight      .tool = []
cardboard_box   .tool = ["tape gun"]
house           .tool = ["post", "welcome mat", "furniture"]
garbage         .tool = ["garbage bag"]
corpse          .tool = []


rape_target     .combine = ["lube", "rubber", "weapon", "sleeping pills"]
sexual_interest .combine = ["lube", "rubber"]
love_interest   .combine = ["lube", "rubber"]
meat            .combine = ["seasoning", "Tableware"]
vegetable       .combine = ["seasoning", "Tableware"]
child           .combine = []
dog             .combine = ["doghouse"]
sanitizer       .combine = ["towel"]
alcohol         .combine = ["snack", "muddler"]
dildo           .combine = ["lube"]
fleshlight      .combine = ["lube"]
cardboard_box   .combine = ["tape gun"]
house           .combine = ["post", "welcome mat", "furniture"]
garbage         .combine = ["garbage bag"]
corpse          .combine = ["body bag", "coffin", "embalming fluid", "autopsy tools", "shroud"]

# A tool used to protect against damage from something. Concrete Noun only.

rape_target     .prevent= ["rape alert", "pill", "pepper spray", "self-defense training"]
sexual_interest .prevent= []
love_interest   .prevent= []
meat            .prevent= ["probiotics", "refrigeration", "vacuum sealing"]
vegetable       .prevent= ["probiotics", "refrigeration", "proper washing"]
child           .prevent= ["rubber"]
baby            .prevent= ["rubber"]
dog             .prevent= ["rabies vaccine"]
sanitizer       .prevent= []
alcohol         .prevent= ["chaser"]
dildo           .prevent= []
fleshlight      .prevent= []
cardboard_box   .prevent= ["bubble wrap", "packing tape", "silica gel packets", "plastic wrap"]
house           .prevent= ["lightning rod", "fire extinguisher", "smoke detector", "security system", "weatherproofing", "insulation"]
corpse          .prevent= ["embalming chemicals", "body bag", "refrigeration unit", "coffin", "mortuary cooler"]


rape_target     .postvent= ["rape kit", "abortion", "after pill"]
sexual_interest .postvent= ["Urology", "STD test", "abortion", "after pill"]
love_interest   .postvent= ["Urology", "STD test", "abortion", "after pill"]
meat            .postvent= ["Probiotics", "Vomitting"]
vegetable       .postvent= ["Probiotics", "Vomitting"]
child           .postvent= []
baby            .postvent= []
dog             .postvent= []
sanitizer       .postvent= []
alcohol         .postvent= ["Prairie Oyster"]
dildo           .postvent= ["Urology", "STD test"]
fleshlight      .postvent= ["Urology", "STD test"]
cardboard_box   .postvent= ["Duct tape"]
house           .postvent= ["Home repair"]
garbage         .postvent= []
corpse          .postvent= []



rape_target     .unit= ["case", "years imprisonment"]
meat            .unit= ["kcal", "gram", "pound", "slice", "dish", "serving"]
vegetable       .unit= ["kcal", "gram", "pound", "slice", "dish", "serving"]
love_interest   .unit= []
child           .unit= []
baby            .unit= []
dog             .unit= []
sanitizer       .unit= ["bottle", "litter", "spray"]
alcohol         .unit= ["cup", "bottle", "shot", "pint"]
dildo           .unit= []
fleshlight      .unit= []
sexual_interest .unit= []
cardboard_box   .unit= ["piece", "cubic foot", "cubic meter", "bundle", "stack", "pallet"]
house           .unit= ["square foot", "square meter", "room", "story", "acre", "plot"]
garbage         .unit= ["bag", "truckload", "bin", "container"]
corpse          .unit= ["body", "cadaver", "remains", "skeleton", "bag"]

rape_target     .cant_consume = ["have ED"]
meat            .cant_consume = ["be vegan", "be on diet", "be full", "have meat allergy"]
love_interest   .cant_consume = ["have ED", "be lgbt", "be married"]
child           .cant_consume = ["be infertile"]
baby            .cant_consume = ["be infertile"]
dog             .cant_consume = ["have dog allergy", "live in a no-pets apartment", "be afraid of dogs"]
sanitizer       .cant_consume = ["be muslim"]
alcohol         .cant_consume = ["be muslim", "be on sober", "be pregnant", "have liver disease", "be underage"]
vegetable       .cant_consume = ["have vegetable allergy", "be full"]
dildo           .cant_consume = []
fleshlight      .cant_consume = ["have ED"]
sexual_interest .cant_consume = ["have ED", "be asexual"]
cardboard_box   .cant_consume = []
house           .cant_consume = []
garbage         .cant_consume = []
corpse          .cant_consume = []

# The damage that its existence can cause to other existance

rape_target     .damage_to_other = ["STD"]
meat            .damage_to_other = ["Food poisoning"]
love_interest   .damage_to_other = ["STD"]
child           .damage_to_other = []
dog             .damage_to_other = ["Rabies"]
sanitizer       .damage_to_other = ["Skin irritation"]
alcohol         .damage_to_other = ["Alcoholism", "Drunk driving"]
vegetable       .damage_to_other = ["Food poisoning", "Pesticide damage"]
dildo           .damage_to_other = ["Vaginal lacerations"]
fleshlight      .damage_to_other = ["STD", "Balanoposthitis"]
sexual_interest .damage_to_other = ["STD"]
cardboard_box   .damage_to_other = []
house           .damage_to_other = ["Dust allergy"]
garbage         .damage_to_other = ["Odor damage"]
corpse          .damage_to_other = ["Odor damage", "Disease spread", "Psychological trauma", "Environmental contamination"]

rape_target     .damage_to_itself = ["Vaginal lacerations", "pregnancy"]
meat            .damage_to_itself = ["Get rotten"]
love_interest   .damage_to_itself = ["STD"]
child           .damage_to_itself = ["Childhood cancer"]
dog             .damage_to_itself = ["Rabies"]
sanitizer       .damage_to_itself = ["Evaporate"]
alcohol         .damage_to_itself = ["Evaporate"]
vegetable       .damage_to_itself = ["Contamination"]
dildo           .damage_to_itself = ["Bent"]
fleshlight      .damage_to_itself = ["torn"]
sexual_interest .damage_to_itself = []
cardboard_box   .damage_to_itself = []
house           .damage_to_itself = []
garbage         .damage_to_itself = []
corpse          .damage_to_itself = ["get rotten"]



rape_target     .quality_adj_positive = []
meat            .quality_adj_positive = ["delicious", "fresh", "free-range"]
love_interest   .quality_adj_positive = ["young", "beauty", "hot", "thin"]
child           .quality_adj_positive = ["cute"]
dog             .quality_adj_positive = ["cuty", "gentle"]
sanitizer       .quality_adj_positive = [] # ?
alcohol         .quality_adj_positive = ["delicious", "strong"]
vegetable       .quality_adj_positive = ["delicious", "fresh", "No pesticides used"]
dildo           .quality_adj_positive = ["thick", "hard", "light"]
fleshlight      .quality_adj_positive = ["tight", "light"]
sexual_interest .quality_adj_positive = ["lube"]
cardboard_box   .quality_adj_positive = ["sturdy", "durable", "spacious", "eco-friendly"]
house           .quality_adj_positive = ["cozy", "spacious", "modern", "well-maintained"]
garbage         .quality_adj_positive = ["recyclable", "biodegradable", "properly sorted", "efficiently managed"]
corpse          .quality_adj_positive = ["well-preserved", "intact", "identifiable", "respectfully handled"]

rape_target     .quality_adj_negative = []
meat            .quality_adj_negative = ["bad taste", "spoiled", "No free-range"]
love_interest   .quality_adj_negative = ["old", "ugly", "fat"]
child           .quality_adj_negative = ["ugly"]
dog             .quality_adj_negative = ["ugly", "Vicious"]
sanitizer       .quality_adj_negative = [] # ?
alcohol         .quality_adj_negative = ["bad taste", "weak"]
vegetable       .quality_adj_negative = ["bad taste", "spoiled", "pesticides used"]
dildo           .quality_adj_negative = ["thin", "soft", "heavy"]
fleshlight      .quality_adj_negative = ["loose", "heavy"]
sexual_interest .quality_adj_negative = ["lube"]
cardboard_box   .quality_adj_negative = ["flimsy", "damaged", "soggy", "undersized"]
house           .quality_adj_negative = ["dilapidated", "cramped", "outdated", "drafty"]
garbage         .quality_adj_negative = ["putrid", "hazardous", "unsorted", "overflowing", "toxic"]
corpse          .quality_adj_negative = ["decomposed", "unidentifiable", "mutilated", "contaminated", "malodorous"]

rape_target     .timing_amount_fluctuation = ["Immigrant increase", "prostitution  prohibition", "Decline in public order"]
meat            .timing_amount_fluctuation = ["BBQ boom", "Food contamination", "end of year", "BSE pandemic"]
love_interest   .timing_amount_fluctuation = ["Marriage boom", "marriage decline", "aging population"]
child           .timing_amount_fluctuation = ["baby boom", "marriage decline", "aging population"]
baby            .timing_amount_fluctuation = ["baby boom", "marriage decline", "aging population"]
dog             .timing_amount_fluctuation = ["Pet boom", "Rabies pandemic"]
sanitizer       .timing_amount_fluctuation = ["Pandemic"]
alcohol         .timing_amount_fluctuation = ["liqueur boom", "alcohol prohibition", "end of year"]
vegetable       .timing_amount_fluctuation = ["vegan boom", "Cool summer/warm winter", "harvest season"]
dildo           .timing_amount_fluctuation = []
fleshlight      .timing_amount_fluctuation = []
sexual_interest .timing_amount_fluctuation = []
cardboard_box   .timing_amount_fluctuation = ["Moving season", "Holiday shopping", "E-commerce boom", "Recycling initiatives"]
house           .timing_amount_fluctuation = ["Housing market crash", "Real estate bubble", "Urbanization trend", "Economic recession"]
garbage         .timing_amount_fluctuation = ["Recycling campaigns", "Waste reduction initiatives", "Landfill capacity issues", "Environmental regulations"]
corpse          .timing_amount_fluctuation = ["Pandemic outbreaks", "War", "Natural disasters", "Funeral industry strikes", "Epidemics"]


rape_target     .near_person = ["lover", "cop", "witness"]
sexual_interest .near_person = ["lover"]
love_interest   .near_person = ["lover"]
child           .near_person = ["parent", "teacher"]
baby            .near_person = ["parent", "sitter"]
dog             .near_person = ["owner", "veterinarian"]
meat            .near_person = ["chef", "butcher"]
vegetable       .near_person = ["chef", "farmer"]
dildo           .near_person = []
fleshlight      .near_person = []
alcohol         .near_person = ["bartender"]
sanitizer       .near_person = ["doctor"]
cardboard_box   .near_person = []
house           .near_person = ["resident"]
garbage         .near_person = ["garbage collector"]
corpse          .near_person = ["gravekeeper", "grave visitor"]






rape_target     .written_on = []
sexual_interest .written_on = []
love_interest   .written_on = []
child           .written_on = []
baby            .written_on = []
dog             .written_on = []
meat            .written_on = ["Made in Australia", "Keep refrigerateds", "free-range", "Best before:"]
vegetable       .written_on = ["Organically grown", "Made in China", "Best before:"]
dildo           .written_on = []
fleshlight      .written_on = []
alcohol         .written_on = ["Alcohol content: XX%", "Drink responsibly", "Made in France", "Best before:", "Keep away from children"]
sanitizer       .written_on = ["Kills 99.9 percent of germs", "Alcohol content: XX%", "Flammable", "Keep away from children", "Made in USA"]
cardboard_box   .written_on = ["Fragile", "Handle with care", "This side up", "Recyclable", "Made in China"]
house           .written_on = ["House number", "Street name", "No trespassing", "For sale", "Under construction", "For rent", "No soliciting", "Beware of dog"]
garbage         .written_on = ["Hazardous waste", "Recyclable", "Compostable", "Non-recyclable", "Biohazard", "Collection day: [Day]", "Keep lid closed", "No hot ashes"]
corpse          .written_on = []

rape_target     .repair = ["Obstetrician-Gynecologist", "Counselor"]
sexual_interest .repair = []
love_interest   .repair = ["Marriage counselor"]
child           .repair = ["Pediatrician"]
baby            .repair = ["Pediatrician"]
dog             .repair = ["Veterinarian"]
meat            .repair = []
vegetable       .repair = []
dildo           .repair = []
fleshlight      .repair = []
alcohol         .repair = []
sanitizer       .repair = []
cardboard_box   .repair = []
house           .repair = ["Contractor", "Plumber", "Electrician", "Carpenter", "Roofer", "Painter"]
garbage         .repair = []
corpse          .repair = ["Embalmer"]

#rape_target     .media = ["news"]
#sexual_interest .media = ["tinder", "porn site"]
#love_interest   .media = ["tinder"]
#child           .media = []
#baby            .media = []
#dog             .media = ["animal shelter flyer", "pet store flyer"]
#meat            .media = ["restaurant menu", "butcher showcase"]
#vegetable       .media = ["restaurant menu", "market shelf"]
#dildo           .media = []
#fleshlight      .media = []
#alcohol         .media = ["bar menu"]
#sanitizer       .media = []
#cardboard_box   .media = []
#house           .media = ["Real estate agency flyer"]
#garbage         .media = []



