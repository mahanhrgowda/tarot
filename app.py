import streamlit as st
import random
from datetime import date, time, datetime, timedelta, timezone

# List of 36 Lenormand cards with emojis, short meanings, lengthy descriptions, reversed meanings, and reversed descriptions
# Reversed meanings based on various sources including https://en.tarotquest.fr/article-en-lenall-petit-lenormand-cards-meaning.html

lenormand_cards = [
    {
        "name": "The Rider",
        "emojis": "🏇💨",
        "meaning": "energy, passion, speed, activity, news, messages",
        "lengthy_description": "The Rider represents energy, passion, speed, activity, news, and messages. It symbolizes swift movement and the arrival of important information or visitors. This card suggests a dynamic period filled with action and quick developments. It highlights the need for adaptability and quick thinking. The Rider encourages embracing change and staying open to new communications. 🏇💨",
        "reversed_meaning": "delays, stagnation, lost messages, news that does not arrive",
        "reversed_lengthy_description": "The Rider reversed represents delays, stagnation, lost messages, and news that does not arrive. It symbolizes blocked movement and the non-arrival of expected information or visitors. This card suggests a period of slowdown and frustrations in developments. It highlights the challenges of impatience and stalled progress. The Rider reversed encourages patience and reevaluating plans during times of inactivity. 🏇💨"
    },
    {
        "name": "The Clover",
        "emojis": "🍀😄",
        "meaning": "luck, lightheartedness, small happinesses, opportunity, being untroubled, comedy",
        "lengthy_description": "The Clover represents luck, lightheartedness, small happinesses, opportunity, being untroubled, and comedy. It symbolizes unexpected good fortune and moments of joy that lighten the mood. This card suggests a time of positive surprises and carefree moments. It highlights the value of optimism and finding humor in life. The Clover encourages appreciating small blessings and maintaining a positive outlook. 🍀😄",
        "reversed_meaning": "missed opportunities, fleeting luck, tricky situations",
        "reversed_lengthy_description": "The Clover reversed represents missed opportunities, fleeting luck, and tricky situations. It symbolizes fortune that slips away and moments of disappointment that dampen the mood. This card suggests a time of overlooked chances and minor setbacks. It highlights the importance of vigilance to seize moments before they pass. The Clover reversed encourages learning from missed luck and staying resilient in the face of small misfortunes. 🍀😄"
    },
    {
        "name": "The Ship",
        "emojis": "🚢🌊",
        "meaning": "departure, farewell, distance, voyage, travel, journey, adventure",
        "lengthy_description": "The Ship represents departure, farewell, distance, voyage, travel, journey, and adventure. It symbolizes exploration and moving away from the familiar toward new horizons. This card suggests a period of transition or literal travel. It highlights the excitement and uncertainty of journeys. The Ship encourages embracing new experiences and letting go of the past. 🚢🌊",
        "reversed_meaning": "delays in travel, stagnation, missed opportunities, blocked change",
        "reversed_lengthy_description": "The Ship reversed represents delays in travel, stagnation, missed opportunities, and blocked change. It symbolizes hindered exploration and staying stuck in the familiar. This card suggests a period of postponed transitions or canceled plans. It highlights the frustrations of immobility and unfulfilled adventures. The Ship reversed encourages finding alternative paths and patience during stalled journeys. 🚢🌊"
    },
    {
        "name": "The House",
        "emojis": "🏠🔒",
        "meaning": "home, establishment, safety, tradition, custom, privacy, conservation",
        "lengthy_description": "The House represents home, establishment, safety, tradition, custom, privacy, and conservation. It symbolizes stability, family, and a secure foundation in life. This card suggests focus on domestic matters or personal security. It highlights the importance of roots and traditions. The House encourages building a safe and harmonious home environment. 🏠🔒",
        "reversed_meaning": "domestic issues, instability at home, family conflict",
        "reversed_lengthy_description": "The House reversed represents domestic issues, instability at home, and family conflict. It symbolizes insecurity, disrupted family bonds, and a lack of safety in personal foundations. This card suggests a time of tension in home-related matters or feeling uprooted. It highlights the challenges of unresolved past or current family problems. The House reversed encourages addressing conflicts and rebuilding stability in your living situation. 🏠🔒"
    },
    {
        "name": "The Tree",
        "emojis": "🌳🌱",
        "meaning": "growth, grounded, past connection, personal growth, spirituality, health",
        "lengthy_description": "The Tree represents growth, grounded, past connection, personal growth, spirituality, and health. It symbolizes deep roots, vitality, and long-term development. This card suggests a time for healing and spiritual reflection. It highlights the connection to ancestry and nature. The Tree encourages nurturing health and allowing time for growth. 🌳🌱",
        "reversed_meaning": "health problems, stagnation, slow recovery, uprooted feeling",
        "reversed_lengthy_description": "The Tree reversed represents health problems, stagnation, slow recovery, and an uprooted feeling. It symbolizes blocked vitality and disrupted long-term development. This card suggests a period of fatigue or difficulty in personal growth. It highlights the need to address health or spiritual imbalances. The Tree reversed encourages seeking healing and reconnecting with one's roots to regain strength. 🌳🌱"
    },
    {
        "name": "The Clouds",
        "emojis": "☁️❓",
        "meaning": "confusion, unclarity, misunderstanding, insecurity, doubt, hidden secrets",
        "lengthy_description": "The Clouds represents confusion, unclarity, misunderstanding, insecurity, doubt, and hidden secrets. It symbolizes uncertainty and temporary obstacles in clarity. This card suggests a period of doubt or confusion that will pass. It highlights the need to seek truth amid ambiguity. The Clouds encourages patience and waiting for clarity to emerge. ☁️❓",
        "reversed_meaning": "clarity emerging, resolution of confusion, positive outlook",
        "reversed_lengthy_description": "The Clouds reversed represents clarity emerging, resolution of confusion, and a positive shift from uncertainty. It symbolizes the dissipation of doubts and hidden secrets coming to light. This card suggests a period of improving visibility and reduced anxiety. It highlights the relief of overcoming misunderstandings. The Clouds reversed encourages embracing the emerging truth and moving forward with confidence. ☁️❓"
    },
    {
        "name": "The Snake",
        "emojis": "🐍🔥",
        "meaning": "desire, seduction, deception, craving, attraction, sexuality, wisdom, forbidden knowledge",
        "lengthy_description": "The Snake represents desire, seduction, deception, craving, attraction, sexuality, wisdom, and forbidden knowledge. It symbolizes complexity in relationships or situations involving betrayal or temptation. This card suggests caution in dealings with others. It highlights the duality of wisdom and danger. The Snake encourages discernment and learning from challenges. 🐍🔥",
        "reversed_meaning": "overcoming deception, resolution of issues, positive transformation",
        "reversed_lengthy_description": "The Snake reversed represents overcoming deception, resolution of issues, and positive transformation. It symbolizes healing from betrayal or temptation and gaining true wisdom. This card suggests a time of rebirth and clarity. It highlights the power to break free from negative influences. The Snake reversed encourages embracing change and using past experiences for empowerment. 🐍🔥"
    },
    {
        "name": "The Coffin",
        "emojis": "⚰️😔",
        "meaning": "ending, dying, funeral, loss, grief, mourning, sadness",
        "lengthy_description": "The Coffin represents ending, dying, funeral, loss, grief, mourning, and sadness. It symbolizes closure and the end of a phase, leading to transformation. This card suggests letting go of the old to make way for the new. It highlights the process of grieving and renewal. The Coffin encourages accepting endings as opportunities for new beginnings. ⚰️😔",
        "reversed_meaning": "resistance to change, prolonged endings, delayed closure",
        "reversed_lengthy_description": "The Coffin reversed represents resistance to change, prolonged endings, and delayed closure. It symbolizes difficulty in letting go and extended periods of grief. This card suggests a challenging time in accepting loss. It highlights the need to confront mourning head-on. The Coffin reversed encourages pushing through resistance to achieve transformation. ⚰️😔"
    },
    {
        "name": "The Bouquet",
        "emojis": "🌸🤝",
        "meaning": "flattery, social life, pleasantness, cordiality, etiquette, politeness, appreciation",
        "lengthy_description": "The Bouquet represents flattery, social life, pleasantness, cordiality, etiquette, politeness, and appreciation. It symbolizes harmonious interactions and social charm. This card suggests enjoyable social gatherings or receiving compliments. It highlights the beauty in relationships and kindness. The Bouquet encourages cultivating positive social connections. 🌸🤝",
        "reversed_meaning": "rejected offers, superficiality, poisoned gifts",
        "reversed_lengthy_description": "The Bouquet reversed represents rejected offers, superficiality, and poisoned gifts. It symbolizes disharmonious interactions and false charm. This card suggests disappointing social experiences or insincere compliments. It highlights the pitfalls in shallow relationships. The Bouquet reversed encourages discerning true kindness and avoiding superficial ties. 🌸🤝"
    },
    {
        "name": "The Scythe",
        "emojis": "⚔️🚨",
        "meaning": "accidents, hasty decisions, danger, a warning, speed, reckoning",
        "lengthy_description": "The Scythe represents accidents, hasty decisions, danger, a warning, speed, and reckoning. It symbolizes sudden changes or cuts, often unexpected. This card suggests the need for caution and quick resolution. It highlights the consequences of actions. The Scythe encourages careful decision-making and heeding warnings. ⚔️🚨",
        "reversed_meaning": "hesitation, avoided cuts, incomplete changes",
        "reversed_lengthy_description": "The Scythe reversed represents hesitation, avoided cuts, and incomplete changes. It symbolizes delayed decisions or softened impacts of sudden events. This card suggests a time of indecision and lingering issues. It highlights the risks of procrastination. The Scythe reversed encourages taking action to complete necessary changes. ⚔️🚨"
    },
    {
        "name": "The Whip",
        "emojis": "🗣️💥",
        "meaning": "conflict, discussions, arguments, debate, scolding, opposition, objection",
        "lengthy_description": "The Whip represents conflict, discussions, arguments, debate, scolding, opposition, and objection. It symbolizes tension and repeated issues or debates. This card suggests addressing conflicts directly. It highlights the need for resolution in disputes. The Whip encourages clear communication to resolve tensions. 🗣️💥",
        "reversed_meaning": "resolution of conflict, reduced tension, end of repetition",
        "reversed_lengthy_description": "The Whip reversed represents resolution of conflict, reduced tension, and the end of repetition. It symbolizes easing of arguments and harmonious discussions. This card suggests a time of peace after disputes. It highlights the benefits of resolved issues. The Whip reversed encourages maintaining calm and fostering positive communication. 🗣️💥"
    },
    {
        "name": "The Birds",
        "emojis": "🕊️🗨️",
        "meaning": "worry, excitement, gossip, chattering, nervousness, stress",
        "lengthy_description": "The Birds represents worry, excitement, gossip, chattering, nervousness, and stress. It symbolizes communication, often superficial or anxious. This card suggests a time of chatter or minor worries. It highlights the impact of words and conversations. The Birds encourages managing stress and listening carefully. 🕊️🗨️",
        "reversed_meaning": "miscommunication, anxiety, scattered thoughts",
        "reversed_lengthy_description": "The Birds reversed represents miscommunication, anxiety, and scattered thoughts. It symbolizes disrupted conversations and heightened nervousness. This card suggests a period of confusion in interactions. It highlights the dangers of gossip gone wrong. The Birds reversed encourages clarifying messages and reducing stress through focus. 🕊️🗨️"
    },
    {
        "name": "The Child",
        "emojis": "👶🌟",
        "meaning": "new start, child, innocent, beginner, apprentice, small, curious",
        "lengthy_description": "The Child represents new start, child, innocent, beginner, apprentice, small, and curious. It symbolizes innocence, new beginnings, and childlike wonder. This card suggests a fresh approach or a small matter. It highlights purity and curiosity. The Child encourages embracing newness with openness and playfulness. 👶🌟",
        "reversed_meaning": "naivety, delays in new starts, immaturity",
        "reversed_lengthy_description": "The Child reversed represents naivety, delays in new starts, and immaturity. It symbolizes blocked innocence or problematic beginnings. This card suggests challenges in fresh approaches or small matters. It highlights the risks of childish behavior. The Child reversed encourages maturing perspectives and overcoming initial hurdles. 👶🌟"
    },
    {
        "name": "The Fox",
        "emojis": "🦊🕵️",
        "meaning": "deception, cunning, caution, slyness, suspicion, clever",
        "lengthy_description": "The Fox represents deception, cunning, caution, slyness, suspicion, and clever. It symbolizes trickery or smart maneuvering in situations. This card suggests being alert to deceit or self-interest. It highlights the need for shrewdness. The Fox encourages using intelligence to navigate challenges. 🦊🕵️",
        "reversed_meaning": "mistrust, deception exposed, over-caution",
        "reversed_lengthy_description": "The Fox reversed represents mistrust, deception exposed, and over-caution. It symbolizes the revelation of tricks or excessive suspicion. This card suggests a time of uncovered lies or failed cunning. It highlights the consequences of paranoia. The Fox reversed encourages building trust and learning from exposed deceits. 🦊🕵️"
    },
    {
        "name": "The Bear",
        "emojis": "🐻🛡️",
        "meaning": "power, leadership, protection, authority, boss, strength",
        "lengthy_description": "The Bear represents power, leadership, protection, authority, boss, and strength. It symbolizes a strong figure or personal power. This card suggests dealing with authority or protecting what's yours. It highlights resilience and leadership. The Bear encourages standing strong and protecting boundaries. 🐻🛡️",
        "reversed_meaning": "overbearing, loss of control, weakened position",
        "reversed_lengthy_description": "The Bear reversed represents overbearing behavior, loss of control, and a weakened position. It symbolizes misused power or diminished authority. This card suggests challenges in leadership or protection. It highlights the dangers of excessive force. The Bear reversed encourages balancing strength and avoiding dominance. 🐻🛡️"
    },
    {
        "name": "The Star",
        "emojis": "⭐️🧭",
        "meaning": "hope, inspiration, serenity, wish, guidance, navigation",
        "lengthy_description": "The Star represents hope, inspiration, serenity, wish, guidance, and navigation. It symbolizes optimism and following one's dreams. This card suggests a time of clarity and positive outlook. It highlights inspiration and direction. The Star encourages following your inner compass to achieve goals. ⭐️🧭",
        "reversed_meaning": "lost direction, unrealistic dreams, disillusionment",
        "reversed_lengthy_description": "The Star reversed represents lost direction, unrealistic dreams, and disillusionment. It symbolizes faded hope and misguided inspiration. This card suggests a period of confusion and dashed wishes. It highlights the need to realign with reality. The Star reversed encourages grounding dreams and finding true guidance. ⭐️🧭"
    },
    {
        "name": "The Stork",
        "emojis": "🦩📦",
        "meaning": "change, movement, progress, relocation, delivery, improvement",
        "lengthy_description": "The Stork represents change, movement, progress, relocation, delivery, and improvement. It symbolizes transitions and positive shifts. This card suggests moving to better circumstances. It highlights adaptation and growth. The Stork encourages embracing change for betterment. 🦩📦",
        "reversed_meaning": "resistance to change, stagnation, slow progress",
        "reversed_lengthy_description": "The Stork reversed represents resistance to change, stagnation, and slow progress. It symbolizes delayed transitions and missed improvements. This card suggests challenges in moving forward. It highlights the frustrations of stuck situations. The Stork reversed encourages overcoming resistance to achieve movement. 🦩📦"
    },
    {
        "name": "The Dog",
        "emojis": "🐶🤝",
        "meaning": "loyalty, friendship, trust, companion, reliable, faithful",
        "lengthy_description": "The Dog represents loyalty, friendship, trust, companion, reliable, and faithful. It symbolizes dependable relationships and support. This card suggests trustworthy people or situations. It highlights the value of loyalty. The Dog encourages building and honoring trusting bonds. 🐶🤝",
        "reversed_meaning": "betrayal, unreliable friends, strained relationships",
        "reversed_lengthy_description": "The Dog reversed represents betrayal, unreliable friends, and strained relationships. It symbolizes broken trust and lack of support. This card suggests issues in friendships or alliances. It highlights the pain of disloyalty. The Dog reversed encourages reevaluating relationships and seeking genuine connections. 🐶🤝"
    },
    {
        "name": "The Tower",
        "emojis": "🗼🏛️",
        "meaning": "authority, solitude, bureaucracy, institution, isolation, corporate",
        "lengthy_description": "The Tower represents authority, solitude, bureaucracy, institution, isolation, and corporate. It symbolizes official structures or personal boundaries. This card suggests dealing with institutions or feeling isolated. It highlights stability but rigidity. The Tower encourages respecting authority while maintaining independence. 🗼🏛️",
        "reversed_meaning": "breakdown of structures, isolation ending, vulnerability",
        "reversed_lengthy_description": "The Tower reversed represents breakdown of structures, isolation ending, and vulnerability. It symbolizes crumbling authority or exposed weaknesses. This card suggests changes in institutions or personal boundaries. It highlights the opportunity for freedom from rigidity. The Tower reversed encourages adapting to changes and building new foundations. 🗼🏛️"
    },
    {
        "name": "The Garden",
        "emojis": "🌳🎉",
        "meaning": "public, party, community, gathering, social network, audience",
        "lengthy_description": "The Garden represents public, party, community, gathering, social network, and audience. It symbolizes social events and community involvement. This card suggests networking or public appearances. It highlights the joy of social interactions. The Garden encourages engaging with groups and communities. 🌳🎉",
        "reversed_meaning": "isolation, social conflicts, missed connections",
        "reversed_lengthy_description": "The Garden reversed represents isolation, social conflicts, and missed connections. It symbolizes disrupted community and failed gatherings. This card suggests a time of withdrawal or disputes in groups. It highlights the challenges of loneliness in social settings. The Garden reversed encourages resolving conflicts and seeking meaningful interactions. 🌳🎉"
    },
    {
        "name": "The Mountain",
        "emojis": "🏔️🚧",
        "meaning": "obstacle, delay, challenge, blockade, stagnation, burden",
        "lengthy_description": "The Mountain represents obstacle, delay, challenge, blockade, stagnation, and burden. It symbolizes significant barriers or delays. This card suggests overcoming large challenges. It highlights perseverance in the face of adversity. The Mountain encourages patience and strategy to surmount difficulties. 🏔️🚧",
        "reversed_meaning": "overcoming obstacles, progress after delays, reduced burden",
        "reversed_lengthy_description": "The Mountain reversed represents overcoming obstacles, progress after delays, and reduced burden. It symbolizes the clearing of barriers and forward movement. This card suggests a time of relief from challenges. It highlights the rewards of perseverance. The Mountain reversed encourages capitalizing on newfound momentum. 🏔️🚧"
    },
    {
        "name": "The Crossroad",
        "emojis": "🛣️🤔",
        "meaning": "decision, choice, multiple options, alternatives, freedom, hesitation",
        "lengthy_description": "The Crossroad represents decision, choice, multiple options, alternatives, freedom, and hesitation. It symbolizes points of choice and potential paths. This card suggests weighing options carefully. It highlights the power of free will. The Crossroad encourages making informed choices for the future. 🛣️🤔",
        "reversed_meaning": "risky paths, wrong decisions, need to undo choices",
        "reversed_lengthy_description": "The Crossroad reversed represents risky paths, wrong decisions, and the need to undo choices. It symbolizes misguided options and regretful hesitation. This card suggests challenges in decision-making. It highlights the consequences of poor judgment. The Crossroad reversed encourages correcting course and learning from mistakes. 🛣️🤔"
    },
    {
        "name": "The Mice",
        "emojis": "🐭💸",
        "meaning": "theft, loss, stress, worry, diminishment, disease",
        "lengthy_description": "The Mice represents theft, loss, stress, worry, diminishment, and disease. It symbolizes gradual erosion or small annoyances accumulating. This card suggests addressing minor issues before they grow. It highlights the need to protect resources. The Mice encourages vigilance and reducing stress. 🐭💸",
        "reversed_meaning": "significant danger to reserves, neglect in maintenance, increased loss",
        "reversed_lengthy_description": "The Mice reversed represents significant danger to reserves, neglect in maintenance, and increased loss. It symbolizes accelerated erosion and major annoyances. This card suggests urgent attention to growing problems. It highlights the risks of ignored issues. The Mice reversed encourages immediate action to safeguard assets. 🐭💸"
    },
    {
        "name": "The Heart",
        "emojis": "❤️💖",
        "meaning": "love, affection, caring, tenderness, compassion, romance",
        "lengthy_description": "The Heart represents love, affection, caring, tenderness, compassion, and romance. It symbolizes emotional connections and heartfelt feelings. This card suggests a time of love or emotional fulfillment. It highlights the importance of compassion. The Heart encourages opening up to love and nurturing relationships. ❤️💖",
        "reversed_meaning": "lack of love, suffocating relationships, misplaced trust",
        "reversed_lengthy_description": "The Heart reversed represents lack of love, suffocating relationships, and misplaced trust. It symbolizes emotional disconnects and unfulfilled feelings. This card suggests challenges in romance or compassion. It highlights the pain of broken hearts. The Heart reversed encourages healing emotions and setting healthy boundaries. ❤️💖"
    },
    {
        "name": "The Ring",
        "emojis": "💍🤝",
        "meaning": "commitment, partnership, agreement, contract, promise, cycle",
        "lengthy_description": "The Ring represents commitment, partnership, agreement, contract, promise, and cycle. It symbolizes bindings and long-term connections. This card suggests honoring commitments or entering agreements. It highlights loyalty and repetition. The Ring encourages fulfilling promises and valuing partnerships. 💍🤝",
        "reversed_meaning": "broken covenants, compromised unions, overly strong bonds",
        "reversed_lengthy_description": "The Ring reversed represents broken covenants, compromised unions, and overly strong bonds. It symbolizes failed commitments and strained partnerships. This card suggests issues in agreements or cycles. It highlights the need to release unhealthy ties. The Ring reversed encourages reevaluating promises and seeking balanced connections. 💍🤝"
    },
    {
        "name": "The Book",
        "emojis": "📖🔒",
        "meaning": "knowledge, secrets, education, information, research, mystery",
        "lengthy_description": "The Book represents knowledge, secrets, education, information, research, and mystery. It symbolizes hidden knowledge or the need for study. This card suggests discovering secrets or learning new things. It highlights the power of information. The Book encourages seeking knowledge and uncovering truths. 📖🔒",
        "reversed_meaning": "lack of understanding, ignorance, ineffective training",
        "reversed_lengthy_description": "The Book reversed represents lack of understanding, ignorance, and ineffective training. It symbolizes blocked knowledge or unrevealed secrets. This card suggests challenges in learning or research. It highlights the frustrations of mysteries unsolved. The Book reversed encourages persistent study and seeking clarity. 📖🔒"
    },
    {
        "name": "The Letter",
        "emojis": "✉️📩",
        "meaning": "news, communication, document, message, email, paper",
        "lengthy_description": "The Letter represents news, communication, document, message, email, and paper. It symbolizes written or formal communication. This card suggests receiving important information. It highlights the role of messages in daily life. The Letter encourages clear and timely communication. ✉️📩",
        "reversed_meaning": "bad news, lost messages, withheld information",
        "reversed_lengthy_description": "The Letter reversed represents bad news, lost messages, and withheld information. It symbolizes disrupted or negative communication. This card suggests delays or unpleasant documents. It highlights the issues with miscommunication. The Letter reversed encourages careful wording and verifying information. ✉️📩"
    },
    {
        "name": "The Man",
        "emojis": "👨‍🦱🧔",
        "meaning": "male, partner, self (if male), significant person, animus",
        "lengthy_description": "The Man represents male, partner, self (if male), significant person, and animus. It symbolizes a male figure or masculine energy in the reading. This card suggests focus on a man or male aspects. It highlights leadership or protection. The Man encourages recognizing masculine influences. 👨‍🦱🧔",
        "reversed_meaning": "man who has fled, blind date, change of partner",
        "reversed_lengthy_description": "The Man reversed represents a man who has fled, blind date, or change of partner. It symbolizes instability in male figures or masculine energy. This card suggests shifts or absences in significant men. It highlights transitions in relationships. The Man reversed encourages adapting to changes in masculine influences. 👨‍🦱🧔"
    },
    {
        "name": "The Woman",
        "emojis": "👩‍🦰👩",
        "meaning": "female, partner, self (if female), significant person, anima",
        "lengthy_description": "The Woman represents female, partner, self (if female), significant person, and anima. It symbolizes a female figure or feminine energy in the reading. This card suggests focus on a woman or female aspects. It highlights nurturing or intuition. The Woman encourages recognizing feminine influences. 👩‍🦰👩",
        "reversed_meaning": "woman who has disappeared, blind date, change of partner",
        "reversed_lengthy_description": "The Woman reversed represents a woman who has disappeared, blind date, or change of partner. It symbolizes instability in female figures or feminine energy. This card suggests shifts or absences in significant women. It highlights transitions in relationships. The Woman reversed encourages adapting to changes in feminine influences. 👩‍🦰👩"
    },
    {
        "name": "The Lily",
        "emojis": "🌸🕊️",
        "meaning": "purity, peace, maturity, serenity, harmony, wisdom",
        "lengthy_description": "The Lily represents purity, peace, maturity, serenity, harmony, and wisdom. It symbolizes calm and mature perspectives. This card suggests a time of peace or ethical considerations. It highlights inner harmony and virtue. The Lily encourages seeking peace and acting with integrity. 🌸🕊️",
        "reversed_meaning": "dishonesty, betrayal, lack of creativity, fertility issues",
        "reversed_lengthy_description": "The Lily reversed represents dishonesty, betrayal, lack of creativity, and fertility issues. It symbolizes disrupted peace and immature actions. This card suggests conflicts in harmony or ethics. It highlights the loss of serenity. The Lily reversed encourages restoring integrity and addressing disharmony. 🌸🕊️"
    },
    {
        "name": "The Sun",
        "emojis": "☀️🌞",
        "meaning": "success, vitality, warmth, positivity, enlightenment, energy",
        "lengthy_description": "The Sun represents success, vitality, warmth, positivity, enlightenment, and energy. It symbolizes happiness and positive outcomes. This card suggests a period of joy and clarity. It highlights optimism and life force. The Sun encourages embracing positivity and shining bright. ☀️🌞",
        "reversed_meaning": "lack of optimism, overconfidence, excessive zeal",
        "reversed_lengthy_description": "The Sun reversed represents lack of optimism, overconfidence, and excessive zeal. It symbolizes dimmed vitality and misguided energy. This card suggests challenges in achieving happiness. It highlights the risks of burnout or false positivity. The Sun reversed encourages balanced enthusiasm and realistic views. ☀️🌞"
    },
    {
        "name": "The Moon",
        "emojis": "🌕🌙",
        "meaning": "intuition, fame, emotions, recognition, illusion, imagination",
        "lengthy_description": "The Moon represents intuition, fame, emotions, recognition, illusion, and imagination. It symbolizes emotional depths and creative inspiration. This card suggests a time of intuition or public attention. It highlights the power of dreams. The Moon encourages trusting instincts and exploring emotions. 🌕🌙",
        "reversed_meaning": "fertility problems, lack of inspiration, depressive state",
        "reversed_lengthy_description": "The Moon reversed represents fertility problems, lack of inspiration, and depressive state. It symbolizes blocked intuition and faded recognition. This card suggests emotional lows or illusions shattered. It highlights challenges in creativity. The Moon reversed encourages seeking light in darkness and rebuilding inspiration. 🌕🌙"
    },
    {
        "name": "The Key",
        "emojis": "🔑✅",
        "meaning": "solution, access, certainty, unlock, answer, achievement",
        "lengthy_description": "The Key represents solution, access, certainty, unlock, answer, and achievement. It symbolizes finding answers and opening doors. This card suggests success in overcoming obstacles. It highlights certainty and breakthrough. The Key encourages pursuing solutions with confidence. 🔑✅",
        "reversed_meaning": "solution that does not happen, dependency on others, wrong choices",
        "reversed_lengthy_description": "The Key reversed represents a solution that does not happen, dependency on others, and wrong choices. It symbolizes blocked access and uncertainty. This card suggests failures in unlocking potential. It highlights the frustrations of missed achievements. The Key reversed encourages reevaluating approaches and seeking alternative keys. 🔑✅"
    },
    {
        "name": "The Fish",
        "emojis": "🐟💰",
        "meaning": "wealth, business, abundance, independence, freedom, flow",
        "lengthy_description": "The Fish represents wealth, business, abundance, independence, freedom, and flow. It symbolizes financial gain and going with the flow. This card suggests prosperity or multiple options. It highlights entrepreneurial spirit. The Fish encourages pursuing abundance and adaptability. 🐟💰",
        "reversed_meaning": "poor business, depleted resources, missed opportunities",
        "reversed_lengthy_description": "The Fish reversed represents poor business, depleted resources, and missed opportunities. It symbolizes financial loss and restricted flow. This card suggests challenges in independence or abundance. It highlights the need to conserve. The Fish reversed encourages careful management and recovering from setbacks. 🐟💰"
    },
    {
        "name": "The Anchor",
        "emojis": "⚓️🛡️",
        "meaning": "stability, security, endurance, persistence, reliability, work",
        "lengthy_description": "The Anchor represents stability, security, endurance, persistence, reliability, and work. It symbolizes grounding and long-term security. This card suggests steadiness in career or relationships. It highlights dedication and reliability. The Anchor encourages perseverance and building lasting foundations. ⚓️🛡️",
        "reversed_meaning": "blocked situation, overwhelming weight, need for detachment",
        "reversed_lengthy_description": "The Anchor reversed represents blocked situation, overwhelming weight, and need for detachment. It symbolizes instability and burdensome security. This card suggests challenges in endurance or reliability. It highlights the pitfalls of being too anchored. The Anchor reversed encourages releasing holds and seeking flexibility. ⚓️🛡️"
    },
    {
        "name": "The Cross",
        "emojis": "✝️😔",
        "meaning": "suffering, faith, burden, religion, destiny, principle",
        "lengthy_description": "The Cross represents suffering, faith, burden, religion, destiny, and principle. It symbolizes trials and spiritual lessons. This card suggests a period of hardship or sacrifice. It highlights the role of faith in overcoming. The Cross encourages acceptance and finding meaning in challenges. ✝️😔",
        "reversed_meaning": "fulfilling destiny, reversal of fortune, opposition to destiny",
        "reversed_lengthy_description": "The Cross reversed represents fulfilling destiny, reversal of fortune, or opposition to destiny. It symbolizes relief from burdens or challenged faith. This card suggests transformations in trials. It highlights the potential for positive shifts in hardship. The Cross reversed encourages embracing destiny's turns and maintaining principles. ✝️😔"
    }
]

st.title("Personalized Tarot Reading App")

st.markdown("""
### About the Process
This app generates a personalized tarot reading using your name, birth date, and time. These details create a unique seed for the random number generator, combined with the current system time to mimic real-world unpredictability—like shuffling a physical deck at different moments. This ensures each reading is unique yet tied to your personal inputs. Cards are randomly selected and can appear upright or reversed, providing nuanced interpretations.
""")

name = st.text_input("Enter your name")
birth_date = st.date_input("Enter your birth date")

# Set default birth time to current IST time
ist_tz = timezone(timedelta(hours=5, minutes=30))
default_birth_time = datetime.now(ist_tz).time()
birth_time = st.time_input("Enter your birth time", value=default_birth_time, step=timedelta(minutes=1))

question = st.text_input("Enter your question (optional)")

if st.button("Get Your Tarot Reading"):
    if name and birth_date and birth_time:
        # Create a seed based on inputs and current time for unpredictability
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        seed_str = name + birth_date.strftime("%Y-%m-%d") + birth_time.strftime("%H:%M") + (question if question else "") + current_time
        random.seed(hash(seed_str))
        
        # Draw 3 unique cards
        drawn_cards = random.sample(lenormand_cards, 3)
        
        positions = ["Past", "Present", "Future"]
        
        if question:
            st.write(f"### Reading for: {question}")
        st.write("### Your Three-Card Tarot Spread:")
        for pos, card in zip(positions, drawn_cards):
            orientation = random.choice(["Upright", "Reversed"])
            if orientation == "Upright":
                meaning = card["meaning"]
                description = card["lengthy_description"]
            else:
                meaning = card["reversed_meaning"]
                description = card["reversed_lengthy_description"]
            
            st.subheader(f"{pos}: {card['name']} {card['emojis']} ({orientation})")
            st.write(f"**{orientation} Meaning:** {meaning}")
            st.write(f"**{orientation} Description:** {description}")
    else:
        st.warning("Please fill in all fields to get your reading!")
