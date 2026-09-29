[00:00:00] Hello everyone, welcome to this brand
[00:00:02] new series on Langen, the framework
[00:00:04] that's changing how we build intelligent
[00:00:06] context aware applications using live
[00:00:08] language models. If you have ever
[00:00:10] wondered how chatbots, AI agents, or
[00:00:13] retrieval based systems actually work
[00:00:15] behind the scenes, you're in the right
[00:00:17] place. In this series, we'll go beyond
[00:00:20] just theory. We'll build real world lang
[00:00:23] project step by step from simple
[00:00:25] conversational bots to AI systems that
[00:00:28] can use tools reason with data and even
[00:00:31] connect with external APIs and
[00:00:33] databases. By the end, you'll have the
[00:00:36] skills to design your own AI assistant
[00:00:38] or integrate LLM into your apps
[00:00:40] confidently. But before we dive in,
[00:00:43] let's understand what Langen really is.
[00:00:46] Langen is a framework that bridges LLMs
[00:00:49] with real data and real tasks. It helps
[00:00:53] developers manage prompts, memory,
[00:00:55] retrievalss, agents, and chains all in a
[00:00:58] structured modular way. Think of it as a
[00:01:01] toolbox that turns a large language
[00:01:03] model into powerful goal oriented
[00:01:06] system.
[00:01:08] In the upcoming videos, we'll explore
[00:01:10] langen concepts like chain, agents,
[00:01:12] retrieval, and vector stores and much
[00:01:14] more. Each topic will include hands-on
[00:01:17] coding demos and project based learning.
[00:01:20] So if you're excited to build real AI
[00:01:22] apps with Langen, make sure to
[00:01:24] subscribe, hit the bell icon, and follow
[00:01:26] the C series from the start. Let's
[00:01:29] unlock the true potential of language
[00:01:31] models together. I'm Object, and this is
[00:01:33] the Langen series. Let's get started. So
[00:01:36] in this video, we're going to have our
[00:01:38] first interaction with an LLM. So for
[00:01:41] that, first of all, I'd like to create a
[00:01:43] virtual environment. So open a terminal
[00:01:45] in VS code. I've opened a folder in VS
[00:01:48] Code. Uh and then open a terminal. So
[00:01:51] we'll create our virtual environment
[00:01:53] virtual env.
[00:01:56] And I'm going to activate this virtual
[00:01:58] environment and install my libraries
[00:02:00] inside this. Okay. So the virtual
[00:02:02] environment is created and now I'm going
[00:02:05] to install
[00:02:07] some libraries here. So pip install
[00:02:10] langen
[00:02:11] google genai
[00:02:15] and I'll also install langen
[00:02:18] community
[00:02:20] and let's also have python
[00:02:25] do env or env. So let's install these
[00:02:28] three libraries.
[00:02:32] And while this is being installed I'm
[00:02:34] also going to create a requirements file
[00:02:37] requirements.tx txt and then mention
[00:02:39] these three libraries name here. So the
[00:02:42] first name is langchain
[00:02:45] community.
[00:02:46] Second is langchain google genai. Well,
[00:02:50] you might be wondering why we're
[00:02:53] installing
[00:02:54] Google geni because uh the
[00:02:59] Google
[00:03:01] Google geni models or like the gemini
[00:03:03] models are kind of free. The flash
[00:03:06] models are free. So we will be using
[00:03:08] those models for our LLM interaction.
[00:03:11] I'm also going to create av file here
[00:03:16] file
[00:03:18] and inside this file we'll have our uh
[00:03:22] Gemini API key which will be defined as
[00:03:25] Google API key and then you can paste
[00:03:29] your Google API key in
[00:03:33] in this place here. So paste your key.
[00:03:37] Uh I'm going to replace
[00:03:39] replace my key here when I'm going to
[00:03:41] run the application here. Okay. So for
[00:03:44] the first first program or for the first
[00:03:47] interaction, we're going to create a pi
[00:03:49] file. But I would like to organize
[00:03:51] everything inside this single folder
[00:03:52] only for the future videos too. So let's
[00:03:55] just create a new folder and then
[00:03:59] type lm interaction
[00:04:01] and then inside this I am going to
[00:04:04] create a file called chat model
[00:04:07] uh_jemini
[00:04:09] dot
[00:04:11] py okay so we are inside our pi file and
[00:04:15] then this will be our first
[00:04:18] python program which which will also be
[00:04:22] our first program to interact with
[00:04:25] Gemini model. So for that I'm going to
[00:04:28] use the langen ecosystem. As you know
[00:04:30] that this is a series of langen. So we
[00:04:33] will import some libraries from langchen
[00:04:36] google_jai
[00:04:39] import
[00:04:42] chat google generative AI and then
[00:04:44] another library is from env import
[00:04:49] uh load.env.
[00:04:52] So I'm going to call this function load
[00:04:55] env. This is going to load our Google
[00:04:57] API key uh from the env file and then
[00:05:02] I'm going to define my model. My model
[00:05:04] as I said will be a Gemini model. So for
[00:05:08] that I'm going to use a Gemini
[00:05:11] 2.5/model today.
[00:05:15] And let's also invoke our model here. So
[00:05:19] model.invoke let's provide a prompt or
[00:05:22] like we can define a prompt here in
[00:05:24] string. So I'll say what is the capital
[00:05:28] city of USA
[00:05:31] and then I'm going to invoke my model
[00:05:33] with this prompt here.
[00:05:35] Let's save this in result. The model
[00:05:40] output will be saved in the result. And
[00:05:43] then I want to print out the
[00:05:45] [clears throat] result here.
[00:05:46] So let me clear this.
[00:05:49] So now if I run my application here, I
[00:05:52] can directly run my Python file from
[00:05:54] this button here. So run Python file. It
[00:05:56] activates my virtual environment and
[00:05:59] then the Python file is being run. And
[00:06:01] you can see my result here. But we don't
[00:06:04] only get the result, but we get a lot of
[00:06:06] things inside this. We get the answers.
[00:06:10] We also get some metadata from the
[00:06:13] response. uh the number of tokens and
[00:06:16] tokens and then uh stuff like that. What
[00:06:18] we only want here is our content part.
[00:06:21] So I'm going to hit result content. I'm
[00:06:23] going to clear this again and then run
[00:06:26] it. And we can see our result here. The
[00:06:30] capital city of USA is Washington DC.
[00:06:34] Well, this is our very first interaction
[00:06:37] with a LLM here. So throughout this
[00:06:41] throughout the course of this video,
[00:06:42] we're going to use um Gemini models as
[00:06:45] well as some hugging bas models wherever
[00:06:47] applicable. We saw our very first
[00:06:49] interaction with an LLM. But I'll show
[00:06:53] you one problem that this LLM call has.
[00:06:56] So let me run this again
[00:07:04] or like let me
[00:07:08] run this again. We got the answer but
[00:07:10] I'm going to change the prompt here. So
[00:07:12] hello my name is Abishek.
[00:07:17] What is your name?
[00:07:21] So if I run this
[00:07:27] it gives me an output. So I'm a large
[00:07:29] language model and AI. I don't have a
[00:07:32] personal name like human does. You can
[00:07:33] just call me I assistant if you like.
[00:07:36] And then in the initials of this message
[00:07:38] it's written hello Abishek how can I
[00:07:40] help you today? So now if I type
[00:07:45] do you remember
[00:07:48] my name
[00:07:50] and then run this
[00:07:53] we'll see the problem here.
[00:07:59] As an AI I don't have memory of past
[00:08:01] conversation or personal information
[00:08:02] about you. So no I don't remember your
[00:08:04] name. So each and every LLM calls that
[00:08:07] we make are actually independent here.
[00:08:12] So how do we maintain these multi-turn
[00:08:15] conversations meaning the contextual
[00:08:17] conversation like we have in this chat
[00:08:19] GBT or like Gemini models. So we'll try
[00:08:22] to implement that here. So for that I'm
[00:08:25] going to create a new folder
[00:08:28] called chatbots
[00:08:31] and inside this I'm going to create a
[00:08:33] new file
[00:08:35] chatbot.py.
[00:08:38] Uh
[00:08:47] so let me install a langen core if I
[00:08:50] haven't done it. So pp install lang gen
[00:08:54] core.
[00:08:57] Okay, I've already installed this. I can
[00:08:59] also maintain
[00:09:01] mention this in the requirement rank
[00:09:04] code.
[00:09:07] So here I'm first going to import my
[00:09:12] Gemini model.
[00:09:15] import chat Google generative model and
[00:09:19] then from langen core
[00:09:23] langen core dot messages I'm going to
[00:09:25] import system message human message and
[00:09:30] AI message
[00:09:33] so in this chatbot we'll try to maintain
[00:09:35] that contextual information so that the
[00:09:38] AI remember our remembers our name so
[00:09:41] from
[00:09:43] envo
[00:09:45] load.
[00:09:46] Okay, I'm going to load my credentials
[00:09:49] here. Then I'm going to define my model
[00:09:52] which will be chat Google generative AI.
[00:09:55] The model name is going to be Gemini
[00:10:01] 2.5/model.
[00:10:07] Now for the first
[00:10:10] message I will now define a chat history
[00:10:13] here which will be a list and inside
[00:10:16] this I'm first going to provide a system
[00:10:18] message and the system message is going
[00:10:21] to say that you are
[00:10:26] you are a helpful
[00:10:30] AI assistant.
[00:10:36] Okay. So I'll give this in loop so that
[00:10:39] I can continue talking with the bot. So
[00:10:43] I'm going to
[00:10:45] create a variable for user to type their
[00:10:48] message.
[00:10:50] So this is where user will be typing the
[00:10:53] message
[00:10:55] and then whatever message the user types
[00:10:59] I'm going to append this in my chat
[00:11:01] history
[00:11:03] so that so that the chat history list
[00:11:06] will have the information about what the
[00:11:10] conversation is being happening
[00:11:16] equals to user input.
[00:11:20] Now I also need a break from this chat.
[00:11:24] A way to break this chat. So user input
[00:11:26] dot lower equals to exit. If the user
[00:11:30] types exit and I'm going to break this
[00:11:33] or else I'm going to just invoke the
[00:11:36] model
[00:11:38] using my chatty.
[00:11:41] not just going to provide a single
[00:11:44] prompt to the user but I'm going to
[00:11:46] provide the model the entire contextual
[00:11:49] history of a conversation
[00:11:52] then the model is also going to reply
[00:11:56] back here so that will also be appended
[00:12:03] so chat do append and then it will be
[00:12:05] appended as an AI message
[00:12:09] where the content is going to P result
[00:12:12] dot
[00:12:14] content.
[00:12:19] Okay. And I'm also going to print my B
[00:12:21] response here.
[00:12:25] So result dot content.
[00:12:30] Finally once the conversation breaks out
[00:12:32] I'm going to print the entire chat
[00:12:34] history. We had chat history.
[00:12:39] Now if we run this we'll see that
[00:12:44] because of this particular
[00:12:46] list here where we have stored
[00:12:48] everything or every conversation that we
[00:12:50] had throughout this loop the model will
[00:12:54] be able to have some contextual
[00:12:56] information and at least remember our
[00:12:57] name or at least remember what we've
[00:12:59] talked about in the past. So let me
[00:13:01] clear this output and then run this
[00:13:02] again. Save this and run this again. Do
[00:13:06] I have any errors? Yeah. So there's a
[00:13:09] comma missing here.
[00:13:12] Chat history.
[00:13:14] Okay. So run run it.
[00:13:22] So it's asking for my message. I'm going
[00:13:24] to say hello.
[00:13:27] My name is Abishek.
[00:13:32] What is your name?
[00:13:42] Oh, okay. So, I probably gave the wrong
[00:13:45] model name here. Okay. So, I made a
[00:13:47] mistake here. So, let me clear this
[00:13:49] again. I'm going to recolor this.
[00:13:51] Gemini- 2.5- flash is the correct model
[00:13:55] name. So, let me run this again.
[00:14:00] Okay. So, hello.
[00:14:03] I'm shape.
[00:14:06] What is
[00:14:08] the name?
[00:14:12] So the model says hello Abishek I do not
[00:14:14] have a name. I'm a large language model
[00:14:16] trained by Google. So let me also ask a
[00:14:19] few more questions. What are you
[00:14:23] trained on?
[00:14:26] So I've been trained by Google on a
[00:14:28] massive data set of text and code.
[00:14:33] uh this data set includes a wide variety
[00:14:35] of information from the internet and
[00:14:36] then and stuff like that. So I'm going
[00:14:39] to ask another question. What is the
[00:14:42] capital of
[00:14:44] India?
[00:14:47] So the capital of India is New Delhi.
[00:14:50] Now we'll check if the bot remembers our
[00:14:53] name or not. Do you
[00:14:58] remember my name?
[00:15:01] And yes, it does remember my name
[00:15:03] because why it remembers our name is if
[00:15:07] we hit exit and then see our entire chat
[00:15:10] history, we can see that
[00:15:13] our entire chat history is being saved
[00:15:15] here. So this was the first message that
[00:15:18] we gave to the AI assistant. I asked
[00:15:22] this question.
[00:15:24] The AI replied me with this answer.
[00:15:29] I again asked another question using a
[00:15:31] human message and then just because of
[00:15:34] the existence of this contextual
[00:15:36] information
[00:15:39] the bot was able to remember what the
[00:15:41] conversation was about or like was able
[00:15:44] to remember the stuffs that we said in
[00:15:47] the past. So in the last video we saw
[00:15:50] how we can include contextual
[00:15:53] information in our chatbot. So in this
[00:15:55] video we're going to talk about
[00:15:57] something. We know what simple prompts
[00:16:00] are. We've already given prompts to our
[00:16:02] chatbot. But in this video we're going
[00:16:04] to introduce a concept called chat
[00:16:06] prompt template. So chat prompt template
[00:16:08] in lang chain. It is a tool that helps
[00:16:11] you design and organize prompt for
[00:16:13] chatbased AI models in a structured way.
[00:16:15] So instead of writing the entire message
[00:16:17] each time, uh you can actually give a
[00:16:20] pattern that includes different roles
[00:16:22] like system, human and AI along with
[00:16:25] placeholders for dynamic values. So such
[00:16:28] placeholders are actually later filled
[00:16:30] with real data when the prompt is
[00:16:32] actually used. So what this does is it
[00:16:36] makes it easier to maintain uh reuse and
[00:16:38] modify prompts uh without changing the
[00:16:41] main logic of your application. So if I
[00:16:44] say it in simple terms, it's like
[00:16:46] creating a reusable message template
[00:16:48] that guides how our chatbot or AI
[00:16:51] assistant uh should behave and respond
[00:16:53] in a conversation. So I'm going to
[00:16:56] include my chat chat prompt template in
[00:17:00] my next program. So I'm going to create
[00:17:03] a new file here.
[00:17:06] Prompt
[00:17:08] template.py.
[00:17:11] So
[00:17:13] have our import langen_core
[00:17:16] dotprompts
[00:17:19] import chat prompt template.
[00:17:23] I'll have my model to lang google geni
[00:17:26] import chat google generative AI and
[00:17:30] I'll also have my messages here. So from
[00:17:33] langen
[00:17:35] uh I'm not sure if I'll use this or not
[00:17:37] but we'll keep it for now. messages,
[00:17:40] input,
[00:17:42] system message, human message, and AI
[00:17:45] message.
[00:17:47] Okay, first of all, what we're going to
[00:17:49] do is I might not invoke the model at
[00:17:52] all. I'm just going to show you uh how
[00:17:55] our prompts are created using chat
[00:17:56] prompt template. Okay, so this is
[00:17:58] actually chat prompt template, not chat
[00:18:00] message prompt template. So I'm first
[00:18:04] going to create a template here. So chat
[00:18:06] template
[00:18:08] equals to chat prompt template.
[00:18:12] I'm going to create a list inside this.
[00:18:14] And then [clears throat]
[00:18:16] for our system message I'm going to type
[00:18:20] in
[00:18:22] type in this part and then you are a
[00:18:27] helpful
[00:18:31] domain expert. So the domain is going to
[00:18:35] be a placeholder which will be filled
[00:18:37] later on whenever we execute the stratum
[00:18:39] template. And for the human message
[00:18:43] I'm going to type
[00:18:46] explain in
[00:18:48] simple terms
[00:18:51] simple terms the concept of
[00:18:56] topic and then the topic is also going
[00:18:58] to be a placeholder here. So whenever I
[00:19:01] create a prompt, what I'm going to do is
[00:19:03] I'm going to use my chat template dot
[00:19:07] invoke
[00:19:08] and inside this since we have two
[00:19:11] different placeholders here. So I'm
[00:19:13] going to provide the value of those
[00:19:15] placeholders. The first one is domain.
[00:19:18] So we'll call this quantum quantum
[00:19:22] mechanics or quantum physics
[00:19:26] or something like that. And then the
[00:19:28] next is our topic. So I'm keeping the
[00:19:32] topic as warm.
[00:19:37] Okay. Now if I try and print this
[00:19:41] prompt, what I'm going to see is a
[00:19:44] generated prompt from this chat prompt
[00:19:46] template here where we have these two
[00:19:51] messages along with their placeholders.
[00:19:52] So let me clear this and then run this
[00:19:55] again.
[00:19:59] So if I run this I can see my
[00:20:05] I can see my prompts here. So the first
[00:20:07] one is a system message. You are a
[00:20:09] helpful quantum physics expert because
[00:20:12] the placeholder is being filled here and
[00:20:14] then uh the human message explain in
[00:20:17] simple terms the concept of wormhole. So
[00:20:20] if I need to invoke this I can directly
[00:20:22] define my model here. So if you define a
[00:20:24] model then you can directly invoke your
[00:20:27] model using this
[00:20:31] prompt here. So model invoke and then
[00:20:34] prompt. I I think you can do this by
[00:20:36] yourself and then check out the result
[00:20:39] here. What I wanted to show you in this
[00:20:41] video is a new style of generating our
[00:20:45] prompts using this chat prom template.
[00:20:49] When building a chatbot, one of the
[00:20:51] biggest challenges is making it remember
[00:20:53] the conversation. You don't want to
[00:20:55] treat AI or you don't want the AI to
[00:20:58] treat every every user message as a
[00:21:00] brand new question. So that is where the
[00:21:03] message placeholder comes in. Uh it's
[00:21:06] like a dynamic container for a chat
[00:21:08] history. Instead of manually combining
[00:21:10] all previous messages into a single
[00:21:13] string every time you generate a prompt,
[00:21:15] you just put a placeholder in your
[00:21:17] template and lang fills it automatically
[00:21:21] uh with the actual conversation that
[00:21:23] happened so far. Uh so the placeholder
[00:21:25] doesn't just dump text, it preserves the
[00:21:28] role of each message whether it came
[00:21:31] from the human, the AI or the system. Uh
[00:21:34] so this means that uh the AI can
[00:21:36] actually uh identify between
[00:21:39] instructions, user prompts and is and
[00:21:42] its own pass responses. So that is what
[00:21:45] allows multi-turn conversations to feel
[00:21:47] natural that we see in chat GPT or
[00:21:50] Gemini interfaces that we use. So
[00:21:52] another powerful aspect of such is
[00:21:56] reusability. So you can define a single
[00:21:58] chat template with a message placeholder
[00:22:00] and it works for any number of previous
[00:22:03] conversations that we had. So whether
[00:22:04] the conversation has two turns or 20
[00:22:07] turns, the placeholder always inserts
[00:22:09] the right history in the right format.
[00:22:11] So this also keeps the template clean
[00:22:13] and you don't need complex logic to
[00:22:16] actually stitch the chat together or
[00:22:18] like put the chat together. So finally
[00:22:20] message placeholders uh work seamlessly
[00:22:23] with lang chains role based messages
[00:22:25] like system message human message and AI
[00:22:28] message that we've already seen. So this
[00:22:31] combination actually uh uh ensures that
[00:22:35] our prompts are structured uh clear and
[00:22:39] and also are context aware which is
[00:22:41] actually essential when using LMS for
[00:22:44] chatbot or customer support agents. Uh
[00:22:47] so message placeholder is what lets a
[00:22:50] chatbot remember understand rules and
[00:22:53] continue
[00:22:55] conversation smoothly without you
[00:22:56] manually managing
[00:22:59] every previous line of dialogue. So that
[00:23:01] is what we're going to do in our
[00:23:04] upcoming code.
[00:23:11] So I'm going to create a new file called
[00:23:13] message placeholder
[00:23:17] holder.py. What I'm also going to do is
[00:23:20] create a new file that actually contains
[00:23:24] or saves my conversation here. So let me
[00:23:27] write it at chatbot history
[00:23:31] uh txt. As I told you that uh whenever
[00:23:35] we save our conversation, we save it in
[00:23:37] such a way that um that the information
[00:23:41] of the message is being preserved. So
[00:23:45] I'll put a few messages here. So the
[00:23:47] first one is a human message where it
[00:23:50] says that I want to request a rep for my
[00:23:52] order and the AI message uh says this
[00:23:55] thing. So okay I will use this and what
[00:23:58] I'm going to do is in my message
[00:24:00] placeholder I am going to
[00:24:03] load this chat and then create a new
[00:24:06] prompt based on my uh new user input. So
[00:24:11] first of all I'm just going to use from
[00:24:14] line gen core dot promps
[00:24:17] import the first one is going to be chat
[00:24:20] prom template
[00:24:23] it should be promps.
[00:24:25] So chat prom template and then the other
[00:24:27] is going to be a message placeholder. So
[00:24:30] our chat template is going to be
[00:24:32] something that we've already seen.
[00:24:36] So chat template equals to chat prompt
[00:24:39] template.
[00:24:43] So this will contain a system message
[00:24:47] uh which says you are a very helpful
[00:24:53] helpful
[00:24:55] customer support agent
[00:24:59] and and then I'll also load our
[00:25:02] conversation history that we already
[00:25:04] have in this file. So for that I'm going
[00:25:06] to define a message placeholder with a
[00:25:10] variable name and then and then the
[00:25:12] variable name is going to be like
[00:25:16] uh chat
[00:25:19] history.
[00:25:22] It's just a variable name. It does not
[00:25:24] need to match with the file name
[00:25:25] provided here. And then the third is
[00:25:28] going to be a human message.
[00:25:32] a new human message that will come uh
[00:25:36] in this particular place here.
[00:25:40] So I'll also indicate this as a string.
[00:25:43] Okay. So this is our chat template. Now
[00:25:47] I'm going to load a chat history from a
[00:25:50] file. So for that I will create a list
[00:25:53] called chat history.
[00:25:55] So with open uh chat_history
[00:26:00] txt
[00:26:02] as file
[00:26:05] I can load a chat history chat history
[00:26:08] uh dot extend
[00:26:11] file
[00:26:13] dot read lines.
[00:26:16] Okay.
[00:26:18] Now
[00:26:20] uh I will create my new prompt here
[00:26:23] based on the chat template that I have
[00:26:28] as well as the chat history that I just
[00:26:29] loaded. So
[00:26:32] inside my chat history
[00:26:35] variable
[00:26:37] is going to be my chat history list.
[00:26:43] chat
[00:26:45] history list.
[00:26:49] Okay, so this should be inside
[00:26:52] curly braces. So chat history list and
[00:26:56] chat history along with this I'm going
[00:26:58] to also have a query because the query
[00:27:01] also contains a placeholder here. So in
[00:27:04] the query I'll ask where is my refund.
[00:27:09] So I can invoke this using a model too,
[00:27:11] but I just want to show you the use of
[00:27:13] placeholder here. So I'm just going to
[00:27:14] print my prompt or my new prompt here.
[00:27:18] Okay. So let me rerun this and then we
[00:27:22] can see
[00:27:25] uh something's not right. Okay. So this
[00:27:27] should be txt.
[00:27:29] Clear this again. Then run it.
[00:27:37] I definitely made some mistake here.
[00:27:42] Oh, it should be chatbot history, not
[00:27:44] chat history.
[00:27:46] Chatbot history.
[00:27:49] Okay, if I load this again, then we can
[00:27:52] see uh that the first message is a human
[00:27:57] message.
[00:28:00] uh you are a very helpful customer
[00:28:03] support agent. So far we focused on
[00:28:06] making AI conversations more natural and
[00:28:09] context aware. So we looked at how the
[00:28:11] AI can remember previous messages using
[00:28:13] features like message placeholder which
[00:28:16] allowed our chat bots to maintain
[00:28:17] multi-turn conversations like chat GPT
[00:28:19] or Gemini. Uh back then the AI could
[00:28:23] generate responses freely which worked
[00:28:25] well for casual conversation but the
[00:28:27] outputs were often unstructured
[00:28:29] sometimes too long inconsistent or
[00:28:32] sometimes hard to process automatically.
[00:28:34] Now we're moving into the next step
[00:28:36] which is structured responses. So
[00:28:38] instead of letting the AI respond
[00:28:40] however it wants, we want to define a
[00:28:43] schema that specifies the exact fields
[00:28:45] and types of information we want in the
[00:28:47] response. So this actually guides the AI
[00:28:50] to produce outputs that are predictable,
[00:28:52] organized and easy to work with. So for
[00:28:54] example, we can ask it to summarize the
[00:28:56] review and identify the sentiment and it
[00:28:59] will return the information in a clean
[00:29:01] and structured format. So the key idea
[00:29:04] is that structured output turns the AI
[00:29:08] from just a conversational partner into
[00:29:09] a reliable data source. So it
[00:29:11] complements the uh whatever we've done
[00:29:14] before. The AI still remembers the
[00:29:16] context of the conversation but now uh
[00:29:18] its responses are also consistent and u
[00:29:22] more readable making it much easier to
[00:29:24] integrate into applications dashboard or
[00:29:27] any system that needs such actionable
[00:29:30] data. So let me jump to the code and
[00:29:33] then show you what I mean by that
[00:29:35] concept here. So
[00:29:38] I'm going to create a new folder here
[00:29:42] which is going to be structured
[00:29:45] structured outputs. Let me give this as
[00:29:49] number three.
[00:29:53] So inside this I'm going to create a new
[00:29:55] file
[00:29:56] and then the file name is going to be
[00:29:58] structured
[00:30:01] output.py.
[00:30:05] So here again we're going to be using
[00:30:08] the geni model from Google. So import
[00:30:15] chat Google generative model. I'm also
[00:30:18] going to
[00:30:20] load my credentials. So env import load
[00:30:25] env. And here I'm going to introduce
[00:30:29] something new which is a typed dict
[00:30:33] type. So I'm going to load my credential
[00:30:39] define my model
[00:30:43] which is going to be a Gemini model.
[00:30:49] So as I said we want a proper structured
[00:30:53] output right? So for that we're going to
[00:30:54] define a schema. Let's write review.
[00:30:59] Uh
[00:31:01] so and the type is going to be typed
[00:31:04] tick. What we want is a summary which is
[00:31:07] going to be in string and a sentiment
[00:31:10] value
[00:31:12] uh which is going to be also be in a
[00:31:15] string. So it can be a positive,
[00:31:17] negative or sentiments like that. So now
[00:31:22] what I'm going to do is instead of
[00:31:24] directly invoking the model, I'm going
[00:31:26] to convert this model output into a
[00:31:28] structured model output. So
[00:31:31] structured
[00:31:36] model equals to model dot with
[00:31:40] structured output
[00:31:42] and then I'm going to provide my review
[00:31:44] class here. So what this does is
[00:31:47] whenever this model is invoked it tries
[00:31:50] to base its output on this particular
[00:31:53] structure provided here. Okay. So let me
[00:31:57] define my prompt. I'm not going to use a
[00:31:59] prompt uh chat prompt template. You know
[00:32:01] how to use that. So I'm just going to
[00:32:03] give my prompt here in a simple
[00:32:05] approach. So let's say this hardware is
[00:32:09] great
[00:32:11] but
[00:32:14] the the software feels
[00:32:18] kind of bloated.
[00:32:22] So many
[00:32:24] boilerplate
[00:32:27] boilerplate apps and my phone keeps
[00:32:33] hanging
[00:32:36] when I play PUBG.
[00:32:40] Okay. So this is going to be my review.
[00:32:43] uh and then based on this I'm going to
[00:32:47] invoke my model with a structured model
[00:32:50] dot invoke and then provide my prompt
[00:32:54] here
[00:32:58] and then I'm going to print my
[00:33:03] response. So now if I try to run this,
[00:33:07] let me run this.
[00:33:09] So what I'm going to see is I'm going to
[00:33:12] see a structured model output in this.
[00:33:14] So as I said we
[00:33:18] gave the model a schema
[00:33:20] to base its response upon and then the
[00:33:24] response is just based on the schema.
[00:33:26] Here we have a sentiment a sentiment and
[00:33:28] then the summary. So the sentiment is
[00:33:31] negative and then the summary is just
[00:33:33] hardware is great but software is
[00:33:35] bloated with bullet coursees and the
[00:33:37] phone hangs when playing PUBG. So it is
[00:33:39] just trying to summarize this particular
[00:33:42] provided review prompt here and then the
[00:33:46] response is quite well structured. Well,
[00:33:48] if I try to do something like this. So
[00:33:52] [clears throat]
[00:33:53] if I give a new prompt and then
[00:33:58] uh okay um I'll also show you what
[00:34:01] happens if we don't provide such
[00:34:02] structured outputs here. So my prompt is
[00:34:05] going to be uh
[00:34:08] generate
[00:34:11] sentiment and
[00:34:14] summary of
[00:34:17] the review below.
[00:34:20] Review given
[00:34:22] the review is.
[00:34:26] So if I paste my review here
[00:34:29] or I can just do this. Uh [snorts] I can
[00:34:32] hit new prompt and then
[00:34:35] use this as f string
[00:34:41] and then include my
[00:34:43] review using this prompt placeholder.
[00:34:47] Well, if I invoke this with not my
[00:34:50] structured model but with my model, then
[00:34:53] I'm going to see that my response is
[00:34:55] going to be very much unstructured which
[00:34:58] I which I don't actually want. So, I'm
[00:35:00] not going to print this for now. Let's
[00:35:02] not print this. Uh, we'll just print it
[00:35:06] with the previous upper that we've done.
[00:35:12] Okay, something's wrong. I'm not sure
[00:35:15] what. So, let me check again. Uh,
[00:35:22] ah, okay. We've not used the function
[00:35:26] invoke here. So let me write invoke
[00:35:29] clear this and run this again.
[00:35:41] I'm not printed by result in fact. So
[00:35:43] let me print by result too.
[00:35:56] So as you can see uh the response is
[00:36:00] quite mixed. Uh it says here's the
[00:36:03] sentiment and summary of the review
[00:36:04] sentiment mixed to negative positive the
[00:36:08] hardware is slightly
[00:36:10] highly praised and then yeah stuffs like
[00:36:12] that which is not actually structured.
[00:36:14] So we can actually
[00:36:17] base our LLM output
[00:36:20] response [clears throat] and then ask it
[00:36:23] to base it on on the provided schema.
[00:36:26] Here we can also include the details of
[00:36:29] of such schema but we'll do that in our
[00:36:32] upcoming video. In our previous video we
[00:36:34] explored structured outputs where the AI
[00:36:37] was guided to return information in a
[00:36:39] specific format like a summary and
[00:36:41] sentiment. That approach made the AI's
[00:36:44] response predictable and easy to use,
[00:36:47] but it was relatively simple. We were
[00:36:49] mostly extracting a summary and a single
[00:36:52] sentiment value. So in this next step,
[00:36:54] we taking structured output to the next
[00:36:57] level by introducing rich schemas with
[00:37:00] multiple fields, annotation and optional
[00:37:02] elements. Uh now instead of just a
[00:37:05] summary, we can ask the AI to extract
[00:37:07] multiple layers of information from a
[00:37:09] single piece of text. the key themes
[00:37:12] that is talked about, a concise summary,
[00:37:15] overall sentiment, and even detailed
[00:37:18] pros and cons. We're also telling the AI
[00:37:21] exactly how each field should be
[00:37:22] formatted and making it strict so it
[00:37:26] follows to the schema precisely. So,
[00:37:29] this approach transforms the AI into a
[00:37:32] powerful data extractor. uh you can feed
[00:37:35] it complex reviews, articles or even
[00:37:37] long form text and it will actually
[00:37:40] return you a structured machine readable
[00:37:42] object that you can directly use in
[00:37:46] dashboards, analytical tools or even
[00:37:48] databases. So the AI is no longer just
[00:37:51] answering your questions or chatting.
[00:37:53] Now it's systematically organizing
[00:37:55] knowledge in a way that applications can
[00:37:57] consume automatically. So by building on
[00:37:59] what we learned about contextual and
[00:38:01] structured output, uh the following uh
[00:38:05] implementation will show you how to
[00:38:08] scale from simple structured
[00:38:10] uh output to detailed multi- field
[00:38:13] extraction making AI truly practical for
[00:38:16] real world task like review analysis,
[00:38:18] product insights or content
[00:38:20] summarization. So let's go for the code
[00:38:22] now.
[00:38:28] Okay, I'm going to create a new file
[00:38:30] inside this
[00:38:33] detailed output structured.py.
[00:38:38] Uh I'm going to use these same fields,
[00:38:42] the same model that I have here. I'll
[00:38:45] just paste this but but what I'm going
[00:38:49] to do is I'm going to add a few more uh
[00:38:52] fields inside the schema here. So let me
[00:38:55] first add key themes. Uh and then I'll
[00:38:59] also add an import of annotated
[00:39:02] and then optional here. So these two
[00:39:05] imports will be essential for me. So key
[00:39:08] themes will actually be uh annotated
[00:39:12] list of strings.
[00:39:16] So what we can also do is we can also
[00:39:18] write a detail about this field here. So
[00:39:21] we can say that
[00:39:24] uh
[00:39:26] key themes must write down all the
[00:39:30] themes
[00:39:32] all the important
[00:39:36] concepts
[00:39:39] discussed in the review in a list and in
[00:39:43] the summary I'm I'm again going to use
[00:39:46] an annotated key and inside this I'm
[00:39:49] going to Right. Must write down must
[00:39:53] write down a brief summary
[00:39:56] of the
[00:39:58] of the review. Uh
[00:40:01] close this uh inside my sentiment I'm
[00:40:04] again going to use an annotated.
[00:40:07] So with annotated I'm going to say must
[00:40:12] return
[00:40:15] a sentiment value
[00:40:20] uh or sentiment of the review
[00:40:23] either positive or
[00:40:27] negative
[00:40:32] and I'll also add pros and cons here.
[00:40:35] So,
[00:40:37] okay, I I need to close this bracket at
[00:40:40] last. Also, I need to do the same here.
[00:40:43] I'm also going to add pros and cons. So,
[00:40:46] pros is going to be annotated. But this
[00:40:49] is going to be a optional list. If the
[00:40:52] model does not find anything like pros
[00:40:54] and cons inside the review, then it is
[00:40:56] not going to put it or else if it finds
[00:40:58] something then then it will put it
[00:41:01] inside our uh pros list. So this is
[00:41:06] going to be optional
[00:41:09] uh str and then uh write down
[00:41:14] all the pros inside
[00:41:19] all the pros inside a list and also
[00:41:22] we'll do the same for cons
[00:41:25] annotated
[00:41:28] optional
[00:41:31] list of strings and this will also be
[00:41:35] write down all the cons inside
[00:41:41] a list. Okay, so I'm going to uh add
[00:41:45] some more prompts to this or some more
[00:41:48] details to this prompt here. So let me
[00:41:50] copy a prompt from somewhere. This
[00:41:53] prompt is from Google Pixel phone and it
[00:41:56] is quite detailed here. So you can just
[00:41:59] pause the video and then type it if you
[00:42:00] want. I'm going to perform this word rap
[00:42:04] for you so that it'll be easier for you
[00:42:06] to type this. So this is going to be my
[00:42:08] prompt and then based on this prompt uh
[00:42:11] let me remove this and then I will
[00:42:14] invoke a structured model here to see my
[00:42:18] result.
[00:42:20] So yeah so let me go ahead and then run
[00:42:25] this code. So if I run this
[00:42:29] as you can see with the structured
[00:42:30] output uh the model's response is going
[00:42:34] to be kind of structured here. So the
[00:42:36] key theme is Google 10 pixel pro GPU
[00:42:39] performance because it talks about the
[00:42:41] GPU performance somewhere around here
[00:42:44] with uh talking about its chipsets also
[00:42:49] it talks about the tensor G5 chipsets
[00:42:51] more gaming performance comparison with
[00:42:53] Pixel 9 Pro and things like that. The
[00:42:55] sentiment is mixed. It does not say
[00:42:58] positive or negative here. So
[00:43:03] we can also ask it to fix that. Uh
[00:43:06] but like it is okay for now. Uh the
[00:43:09] summary is also provided. And then the
[00:43:12] pros and cons, I don't think it's
[00:43:14] provided because the model could not
[00:43:16] find or the or the model could not
[00:43:20] identify the exact pros and cons in this
[00:43:22] particular review since this is
[00:43:23] optional. So the model could not write
[00:43:25] it or if we remove optional from here
[00:43:29] and then ask the model that it has to
[00:43:31] include the pros and cons or the or like
[00:43:35] just the pros the model will do that and
[00:43:37] then include all the pros of the review
[00:43:40] provided. So let's run this again
[00:43:48] and then we see that uh summary is
[00:43:52] provided.
[00:43:54] Uh okay what else is provided here?
[00:43:56] Summary is provided key things is key
[00:43:58] things is provided sentiment is provided
[00:44:00] and then it should also contain pro
[00:44:02] somewhere. Let me copy this and then see
[00:44:06] it in my
[00:44:10] uh copy. Let's open a JSON formatter
[00:44:14] window
[00:44:16] if we can see the pros or not.
[00:44:22] So JSON formatter
[00:44:29] paste this paste my JSON here and and
[00:44:31] then we see that it still hasn't
[00:44:33] generated any pros here but um that's
[00:44:37] okay for now still our response is kind
[00:44:40] of structured here. So this is how we
[00:44:43] can take our structured response to
[00:44:46] somewhat another level where we can
[00:44:48] include the details of what each of
[00:44:51] these keys that we want that we want to
[00:44:53] include in the responses mean and then
[00:44:56] what format should they be provided in.
[00:44:59] In our previous video, we explored
[00:45:01] structured outputs where the AI was
[00:45:03] guided to extract specific fields like
[00:45:06] summary or sentiment. That approach
[00:45:08] worked well but the schema was
[00:45:10] relatively simple. Uh now we're taking
[00:45:13] structured output a step further by
[00:45:16] using pyentic models to define a rich
[00:45:18] detailed schema. So Pyntic is a Python
[00:45:21] library that allows us to create data
[00:45:23] models with type validation default
[00:45:25] values optional fields and and clear uh
[00:45:30] details. So this means that we can tell
[00:45:32] the AI exactly what kind of data we
[00:45:34] expect for each field and we can trust
[00:45:36] that the output will confirm to these
[00:45:39] types here. So by integrating pyic with
[00:45:42] lang chain structured outputs uh we can
[00:45:44] define multiple fields like key themes a
[00:45:47] brief summary sentiment pros cons and
[00:45:49] even the reviewer's name with strict
[00:45:51] validation. Um the AI then produces the
[00:45:55] responses that are not just structured
[00:45:57] but also type safe, consistent and fully
[00:46:00] compatible with Python applications.
[00:46:03] So this is especially useful when
[00:46:05] dealing with long or complex text. So
[00:46:07] instead of u getting unstructured
[00:46:10] paragraphs, the AI learns to organize
[00:46:13] information into a machine readable
[00:46:14] object that can be directly used in
[00:46:16] dashboards, analytical tools or
[00:46:18] database. And because of Pythics
[00:46:20] validation, we reduce the risk of errors
[00:46:22] like missing fields or wrong data types
[00:46:24] too. So the integration takes structured
[00:46:27] outputs from simple field extraction to
[00:46:28] a robust, reliable and a developer
[00:46:31] friendly approach. Uh it also kind of
[00:46:33] ensures that the AI not only remembers
[00:46:35] the conversation context but also
[00:46:36] returns precise, actionable and
[00:46:38] validated
[00:46:40] information
[00:46:41] making it ready for uh real world
[00:46:45] applications. So let's go to the code
[00:46:47] now.
[00:46:52] So I'm going to create a new file here
[00:46:56] or this is going to be uh sorry three
[00:47:01] pantic
[00:47:02] structured
[00:47:06] structured
[00:47:07] output.py.
[00:47:11] Okay. So let's start.
[00:47:14] As always, we're going to use the same
[00:47:16] geni model. import go chat Google
[00:47:20] generative AI. I'm going to install uh
[00:47:24] one more library here which is called
[00:47:25] pyante.
[00:47:27] So included in requirements.ext text and
[00:47:30] then I can directly install this using
[00:47:32] this command
[00:47:35] and I also okay that is all for now
[00:47:39] because I don't have any emails right
[00:47:40] now or else we would have to have to
[00:47:43] install some other libraries too. So
[00:47:45] what I'm going to do is from env
[00:47:48] import load env uh from
[00:47:53] typing
[00:47:55] uh import type
[00:48:00] Sorry, import
[00:48:04] date. I I'll also include an annotated
[00:48:07] literal
[00:48:09] uh and also a keyword called optional.
[00:48:12] Not sure I'm going to use each and every
[00:48:13] one of these though. But still uh we'll
[00:48:16] keep it in the import. So I'll import
[00:48:18] from pyic import base model.
[00:48:23] And then I'm going to load my
[00:48:25] credential. I'm going to define my
[00:48:27] model.
[00:48:29] Uh my model will be
[00:48:34] Gemini 2.5 slash.
[00:48:39] Now I'm going to define a similar schema
[00:48:42] like we did like we did in earlier code.
[00:48:45] So I'm going to define a class which
[00:48:47] will be called review and the import
[00:48:49] will not be a type but it will be a base
[00:48:52] model from our py class.
[00:48:55] So like I said earlier, I'm going to use
[00:48:59] uh
[00:49:01] use a keyword called key themes.
[00:49:04] And
[00:49:06] instead of doing like uh annotated list
[00:49:10] of list of our content, what we'll do is
[00:49:14] we'll include
[00:49:16] a class called field here and then
[00:49:19] define this as a field. So this is going
[00:49:21] to be a a list of string. Uh its type is
[00:49:27] going to be list of string and its
[00:49:29] detail will be included in the field
[00:49:31] value. So I can include a field and then
[00:49:34] write down the details here. So write
[00:49:36] down
[00:49:38] three key themes
[00:49:42] [snorts] discussed in
[00:49:45] the review
[00:49:48] in a list.
[00:49:51] Uh the next is going to be my summary.
[00:49:55] My summary is going to be a string. And
[00:49:58] then I'll again write a field to write
[00:50:00] down the details of that sum of that
[00:50:02] summary keyword. Now this is going to be
[00:50:04] a brief
[00:50:06] summary
[00:50:08] of
[00:50:10] of the review.
[00:50:12] I'll also write sentiment.
[00:50:15] And in case of sentiment, we had
[00:50:17] something like a mix sentiment earlier.
[00:50:19] But I'm going to fix the model or ask
[00:50:22] the model to give either positive or
[00:50:24] negative sentiment here. So for that I'm
[00:50:26] going to use literal. So one will be
[00:50:28] positive. One option will be positive
[00:50:32] and then the other option is going to be
[00:50:34] a negative literal.
[00:50:38] So for that I'm also going to write down
[00:50:39] the details.
[00:50:42] Uh description equals to
[00:50:46] return
[00:50:48] the sentiment of the
[00:50:53] sentiment of the review either
[00:50:57] positive or negative.
[00:51:00] And this is going to guide me guide my
[00:51:03] model to return either positive or
[00:51:05] negative here. Now uh I'll also include
[00:51:09] a name here. So name is going to be in
[00:51:11] string and then I'll keep an optional
[00:51:14] keyword here because the names might not
[00:51:16] be available
[00:51:18] uh in the review but if it is then uh
[00:51:21] the model will definitely show the name
[00:51:23] too. So the description is going to be
[00:51:26] the name of the
[00:51:29] reviewer or or I'm going to say write
[00:51:32] down
[00:51:33] write down the name of the reviewer.
[00:51:38] Okay. So this is my output schema that I
[00:51:41] want my model to provide my output with.
[00:51:43] So I'm going to create a structured
[00:51:46] model. So this is going to be model dot
[00:51:51] with structured output
[00:51:55] and then I'll provide my class and then
[00:51:58] uh I'll also instruct this
[00:52:02] instruct the model to strictly follow
[00:52:04] the provided schema. Now
[00:52:09] uh let me provide my prompt. I can copy
[00:52:12] my prompt from the previous video or the
[00:52:15] previous code that I had. So I'm going
[00:52:18] I'm just going to copy everything else
[00:52:20] from now on here. So it is going to be a
[00:52:23] prompt and then my prompt will be
[00:52:25] invoked using the structure model
[00:52:29] and the code is complete. So let's run
[00:52:32] this code. Let me check if everything is
[00:52:33] all right. Okay, it seems okay.
[00:52:36] So let me run this. Uh when we run this,
[00:52:41] the model output will be based strictly
[00:52:43] on the schema as provided earlier.
[00:52:56] Okay. So we have key themes. We have
[00:52:59] three key themes here. One, two, and
[00:53:02] three key themes. We also have a
[00:53:03] summary. Uh and then and then okay what
[00:53:08] else? Uh we have a sentiment which is
[00:53:12] called which is strictly following the
[00:53:15] uh literal or the option that I provided
[00:53:17] here and then the name is actually not
[00:53:19] specified. So if I change this prompt
[00:53:24] and then add a few text like add a name
[00:53:28] to this reviewed by Abishek then I'll
[00:53:31] see
[00:53:33] that the model also includes my name
[00:53:37] here. It should include my name here.
[00:53:39] Let's see the output. So yeah you can
[00:53:42] see the name is being included and then
[00:53:44] everything else is present based on the
[00:53:46] schema that we provided. In this video,
[00:53:49] we're exploring a powerful combination
[00:53:51] of langen features that help us control,
[00:53:55] structure, and process AI outputs in
[00:53:58] multi-step workflows. So there are three
[00:54:00] key concepts at player. One is prompt
[00:54:03] template. Second one is str output
[00:54:05] parser and and the third one is
[00:54:07] chaining. So first let's talk about
[00:54:09] prompt template. So prompt template
[00:54:11] allows us to create reusable structured
[00:54:14] prompts with placeholders for dynamic
[00:54:16] content. Instead of hard- coding every
[00:54:18] instruction for the AI, we can define a
[00:54:22] template once specifying exactly what we
[00:54:24] want and then fill in fill in the
[00:54:27] variables as needed. For example, we can
[00:54:30] have one template that asks the AI to
[00:54:32] write a detailed report on any topic and
[00:54:35] then another template that takes the
[00:54:37] generated block of text from the
[00:54:40] previous prompt and then generate a
[00:54:42] concise summary about it. So prompt
[00:54:44] templates gives us the consistency and
[00:54:46] control over how we interact with the AI
[00:54:49] which is crucial for predictable
[00:54:51] results. The next concept we have is STR
[00:54:54] output parser. So whenever the AI
[00:54:56] generates text the raw output can be
[00:54:58] inconsistent. It can have extra lines,
[00:55:01] unexpected formatting or maybe some
[00:55:04] minor variations in the wording. So str
[00:55:07] output parser acts like this cleaning
[00:55:10] and standardizing tool and it also
[00:55:12] ensures that uh no matter how the AI
[00:55:15] phrases its output, the output is
[00:55:18] converted into a neat predictable string
[00:55:21] that we can feed into the next step
[00:55:23] directly. So this is especially
[00:55:27] important whenever we are building
[00:55:30] multi-step workflows one after the other
[00:55:33] because one wrong uh output can easily
[00:55:37] break the next prompt or the step in the
[00:55:40] process. Now whenever we talk about
[00:55:42] multi-step workflows
[00:55:44] we introduce this concept of chaining
[00:55:47] where the output of one prompt becomes
[00:55:49] the input to the next. So by connecting
[00:55:52] this multiple prompts in a chain, what
[00:55:54] we can do is we can perform complex task
[00:55:57] that requires several steps. For
[00:55:59] instance, let's say we first generate a
[00:56:02] detailed report on a topic using one
[00:56:04] template, parse it into a clean string
[00:56:06] using str output parser and then feed it
[00:56:09] into another template to create this
[00:56:11] short concise memory.
[00:56:13] Now this chain ensures that the flow of
[00:56:15] information is seamless while templates
[00:56:17] and parsers gives us the control and
[00:56:19] reliability at each step. To summarize,
[00:56:24] the approach
[00:56:26] allows us to uh break down or decompose
[00:56:29] this complex AI task into structure and
[00:56:31] manageable steps. To summarize these
[00:56:34] three key concepts, prompt templates
[00:56:36] defines what we want and keep
[00:56:38] instructions consistent. STR output
[00:56:41] parser ensures clean and reliable
[00:56:43] outputs and chaining lets us link
[00:56:46] multiple steps together to produce more
[00:56:48] advanced result. Now when we combine
[00:56:51] these three together we can build these
[00:56:54] multi-step AI workflows for real world
[00:56:58] application.
[00:56:59] So now let's go into the practical
[00:57:02] implementation of these three concepts
[00:57:04] that we have just talked about.
[00:57:08] Okay. Okay. So, I'm going to create a
[00:57:09] folder
[00:57:11] here
[00:57:15] output parsers.
[00:57:19] Let's create a file inside this str
[00:57:22] output parsers.ai.
[00:57:27] So, let's import
[00:57:30] a model first. Import
[00:57:33] chat Google generative AI. Let's also
[00:57:37] import
[00:57:42] uh and then we'll import
[00:57:46] prompts from langen core
[00:57:53] prompt template sorry prompt template
[00:57:56] okay we'll do this first we'll show how
[00:58:00] we break down the steps and then we'll
[00:58:02] link up together uh using chaining at
[00:58:04] last So first of all I'm going to define
[00:58:07] a model.
[00:58:09] The model is the Gemini flash model.
[00:58:16] Okay.
[00:58:18] Now uh I will generate my first prompt
[00:58:23] using prompt templates. So first
[00:58:26] prompt
[00:58:28] we'll define this using template one.
[00:58:31] This is done using prompt template.
[00:58:35] The template detail is write a detailed
[00:58:40] report on
[00:58:44] topic. The topic is going to be my
[00:58:46] placeholder. But what will come inside
[00:58:48] that placeholder is this input variable.
[00:58:52] And this input variable is going to be
[00:58:54] my topic.
[00:58:58] Okay.
[00:59:00] If I need to invoke this, I can invoke
[00:59:01] this using this prompt one template one
[00:59:06] dot invoke.
[00:59:08] Uh
[00:59:11] the topic is let's say uh English
[00:59:14] Premier League.
[00:59:16] English Premier League 2024
[00:59:21] or 2023 2024.
[00:59:28] Okay. So this is my topic.
[00:59:32] If we want to check what kind of prompt
[00:59:35] it's it generates, we can run this and
[00:59:39] then see
[00:59:42] that the that using the prompt template
[00:59:45] we can generate such kind of prompts
[00:59:47] here. Right? D report on English Premier
[00:59:49] League 2023 2024. Simply this particular
[00:59:52] topic is going to be replaced here in
[00:59:55] the placeholder. Okay. I don't want to
[00:59:57] print this. Now I want to generate my
[01:00:00] second prompt.
[01:00:03] [snorts] Second prompt, we'll define it
[01:00:05] using template 2. We'll use prompt
[01:00:08] template.
[01:00:09] And then the template details is going
[01:00:11] to be write a four point summary
[01:00:18] on the following.
[01:00:21] The placeholder is going to be text.
[01:00:25] uh now after this what I'm going to do
[01:00:28] is I'm going to define my input
[01:00:29] variables which will be my text here. So
[01:00:33] based on this I can again generate
[01:00:35] prompt two. So prompt two is going to be
[01:00:38] invoke from template 2.
[01:00:41] Template 2 dot invoke and then my text
[01:00:46] will be uh
[01:00:50] okay where will my text come from? Okay,
[01:00:52] my text has to come from this first
[01:00:54] prompt here. So for that I will have to
[01:00:58] invoke the model using this particular
[01:01:00] prompt here. So model dot invoke. Okay,
[01:01:03] let's write this result one.
[01:01:06] And then model dot invoke uh this has to
[01:01:10] be prompt one and then we need the
[01:01:14] content of this one not the entire
[01:01:17] response but only the content part or
[01:01:19] the text part. So here what I'll have to
[01:01:22] put is I'll have to put rest
[01:01:26] result one.
[01:01:30] Okay. Now based on this I'll have to
[01:01:32] again invoke the model
[01:01:38] prompt
[01:01:40] to uh
[01:01:44] prompt two.
[01:01:47] But now I can print
[01:01:50] my result dot content here. Okay.
[01:01:54] So here we've only used prompt template
[01:01:56] the first concept that we've talked
[01:01:58] about. So we can define a template in
[01:02:01] such a way and then generate the prompt
[01:02:03] based on uh based on the template that
[01:02:07] we've created using prompt template and
[01:02:08] then invoke the model. So, but one thing
[01:02:11] that you need to remember here is result
[01:02:14] one if we only invoke the model and not
[01:02:16] print its content. This is not going to
[01:02:19] give me a standard string response here.
[01:02:23] So for that what I need is I want to
[01:02:27] take out the content part of this result
[01:02:30] one. But still I might not be sure that
[01:02:32] this provides me a string here. For that
[01:02:35] I'm going to do str result just to be on
[01:02:38] the safer side because the prompt needs
[01:02:40] to be a result here or a string here
[01:02:44] because the content we pass in this
[01:02:46] particular text has to be a string. So
[01:02:49] now what we can do is we can print out
[01:02:51] result one to here and then we'll run
[01:02:53] this model first then we'll invoke
[01:02:56] invoke str output parser and jin
[01:02:59] later on. Let's also use a divider
[01:03:04] so that it becomes clear to us. Okay.
[01:03:07] Now if I run this, I don't think I have
[01:03:09] any errors. Let me run this.
[01:03:39] Okay, let's go down up here.
[01:03:52] So
[01:03:53] here we have the
[01:03:56] here we have the result from the first
[01:03:57] prompt. So it is in in fact giving me in
[01:04:01] terms of points. So this is a detailed
[01:04:06] detailed uh report about
[01:04:10] English Premier League. And then from
[01:04:12] the second prompt we have a fourpoint
[01:04:14] summary about the English Premier
[01:04:15] League. It is summarizing whatever text
[01:04:17] is being generated upwards here. Okay,
[01:04:19] this is working well. But
[01:04:22] we could have made this code a lot
[01:04:24] shorter here. So how do we do that? Now
[01:04:27] we introduce the concept of str output
[01:04:29] passes to make sure that our output is
[01:04:32] in string and then
[01:04:35] based on that we also introduce the
[01:04:38] concept of chaining so that we don't
[01:04:39] have to write two different invokes
[01:04:42] here. So now we're going to use that
[01:04:44] particular approach. So I don't need to
[01:04:48] clear anything much. I'm going to
[01:04:50] comment this out. I'm also going to
[01:04:52] comment these two lines out.
[01:04:55] Uh I'll have my prompt one.
[01:05:03] In fact, I don't even need to generate
[01:05:05] prompt one, prompt two. So I'll just
[01:05:08] have two different templates. I'll uh
[01:05:12] import uh STR output parser here. So
[01:05:15] langen code dot output parsers import
[01:05:18] str output parser.
[01:05:21] Okay, I'm going to remove all of this so
[01:05:22] that you don't get confused here. So I
[01:05:25] don't need this. I don't need this. What
[01:05:28] I'll have to define is a chain. So my
[01:05:31] chain is going to be
[01:05:34] first
[01:05:36] invoke template one then invoke a model.
[01:05:38] Okay, I also need to define a parser
[01:05:40] here. So, parser object from str output
[01:05:44] parser class. Okay, so the model
[01:05:48] response needs to be converted into a
[01:05:49] standard string format using the str
[01:05:52] output parser. Then after that, I'll
[01:05:54] have to invoke model uh template 2
[01:05:57] first. Then again, I'll have to invoke
[01:06:00] the model, pass the prompt from template
[01:06:02] to the model, and then use a parser
[01:06:03] again. So all of those steps can be
[01:06:07] reduced to this single step using the
[01:06:09] concept of chain.
[01:06:12] Now to get the result what I need to do
[01:06:14] is I just need to invoke the chain and
[01:06:16] not the model because the model
[01:06:18] invocation process is already defined
[01:06:20] inside this chain here.
[01:06:23] So so
[01:06:25] what parameter do we need to provide
[01:06:27] here? If we look at template one the
[01:06:29] entry point to template one is this
[01:06:31] particular topic here. So what we need
[01:06:33] to do is we just need to provide a topic
[01:06:35] inside this.
[01:06:37] The topic can be English Premier League
[01:06:42] 2023
[01:06:44] 2024
[01:06:46] and then I can simply provide print out
[01:06:48] the result inside this and still the
[01:06:51] model will work but the model will only
[01:06:55] print out the output of this particular
[01:06:59] second template here. All of these in
[01:07:01] between task will be handled by this
[01:07:03] chain. So let's run this.
[01:07:07] It will take some time to run because
[01:07:10] there are two model invocations in
[01:07:11] between.
[01:07:13] [snorts]
[01:07:42] So as you can see we can directly see
[01:07:45] the output of this particular second
[01:07:47] template here because everything in
[01:07:49] between is being handled by this chain
[01:07:51] and the final result is a fourpoint
[01:07:53] summary that we get from this particular
[01:07:56] topic here. So what is happening here?
[01:08:00] Everything that we did earlier has been
[01:08:02] happening here too. But the
[01:08:06] but since we're only printing the final
[01:08:09] result, we're seeing the final result
[01:08:11] here. So this concept of chain is very
[01:08:15] crucial in implementing such multi-step
[01:08:17] workflows that we've talked about
[01:08:18] earlier. In our previous video, we
[01:08:21] learned how to use prompt templates to
[01:08:24] give the model clear instructions and
[01:08:26] how to use SCR output parser to clean up
[01:08:29] the model's text responses. But what if
[01:08:32] we want the model to not just write text
[01:08:35] but actually return structured data like
[01:08:37] proper JSON objects with specific
[01:08:40] fields? That's where the structured
[01:08:42] output parser comes in. Uh think of it
[01:08:45] like giving the model a blue blueprint
[01:08:47] for for its answer. So instead of
[01:08:49] letting it respond however it wants, we
[01:08:51] define a clear structure like for
[01:08:53] example we can say give me three facts
[01:08:55] about black holes and each fact should
[01:08:58] go into its own field. fact one, fact
[01:09:00] two and fact three. So we define this
[01:09:02] structure using response schema which
[01:09:05] defines uh what each field represents.
[01:09:08] Then the structured output parser uses
[01:09:11] that schema to make sure the AI's output
[01:09:14] follows the exact format we asked for.
[01:09:16] Uh usually that is a validation object.
[01:09:20] Now, if you worked with LLMs
[01:09:23] before or you followed our video, uh you
[01:09:26] know that sometimes the model does not
[01:09:28] exactly uh follow the instruction
[01:09:31] perfectly. So, it might it might miss a
[01:09:35] field, forget the brackets or add some
[01:09:37] extra text. Now, that's where the output
[01:09:40] fixing error or the output fixing parser
[01:09:43] saves the day. It automatically
[01:09:45] identifies when the output isn't in the
[01:09:47] correct format and uses the model itself
[01:09:50] to repair or reformat the response until
[01:09:52] it matches the required schema. So what
[01:09:56] we are trying to do here is we're really
[01:09:59] teaching the model to think structurally
[01:10:02] to not just like generate sentences but
[01:10:04] also to produce clean structured content
[01:10:08] uh that a program can directly read and
[01:10:11] use.
[01:10:12] So this actually becomes powerful when
[01:10:16] we want to build uh systems like
[01:10:19] knowledge extractors, facts, fact
[01:10:21] generators or even uh data analysis
[01:10:24] tools where consistency matters. And
[01:10:27] just like we did in the previous video,
[01:10:29] we wrap everything inside a chain. So
[01:10:32] the flow looks like the following here.
[01:10:34] So the prompt first defines the task,
[01:10:36] the model generate the response and the
[01:10:39] parser ensures the output is valid and
[01:10:42] well formatted. So the concept brings
[01:10:45] together everything we've learned so
[01:10:47] far. Clear prompting, structured control
[01:10:49] and automatic error correction, meeting
[01:10:52] making our AI output uh also ready for
[01:10:56] [snorts] uh automation. So now let's go
[01:10:59] to the implementation of whatever we
[01:11:01] talked in this video.
[01:11:07] Let me create a new file called
[01:11:10] structured
[01:11:14] output parser.py.
[01:11:18] Okay, first model.
[01:11:25] [snorts] We've been doing this since our
[01:11:26] first video. So I I hope you understand
[01:11:30] this. Then the credentials.
[01:11:40] Then we're importing a prompt template
[01:11:42] from langen core.
[01:11:52] Then we'll import our output parsers
[01:11:55] here. So uh it will again come from lang
[01:11:59] code output parsers import structured
[01:12:01] output parser
[01:12:03] and a response schema.
[01:12:11] Okay I did something wrong here. So this
[01:12:13] is going to be
[01:12:18] oh okay so it does not come from langen
[01:12:21] port but it comes from langen. So output
[01:12:24] parsers import structure output parser
[01:12:27] and
[01:12:31] okay something is wrong here. Oh I
[01:12:33] should have written from not
[01:12:36] import structured output parser and then
[01:12:39] a response schema.
[01:12:41] Now uh from langchain.output parsers
[01:12:44] I'll need output fixing parser to
[01:12:49] uh so this library allows the model to
[01:12:52] recorrect if there is any error in terms
[01:12:55] of it response.
[01:12:58] So load env I'll first define my model.
[01:13:15] Okay. Now we'll define our schema here
[01:13:17] or the response schema that we want.
[01:13:20] So basically we're going to pass a topic
[01:13:24] and then we will ask the model to
[01:13:26] generate three facts and then we'll
[01:13:28] create a placeholder using these
[01:13:30] response schema for those facts here. So
[01:13:33] so for the first one we'll call fact one
[01:13:37] and then
[01:13:39] uh it detail will be first fact about a
[01:13:44] certain topic. Okay we'll say black
[01:13:46] hole.
[01:13:49] So this will be our first one. We'll
[01:13:51] again define a response schema. We'll
[01:13:54] have fact two
[01:13:58] and then add a description.
[01:14:00] So this will be second fact about black
[01:14:04] hole.
[01:14:07] And then we'll do a response schema
[01:14:08] again. name equals to
[01:14:13] fact three
[01:14:16] description equals to third
[01:14:19] fact about black hole.
[01:14:25] Okay. So we will define our parser. So
[01:14:29] this is going to be a structured output
[01:14:30] parser but the structured output parser
[01:14:33] will be based on the schema that I have
[01:14:37] provided earlier. So structure output
[01:14:39] parser from
[01:14:41] response is schemas and then I'll and
[01:14:46] and then I'll pass in the schema here.
[01:14:47] So again at last if the model does not
[01:14:52] uh obey us in passing
[01:14:56] the in uh generating the output based on
[01:14:59] this schema. I'm going to use a output
[01:15:02] fixing parser
[01:15:04] from
[01:15:06] llm.
[01:15:09] The llm is going to be our model and
[01:15:12] then the parser is going to be a parser
[01:15:14] which will strictly adhere the model uh
[01:15:18] to the given schema here. So now let me
[01:15:20] generate a template.
[01:15:23] Uh
[01:15:25] so template equals to I'm going to use
[01:15:28] this using prompt template. We've
[01:15:29] already done this earlier.
[01:15:32] So template will be give me
[01:15:35] three facts about
[01:15:39] topic.
[01:15:42] Uh
[01:15:44] write something more. Return only valid
[01:15:49] JSON instruction.
[01:15:55] instruction that follows this format and
[01:15:59] I'll provide a format here. Uh let me
[01:16:03] enclose this using
[01:16:06] string tag
[01:16:08] so that I can give multi-line strings
[01:16:11] here. So now uh the format
[01:16:16] will be uh format or the instruction
[01:16:20] format instruction
[01:16:24] or we'll we will we'll call it the
[01:16:26] response format here. So response format
[01:16:32] uh the topic
[01:16:35] sorry the input variables at first is
[01:16:38] going to be our topic
[01:16:42] and then I'll also define a partial
[01:16:44] variables for the response format that
[01:16:47] we provided here. So response
[01:16:51] format and this is going to come from
[01:16:54] parser dot get format instruction.
[01:16:59] So this particular parser will provide
[01:17:01] this schema or the response format to
[01:17:04] this template here. Now I'll create a
[01:17:07] chain where I'll pass in the template
[01:17:10] first then a model first and then the
[01:17:13] passer here.
[01:17:16] So first of all the prompt will be
[01:17:18] generated using template and it will be
[01:17:20] passed to the model and then the model
[01:17:22] response will be fixed by the parser.
[01:17:24] Now I can invoke this chain
[01:17:28] using the entry point which is our
[01:17:31] template. So I'll need to provide a
[01:17:33] topic here
[01:17:36] and the topic will be black hole
[01:17:39] and then I can print out the result.
[01:17:44] Let me clear this and run this again.
[01:17:49] Okay, I missed topic here. So, clear
[01:17:52] this
[01:17:54] and run it again.
[01:18:01] There are a few spelling mistakes, but
[01:18:02] it's okay. I can see that I got a JSON
[01:18:06] format where I have fact one
[01:18:09] uh fact two and
[01:18:13] where's three? Okay, I have fact three
[01:18:15] just like the way that we've asked for
[01:18:18] in our schema map. Uh so what is being
[01:18:23] done here? The prompt template is
[01:18:24] generating
[01:18:26] a prompt based on the template that we
[01:18:29] provided here. The structured output
[01:18:32] parser uh is is asking the model to base
[01:18:36] its
[01:18:37] response on on the basis of this
[01:18:40] provider schema. Here the output fixing
[01:18:42] parser is strictly
[01:18:46] uh asking the model to follow this
[01:18:48] particular schema. Here in the prompt
[01:18:51] template one extra variable we provided
[01:18:53] is the partial variables. that partial
[01:18:55] variables is the
[01:18:58] response schema that we provided here
[01:19:00] and then we've extracted it from the
[01:19:03] parser uh parser object of structured
[01:19:07] output parser and then we've generated a
[01:19:09] chain and generated the response. So I
[01:19:12] hope this runs for you on your end as
[01:19:14] well. If you in our previous video we
[01:19:16] talked about how large language models
[01:19:19] often gives us free flowing text
[01:19:21] responses and then how we can use tools
[01:19:24] like structured output parser to make
[01:19:26] those responses more organized and
[01:19:27] consistent. But now we're taking a same
[01:19:30] idea into a step further by introducing
[01:19:33] a much more powerful and professional
[01:19:35] tool called the pyantic output parser.
[01:19:37] So what exactly does it do? Now think of
[01:19:40] it in this way. So when we ask a large
[01:19:43] language model for structured
[01:19:45] information like someone's name, age or
[01:19:47] city, the model tries its best to follow
[01:19:50] our instruction. But sometimes it gives
[01:19:53] extra text, sometimes it forgets a field
[01:19:56] or sometimes it just formats things
[01:19:58] incorrectly. The parenting output parser
[01:20:01] uh helps us control and validate those
[01:20:04] responses. So it makes sure the models
[01:20:07] output isn't just structured but also
[01:20:09] it's correct, complete and reliable.
[01:20:13] This parser is built on top of a Python
[01:20:15] library called Pyntic. And Pyic is all
[01:20:18] about data validation. It actually lets
[01:20:21] us define what kind of data we expect.
[01:20:23] For example, like we can say the name
[01:20:25] should be text, age should be number and
[01:20:28] then it has to be greater than 18 and
[01:20:30] the city should be a word. So when the
[01:20:33] model gives us a response, the parser
[01:20:35] checks if everything fit those rules or
[01:20:37] not. If something is missing or invalid,
[01:20:39] uh the parser immediately flags it or
[01:20:42] even corrects it when combined with a
[01:20:44] tools like out tools like output fixing
[01:20:47] output fixing parser. Now if you
[01:20:50] remember the structured output parser we
[01:20:51] used earlier in the previous video, it
[01:20:53] also gave us structured data. So what is
[01:20:57] the difference between these two here?
[01:20:59] So the key difference is that structured
[01:21:00] output parser mainly focuses on
[01:21:02] formatting. It helps the model respond
[01:21:04] in a defined structure but the pyetic
[01:21:07] output parser uh adds this layer of
[01:21:09] intelligence and validation on top of
[01:21:12] that. So it actually does not just
[01:21:15] organize the response but it also checks
[01:21:17] the response and ensures that it matches
[01:21:19] the exact data type and the constraints
[01:21:21] we define. So that means uh we'll get
[01:21:25] fewer errors uh cleaner data and a far
[01:21:27] more predictable output which is
[01:21:28] especially important when you're
[01:21:29] building real world application. So the
[01:21:32] beauty of this parser is that the once
[01:21:34] the model output passes through it, you
[01:21:37] can get a clean and reliable data ready
[01:21:41] to use in your code or application
[01:21:44] directly. Like you don't need to worry
[01:21:46] about
[01:21:48] converting things to string, fixing JSON
[01:21:50] or like checking for missing fields.
[01:21:52] Everything comes out neat and validated
[01:21:55] exactly the way you want it. Uh so the
[01:21:58] pyic output parser takes the concept of
[01:22:00] this structured output and then upgrades
[01:22:03] it with validation and reliability. If
[01:22:07] the structured output was our first step
[01:22:10] towards getting a structured response
[01:22:12] from LLM then the penting version is a
[01:22:14] professional grade tool uh the one that
[01:22:16] makes your AI pipeline more stable and
[01:22:19] then uh production ready. So that is why
[01:22:24] this concept is so much important to
[01:22:26] understand. Because as we start building
[01:22:29] more complex uh
[01:22:33] systems, we will rely on such kind of
[01:22:36] validated structured output to make sure
[01:22:38] our AI
[01:22:40] uh gives us the output in the format
[01:22:43] that we expect. So after this brief
[01:22:45] introduction, let's go to the code and
[01:22:47] see what we have talked about and
[01:22:49] implement it in real life.
[01:22:58] Okay. So I'm going to create a new file
[01:23:01] here.
[01:23:02] I'm going to call this pyantic
[01:23:05] parser.py.
[01:23:08] So
[01:23:10] I will have some import. First of all,
[01:23:12] our model
[01:23:19] then envy
[01:23:40] output parser.
[01:23:50] Uh you can also use this output fixing
[01:23:53] parser if you want but uh I'm not going
[01:23:55] to do this right now. I've already shown
[01:23:58] you how to use it in the previous video.
[01:24:01] So from Pyantic I'm going to import base
[01:24:03] model
[01:24:04] and then I'm going to import a field.
[01:24:07] Okay. So load the credentials
[01:24:10] define the model
[01:24:19] and after that I'm going to create this
[01:24:22] pentic validation class called person.
[01:24:26] So here I'll have base model as a
[01:24:29] parameter I'm going to include three
[01:24:32] things name age and string. So name is
[01:24:35] going to be a string. its field and its
[01:24:38] detail is
[01:24:40] uh the person's
[01:24:44] full name.
[01:24:46] Then I'm going to have an age. Age is
[01:24:48] going to be an integer and I'll also
[01:24:51] define its detail. So the age uh has to
[01:24:56] be greater than
[01:24:58] 18 and then it has to be less than uh
[01:25:03] let's say 100.
[01:25:05] Then I'll also add the detail or the
[01:25:09] description.
[01:25:13] The person's age
[01:25:17] must be greater than 18. Well, I've
[01:25:21] already defined that here. Now I'm going
[01:25:23] to define a city. It is going to be
[01:25:26] string.
[01:25:28] Okay. Field
[01:25:31] field field and its detail.
[01:25:34] So
[01:25:38] the city
[01:25:40] where the person lives.
[01:25:43] Okay. Now I have defined this class. I'm
[01:25:46] going to
[01:25:48] create an object a pyic parser
[01:25:51] pyic output parser and then the pyic
[01:25:54] object is the class that we have
[01:25:56] defined.
[01:25:59] Okay. Now let's create a template
[01:26:02] from the prompt template that we have.
[01:26:05] So the template is going to be I'm going
[01:26:08] to create a multiple string or
[01:26:10] multi-line string here.
[01:26:13] So the prompt template is giving me give
[01:26:15] me
[01:26:18] give me the name, age and city of a
[01:26:25] of a fictional
[01:26:30] fictional place
[01:26:33] person. Uh okay what else? Make sure the
[01:26:37] age is greater than 18 and less than
[01:26:43] 100. Also uh return
[01:26:49] return the response in following format
[01:26:53] and the format is
[01:26:56] our uh response format just like we did
[01:27:00] earlier.
[01:27:02] Okay. What else? I need a input
[01:27:03] variable. Input variable is going to be
[01:27:08] a place name
[01:27:11] and then my partial variables. Partial
[01:27:14] variables is going to come from uh this
[01:27:18] is response
[01:27:20] format and then it is going to come from
[01:27:22] parser or the parser object dot get
[01:27:25] format instructions.
[01:27:28] Okay.
[01:27:35] Now what I can do is I can directly
[01:27:37] define a chain. So it will first call up
[01:27:41] template then model and then the parser.
[01:27:46] Uh then after that I can invoke this
[01:27:50] chain
[01:27:52] using the entry point to this chain
[01:27:54] which is a place name.
[01:27:56] So let's say Nepal
[01:28:00] and then print a result here.
[01:28:04] So the code seems to be okay. If you
[01:28:07] have any problem viewing this, let me do
[01:28:10] a word wrap so that you can see
[01:28:12] everything else here. Now let me run
[01:28:14] this code and see what we get in our
[01:28:17] response. We should get the name, age
[01:28:19] and city just like we asked for. Okay.
[01:28:22] So if if we see here we see a name
[01:28:25] Pracastahal age is 45 and city is
[01:28:29] provided here just like in the format
[01:28:32] that we asked for. So this is how we use
[01:28:34] pyic output parser uh using lang graph.
[01:28:38] So this is all for this video. I hope it
[01:28:40] runs in your end as well. In our
[01:28:42] previous video, we've already worked
[01:28:44] with simple chains connecting multiple
[01:28:46] steps together where the output of one
[01:28:48] step becomes the input for the next.
[01:28:52] Now, we'll talk about a concept concept
[01:28:55] a bit deeper and talk about why chains
[01:28:58] are so useful and how we can make them
[01:29:00] more powerful using something called
[01:29:02] sequential chains. The biggest advantage
[01:29:05] of using chains is that uh they help us
[01:29:07] organize complex AI workflows into
[01:29:10] smaller logical steps. So instead of
[01:29:13] sending one massive prompt and hoping
[01:29:15] the models model handles everything
[01:29:18] correctly, we break the process down.
[01:29:20] Maybe first generate something then
[01:29:22] summarize it and then finally maybe
[01:29:24] analyze it. This modular structure makes
[01:29:27] our workflow much more cleaner, more
[01:29:29] reusable and then easier to debug. So if
[01:29:32] one part of the chain isn't doing well,
[01:29:34] we can just improve that step without
[01:29:37] touching the rest. So it's a very
[01:29:38] practical way to scale our AI projects.
[01:29:41] Now let's talk about sequential chains.
[01:29:43] Uh which is one of the most useful type
[01:29:45] of chains in lang chain. So sequential
[01:29:47] chains work in a step-by-step manner.
[01:29:49] The output from one stage is is
[01:29:51] automatically passed to the next stage
[01:29:53] in order. So think of it like an
[01:29:55] assembly line. So each component in the
[01:29:58] chain has a specific role and together
[01:30:00] they create a complete workflow. So for
[01:30:03] example, step one could generate a
[01:30:05] detailed article. Step two could
[01:30:07] generate summarize it into a few
[01:30:10] sentences and then step three could
[01:30:12] maybe extract keywords or insights from
[01:30:14] that summary. The entire process runs
[01:30:16] very smoothly with data flowing
[01:30:18] automatically between steps. So now
[01:30:20] what's great about sequential chains is
[01:30:22] that they makes complex reasoning task
[01:30:25] easier to redesign and control. So we
[01:30:28] can exactly fix what happens at its each
[01:30:31] it stage and then how information moves
[01:30:33] between them. And since everything is
[01:30:35] modular uh we can mix and match our
[01:30:38] components, change a prompt, switch a
[01:30:40] model or maybe add a new processing step
[01:30:43] all without rewriting the entire
[01:30:45] pipeline. So in this video we'll
[01:30:47] actually implement a sequential chain
[01:30:49] and see how it helps us combine multiple
[01:30:52] prompts and models into one connected
[01:30:54] process. And by the end of this video
[01:30:56] you will be able to understand not how
[01:30:59] not how just to build one or not just
[01:31:01] how to build one but also why sequential
[01:31:03] chaining is one of the most powerful
[01:31:05] ideas in line chain for creating
[01:31:07] intelligent and multi-step AI
[01:31:08] applications. So now let's go to the
[01:31:11] code.
[01:31:14] So I'm going to create a new folder here
[01:31:17] called
[01:31:19] uh it's folder number five called chains
[01:31:22] and inside this chain I'm going to
[01:31:23] create my first chain called sequential
[01:31:27] chain.py
[01:31:29] pipe.
[01:31:30] Okay. So again, first of all, we'll have
[01:31:34] a model
[01:31:39] and then avo
[01:31:46] template. So that is going to come from
[01:31:49] langen core.
[01:31:55] And then we'll also use this str output
[01:31:59] passer that we've already used earlier
[01:32:01] too. And then that is also going to come
[01:32:03] from langen core.
[01:32:08] Load our credentials.
[01:32:10] Define our model.
[01:32:19] Now I'm going to
[01:32:22] provide two template. The first template
[01:32:26] will be a prompt template.
[01:32:29] We've done a similar example earlier
[01:32:31] too, but uh I'm going to use it anyway
[01:32:34] here. So, generate
[01:32:37] three detailed
[01:32:39] uh detailed report
[01:32:43] on a topic
[01:32:46] topic. Uh I'm also going to use my input
[01:32:49] variables. My input variables will be a
[01:32:52] topic. So this is going to be my first
[01:32:54] prompt that will be generated from
[01:32:57] prompt template. The next will be
[01:33:00] another prompt that says
[01:33:04] uh generate a threepoint summary.
[01:33:08] Threepoint summary on following text
[01:33:12] and then I'll provide a text here.
[01:33:15] Uh
[01:33:17] so
[01:33:19] my input variables is going to be a
[01:33:21] text.
[01:33:23] And then uh I already have a model. So
[01:33:26] I'll define my parser which will be from
[01:33:29] str output parser. And then I'll define
[01:33:32] a chain which is a sequential chain
[01:33:34] here. So first of all I'll go to prompt
[01:33:36] one. Then I'll call the model. Then I'll
[01:33:38] go to parser and then I'll go to prompt
[01:33:42] two. And then I'll again call a model
[01:33:45] and then I'll go to parser again. And
[01:33:47] finally I I'll invoke this chain and
[01:33:49] then store the output in the result. So
[01:33:53] chain do.invoke. I'll define an entry
[01:33:54] point for this chain which is topic.
[01:33:58] So,
[01:34:00] so my topic is going to be
[01:34:03] my topic is going to be uh 3II
[01:34:08] interstellar.
[01:34:12] Okay. Threei 3i atlas
[01:34:16] interstellar object which is quite
[01:34:19] uh in use these days. So I'm going to
[01:34:22] use this topic and then I'll just print
[01:34:25] out the result. So, so this here is a
[01:34:29] sequential chain here. So, let me run
[01:34:31] this and while this is being run, I'll
[01:34:33] try to explain you what's happening
[01:34:35] here. Okay, something's wrong.
[01:34:40] Ah, this is a model name.
[01:34:45] So, let me run this again.
[01:34:48] So, we have our model. The first prompt
[01:34:51] is generated from this prompt template.
[01:34:53] The second prompt is generated from this
[01:34:55] prompt template. So based on the first
[01:34:57] prompt which is passed to the model and
[01:34:59] then and then the output is passed
[01:35:01] through the string output parser which
[01:35:03] means the entire output will be
[01:35:05] converted to string and then and then
[01:35:07] that particular output will be passed to
[01:35:09] this text here uh using prompt two and
[01:35:12] the model and then the output will be
[01:35:14] passed again by str output parser and
[01:35:16] then finally be printed here.
[01:35:19] So it might take some time to run
[01:35:21] because we've got multiple models here.
[01:35:24] So let's see the output.
[01:35:42] Okay, we have a three-point summary
[01:35:44] about 3i atlas. So the first point is
[01:35:48] provided here. The second point is here
[01:35:50] and the third point is here. The content
[01:35:52] is not that important right now. Uh I
[01:35:54] just wanted to show you the
[01:35:56] implementation of chains. In our last
[01:35:59] video we explored sequential chains
[01:36:01] where each step in the chain executes
[01:36:04] one after another in a fixed order. That
[01:36:06] was great for workflows that all that
[01:36:08] always follows the same path. But what
[01:36:11] if you want your AI workflow to make
[01:36:14] choices along the way? What if the next
[01:36:16] step depends on the output of the
[01:36:17] previous step? Now that's where the
[01:36:19] conditional chain comes in. So
[01:36:21] conditional chains lets you design
[01:36:23] workflows that branch based on certain
[01:36:26] conditions. So instead of a single fixed
[01:36:28] path, you can define multiple possible
[01:36:30] paths and the chain decides which one to
[01:36:33] follow depending on the model's response
[01:36:35] or some other criteria. So think of it
[01:36:38] like you choose your own adventure book.
[01:36:40] Depending on your choice, the story
[01:36:41] takes a different direction. Conditional
[01:36:44] chains give your AI workflows that same
[01:36:46] flexibility. Okay, let's take an
[01:36:48] example. So imagine you're processing
[01:36:50] customer feedback. So if the feedback
[01:36:52] mentions a bug, you might want to send
[01:36:55] it to the development team. If it's a
[01:36:57] feature request, you might want to send
[01:36:59] it to a product team. And if it's a
[01:37:01] compliment, maybe you log it and then
[01:37:03] thank the user automatically. So with a
[01:37:06] conditional chain, the workflow
[01:37:07] evaluates the content and routes it
[01:37:10] automatically. You don't have to
[01:37:12] manually check each case. The chain
[01:37:14] handles the branching logic. So the real
[01:37:17] advantage of a conditional chain is that
[01:37:19] they make your workflow dynamic and
[01:37:21] intelligent. So you're no longer limited
[01:37:23] to linear processes. Instead, your AI
[01:37:26] can adapt its upcoming step based on the
[01:37:29] data it sees. Now this is incredibly
[01:37:32] useful for real world application where
[01:37:34] inputs can vary widely like customer
[01:37:36] support, content analysis, data
[01:37:38] classification and much more. So in this
[01:37:42] video we'll implement a conditional
[01:37:44] chain and see exactly how to set up
[01:37:47] multiple parts and conditions. So by the
[01:37:49] end of this video, you'll understand how
[01:37:51] to create a flexible AI pipeline that
[01:37:53] responds intelligently to different
[01:37:55] situations, making your applications
[01:37:57] more robust and closer to human like
[01:38:00] decision-m. Now let's jump onto the
[01:38:02] code.
[01:38:08] Okay, I'll create a new file here
[01:38:11] and I'll call it uh
[01:38:15] conditional chain.py.
[01:38:19] First of all, we'll have a model.
[01:38:25] then env
[01:38:32] template.
[01:38:42] Then I will have
[01:38:45] uh the pyic output parser which will
[01:38:47] come from length and core dot output
[01:38:49] parsers import
[01:38:53] identic output parser.
[01:38:57] uh then I will use this runnable schema
[01:39:02] dot runnable
[01:39:04] importable
[01:39:07] branch for
[01:39:09] flexive branching chain logic and then
[01:39:11] runnable lambda for a lambda function
[01:39:14] since we using pye model so we'll
[01:39:18] include a base model and a field
[01:39:22] and also uh let me write this
[01:39:28] literal class from the typing function.
[01:39:32] Load the library.
[01:39:36] Load the model.
[01:39:48] Okay. Now,
[01:39:51] uh I'll also have one more parcel which
[01:39:53] is the str output parser.
[01:39:55] So [clears throat]
[01:39:56] my parser object will also be created
[01:39:59] str out parser. Now I will create a
[01:40:01] pentic class here for feedback.
[01:40:06] So this will be a base model.
[01:40:09] I will try to find the sentiment of the
[01:40:12] feedback which will have two options.
[01:40:15] And it can be the positive feedback or a
[01:40:18] negative feedback.
[01:40:20] And then its detail will be given here
[01:40:23] field
[01:40:24] and description
[01:40:26] is the sentiment of
[01:40:30] the feedback
[01:40:34] feedback provider.
[01:40:36] Okay. I will have a parser two which
[01:40:39] will be my pyic parser or pyic output
[01:40:42] parser
[01:40:45] and then the pyic object will be my
[01:40:47] feedback class.
[01:40:50] Now I'll have a prompt one
[01:40:57] which will be my prompt template
[01:41:01] uh
[01:41:04] prompt
[01:41:06] template.
[01:41:09] It template will be classify
[01:41:12] the
[01:41:14] classify the sentiment of
[01:41:19] following feedback text into positive or
[01:41:23] negative
[01:41:28] and then this will be my feedback test
[01:41:32] uh feedback placeholder. So input
[01:41:35] variables
[01:41:38] will be
[01:41:42] feedback
[01:41:44] and and I'll also have a partial
[01:41:46] variable
[01:41:48] uh because I'll provide a format
[01:41:50] instruction here
[01:41:52] uh statement and provide the response
[01:41:57] in following format
[01:42:00] and then this will have our response
[01:42:04] format. Right. So I'll have a partial
[01:42:06] variable
[01:42:09] uh
[01:42:11] uh okay this has to be a dictionary.
[01:42:15] So response
[01:42:18] format is going to come from parser 2
[01:42:21] parser 2 dot get format instructions.
[01:42:26] Okay I'm going to use a word so that uh
[01:42:29] it will be easier for you to view here.
[01:42:32] Okay. This is my [clears throat] first
[01:42:36] first prompt here. I'll first define a
[01:42:39] classifier chain
[01:42:42] which will follow prompt one
[01:42:45] model one
[01:42:48] or the same model that I have. I'll just
[01:42:49] use the model and then parser
[01:42:54] and then parser two because I'm going to
[01:42:55] use the pyic parser here. Next, I'll
[01:43:00] again have another prompt
[01:43:03] which is going to say
[01:43:05] template
[01:43:09] uh write an appropriate
[01:43:13] feedback
[01:43:15] to this positive
[01:43:18] sorry appropriate response
[01:43:22] response do this positive feedback
[01:43:27] and then I'll provide write my feedback
[01:43:29] here. I'll have an input variable.
[01:43:33] Uh this will be feedback
[01:43:37] and I also have prompt three
[01:43:41] that will work for the negative
[01:43:43] feedback.
[01:43:48] So negative feedback
[01:43:53] and then the value will be prompt three.
[01:43:56] So here I'm going to declare a branch
[01:43:58] chain.
[01:44:01] Branch chain as we can see this is a
[01:44:03] sequential chain we have here. But based
[01:44:05] on the output of this chain now we'll
[01:44:08] move on to the branch chain and then
[01:44:10] either select one of these uh two
[01:44:15] prompts and then generate the response.
[01:44:17] Now
[01:44:19] for branching I'm going to use runnable
[01:44:21] branch
[01:44:23] and not this bracket. I need a small
[01:44:24] bracket here. So runnable runs I'm going
[01:44:27] to declare a lambda function here. So
[01:44:29] lambda x x [laughter]
[01:44:34] sentiment
[01:44:37] equals to
[01:44:40] uh positive.
[01:44:44] So, so if the sentiment is positive then
[01:44:50] uh my chain will be prompt to
[01:44:54] model and then parser
[01:44:59] parser else
[01:45:03] if my sentiment is negative lambda
[01:45:07] x [snorts]
[01:45:08] x dot
[01:45:11] sentiment equals to
[01:45:14] negative then my chain will be from
[01:45:17] three
[01:45:20] from three
[01:45:22] model and then a passer
[01:45:28] and I need to
[01:45:31] declare this as a runnable lambda
[01:45:37] uh lambda x. So if else if and then the
[01:45:42] last one is else condition here.
[01:45:45] So if the sentiments are either of these
[01:45:47] positives and negative sentiment then
[01:45:49] I'm going to say no valid sentiment
[01:45:52] found in my
[01:45:55] review or feedback.
[01:46:00] Okay, the bracket should not close here.
[01:46:02] So this is done.
[01:46:05] Now what I'm going to do is I'm going to
[01:46:07] combine these two chains into one chain.
[01:46:09] So first one is our classified chain and
[01:46:12] then the second one is our branch chain.
[01:46:14] So we can also combine a sequential
[01:46:18] chain and a conditional chain into one
[01:46:21] single chain here like this. The first
[01:46:23] one that is going to be executed is our
[01:46:24] SE is a sequential chain or the
[01:46:27] classified chain and and based on the
[01:46:28] response of the classifier chain we will
[01:46:31] then move to branch chain and then
[01:46:34] uh the model will work accordingly. So
[01:46:36] we'll invoke this chain dot invoke the
[01:46:41] entry point is the classifier chain and
[01:46:43] then and then in the classifier chain
[01:46:45] the entry point is feedback one sorry
[01:46:47] prompt one where I need to provide a
[01:46:49] feedback here. So let me provide a
[01:46:53] feedback and then see that
[01:46:58] the phone is actually
[01:47:03] actually amazing.
[01:47:06] Let me print the result and see what we
[01:47:08] get here. It should actually trigger
[01:47:13] prompt two and then we should get an
[01:47:15] appropriate response for this positive
[01:47:17] feedback here. So let's run this.
[01:47:21] So now we see that we get a positive
[01:47:24] response and then uh there are uh
[01:47:30] the the model classifies this feedback
[01:47:33] as positive and then based on it it
[01:47:36] generates a response. Now I'm going to
[01:47:39] change this. Okay, the phone is actually
[01:47:41] horrible.
[01:47:43] The UI is stuck and then things like
[01:47:45] that.
[01:47:47] The UI is stuck.
[01:47:50] And then if I run this
[01:47:58] so the model is in fact giving out a lot
[01:48:00] of things but you know that we can
[01:48:02] structure the output uh using the pyic
[01:48:05] output parser or this or or like we can
[01:48:09] base it on some some form of schema as
[01:48:11] we've already done earlier. So you can
[01:48:14] uh actually uh implement it yourself. So
[01:48:20] here we get that the response.
[01:48:24] Okay. So it says that when responding to
[01:48:28] negative feedback so it classifies the
[01:48:31] feedback as negative here for this
[01:48:34] thing. So in this video we saw how we
[01:48:37] could implement conditional chains using
[01:48:40] runnable branch runnable lambda as well
[01:48:42] as how we could combine a sequential
[01:48:44] chain and and a conditional chain into
[01:48:46] one and then make our uh workflow
[01:48:52] automated here. So far in the series
[01:48:54] we've explored sequential chains where
[01:48:57] each step executes one after the other
[01:48:59] and conditional chains where the
[01:49:01] workflow can branch based on certain
[01:49:03] conditions. Now we're moving into
[01:49:05] another powerful concepts in line chain
[01:49:07] called parallel chains. So what exactly
[01:49:09] is parallel chain? So in simple terms we
[01:49:12] can say that parallel chain allows us to
[01:49:14] run multiple workflows at the same time
[01:49:15] independently of each other and then
[01:49:18] combine their results. So think of it
[01:49:21] like a team working on various tasks
[01:49:23] simultaneously. So one team member is
[01:49:26] taking notes, another is taking or like
[01:49:28] creating quiz questions and and then
[01:49:30] later on someone merges both into a
[01:49:33] final report. So by doing things in
[01:49:35] parallel, we can save time, make the
[01:49:37] workflow more efficient and then handle
[01:49:39] multiple aspects of a task at once.
[01:49:43] And then that is also key advantage of
[01:49:45] parallel chain uh efficiency and
[01:49:48] modularity
[01:49:50] because each component can focus on a
[01:49:52] specific task without waiting for the
[01:49:54] others to finish and once all the
[01:49:56] parallel task are complete uh the output
[01:49:58] can be combined in a meaningful way
[01:50:00] creating a complete and comprehensive
[01:50:02] result. So what are we going to do in
[01:50:05] this video? So our plan for this video
[01:50:07] is first we'll take a block of text then
[01:50:10] we'll run two parallel task. One will
[01:50:14] generate short and simple notes from the
[01:50:16] text and then the other will generate a
[01:50:19] set of short quiz questions based on the
[01:50:21] same text and then finally once these
[01:50:23] two parallel tasks are done we'll merge
[01:50:25] the notes and the quiz into a single
[01:50:27] comprehensive document.
[01:50:29] This will show exactly how parallel
[01:50:31] chains can handle multiple output at
[01:50:33] once and then combine them seamlessly
[01:50:35] making our AI workflow both fast and
[01:50:38] organized. Now let's jump onto the code.
[01:50:45] So create a new file
[01:50:48] called sequent parallel chain not
[01:50:51] sequential chain parallel chain.py.
[01:50:54] Okay. First of all, our language model,
[01:51:02] then av function.
[01:51:08] Then I need a prompt template which will
[01:51:11] we'll get from langchen.prompts.
[01:51:20] Let's also use the str output parser.
[01:51:30] And we'll have a runnable parallel from
[01:51:34] line chain dots schema dot runnable for
[01:51:38] our runnable uh sorry for our parallel
[01:51:42] chain
[01:51:44] to run here. Okay. Now let's load the
[01:51:46] credentials. Define a model.
[01:52:02] Now first of all I'll define a prompt.
[01:52:05] First prompt will be
[01:52:08] about
[01:52:14] generating a short and
[01:52:18] like let's say generate short and simple
[01:52:22] uh nodes
[01:52:24] for or from the
[01:52:28] following or for the following topic.
[01:52:30] Sorry. For the following
[01:52:34] topic,
[01:52:38] we would place a topic in the
[01:52:40] placeholder. Our input variables is
[01:52:43] going to be topic.
[01:52:45] We're not going to enforce any kind of
[01:52:48] schema for our
[01:52:50] response right now. So, we'll just leave
[01:52:52] it to this. Our next template will be a
[01:52:56] prompt template.
[01:52:59] And this will be about generating
[01:53:03] uh generate
[01:53:05] five short question answer from the
[01:53:11] following
[01:53:14] text
[01:53:16] or input variable is going to be a text
[01:53:22] and then after this I'll have prompt
[01:53:24] three
[01:53:26] prompt template it.
[01:53:29] Um this will generate
[01:53:34] uh
[01:53:36] okay short question answer is done and
[01:53:38] then the summary is also done right. So
[01:53:40] we will have prompt three to merge the
[01:53:44] provided
[01:53:46] notes and quiz into a single document.
[01:53:53] document uh
[01:53:57] then I'll provide nodes
[01:54:01] in nodes placeholder and then base
[01:54:06] in quiz placeholder.
[01:54:11] Okay. So now let's create an object of
[01:54:16] our parser here.
[01:54:23] So parser equals to strl output parser.
[01:54:30] I'm going to create a runnable chain
[01:54:34] parallel chain which will be done using
[01:54:38] runnable parallel.
[01:54:41] The first component of this chain is to
[01:54:43] create nodes and I'll name it nodes. How
[01:54:46] we'll run this is we'll first start with
[01:54:49] prompt one then pass it to the model
[01:54:53] and then uh model and then run a passer
[01:54:57] on it.
[01:55:00] In the second chain
[01:55:02] we'll name it quiz. I will pass
[01:55:07] prompt
[01:55:08] prompt to
[01:55:11] prompt
[01:55:13] two
[01:55:15] then model and then a passer
[01:55:22] passer. Okay.
[01:55:26] Now
[01:55:28] we'll call our final chain which will be
[01:55:31] prompt
[01:55:35] prompt three and then
[01:55:38] model and then passer.
[01:55:42] Now we'll combine the sequential chain
[01:55:44] here final chain and then the parallel
[01:55:46] chain runnable chain. Here we'll call it
[01:55:48] chains equals to first of all we'll
[01:55:51] execute our runnable chain and then
[01:55:52] we'll execute our final chain.
[01:55:57] We'll invoke this chain
[01:56:01] chain dot invoke
[01:56:04] and then we'll uh provide an entry point
[01:56:06] for this one. So the entry point to this
[01:56:09] chain has to be a text
[01:56:14] right. So a topic or a text here. Okay,
[01:56:17] I'll just try to make it uniform. But
[01:56:19] it's okay even if we don't make it
[01:56:21] uniform. Uh because one is going to go
[01:56:25] in topic and then the other is going to
[01:56:27] go to text. I think uh I don't need to
[01:56:30] make it uniform I guess. So let's
[01:56:33] write a text here. I'm going to copy
[01:56:35] this text from some someplace else. But
[01:56:38] I'm going to I will be using a word wrap
[01:56:41] so that you can copy uh copy this or
[01:56:44] like use any text that you want from
[01:56:46] anywhere.
[01:56:48] So this text is a support vector
[01:56:50] machines
[01:56:52] uh view word wrap. Okay, everything is
[01:56:55] wrapped inside this view. Now what I'm
[01:56:57] going to do is I'm going to invoke this
[01:57:01] simply invoke this text. The result is
[01:57:03] going to be stored here. Result equals
[01:57:06] to change.invoke invoke and then finally
[01:57:09] I'm going to print my result. So this is
[01:57:12] my parallel chain implementation here.
[01:57:15] Let me run this code and then I'll
[01:57:16] explain what is happening
[01:57:19] here. Okay, while the code is running,
[01:57:22] let's go up. We have prompt one uh which
[01:57:25] generates a short and simple note about
[01:57:28] a following topic. Prompt two is like uh
[01:57:31] generating short answer question from
[01:57:34] the following topic. And then prompt
[01:57:36] three is about merging the output from
[01:57:39] prompt one and prompt two. We have a
[01:57:42] parser and then I I have initialized a
[01:57:45] runnable chain where we uh run these two
[01:57:48] chains in parallel at first. Then the
[01:57:50] output of these two chains are are then
[01:57:52] merged with the final chain and then uh
[01:57:56] a response is created. So if we see here
[01:57:59] so basically a complete node is created
[01:58:02] where we have support vector machine
[01:58:03] nodes. uh the note is created
[01:58:07] here on top and then the quiz is created
[01:58:09] here on the second and then both of
[01:58:12] these are combined into one
[01:58:13] comprehensible documents. So this is how
[01:58:16] we uh implement parallel chain in
[01:58:21] line chain. So I hope this runs on your
[01:58:23] end too. If you have any questions or
[01:58:25] have any or if you have any queries feel
[01:58:27] free to comment down below and I'll try
[01:58:29] to help you out. I will see you in the
[01:58:32] next video again.
[02:00:17] So now we see that we get a positive
[02:00:20] response and then uh there are uh
[02:00:25] the the model classifies this feedback
[02:00:28] as positive and then based on it it
[02:00:31] generates a response. Now I'm going to
[02:00:34] change this. Okay, the phone is actually
[02:00:36] horrible.
[02:00:38] The UI is stuck and then things like
[02:00:40] that.
[02:00:42] The UI is stuck.
[02:00:46] And then if I run this,
[02:00:54] so the model is in fact giving out a lot
[02:00:56] of things. But you know that we can
[02:00:58] structure the output uh using the pyic
[02:01:01] output parser or this uh or or like we
[02:01:04] can base it on some some form of schema
[02:01:07] as we've already done earlier. So you
[02:01:09] can uh actually uh implement it
[02:01:13] yourself. So
[02:01:15] here we get that the response.
[02:01:20] Okay. So it says that when responding to
[02:01:23] negative feedback, so it classifies the
[02:01:26] feedback as negative here for this
[02:01:29] thing. So in this video we saw how we
[02:01:33] could implement conditional chains using
[02:01:35] runnable branch, runnable lambda as well
[02:01:38] as how we could combine a sequential
[02:01:39] chain and and a conditional chain into
[02:01:42] one and then make our uh workflow
[02:01:47] automated. Here we've explored different
[02:01:50] type of chain, sequential chain,
[02:01:52] conditional chains, and even parallel
[02:01:53] chains. Each of these help us design
[02:01:55] multi-step workflows and process
[02:01:57] information in a structured way. Now,
[02:01:59] let's focus on something simpler, the
[02:02:01] LLM chain. So, what exactly is an LLM
[02:02:05] chain? At its core, an LLM chain is just
[02:02:08] a singlestep chain. It connects a
[02:02:10] language model to a prompt template,
[02:02:12] letting us easily generate outputs from
[02:02:14] our LLM in a structured and reusable
[02:02:17] way. Think of it as a building block, a
[02:02:19] straightforward chain where we give a
[02:02:21] prompt, the model processes it and then
[02:02:23] gives an output. There's no branching,
[02:02:27] no parallel processing. It is just a
[02:02:28] simple clean uh workflow for a single
[02:02:32] task. The beauty of LM chain is in fact
[02:02:36] in simplicity and reusability. So for
[02:02:38] example, you might want the model to
[02:02:40] suggest a catchy blog title, summarize
[02:02:43] an article and generate ideas for social
[02:02:46] media task. So you create a prompt
[02:02:48] template for the task connect it to the
[02:02:51] model via the LLM chain and then you can
[02:02:53] get or you can reuse that chain for any
[02:02:56] input without rewriting your logic.
[02:02:59] So in this video here's what we'll do.
[02:03:02] We'll define a prompt template asking
[02:03:03] the model to suggest a catchy block
[02:03:05] title for a given topic. We'll connect
[02:03:07] it to a language model using LLM chain.
[02:03:10] Then we'll run the chain with a specific
[02:03:12] topic.
[02:03:14] And finally, we'll see how the chain
[02:03:16] returns a creative usable block title.
[02:03:19] So the following implementation is going
[02:03:21] to demonstrate how LLM chain provides a
[02:03:23] structured, repeatable, and simple
[02:03:25] workflow for generating AI outputs. So
[02:03:29] without any delay, let's go into the
[02:03:31] code.
[02:03:34] So I'm going to create a new file here.
[02:03:38] I'm going to name it LLM chains.py.
[02:03:42] As always, we'll first use our model.
[02:03:47] import
[02:03:49] chat Google generative AI
[02:03:52] from env import
[02:03:56] load.env
[02:03:59] from
[02:04:00] langchen_core.prompts.
[02:04:04] I'm going to import a prompt template
[02:04:09] and and the new concept today is from
[02:04:12] lang chain dot change import lm chain.
[02:04:28] Okay. So first of all load the
[02:04:30] credentials.
[02:04:32] Uh
[02:04:36] we'll load a model
[02:04:39] Gemini 2.5
[02:04:44] flash.
[02:04:46] Then we'll create a prompt
[02:04:48] which will be used using prompt
[02:04:50] template. I'm going to write a template
[02:04:53] for this one. So suggest a catchy
[02:04:58] blog title about a topic
[02:05:02] and my input variable is going to be
[02:05:07] a topic.
[02:05:12] Okay.
[02:05:14] Now I'll I will define a chain
[02:05:18] which is going to be an LLM chain and
[02:05:21] I'm going to pass a model to this and
[02:05:24] then a prompt
[02:05:27] to this.
[02:05:29] Okay. and [snorts]
[02:05:33] and then based on this let me write a
[02:05:36] topic name let's say 3 I atlas
[02:05:40] interstellar object
[02:05:46] I'm going to invoke this chain so
[02:05:49] response equals to chain do invoke I
[02:05:53] need to provide a topic here
[02:05:56] so topic is going to be my topic
[02:05:58] variable
[02:05:59] And then basically I'm going to print
[02:06:01] the response to this. So everything is
[02:06:06] done. Let me clear this. I'm not sure
[02:06:08] about this LLM chain. Uh it might be
[02:06:11] deprecated or something. Let's see.
[02:06:17] Okay. So this is deprecated
[02:06:21] uh with the method. Okay. Runnable
[02:06:23] sequence. So we've already done runnable
[02:06:25] sequence earlier, but it's okay. We're
[02:06:27] doing something that has already been
[02:06:28] deprecated. But still we get our answer
[02:06:31] here. Uh the topic is threei atlas
[02:06:34] interstellar object. Here are some
[02:06:36] catchy blog titles. Since we have not
[02:06:39] structured or directed our uh response
[02:06:42] to be something specific that's why the
[02:06:44] model is generating this long text here
[02:06:48] uh as a catchy block title which we
[02:06:50] don't don't in fact want but like uh it
[02:06:54] is what the model is uh providing me. So
[02:06:57] here's what you can do. You can uh use
[02:07:01] some form of response schema or maybe a
[02:07:04] parentic class uh to direct
[02:07:06] [clears throat] the model to provide
[02:07:08] just a catchy block title just a a
[02:07:12] combination of three to four words
[02:07:15] uh
[02:07:17] block title for this particular topic.
[02:07:19] So I'm going to end this video for now.
[02:07:21] Uh if you have any problem or any page
[02:07:24] do comment down below and I'll try to
[02:07:25] help you out and I'll see you in the
[02:07:27] next video. In our previous videos we've
[02:07:30] worked with LMS and change giving
[02:07:32] prompts and generating responses and
[02:07:34] even combining multiple models to create
[02:07:36] structured workflows. Now we're moving
[02:07:38] into another fundamental concept that
[02:07:40] powers intelligent retrieval search and
[02:07:42] reasoning in modern AI agents.
[02:07:44] Embeddings. So what exactly are
[02:07:47] embeddings? Think of embedding as the
[02:07:49] numerical fingerprints of text. So when
[02:07:52] we feed a sentence like Delhi is the
[02:07:54] capital of India into an embedding
[02:07:56] model, it doesn't just read it as words.
[02:07:59] It converts that text into a vector
[02:08:01] which is a list of numbers.
[02:08:04] Each number in this vector represents a
[02:08:06] small piece of meaning from the original
[02:08:08] text. Together they form a semantic
[02:08:10] representation. meaning that two text
[02:08:12] with similar meaning will have vectors
[02:08:14] that are close to each other in this
[02:08:17] higher dimensional space.
[02:08:19] So we'll make this intuitive. Suppose if
[02:08:22] you take two sentences like Paris is the
[02:08:24] capital of France and Delhi is the
[02:08:26] capital of India. The embeddings will be
[02:08:29] very close because both talk about
[02:08:31] capital cities. But a sentence like I
[02:08:34] love pizza will have a completely
[02:08:35] different embedding far away in vector
[02:08:37] space. Now why do we need embeddings?
[02:08:41] Embeddings are basically essential
[02:08:43] whenever we want our AI to understand
[02:08:45] the context or meaning rather than just
[02:08:47] a plain text. They help us with semantic
[02:08:50] search meaning finding documents similar
[02:08:53] in meaning not just by matching
[02:08:55] keywords.
[02:08:56] It also helps in context retrieval
[02:09:00] that means fetching relevant chunk of
[02:09:03] information to feed on into an LLM. They
[02:09:06] help us with clustering and
[02:09:07] classification which means grouping
[02:09:09] related ideas together and they help us
[02:09:10] with recommendation system meaning
[02:09:12] suggesting similar product or content
[02:09:14] based on its meaning.
[02:09:18] So in this video we'll use hugging face
[02:09:20] embeddings specifically all the
[02:09:24] specifically the model
[02:09:27] in this video we'll use hugging face
[02:09:29] embeddings which is a lightweight and
[02:09:31] efficient
[02:09:34] in this video we'll use hugging face
[02:09:35] embeddings and a lightweight model from
[02:09:39] the hogging face embeddings so we'll
[02:09:42] generate embeddings for a single query
[02:09:44] that is the Delhi is the capital of
[02:09:45] India and then a list of related
[02:09:47] documents. Then when we print them,
[02:09:50] we'll see a long list of numbers and
[02:09:52] those numbers will be the numerical
[02:09:54] representation of our text. But what's
[02:09:56] more important is that we will use those
[02:09:59] emittings to compare similarities, store
[02:10:02] them in a vector database or build
[02:10:04] context aware AI agents that retrieve
[02:10:06] information intelligently. So main
[02:10:09] advantages of these embeddings are huge.
[02:10:11] First of all, they allow semantic
[02:10:13] understanding, meaning the model can
[02:10:15] reason about meaning rather than exact
[02:10:18] wording. Second, they make retrieval
[02:10:20] augmented generation possible or rag
[02:10:23] possible where an AI can look up context
[02:10:27] before answering. And the third, they
[02:10:29] significantly improve accuracy in search
[02:10:32] question answering and knowledge based
[02:10:34] systems. So embedding acts as a bridge
[02:10:36] between the language and numbers
[02:10:38] allowing machines to understand and
[02:10:40] compare the meaning of
[02:10:43] provided text or document. And as we go
[02:10:46] further in this series, we'll see how
[02:10:48] embedding power intelligent agents
[02:10:50] enabling them to remember, reason, and
[02:10:53] respond more accurately. But for now,
[02:10:56] we'll see the very basic implementation
[02:10:58] of these embeddings. So let's go into
[02:11:01] the code.
[02:11:07] Okay, I'm going to create a new folder
[02:11:09] here
[02:11:10] and then call it embeddings.
[02:11:18] Uh
[02:11:20] after that I'm going to create a new
[02:11:21] file. Let's call it hugging face
[02:11:23] embeddings.
[02:11:32] uh hing face embeddings
[02:11:35] do pry. Okay. Now the import is going to
[02:11:38] be quite different here. So first of all
[02:11:41] I think I'll need to install something.
[02:11:43] Let's go to requirements
[02:11:45] here. I'll need to install lang chain
[02:11:50] auging fishing
[02:11:52] face. Okay. I'm going to install this
[02:11:55] these requirements as as everything else
[02:11:58] is installed. The new library will also
[02:12:01] be installed in addition to the other
[02:12:04] libraries that we already have.
[02:12:09] Okay, this is installed. Let's go back
[02:12:10] to our code and then from here we'll
[02:12:13] import from
[02:12:16] langchain_hugging
[02:12:19] face import
[02:12:21] hugging face embeddings.
[02:12:23] Then we'll re uh input env
[02:12:29] uh load env.
[02:12:32] And then we'll also import OS. I'm not
[02:12:34] sure if this is going to be used or not,
[02:12:35] but anyway, let's import it and I'll
[02:12:38] load my credential. Okay. So, what kind
[02:12:40] of credential am I loading here? So, to
[02:12:42] use hugging face embeddings, you need to
[02:12:45] visit the hugging face website and
[02:12:48] create your API key and then save it in
[02:12:50] the environment file here. So you can do
[02:12:53] that yourself or take the reference from
[02:12:56] the hoggingface documentation too or the
[02:12:58] lenins documentation and then uh you can
[02:13:02] create that create that hogging API key
[02:13:05] and then paste it in your env and and
[02:13:07] then that will be loaded here using this
[02:13:10] load env function. Anyway I'm not going
[02:13:12] to go to that. I've already placed my
[02:13:14] hogging face embedding key here. So I'm
[02:13:16] directly going to run this. So
[02:13:18] embeddings equals to hogging face
[02:13:20] embeddings. And then I'm going to use a
[02:13:22] model here that I found out in the
[02:13:25] hogging face model section. So this
[02:13:28] model is sentence
[02:13:30] transformers
[02:13:32] all
[02:13:34] mini LM
[02:13:36] L62.
[02:13:40] Uh I I might also need to import
[02:13:44] sentence transformers here.
[02:13:47] So let me write that down. And then
[02:13:51] uh
[02:13:52] install the requirements install minus r
[02:13:55] requirements. txt.
[02:14:03] So while that is being installed, let's
[02:14:05] continue with our code. As I said, I'll
[02:14:07] have a text,
[02:14:09] simple text. Delhi is the capital of
[02:14:12] India.
[02:14:14] Uh,
[02:14:16] and along with this, I'll have some
[02:14:18] documents
[02:14:21] where I'll say Delhi is the capital of
[02:14:25] India.
[02:14:26] Uh,
[02:14:28] Kolkata is the capital of West Bengal.
[02:14:36] and
[02:14:38] then Paris is the capital of France.
[02:14:45] So what we can do here is like I said we
[02:14:48] can convert this textual data into
[02:14:50] numerical figures. So to do that I'm
[02:14:53] going to use embedding model dot embed
[02:14:56] query
[02:14:59] embed query and then inside this I'm
[02:15:01] going to pass this text here. So if you
[02:15:04] print this out st result if you print
[02:15:08] this out then you'll see that this
[02:15:11] particular text will be converted to
[02:15:14] numbers okay so let me run this now the
[02:15:17] library is now installed I can run this
[02:15:19] code now
[02:15:22] it will take some time to run because
[02:15:23] the model might not be downloaded so it
[02:15:25] will download the model first and then
[02:15:28] uh run our program here okay so once I
[02:15:32] printed did this and the code has run.
[02:15:36] We can see that this particular text is
[02:15:38] now converted into into this combination
[02:15:41] of numbers here. Now this is called
[02:15:44] embeddings.
[02:15:47] Not only this, we can also embed our
[02:15:49] documents here. So if I just type
[02:15:56] So if I just type result doc equals to
[02:16:00] embedding dot since we embedding
[02:16:04] documents so we need to pass in embed
[02:16:07] documents and then pass in the documents
[02:16:09] in this list. Now if we print this uh
[02:16:13] we'll see that we have uh embeddings for
[02:16:17] each of these text in a document. So we
[02:16:20] basically get a list of embeddings and
[02:16:23] then each embedding will
[02:16:26] resemble each sentence that we see here.
[02:16:28] So I think you can run this program on
[02:16:31] your end and then see the result of your
[02:16:33] embedding here. uh what we what we'll
[02:16:37] also do is we'll also try to compare the
[02:16:40] similarity of this particular text with
[02:16:43] these documents here. So let's see what
[02:16:45] happens. Uh what we'll do is we'll do
[02:16:49] result here and then result do here.
[02:16:54] Now we'll compare the similarity score
[02:16:58] and
[02:17:00] and then for the similarity score we'll
[02:17:02] use cosine similarity. For that we'll
[02:17:04] need to uh import something here or
[02:17:06] basically need to install a library
[02:17:08] install pip install scikitlearn
[02:17:14] and then based on that particular
[02:17:18] uh scikitlearn library
[02:17:24] we'll import from
[02:17:27] skarn.mmetrix
[02:17:29] dot dotpise
[02:17:31] we'll import cosine simarity
[02:17:34] And now to compare our uh
[02:17:38] similarity embeddings between our text
[02:17:41] and our document, we'll use cos and
[02:17:44] similarity. And we'll pass uh
[02:17:49] our result here.
[02:17:52] The result which is the embedding of our
[02:17:55] text and then we'll pass our document
[02:17:58] embeddings which is result_doc.
[02:18:02] So let me print out the similarity
[02:18:05] scores here. So
[02:18:07] let me simply print out similarity
[02:18:09] scores whatever we get here
[02:18:14] and then run this program again. So as
[02:18:18] you can see uh the text
[02:18:22] is uh the similarity between the text
[02:18:26] and then and then the first document is
[02:18:29] almost 98%. Similarity between the text
[02:18:32] and the second document is almost 47%
[02:18:35] and the third and the third document is
[02:18:37] all is 27%. Now if I add a a new
[02:18:42] sentence like uh I love pizza here we'll
[02:18:46] see that this similarity score is quite
[02:18:49] low in comparison to the above three
[02:18:52] sentences. Let's print it out. Let's
[02:18:54] clear this and then run this model
[02:18:56] again.
[02:18:58] So we can see that
[02:19:01] the text Delhi is capital of India is
[02:19:05] very much lower similar to I love pizza
[02:19:08] which almost 9% similar to pizza. So the
[02:19:11] highest highest similarity is these two
[02:19:14] sentences. You might get why did not why
[02:19:16] we did not get 100% similarity because
[02:19:19] here uh there is a slight mistake while
[02:19:23] I've typed this word. So if I type Delhi
[02:19:25] is the capital of India and then we get
[02:19:28] the same sentence here it would
[02:19:30] basically be 100%. Let's see if if we
[02:19:32] get a 100% similarity between them or
[02:19:35] not. So yeah we get a 100% similarity
[02:19:38] code between these two sentences. So
[02:19:40] this is the importance of uh embeddings
[02:19:44] basically converting the text into
[02:19:46] numbers represent the semantic meaning
[02:19:48] of that particular text uh which is
[02:19:51] easier for computer to understand and
[02:19:53] everything from now on that we'll do
[02:19:56] will be based on these embeddings.
[02:19:58] Basically if embeddings were not
[02:19:59] possible uh retrieval augmented
[02:20:03] generation would not have been uh
[02:20:06] possible. In the last video, we explored
[02:20:09] the concept of embeddings. How they
[02:20:11] transform text into numerical
[02:20:12] representation that capture meaning.
[02:20:14] Now, we're taking
[02:20:17] one step further and actually use those
[02:20:19] embeddings to make our model retrieve
[02:20:21] and reason over real data. So, in this
[02:20:24] video, we'll build a simple retrieval
[02:20:26] augmented generation or a rack pipeline.
[02:20:29] a system where the model doesn't just
[02:20:31] rely on its internal memory but instead
[02:20:33] looks up relevant information from
[02:20:36] external sources before giving an
[02:20:38] answer. So we'll break down step by
[02:20:42] step. The [snorts] first thing we do
[02:20:43] here is load a document using a text
[02:20:46] loader class. So it's a straightforward
[02:20:48] way to bring in external data. Uh for
[02:20:51] example, a text file, a web page, or
[02:20:53] even a PDF. Here uh we're going to use a
[02:20:57] txt file. uh which might contains note
[02:21:00] research summaries or articles. Next, we
[02:21:04] use the recursive character text
[02:21:06] splitter. Now, this is a very clever
[02:21:08] tool. Uh what it does is it breaks large
[02:21:11] text into smaller manageable chunks,
[02:21:14] usually around 500 characters each in
[02:21:16] our case.
[02:21:18] But why do we do that? Uh we do that
[02:21:20] because language models and embeddings
[02:21:24] work much better when the text is short
[02:21:27] and focused.
[02:21:28] So by so by uh giving them the byite
[02:21:33] side chunk with side overlap we have the
[02:21:36] model preserve the context while
[02:21:39] avoiding cut off issues especially
[02:21:41] useful when dealing with large
[02:21:43] documental books. Now once the text is
[02:21:45] split we move to the embedding step. So
[02:21:49] here we're going to use uh Google's
[02:21:51] Gemini emitting model. Each of these
[02:21:54] chunks will be now converted into a
[02:21:57] vector or embedding just like we saw saw
[02:21:59] in our last video. [snorts]
[02:22:01] Now these embeddings need to be stored
[02:22:03] somewhere efficiently and that's where f
[02:22:05] comes in. So f uh stands for Facebook
[02:22:08] aim Facebook a similarity search uh and
[02:22:11] it is a powerful open source vector
[02:22:13] database that allows us to store and
[02:22:15] search documents very quickly.
[02:22:19] Uh so using F what we do is uh each
[02:22:25] chunk of our content is embedded into a
[02:22:27] vector and then those vectors are stored
[02:22:29] in a f index and f prepares itself to
[02:22:34] find the most similar vectors whenever
[02:22:35] we search. Then uh we'll go for
[02:22:39] something called a retriever. So what
[02:22:41] happens in a retriever is it is like a
[02:22:44] search engine for our AI agent. So when
[02:22:46] we provide a query for example like what
[02:22:48] are the key takeaways for our documents
[02:22:50] the retriever searches through all those
[02:22:53] embeddings inside files and then returns
[02:22:55] the most semantically similar search. So
[02:22:58] this step ensures that our model doesn't
[02:23:00] try to remember everything. Instead what
[02:23:02] it does is it retrieves the right
[02:23:04] information on demand. Uh so after that
[02:23:08] [snorts] we combine all of those
[02:23:10] retrieve text chunks into a single
[02:23:12] string of context. This context acts
[02:23:14] like the background material or nodes
[02:23:16] that we pass to our language model.
[02:23:18] [snorts] Then finally, we initialize our
[02:23:20] Gemini chart model and manually
[02:23:22] construct a prompt that combines both
[02:23:24] the context and the question. So when we
[02:23:27] pass this prompt to the LM, uh it uses
[02:23:29] the provided context to generate a
[02:23:31] factual context of their answer and then
[02:23:33] not something made up from its internal
[02:23:35] knowledge. So this workflow is is the
[02:23:38] backbone of what's known as retrieval of
[02:23:40] media generation or rack.
[02:23:42] >> [snorts]
[02:23:42] >> Instead of letting the model guess or
[02:23:45] holen it uh we ground it with real data
[02:23:48] here so the benefits are uh huge the
[02:23:53] model
[02:23:54] gets more accurate and reliable. Uh it
[02:23:57] can also handle custom data sources and
[02:23:59] it's far more scalable since we can swap
[02:24:02] documents add new data and then do
[02:24:03] something like so in this video we've
[02:24:06] taken [snorts]
[02:24:07] we will take a big step from embeddings
[02:24:09] to retrieval. Now uh let's go to the
[02:24:12] code.
[02:24:16] So I'm going to create a new folder here
[02:24:23] and call it rag or basic rag for now.
[02:24:29] Let a new file
[02:24:32] basic rag.py
[02:24:35] what I'm going to do is I'm going to
[02:24:36] create a docs.txt txt file
[02:24:41] and then uh bring uh bring some
[02:24:45] paragraphs of content. Uh here I already
[02:24:47] have it. So [snorts] I'll have this
[02:24:50] content about AI. I'm going to do word.
[02:24:52] You can bring anything else that you
[02:24:54] want here. It's fine.
[02:24:57] So yeah, this is my uh document for now.
[02:25:03] Okay, we'll go back to our basic ad
[02:25:05] model. So I'm going to generate my model
[02:25:09] first
[02:25:14] and then
[02:25:16] env
[02:25:20] uh I'm also going to load a text loader
[02:25:24] from Langen community.
[02:25:33] Then I'll have a texter
[02:25:36] from Langen.
[02:25:46] Then uh let's also import our embeddings
[02:25:51] from
[02:25:53] Google geni.
[02:25:58] Then we'll use vector stores
[02:26:07] to store our embeddings here and then
[02:26:11] we'll use a retrieval QA. So from lang
[02:26:14] chain
[02:26:17] of chains
[02:26:20] put retrieval not this one
[02:26:28] retrieval QA okay
[02:26:31] now based on this first first let me
[02:26:34] load the credentials load the
[02:26:37] credentials
[02:26:39] okay I'm providing [snorts]
[02:26:40] stepwise
[02:26:43] uh information here. So step one, I'm
[02:26:44] going to load my credentials. In step
[02:26:47] two, I'm going to load the document that
[02:26:52] I have. So I'll be
[02:26:55] defining a loader and then using this
[02:26:58] class here called text loader. My file
[02:27:02] name is docs.txt
[02:27:04] and then I'm going to load this. So
[02:27:06] documents equals to loader.load.
[02:27:10] In step three, I'm going to split the
[02:27:14] text into smaller chunks.
[02:27:17] Smaller chunks.
[02:27:19] So for this, I'm going to use a text
[02:27:21] splitter.
[02:27:23] Recursive text. Sorry, recursive
[02:27:26] character text splitter. Uh I'm going to
[02:27:28] define the chunk size of each
[02:27:31] uh splitted text. Let me give 500. and
[02:27:36] then also chunk overlap because uh
[02:27:42] we might carry some contextual
[02:27:44] information in while breaking those
[02:27:46] chunks. So we want some overlap so that
[02:27:50] uh two different chunks can have
[02:27:52] something common something in common
[02:27:54] between them. So I'm going to split my
[02:27:57] document using the splitter. So text
[02:27:59] splitter dotsplit documents
[02:28:03] documents
[02:28:09] Okay, now I'm now I'm going to
[02:28:15] Okay, this is step three.
[02:28:18] I'm going to step four where I'm going
[02:28:20] to convert
[02:28:22] text embeddings and store in.
[02:28:29] So here what I'm going to do is I'm
[02:28:31] going to define embeddings equals to
[02:28:36] Google gen Google generative embeddings
[02:28:40] where the model is model/
[02:28:43] Gemini embedding
[02:28:47] uh 001. I found this in the langen
[02:28:50] documentation itself.
[02:28:52] And then I'm going to define a vector
[02:28:54] store using phase dot from documents
[02:29:01] docs sorry
[02:29:05] from documents docs comma
[02:29:10] then in step five I'm going to create
[02:29:16] create a retriever
[02:29:19] which fetches
[02:29:22] relevant and documents.
[02:29:30] Okay,
[02:29:32] retriever equals to vector store dot as
[02:29:36] retriever.
[02:29:39] And then I'm going to initialize a
[02:29:41] model.
[02:29:46] Sub model equal to chat Google
[02:29:49] generative AI model equals to Gemini 2.5
[02:29:59] you can even use hoging face models here
[02:30:02] step seven
[02:30:05] I'm going to create a
[02:30:09] retrieval QA chain
[02:30:12] so chain equals to retrieval QA dot
[02:30:17] from_chain
[02:30:19] type where llm equals to llm and
[02:30:24] the retriever equals to retriever
[02:30:30] or model here
[02:30:34] then uh
[02:30:37] I'm going to manually query
[02:30:42] manually query
[02:30:46] uh
[02:30:49] model and retrieve and relevant
[02:30:54] documents.
[02:30:55] So query is going to be like okay what
[02:30:58] is the document about? Let's see.
[02:31:01] So it is about AI. So my query will be
[02:31:04] very simple. So what are the key
[02:31:08] takeaways
[02:31:11] from the document
[02:31:15] and then based on this query
[02:31:18] I can invoke my chain here. So chain dot
[02:31:21] invoke query and then finally I'm going
[02:31:25] to print my answer.
[02:31:34] So print
[02:31:35] response. Okay, the code is done. I have
[02:31:39] tried to provide you stepwise
[02:31:41] implementation of what we talked about
[02:31:43] in the rack pipeline. So let me run
[02:31:46] this. Let me also save this document and
[02:31:49] then run this here.
[02:31:57] So the model will provide answer based
[02:32:00] on okay I need to something I need to
[02:32:02] install something here. So 5G CPU needs
[02:32:04] to be installed. Let's write it down in
[02:32:07] requirements.txt2
[02:32:16] GPU
[02:32:18] install this with install minus rates.
[02:32:23] txt.
[02:32:29] Okay, we can install the CPU version
[02:32:31] because my laptop not be equipped with
[02:32:36] GPU here.
[02:32:43] Okay, so let me run this once again.
[02:32:59] And
[02:33:01] while this is being run uh the answer
[02:33:04] from the LLM is based on the documents
[02:33:07] that are provided and not on its
[02:33:09] internal knowledge base. So the key so
[02:33:12] the key takeaways are uh
[02:33:15] are like actually provided here. uh if
[02:33:17] we need to ask spec something something
[02:33:19] specific from this document like uh what
[02:33:22] is this so
[02:33:25] doing such tasks such as learning reason
[02:33:27] AI comprise okay what kind of technology
[02:33:30] that AI comprise let's ask that
[02:33:39] so what kind of technology
[02:33:43] technologies
[02:33:45] does I
[02:33:48] comprise of. So if you ask this question
[02:33:51] then
[02:33:54] the model is going to provide the answer
[02:33:57] based on the document and not its
[02:34:00] internal knowledge.
[02:34:04] So it says uh AI comprise a variety of
[02:34:06] technology. It's copied just from this
[02:34:09] particular context here. So this is how
[02:34:11] we build a basic direct pipeline. I hope
[02:34:14] you understood the concept. We've been
[02:34:15] exploring how different types of chains
[02:34:17] help us connect multiple components
[02:34:19] together from simple prompt to model
[02:34:22] pipelines to more advanced parallel and
[02:34:24] conditional chains. But now we're going
[02:34:27] one step further and introducing a
[02:34:29] concept that gives us even more control
[02:34:31] and flexibility in how our data flows
[02:34:34] through a chain. Runnable sequence. So
[02:34:37] what exactly is a runnable sequence? So
[02:34:40] think of it like a conveyor built for
[02:34:42] data. Each step in the sequence takes
[02:34:44] the output from the previous step,
[02:34:46] processes it and passes it along to the
[02:34:49] next one. It's part of the new runnable
[02:34:52] interface in lang chain which unifies
[02:34:55] how different components like prompts,
[02:34:57] models and parsers communicate with each
[02:34:59] other. Earlier when we worked with LLM
[02:35:02] chain, the structure was was quite
[02:35:04] fixed. One prompt, one model, one
[02:35:06] output. It worked great for single
[02:35:10] single or simple workflows. But when we
[02:35:12] wanted to do something more dynamic like
[02:35:15] taking a model's output, processing it
[02:35:18] through another template, and then
[02:35:19] feeding it back to another model, things
[02:35:22] start to get messy. That's where a
[02:35:24] runnable sequence shines. It lets us
[02:35:27] build multi-step pipelines where each
[02:35:30] element can be a model, a parser, or
[02:35:32] even another chain all connected in a
[02:35:35] single streamlined sequence. You can
[02:35:37] think of it as a customizable chain
[02:35:40] where you fix exactly how data flows
[02:35:43] from one step to another. Now, in this
[02:35:45] video, we'll be doing something fun to
[02:35:47] demonstrate it. We'll start with a
[02:35:49] prompt that asks the model to write a
[02:35:51] joke about a given topic. Then, we'll
[02:35:53] take that generated joke and then feed
[02:35:55] it to a second prompt, one that asks the
[02:35:58] model to explain the joke. And then
[02:35:59] finally, we'll use an output parcel to
[02:36:02] cleanly process and present our final
[02:36:04] response. So by the end of this video
[02:36:07] you'll understand how runnable sequence
[02:36:09] works, how it is different from earlier
[02:36:14] chain structures we've seen and how you
[02:36:16] can use it to build smooth multi-step
[02:36:18] reasoning pipelines where the model's
[02:36:20] output becomes the input for the next
[02:36:22] stage.
[02:36:24] All right, so let's dive into the code.
[02:36:36] So I'm going to create a folder here
[02:36:41] called Runnables
[02:36:48] and then uh file called runnable
[02:36:53] sequence.py.
[02:36:56] Okay. So first of all import lang Google
[02:37:00] genai
[02:37:03] then I need av
[02:37:09] after that I'm going to import prompt
[02:37:11] template which will come from langen
[02:37:14] core.
[02:37:22] Then I will import an STR output parser
[02:37:25] that is also going to come from lang
[02:37:27] core
[02:37:40] from lang
[02:37:43] from line 4 dot output passers import
[02:37:50] str output passer And after that I'll
[02:37:54] need a runnable sequence which will come
[02:37:56] from langen dots schema dot runnables
[02:38:01] import
[02:38:02] runnable sequence.
[02:38:07] Okay. So first of all load the
[02:38:08] credentials.
[02:38:10] I'll define my first prompt where
[02:38:14] using my prompt template and then the
[02:38:17] template is going to be about write a
[02:38:19] joke about
[02:38:24] about a topic and inside this my input
[02:38:29] variables is going to be
[02:38:33] topic.
[02:38:35] Similarly write second prompt
[02:38:39] again using a prompt template where my
[02:38:41] template
[02:38:42] will be explain the following
[02:38:47] joke
[02:38:49] and then I'll type in joke here my input
[02:38:54] variables is going to be
[02:39:00] joke.
[02:39:04] Okay. So my model will be from chat
[02:39:08] Google AI.
[02:39:12] The model will be Gemini
[02:39:16] 2.5
[02:39:18] flash.
[02:39:21] I'll also define my output parser using
[02:39:24] str output parser
[02:39:27] and then based on that I'm going to
[02:39:29] define a chain or a runnable sequence.
[02:39:32] So first of all I'm going to go to
[02:39:35] prompt and I'll go to model then parser
[02:39:39] then prompt two
[02:39:41] then model
[02:39:44] and then passer again
[02:39:47] uh and then result I'll just invoke this
[02:39:50] runnable sequence
[02:39:53] book.
[02:39:55] So the topic
[02:39:57] is going to be a monkey like and then
[02:40:02] and then finally print a result here. So
[02:40:05] this is how you implement runnable
[02:40:07] sequence. You might see that this is
[02:40:09] similar to the concept of chains that we
[02:40:12] used. We if we had used chains we would
[02:40:15] do it in this way. So change [snorts] it
[02:40:18] would be prompt
[02:40:20] model
[02:40:22] uh cursor
[02:40:24] then prompt two
[02:40:26] and model
[02:40:30] and then parser again. So this is how we
[02:40:32] would implement chain but here we're
[02:40:34] doing it with runnable sequence. Let me
[02:40:36] run this code.
[02:40:54] It will take some time because we have
[02:40:56] multiple model calls here.
[02:40:59] One one model call is this part and then
[02:41:00] the other model call is this part and
[02:41:02] then without the completion of the first
[02:41:04] model call uh we cannot go to the second
[02:41:08] model here. Okay. So couldn't feel the
[02:41:11] love anymore. So the humor breaks in.
[02:41:14] Okay, it's only printing me out the
[02:41:15] explanation about the joke. But uh but
[02:41:20] it's okay. Uh uh it's okay because uh
[02:41:24] I've got what I wanted at the end of
[02:41:26] this runnable sequence. In the last
[02:41:28] video, we explored runnable sequence
[02:41:30] where each step in the chain passed its
[02:41:33] output to the next creating a smooth
[02:41:35] step-by-step flow of data. But now we're
[02:41:37] flipping that idea around and diving
[02:41:39] into something that works side by side
[02:41:41] instead of one after another, which is
[02:41:44] runnable parallel. Simply put, runnable
[02:41:46] parallel allows us to run multiple
[02:41:48] sequences or tasks at the same time in
[02:41:51] parallel. While runnable sequence is all
[02:41:54] about order and dependency where where
[02:41:56] step two awaits for step one, runnable
[02:41:59] parallel is about independence and
[02:42:01] speed. Each branch runs simultaneously
[02:42:03] on the same input producing multiple
[02:42:06] outputs at once. So imagine you're a
[02:42:08] content creator and you have one topic,
[02:42:10] say AI, and you want a tweet, a LinkedIn
[02:42:14] post or maybe an Instagram caption about
[02:42:16] it. So instead of generating them one by
[02:42:18] one, Runnable Parallel lets you generate
[02:42:21] all of them in a single call. So that's
[02:42:24] exactly what we'll be doing in this
[02:42:25] video. We'll create two separate
[02:42:27] prompts. one to generate a tweet and
[02:42:30] another to generate LinkedIn post about
[02:42:32] the same topic. Then we'll wrap them
[02:42:34] inside a runnable parallel. So both
[02:42:37] prompts are executed at the same time
[02:42:39] using the same model. The final output
[02:42:42] will give us both results neatly, one as
[02:42:45] a tweet and then the other as a LinkedIn
[02:42:48] post. So the real advantage here of
[02:42:50] runnable parallel is efficiency. When
[02:42:52] you're building complex AI workflows
[02:42:54] like summarizing document, generating
[02:42:57] multiple content format or running
[02:43:00] multiperspective analysis, runnable
[02:43:02] parallel helps you process everything
[02:43:04] faster and more efficiently uh without
[02:43:07] waiting for one task to finish before
[02:43:09] starting the next. So in this video
[02:43:11] we'll see runnable parallel in action,
[02:43:13] understand how it complements runnable
[02:43:15] sequence and also explore how combining
[02:43:18] both can help us build truly powerful
[02:43:22] multi-step multi-output pipelines. So
[02:43:25] let's get started and then go to the
[02:43:26] code.
[02:43:33] So I'm going to create a new file
[02:43:37] called runnable parallel
[02:43:42] py.
[02:43:44] Uh I'll be using the same import. So I'm
[02:43:46] just going to copy it from here. Okay.
[02:43:49] So these three imports are the same. Uh
[02:43:51] these four imports are the same. And
[02:43:53] then I will need to uh call up runnable
[02:43:56] parallel and runnable sequences. So
[02:43:59] langen dot schema dot runable
[02:44:03] import
[02:44:05] runnable
[02:44:07] uh sequence and then a runnable
[02:44:10] runnable parallel. Okay. So this is also
[02:44:15] same uh I'll have prompt one which tells
[02:44:19] me
[02:44:21] or which is about
[02:44:24] generating a tweet. So generate
[02:44:29] a tweet
[02:44:31] about
[02:44:32] topic
[02:44:34] and then the input variables here
[02:44:38] is a topic
[02:44:40] and another prompt is also the same. So
[02:44:42] I'm just going to copy this.
[02:44:45] So prompt two is generate a
[02:44:49] LinkedIn post about a topic.
[02:44:53] So this is going to be prompt two.
[02:44:57] I'll define my model.
[02:44:59] So model equals [snorts] to
[02:45:02] representative AI
[02:45:05] model= to Gemini
[02:45:08] 2.5
[02:45:13] have a parser.
[02:45:17] So parser equals to str output parser
[02:45:23] and after that I'm going to implement a
[02:45:25] parallel chain
[02:45:28] using uh runnable parallel. So a real
[02:45:34] parallel chain equals to runnable
[02:45:36] parallel and inside this I'll have two
[02:45:39] different runnable sequences.
[02:45:46] Okay. So the first one will be named tw
[02:45:50] and inside this I'll have a runnable
[02:45:52] sequence.
[02:45:59] uh tweet
[02:46:03] it is going to be a runnable sequence
[02:46:06] where I'm going to pass in prompt
[02:46:09] one model and then passer and similarly
[02:46:14] I'll also have second
[02:46:17] runnable sequence
[02:46:20] it will be about two model and parser
[02:46:27] now uh going to invoke this par chain
[02:46:31] par chain.invoke.
[02:46:34] Uh the topic is going to be
[02:46:38] uh
[02:46:40] we will do runnable parallel
[02:46:43] in lang
[02:46:46] and then I'm going to print the result.
[02:46:50] So this is how we implement a runnable
[02:46:52] parallel in lang. uh we'll need uh
[02:46:57] chronable sequences for individual
[02:46:59] parallel events here.
[02:47:02] So let me run this and then see the
[02:47:03] output. Again it is going to take some
[02:47:06] time to run because I have multiple
[02:47:08] runnable sequences here. So these two
[02:47:10] need to be implemented but they'll be
[02:47:12] implemented simultaneously at once and
[02:47:15] then I'll get the final output here.
[02:47:24] Uh also if we need to maybe bind our
[02:47:28] output in some for some some form of
[02:47:30] schema we know that we've already done
[02:47:32] that. Uh we can do it using py or maybe
[02:47:37] uh maybe by defining some for some form
[02:47:40] of uh schema and then we have done it in
[02:47:44] our earlier videos. If you haven't seen
[02:47:46] that uh you can go back and then check
[02:47:48] it out and try it yourself. So here we
[02:47:50] have a tweet and then down here we'll we
[02:47:53] also somewhere have a LinkedIn post uh
[02:47:56] that we need to find but at least it's
[02:47:58] there somewhere uh it is there somewhere
[02:48:01] around there and then uh in in case of
[02:48:04] LinkedIn post I think I'm getting some
[02:48:06] code to code to here like these these
[02:48:10] lines I think are the codes here so
[02:48:11] anyway we have implemented a runnable
[02:48:15] parallel uh in this particular program.
[02:48:19] Today we're diving into one of the most
[02:48:21] essential building block of any Langen
[02:48:23] project which is document loaders. So if
[02:48:26] you've ever wondered how we bring data
[02:48:28] from the real world like PDFs, text
[02:48:31] files, websites or CSVs into our AI
[02:48:34] pipeline, this is where it all begins.
[02:48:36] So document loaders actually act as a
[02:48:39] bridge between raw data and intelligence
[02:48:41] system. So what exactly are document
[02:48:44] loaders here? So think of them as a
[02:48:46] specialized tool that read and import
[02:48:48] data from different sources into langen
[02:48:51] standardized format called documents. So
[02:48:53] each document contains not just text but
[02:48:56] also
[02:48:57] metadata things like file name, source,
[02:49:00] URL or page number which later helps us
[02:49:03] organize and query data more
[02:49:06] efficiently. In simple terms, they are
[02:49:09] the data injection engines of blanken.
[02:49:12] And today we'll look at five most uh
[02:49:15] five of the most commonly used ones.
[02:49:17] Text loader, pipe PDF loader, directory
[02:49:20] loader, web based loader, and then CSV
[02:49:22] loader. So first of all, we'll start
[02:49:24] with the text loader. As the name
[02:49:26] suggests, this one deals with plain text
[02:49:28] files. So it's perfect when you have
[02:49:31] .txt documents, maybe transcript logs or
[02:49:33] notes that you want to feed into your
[02:49:35] system. where uh it it opens the file,
[02:49:40] reads the text and wraps it into a
[02:49:42] length and document object which is
[02:49:45] quite lightweight, fast and ideal for
[02:49:47] structured plain text data. The next is
[02:49:50] a PIP PDF loader. one of the most
[02:49:52] popular loaders especially in editable
[02:49:55] based AI system because PDFs are
[02:49:58] everywhere in research paper, invoices,
[02:50:01] reports, books and they often carry a
[02:50:04] lot of valuable information. So, PIP PF
[02:50:07] loader extracts the text from each page
[02:50:09] and converts them into a structured
[02:50:11] documents keeping track of the metadata
[02:50:15] like page numbers and file sources. And
[02:50:17] then it makes it incredibly useful when
[02:50:21] you need to query or summarize specific
[02:50:23] sections of a PDF rather than treating
[02:50:25] it as a single long text. Now, what if
[02:50:29] you have hundreds of files sitting
[02:50:30] inside a folder and that's where
[02:50:32] document loader comes in. instead of
[02:50:34] manually loading each file uh sorry
[02:50:38] directly loader. So directly loader
[02:50:40] scans through your folder and
[02:50:42] automatically loads every document that
[02:50:44] matches your design pattern. For
[02:50:45] example, all all txt or PDF files. It is
[02:50:49] perfect for large scale projects like
[02:50:51] when you're building a chatbot trained
[02:50:52] on a company's entire set of initial
[02:50:55] docu or internal documents. So it also
[02:50:59] saves you from a lot of manual effort
[02:51:01] and ensures consistency across all your
[02:51:03] data sources. Now uh this is where
[02:51:07] things get interesting because not all
[02:51:10] data lives on your local machine.
[02:51:11] Sometimes the information you need uh is
[02:51:14] scattered across web pages, blogs or
[02:51:17] online articles on the internet and then
[02:51:19] that's where the webbased loader comes
[02:51:21] in. uh this loader fetches the data
[02:51:23] directly from a web page URL, extracts
[02:51:25] the text content uh cleans it up and
[02:51:29] then turns it into a usable document. So
[02:51:31] it's extremely handy for web scraping or
[02:51:34] live data retrieval. For example,
[02:51:36] pulling FAQs from a website, news
[02:51:39] content from an article or product info
[02:51:42] from an online store. With web based
[02:51:44] article, you're not just limited to
[02:51:46] static files. uh your AI can now learn
[02:51:50] from live evolving web content from the
[02:51:52] internet. And finally, we have a CSV
[02:51:54] loader. So that's the one built for
[02:51:58] structural table data like spreadsheet
[02:52:01] data sets or analytical reports. Instead
[02:52:04] of reading the file as raw text, CSV
[02:52:06] loader processes each row of your CSV
[02:52:09] file as a separate document allowing the
[02:52:11] model to understand and retrieve uh
[02:52:15] structured information easily.
[02:52:17] especially useful when combined with
[02:52:19] retrieval or Q&A uh components where you
[02:52:23] might want your AI to answer questions
[02:52:26] like which product has the highest
[02:52:29] highest sales last month or like who's
[02:52:31] the top uh growing employee and and then
[02:52:37] all sorts of stuffs like that from a CSV
[02:52:40] based data source. Uh so as we have
[02:52:44] completed uh these five these five
[02:52:47] document loaders so each loader solves a
[02:52:50] unique problem here. First
[02:52:54] text loader helps with plain text. PIP
[02:52:57] PDF loader handles structured PDF
[02:52:59] documents. Directory loader manages bul
[02:53:02] data. Webpage loader brings in dynamic
[02:53:04] online content. And CSV loader handles
[02:53:06] structured text. Now we're going to see
[02:53:09] the implementation of each of these
[02:53:10] loader in our code.
[02:53:14] Okay. So first of all I'm going to
[02:53:16] create a folder
[02:53:18] uh what is it number nine and I call it
[02:53:21] document loaders
[02:53:23] and then we'll start with the first one
[02:53:27] which is our text loader.py.
[02:53:32] Okay. I'm going to uh create a few files
[02:53:35] here. Let's uh
[02:53:39] okay for this we'll use the docs uh docs
[02:53:43] txt file that we already have and then
[02:53:46] we'll load this. Let me word so that you
[02:53:48] can see the content of this what it's
[02:53:52] written here. I'm not going to use the
[02:53:54] model uh I'm just going to use the
[02:53:56] loader and then show you by loading the
[02:53:59] documents. So from line chain community
[02:54:03] dot document loaders import
[02:54:07] text loader.
[02:54:11] Okay. Uh now you need to create a loader
[02:54:16] object from this text loader. So text
[02:54:18] loader and then provide a file name
[02:54:21] cricket uh sorry docs.txt.
[02:54:26] And then if you need to provide an
[02:54:28] encoding uh you yeah you you can also do
[02:54:30] it. So let's do it. Encoding UTF8
[02:54:38] and then once you do this you can print
[02:54:40] out your docs here. Um so first of all
[02:54:45] let's do loader.load
[02:54:49] and then you can print out your docs
[02:54:50] here.
[02:54:53] Okay. Uh what did I do here? Let's exit
[02:54:55] this and then run this again.
[02:55:00] So as you can see the content inside
[02:55:04] this docs folder has been loaded in
[02:55:08] loaded from my file here and then the
[02:55:11] source is docs.txt. What you can also do
[02:55:14] is you can also see the type of this
[02:55:17] docs.
[02:55:18] So if you print the type of this docs
[02:55:21] then you'll see
[02:55:23] that the type is list here in in the
[02:55:26] list you have uh document which encodes
[02:55:30] the metadata that encodes source uh and
[02:55:33] then inside the document we also have
[02:55:35] page content here. So you can directly
[02:55:38] also use this. So print docs dot sorry
[02:55:43] docs
[02:55:44] zero dot page
[02:55:48] page content which will directly print
[02:55:51] you the content inside the text that we
[02:55:54] have or you can also print out the
[02:55:56] metadata
[02:55:57] doc0 dot
[02:56:00] metadata and then you'll be able to see
[02:56:03] the meta which is the source that we
[02:56:05] have. Okay. So this is
[02:56:10] our first loader that we have.
[02:56:16] Now we'll move to our second loader
[02:56:19] which is our PI PDF loader.
[02:56:23] New file.
[02:56:26] So PIP PDF
[02:56:29] loader.py.
[02:56:32] Here I'm going to copy a simple PDF file
[02:56:36] from somewhere uh and then [snorts]
[02:56:38] paste it here. Okay, you can grab any
[02:56:40] PDF file that you want. Uh,
[02:56:44] and I'll go to PIP PDF
[02:56:47] loader and I'll import from
[02:56:51] langen
[02:56:52] community document loaders import
[02:56:58] by PDF
[02:57:01] loader. Now
[02:57:04] initialize the loader
[02:57:07] object
[02:57:09] and my file name is uh dl curriculum
[02:57:13] PDF. So I'm going to use that same file
[02:57:15] name
[02:57:18] PDF
[02:57:20] just say docs equals to uh
[02:57:24] loader dot load and then print out the
[02:57:28] doc.
[02:57:30] So whatever is present in this document
[02:57:33] will be loaded and then printed out.
[02:57:41] Okay. So we need to install PIP PDF. So
[02:57:44] let's do this
[02:57:46] pipf.
[02:57:53] Okay. and then uh type install. We'll
[02:57:59] just do pi pig. Everything is else is
[02:58:01] installed here.
[02:58:05] And now that is installed, we can run
[02:58:06] our program again which is by PDF
[02:58:09] loader.
[02:58:11] Where is that?
[02:58:14] [snorts]
[02:58:20] And you can see our PDF page content has
[02:58:23] been loaded and it is loaded in the same
[02:58:26] format which contains a a list and then
[02:58:29] that contains a document. Document
[02:58:31] contains some metadata inside this and
[02:58:34] then along with that it it also has its
[02:58:37] page content. So you can follow the same
[02:58:39] process as as we did earlier here to
[02:58:43] print out the page content as well as
[02:58:44] the metadata. Okay. Now we'll move to
[02:58:48] the third type and then our third type
[02:58:50] is going to be our directory loader. So
[02:58:54] for that I'm I'm going to uh
[02:59:00] copy some PDFs inside a directory. So I
[02:59:05] basically have these AI uh AI books and
[02:59:08] a financial report. uh and then using
[02:59:14] using this PDF inside this directory I'm
[02:59:17] going to load the content of this
[02:59:18] particular books folder here. So let me
[02:59:21] open a new file. I'm going to call it
[02:59:24] directory loader.py.
[02:59:28] Uh you can choose any any kind of PDF
[02:59:32] inside a folder and then that will work.
[02:59:34] Okay. So from langen community dot
[02:59:37] document loaders
[02:59:41] import uh directory loaders
[02:59:46] and then we'll also do pi pdf loader
[02:59:48] because we have pdf content inside this.
[02:59:54] So loader equal to directory loader
[02:59:59] directory loader and then we'll provide
[03:00:01] a path to this. So path is a folder
[03:00:04] called books
[03:00:07] and then inside that I have uh contents
[03:00:11] like a file name dot PDF
[03:00:16] and then I'll also define a loader class
[03:00:18] and my and my loader class is going to
[03:00:20] be a pi PDF loader. Okay. So
[03:00:25] what I can do is I can do uh
[03:00:30] loader dot lazy load
[03:00:35] and then for
[03:00:37] document
[03:00:41] in docs
[03:00:43] we'll only print the meta data here. So
[03:00:49] document dot meta data. Okay, let me
[03:00:53] clear this out and then run this again.
[03:00:56] So, I have four different
[03:00:59] uh PDFs here and
[03:01:02] and for those four different PDFs,
[03:01:05] my document loader has has started
[03:01:08] loading whatever it can find inside it.
[03:01:11] So since there is a lot of metadata that
[03:01:15] I have, so it has been loading uh every
[03:01:19] metadata it can find inside my
[03:01:25] uh folder here.
[03:01:28] So it's loading each and every page.
[03:01:30] That is why the metadata uh print is is
[03:01:34] going on. But I think you understand
[03:01:36] what we tried to do here.
[03:01:39] So I'm going to do terminate this.
[03:01:42] And now we'll move to our
[03:01:45] fourth [snorts] one or our fourth loader
[03:01:51] which will be our webbased loader. So
[03:01:54] let me create a new file
[03:01:58] web base loader.py.
[03:02:02] I'm going to import webbased loader from
[03:02:05] langen community
[03:02:07] dot document loaders import
[03:02:11] the [snorts] web base loader. Okay,
[03:02:15] now I don't need anything else. I'm
[03:02:18] simply going to copy a URL about uh
[03:02:25] about a car review that I could find on
[03:02:28] the internet.
[03:02:30] So from this
[03:02:32] I'll use loader
[03:02:36] equals to web based loader and then I'm
[03:02:38] going to pass the URL
[03:02:40] docs equals to loader.load
[03:02:44] and then I'll print out the docs here.
[03:02:48] So this will open a website that
[03:02:50] contains a car review uh on it and then
[03:02:54] I'm loading I'm trying to load the text
[03:02:57] present in this particular URL here. So
[03:02:59] let me run this.
[03:03:02] Okay. So it also needs beautiful soup
[03:03:05] because it will it'll I think go for web
[03:03:08] scripping of this. So reinstall PS4
[03:03:14] here.
[03:03:21] I'll also mention it on the
[03:03:25] requirements.py. Okay. So since this is
[03:03:27] installed, so let me go and then run
[03:03:31] with base loader again. We clear this
[03:03:34] and run this.
[03:03:39] It might take some time because scraping
[03:03:40] might take some time here. And then you
[03:03:42] can see that all of the text inside this
[03:03:44] are loaded and then it's again in the
[03:03:47] same format. So so the format is
[03:03:49] uniform. It has a list inside it. It it
[03:03:53] contains a document inside. we we have
[03:03:56] metadata and then there are a lot of
[03:03:59] other contents in the metadata as well
[03:04:01] and then the page content actually
[03:04:03] contains the text content of that
[03:04:05] particular website. Now finally uh I I'm
[03:04:10] going to uh work on the last last type
[03:04:14] of loader which is a CSV loader. So for
[03:04:17] that I'm going to paste a CSV file here
[03:04:21] on my on my project folder. So you can
[03:04:24] see the CSV file that I have.
[03:04:27] It's just a comma separated file that
[03:04:29] contains some data. You can use any kind
[03:04:31] of CSV file that you want. And now I'm
[03:04:34] going to go to document loader. I'm
[03:04:35] going to create a new file. Five CSV uh
[03:04:40] CSV loader.py.
[03:04:42] Okay. Now again the import is the same
[03:04:45] from langen community.
[03:04:48] We import document loaders. uh import
[03:04:52] CSV loader and then the loader is going
[03:04:56] to be an object of CSV loader. Inside
[03:04:58] this I'm going to provide a file path.
[03:05:02] File path is going to be what is my file
[03:05:04] name. So social network ads dot CSV. Let
[03:05:06] me rename this and then write data dot
[03:05:09] CSV so that it'll be easier for me to
[03:05:12] write down the file name here. So data
[03:05:14] dot CSV
[03:05:16] and data equals to loader do.load upload
[03:05:20] and then if I print data here I will be
[03:05:24] able to see my CSV file content in this
[03:05:27] let me run this and you can see it's
[03:05:31] again pre being presented in a similar
[03:05:33] format inside the list there is a
[03:05:35] document and there is a metadata then
[03:05:37] inside it it contains source and page
[03:05:39] number here uh sorry page content here
[03:05:42] so this is how how how we use uh these
[03:05:46] five document loaders
[03:05:48] this is an essential part of our
[03:05:51] retrieval augmented generation system
[03:05:53] because uh on the very first step we
[03:05:56] need to load uh we need to ingest our we
[03:06:00] need to load our data uh into our rack
[03:06:04] system which can be used as a knowledge
[03:06:06] base for our rack project. So this is
[03:06:10] how we use it. I hope you understood the
[03:06:13] concept and also the implementation
[03:06:15] works for you. So imagine you're
[03:06:17] building an AI assistant that needs to
[03:06:19] remember everything you ever taught it
[03:06:21] from long documents, research papers, or
[03:06:24] even notes scattered across multiple
[03:06:26] files. Now, you wouldn't want your
[03:06:28] assistant to go through all those
[03:06:30] documents every single time you ask a
[03:06:32] question, right? It would be like asking
[03:06:34] a librarian to read every book in the
[03:06:36] library before giving an answer. And
[03:06:39] that's where vector store in line comes
[03:06:41] into play. They're like the memory banks
[03:06:43] of AI system. So far in this langen
[03:06:46] journey, we've talked about how to load
[03:06:48] data and how to split it into smaller
[03:06:50] manageable pieces. We've also seen how
[03:06:52] to generate embeddings, those numerical
[03:06:54] fingerprints that represent meaning
[03:06:55] rather than just words. But once we have
[03:06:58] all those embeddings, we need a place to
[03:07:00] store them efficiently and a way to
[03:07:02] search through them intelligently. And
[03:07:05] that's what a vector store does. You can
[03:07:08] think of a vector store as a smart
[03:07:10] semantic database. Instead of storing
[03:07:13] plain text, it store those
[03:07:14] highdimensional numbers vectors uh that
[03:07:17] capture the meaning behind the text. So
[03:07:19] when a new query comes in, the system
[03:07:22] converts it into an embedding too and
[03:07:24] then compares it with the stored vectors
[03:07:26] to find the ones that are most simply in
[03:07:28] the meaning. So even if your query
[03:07:31] doesn't use the same word as your data,
[03:07:33] it can still find the right answer
[03:07:35] because it understands what you meant,
[03:07:36] not just what you said. So for example,
[03:07:39] if you ask who is known as Captain Cool,
[03:07:42] a traditional keyword search might not
[03:07:44] help unless that exact phrase exists
[03:07:46] somewhere. But a vector store contains
[03:07:49] or the vector store understands that
[03:07:50] Captain Cool is semantically related to
[03:07:54] maybe Mahindra Singh Dhoni
[03:07:57] because their embeddings are close to
[03:07:59] each other in vector space. That's the
[03:08:01] real power of vector database. They let
[03:08:03] your AI think in terms of meaning and
[03:08:05] not in terms of matching words. So in
[03:08:08] langen we can use several vector stores
[03:08:10] like f chroma or pine cone among others.
[03:08:13] Uh in our case in this video we using
[03:08:16] chroma which is lightweight and works
[03:08:18] perfectly for local experiments. It
[03:08:20] stores all those embeddings
[03:08:21] persistently. So even when you restart
[03:08:23] your application your AI doesn't forget
[03:08:26] what it has learned. And when you
[03:08:28] connect this to your retrieval pipeline
[03:08:30] everything falls into place beautifully.
[03:08:32] The documents get embedded stored in the
[03:08:34] vector database and when a user asks
[03:08:36] asks a question the system fetches the
[03:08:39] most relevant chunks uh not because of
[03:08:41] matching keywords but because of the
[03:08:42] shared meaning here. So those retrieved
[03:08:44] chunks are then passed to your language
[03:08:46] model as additional context helping it
[03:08:49] generate accurate and informed answers.
[03:08:51] So vector stores are one of the key
[03:08:53] reasons uh modern AI systems feel so
[03:08:56] intelligent. They make your assistant
[03:08:58] capable of remembering, reasoning and
[03:09:00] retrieving information just like a human
[03:09:04] instantly recalling the most meaningful
[03:09:06] pieces of information it has seen before
[03:09:08] and without vector store your AI would
[03:09:10] simply be guessing and with them it's
[03:09:12] reasoning based on the memory.
[03:09:16] So in short uh we can say that vector
[03:09:18] stores turn static knowledge into
[03:09:20] searchable understanding giving your AI
[03:09:22] a memory that's fast, scalable and
[03:09:25] deeply semantic. So now let's go for the
[03:09:27] implementation of search vector store
[03:09:29] tool.
[03:09:33] Okay. So I'm going to create a new
[03:09:35] folder again here.
[03:09:38] Let's call this folder 11.
[03:09:42] Call it vector store.
[03:09:44] Okay. Inside this I'm going to create my
[03:09:47] first file.
[03:09:50] Vector store.py.
[03:09:53] So uh let me use the langen hogging face
[03:09:56] embeddings. So
[03:10:00] for this part so like this langen
[03:10:03] hogging face embeddings let's also
[03:10:05] import chroma
[03:10:07] uh which is our vector database that
[03:10:09] we're going to use. So I don't think
[03:10:11] I've imported this. So let me install
[03:10:13] pip install
[03:10:17] lang chain chroma
[03:10:25] and I'm also going to mention it on the
[03:10:27] requirements.
[03:10:29] So lang chroma
[03:10:40] from langchain chroma
[03:10:44] import chroma
[03:10:47] uh once it is installed uh the error
[03:10:50] will then go okay chroma then we'll also
[03:10:56] [snorts] import document
[03:10:58] So from lang dot schema import
[03:11:03] document. Okay. Uh
[03:11:07] I'm also going to load my load my
[03:11:11] hogging face credentials here. So from
[03:11:13] env import
[03:11:16] load.env
[03:11:19] and load env function is called.
[03:11:23] Let me define my embedding model here.
[03:11:26] So I'm going to copy this
[03:11:29] uh from my previous code. So this model
[03:11:33] will be used as hoging base embedding. I
[03:11:35] think we've already used this in our
[03:11:36] previous code too. So this is not new
[03:11:38] for you. So here I'm going to create
[03:11:41] some some document. Let me just copy
[03:11:44] these uh these are too longs for me to
[03:11:47] type. So I have some document related to
[03:11:49] some IPL players.
[03:11:52] So let me just copy this and then use
[03:11:54] word. You can pause the video and then
[03:11:56] see what is being typed here. So now
[03:12:00] document one contains page content
[03:12:03] related to Virat Kohli and his team
[03:12:05] called Royal Challenge Bangalore.
[03:12:06] Document two is about Sharma and his
[03:12:09] team. Document three is about MS Dhoni
[03:12:12] and his team. Document four is about
[03:12:14] just Bumrah and his team. And then
[03:12:15] document five is about Rabinda Jada and
[03:12:17] his team. So these are the documents
[03:12:20] that I need to store in my vector
[03:12:22] embeddings. Uh so here what I'm going to
[03:12:25] do is I'm going to combine all of this
[03:12:26] in a single list. So doc 1, do 2, do 3,
[03:12:31] do 4 and do 5.
[03:12:35] Okay. Now let me initialize my vector
[03:12:37] store. This will come from chroma here.
[03:12:41] Chroma. And inside this
[03:12:44] I [snorts] need to define my embedding
[03:12:46] function. My embedding function will be
[03:12:48] my embedding model that I've defined.
[03:12:51] my pers directory.
[03:12:55] Let's just name name it chromad. A new
[03:12:57] folder called chromad will be created in
[03:12:59] my project and then my embeddings will
[03:13:01] be stored inside that.
[03:13:04] Then after that I'll need a collection
[03:13:06] name.
[03:13:08] So the collection name will be sample.
[03:13:14] [cough]
[03:13:14] [clears throat]
[03:13:22] Now since my vector store is initialized
[03:13:25] and now I'm going to add my documents to
[03:13:27] the vector store. So vector store dot
[03:13:28] add documents and then I'm going to add
[03:13:31] the collection of document that I've
[03:13:32] created here.
[03:13:35] Uh-huh.
[03:13:37] So what else? Let me retrieve vector
[03:13:41] store.get
[03:13:43] get
[03:13:45] and then uh let me in some in including
[03:13:50] words here. So embedding should be
[03:13:52] included whenever I retrieve from vector
[03:13:54] store. Document should be retrieved
[03:13:55] whenever I fetch from vector store and
[03:14:00] then metadatas should be retrieved.
[03:14:02] Okay. Now I will have
[03:14:06] my query here.
[03:14:09] Let's say uh who among these are
[03:14:14] ballers.
[03:14:16] So I have some players here or cricket
[03:14:18] players among them. My query is who
[03:14:21] among these are ballers. So what I'm
[03:14:24] going to do is I'm going to run a vector
[03:14:26] search. So vector store dot run a
[03:14:30] similarity search.
[03:14:32] My query will be my query here. And then
[03:14:36] I will fetch a top three result from
[03:14:39] this particular query.
[03:14:41] So and then store everything in result.
[03:14:45] And then let's print out our result
[03:14:47] here.
[03:14:52] So let me run this. Uh
[03:14:57] my documents will be embedded using this
[03:14:59] embedding model here and then be stored
[03:15:01] in this vector database. uh and from
[03:15:04] that vector database uh I will simply
[03:15:06] run a query and then run a similarity
[03:15:10] search in that query and then get the
[03:15:12] relevant result here. So let me see uh
[03:15:17] the first one Mumbai Indian Jaspid Bumra
[03:15:19] is a baller that's nice. Uh the second
[03:15:23] one Mumbai Indian Rohit Sharma is also
[03:15:29] shown as a baller and then and then the
[03:15:32] third one Robinda is also shown as the
[03:15:34] baller. So Virat Kohli and then Msi are
[03:15:39] excluded from these search list and then
[03:15:42] based on the similarity it's found that
[03:15:44] V Rohit Sharma Bumra and then Robin Aar
[03:15:48] are ballers here. Let me also run uh
[03:15:52] another query here if it's okay. Uh
[03:15:57] we can also do something like this. So
[03:16:00] we can also print our result based on
[03:16:03] similarity search with scores. So if we
[03:16:07] see this then then we can we should see
[03:16:10] that the result rohit sharma should have
[03:16:13] a very low similarity score here. So
[03:16:15] similarity search with score.
[03:16:19] Okay. Uh our query will be our query
[03:16:24] and then and then we'll have a toply
[03:16:27] result here.
[03:16:30] So let me run this again and we should
[03:16:33] see that the simatic score for Rohit
[03:16:35] Sharma should be quite less than uh
[03:16:38] Bumra or Ravinday
[03:16:41] because Rohit Sharma is [snorts] not in
[03:16:43] fact a baller. Sometimes he does bowl
[03:16:45] off spin uh but not much. So let's see
[03:16:52] uh play for okay the first one is the
[03:16:55] spin bumra. So this is shown.
[03:16:59] Okay. Wait. Okay. I've not printed the
[03:17:01] result. Let me also print the result.
[03:17:03] Let me omit omit the previous result.
[03:17:05] And then let me print it here.
[03:17:08] And then let me com comment this out.
[03:17:12] And I just want to
[03:17:15] see the result.
[03:17:20] And then you might be wondering where
[03:17:22] this chroma DB is. It should be well
[03:17:25] within here sometime. So yes, you can
[03:17:28] see the folder called chromadv and then
[03:17:32] uh that and then using that particular
[03:17:35] uh chromad vector database my result is
[03:17:37] being pulled here. So just with bumra
[03:17:40] has a similarity of something like 1.01.
[03:17:46] So again it's saying just with bumra and
[03:17:48] then it's saying just with bumra again.
[03:17:50] So, so the top result is
[03:17:54] top result is only Bumra and then not
[03:17:57] the other bowlers here. So, this is how
[03:18:00] uh vector store works. It converts our
[03:18:03] data
[03:18:05] or documents into embeddings and then
[03:18:07] store it and then based on the query we
[03:18:09] have provided we can fetch
[03:18:13] uh following contents as well as uh what
[03:18:17] we can do is we can uh get the most
[03:18:21] similar result or like run the
[03:18:23] similarity search on our given query
[03:18:27] against the stored documents. So I hope
[03:18:30] you understood the concept for vector
[03:18:32] store. It is just like a just like a
[03:18:33] database but instead of storing your
[03:18:36] data it stores the embeddings of your
[03:18:38] documents. You've loaded a ton of
[03:18:40] documents onto your langen pipeline.
[03:18:42] PDFs, text file, web pages, you name it.
[03:18:45] But now comes the big question. How do
[03:18:47] you exactly find the most relevant piece
[03:18:49] of information when the user asks asks a
[03:18:52] question? And that's where the retrieval
[03:18:54] comes into play. Retrievers are like the
[03:18:57] memory search engine of your engine
[03:18:58] system. They don't generate new
[03:19:01] information. Instead, they fetch
[03:19:03] relevant documents from your existing
[03:19:05] knowledge base. So whenever a user query
[03:19:07] comes in, the retriever looks at all
[03:19:10] your index data and returns only the
[03:19:12] chunks that are most relevant to that
[03:19:14] query. In simple terms, think of
[03:19:17] retrievers as your AI AI's librarian.
[03:19:20] You ask a question and it doesn't hand
[03:19:22] you the entire library. it quickly find
[03:19:25] the exact pages or paragraphs that
[03:19:27] matters the most. Now, under the hood,
[03:19:29] retrievers often work with vector
[03:19:31] stores. Whenever you add documents, they
[03:19:34] converted into vector embeddings,
[03:19:35] numerical representation that capture
[03:19:37] the meaning of the text. Then, when a
[03:19:40] question comes in, it's also converted
[03:19:42] into a vector and the retriever compares
[03:19:44] it with all stored vectors to find the
[03:19:46] closest matches. This is how your system
[03:19:49] ensures semantic relevance.
[03:19:51] It's not just matching words but
[03:19:53] understanding the meaning. Langen offers
[03:19:57] various types of retrievers. Some are
[03:19:59] simple keyword based ones, others are
[03:20:01] embedding based and then others are even
[03:20:04] specialized ones like multiquery
[03:20:06] retrieval or contextual compression
[03:20:08] retriever that enhances the retrieval
[03:20:11] quality using alms. Retrieverals are uh
[03:20:15] essentially be or retrievers. The
[03:20:18] retrievers are essential because they
[03:20:20] bridge the gap between your static
[03:20:22] document and your conventional AI. They
[03:20:24] ensure your LLM has contextually rich
[03:20:26] relevant data to reason with without
[03:20:29] needing to retrain or fine-tune the
[03:20:31] model itself. And in this video, we'll
[03:20:33] get hands-on with one of the most
[03:20:36] commonly used retrievers, the Wikipedia
[03:20:38] retriever, where we'll see how to pull
[03:20:40] realtime factual information straight
[03:20:42] from Wikipedia to enrich our AI
[03:20:45] response. So now let's go to the video.
[03:20:51] Okay. So, I'm going to create a new
[03:20:52] folder again here.
[03:20:55] Uh, I'll call it Okay. What is the
[03:21:00] size? Okay. 12. So, let's me create a
[03:21:03] folder 12 dot
[03:21:06] retrievers. Uh, I'll create a new file
[03:21:09] inside this. Let's call it Wikipedia
[03:21:14] 3r.py.
[03:21:17] Okay. So from langen community
[03:21:21] retrievers import
[03:21:24] wikipedia retriever uh
[03:21:27] then I'm going to define my retriever
[03:21:29] object here. So ret object r equals to
[03:21:34] wikipedia retriever.
[03:21:37] I'm going to get the top key results and
[03:21:39] then the language I can also say the
[03:21:41] language and then the language has to be
[03:21:43] English. So my query is uh let's say
[03:21:48] Indian premier
[03:21:51] league
[03:21:53] and then uh what I can do is I can use
[03:21:56] my reviewer object to invoke this query.
[03:22:03] Uh I'm not sure how many documents I'll
[03:22:05] find but let's print out print out the
[03:22:09] length of the document that I'm going to
[03:22:11] find here. So lend the docs. Let me run
[03:22:14] this.
[03:22:17] Okay. So I need to install Wikipedia. So
[03:22:19] let's go to our requirement. Add a new
[03:22:22] library.
[03:22:23] Save it. I'm directly going to install
[03:22:26] this without going to the
[03:22:28] requirements.py
[03:22:31] or other requirements.xt. So let me
[03:22:34] rerun this again.
[03:22:36] Uh where is that? Wikb.
[03:22:39] So let me run this.
[03:22:46] It will take some time because it will
[03:22:48] again uh go to go to Wikipedia and then
[03:22:52] uh get the results from there. So yeah,
[03:22:55] this is my
[03:22:58] uh since I'm since I've only asked for
[03:23:01] top two results. So it is giving me two
[03:23:03] results. And then for this one I can
[03:23:06] print each each and every of my results.
[03:23:08] So for I do in in enumerate
[03:23:13] uh docs
[03:23:15] I can print is the result. So f uh
[03:23:20] result
[03:23:23] I + 1 and then uh print content
[03:23:29] and inside content I can print
[03:23:33] uh
[03:23:34] doc dot
[03:23:37] page content.
[03:23:39] Okay. So if I print this again I will
[03:23:43] have my two documents as well as its
[03:23:45] content too.
[03:23:47] And then that is straight from some
[03:23:49] Wikipedia pages about this particular
[03:23:51] topic here. So this is how we use
[03:23:55] retrievers. Uh in the next video we'll
[03:23:58] see we'll see something else uh
[03:24:02] or like we'll see uh more more in the
[03:24:06] retriever section and then we'll also
[03:24:07] use it on the local data or local
[03:24:10] documents. In the last video we explored
[03:24:12] what retrievers are and why they are
[03:24:14] such an essential part of langen. Now
[03:24:16] let's see how they actually come to life
[03:24:18] with the help of something called a
[03:24:19] vector store retriever. Think of a ve
[03:24:22] store as a smart database that doesn't
[03:24:24] just [snorts] store text, it stores the
[03:24:26] meaning. We've already talked about
[03:24:28] this. Every sentence, paragraph or
[03:24:29] document we feed into it is converted
[03:24:32] into a numerical representation called
[03:24:34] an embedding. And then these embeddings
[03:24:36] capture the semantic meaning of our
[03:24:37] text. So instead of searching for exact
[03:24:39] words, retriever searches for similar
[03:24:42] ideas. So in this video we're using
[03:24:44] Chroma app which we've already used
[03:24:46] earlier which is one of the most popular
[03:24:48] open source vector databases out there.
[03:24:51] Uh
[03:24:53] so once we add our documents into Chroma
[03:24:55] it handles all the heavy lifting storing
[03:24:57] indexing and efficiently searching
[03:24:59] through our vetoriiz data. Now to
[03:25:01] generate these embeddings we'll be using
[03:25:03] hogging face embeddings a special model
[03:25:06] that we've already used in the past. uh
[03:25:10] the model will transform each document
[03:25:12] into a highdimensional vector allowing
[03:25:14] Chroma to understand the relationship
[03:25:16] between different pieces of text and
[03:25:18] then when we convert our chroma vector
[03:25:19] store into a retriever uh what we're
[03:25:22] really doing is giving our application
[03:25:25] to application the power to search
[03:25:28] semantically. So when you ask a question
[03:25:30] like what is chroma used for uh it
[03:25:33] doesn't just look for that exact phrase
[03:25:35] but in but it's fine sentences that
[03:25:38] means something similar even though
[03:25:40] they're using different words. So the
[03:25:42] combination of hoging face embeddings
[03:25:43] and chroma retriever forms the backbone
[03:25:45] of the retrieval augmented generation
[03:25:47] rack system that we've been talking
[03:25:49] about and then a simple form of rag
[03:25:51] we've already implemented in a previous
[03:25:53] video. So by the end of this video,
[03:25:55] you'll see how this retriever transforms
[03:25:57] ordinary text into a scalable
[03:25:59] intelligent knowledge base that your AI
[03:26:01] can reason over effortlessly. Now
[03:26:03] without any delay, let's go to the code.
[03:26:10] Uh so I'm going to delete this Chroma
[03:26:13] database for now because uh it already
[03:26:16] contains embedding uh previous
[03:26:18] embedding. So I'm going to create a new
[03:26:21] file here inside retrievers and then
[03:26:23] call it vector store retrievers.py.
[03:26:28] So let me import chroma first. So from
[03:26:33] langchen
[03:26:35] chroma import chroma
[03:26:38] from langchen_h hoging face
[03:26:42] import hogging face embeddings from
[03:26:45] langen_core
[03:26:47] dot documents
[03:26:49] import document
[03:26:52] okay so uh I'll also need to load env so
[03:26:57] from
[03:26:59] env import load env
[03:27:03] let me into load env load the hogfest
[03:27:06] credentials here I'm going to create a
[03:27:08] document I'll just copy paste it uh from
[03:27:11] somewhere so these will be my source
[03:27:14] documents here let me wrap this up okay
[03:27:19] so these will source documents here we
[03:27:21] have uh these four these four contents
[03:27:25] uh
[03:27:26] each defined inside a document
[03:27:29] Then uh we'll initialize our embedding
[03:27:33] embedding model.
[03:27:35] So this will be our hogging face
[03:27:37] embedding model. We'll use sentence
[03:27:39] transformers and then a model inside
[03:27:41] this sentence transformer. So what we're
[03:27:44] going to do is we're going to create a
[03:27:45] vector store.
[03:27:47] We've already done this again. So we'll
[03:27:50] use comma dot from documents
[03:27:56] from underscore
[03:27:59] documents. Uh
[03:28:02] so our documents will be
[03:28:05] the document that we have here. Our
[03:28:08] embedding
[03:28:10] will be the embedding model that we have
[03:28:13] and then the collection name.
[03:28:16] collection name let's say will be the
[03:28:17] sample. Okay. Now we'll convert our
[03:28:20] vector store into a retriever. So the
[03:28:23] retriever
[03:28:24] equals to vector store dot as retriever.
[03:28:29] I just need to pass the
[03:28:33] search keyword arguments. Uh search
[03:28:36] quirks equals to uh let me pass a dict
[03:28:40] here. So equal to two. So I'm so I'm
[03:28:44] basically getting a top two result here.
[03:28:46] So query equals to let's ask about uh
[03:28:50] embedding. So what does embedding do
[03:28:56] and then uh based on this I'm going to
[03:28:59] invoke my result.
[03:29:01] So retriever
[03:29:04] invoke
[03:29:07] uh and then I'm going to get query
[03:29:10] and based on this I'm I'm just going to
[03:29:12] print the result whatever it it throws
[03:29:15] at me.
[03:29:17] So now
[03:29:19] uh let's run this. We've we have used
[03:29:22] vector store uh as a retriever here.
[03:29:26] Let's run this and then see what
[03:29:28] happens.
[03:29:36] So this all of these are being com
[03:29:38] converted to embeddings
[03:29:41] and then a chromb uh
[03:29:44] database is been created
[03:29:47] and along with that it is being
[03:29:48] converted to uh retrievers uh it is
[03:29:52] being converted as a retriever and then
[03:29:54] giving me the results.
[03:29:56] If you see here what I can see is
[03:30:01] whenever I
[03:30:03] I ask about embedding it gives me this
[03:30:06] result at first and then the embedding
[03:30:10] result.
[03:30:11] Do I have a embedding result? No. I have
[03:30:13] this chroma uh and then also I have this
[03:30:17] langen result here. So I have these
[03:30:20] three documents provided to me for this
[03:30:23] particular question here or let me
[03:30:27] change my question and then ask what is
[03:30:30] comma used for and I just need one
[03:30:35] result here. Let me venture it to one
[03:30:38] and run this.
[03:30:52] So again as you can see my search
[03:30:55] directly redirects me to this chroma is
[03:30:59] a vector database optimizer lm search.
[03:31:01] It also provides me some more answer uh
[03:31:05] few more answers here related to
[03:31:07] embeddings and then the openi but but my
[03:31:11] most relevant uh result is
[03:31:15] the particular document here or this
[03:31:18] particular document here for the query
[03:31:22] here. Okay. So this was another type of
[03:31:25] retriever that we've used. In this
[03:31:27] video, we're going to bring together
[03:31:29] everything we've learned so far, from
[03:31:31] document loaders and text splitters to
[03:31:34] embeddings, vector stores, and
[03:31:36] retrievers, and use them to build
[03:31:38] something real. Imagine being able to
[03:31:42] ask questions directly about the content
[03:31:44] of any YouTube video without manually
[03:31:47] watching or scrubbing through it. That's
[03:31:49] exactly what we're going to do. We'll
[03:31:52] start by pulling the transcript of a
[03:31:54] YouTube video using the YouTube
[03:31:55] transcript API. This gives us all the
[03:31:58] spoken text which then becomes the
[03:32:00] foundation of our knowledge base. Now
[03:32:03] we'll use a recursive character text
[03:32:05] reader to break that long trans
[03:32:08] transcript into manageable chunks so our
[03:32:10] system can process and retrieve
[03:32:12] information efficiently. Then comes the
[03:32:15] magic. We'll convert those chunks into
[03:32:17] embeddings using a hogging face model
[03:32:19] and store them in a fires vector
[03:32:22] database. This allows our system to
[03:32:24] search and retrieve context content
[03:32:27] that's semantically related to any
[03:32:29] questions we ask. Once that's done,
[03:32:32] we'll turn fires into a retriever, which
[03:32:35] will find the most relevant parts of the
[03:32:37] transcript related to our query.
[03:32:40] Finally, we'll use a Gemini flash model,
[03:32:43] Google's powerful language model to
[03:32:45] analyze that content and generate an
[03:32:47] accurate transcriptbased answer to our
[03:32:49] question. In short, we're transforming a
[03:32:52] YouTube video into an intelligent,
[03:32:54] searchable knowledge source. By the end
[03:32:57] of this video, you'll understand how all
[03:32:59] the individual engine components like
[03:33:01] loaders, splitters, embeddings,
[03:33:03] retrievers, and models come together to
[03:33:06] create a fully functional question
[03:33:08] answering pipeline powered by a real
[03:33:10] video content. So, let's go to the
[03:33:12] implementation.
[03:33:18] So, I'm going to create a new folder
[03:33:20] again.
[03:33:25] Let's call this
[03:33:28] the rack systems
[03:33:38] and inside this I'm going to create a
[03:33:39] new file
[03:33:41] YouTube_rank.py.
[03:33:45] Okay, first of all, I'm going to uh
[03:33:50] pull up YouTube transcript API
[03:33:54] import
[03:33:57] YouTube transcript
[03:34:00] API
[03:34:02] and transcripts
[03:34:06] disabled.
[03:34:08] We'll need to install this library here
[03:34:10] because I once I try to run this.
[03:34:14] So we'll need to install YouTube
[03:34:16] transcript API. So let me just do pip
[03:34:20] install YouTube
[03:34:24] transcript
[03:34:25] API.
[03:34:32] Okay, then I'm going to
[03:34:36] import
[03:34:39] recursive character text here.
[03:34:43] After this
[03:34:46] uh embedding from our hugging face
[03:34:48] models
[03:34:53] then we'll import our model.
[03:35:03] I'll also import import the prompt
[03:35:05] template.
[03:35:13] Then I'll import the vector database.
[03:35:22] And then finally to load our credential
[03:35:24] I'll import load.b.
[03:35:33] So step one is
[03:35:36] indexing or document induction.
[03:35:40] documentation.
[03:35:43] So I'll take a video ID and for video ID
[03:35:47] I'm going to take my own YouTube video
[03:35:49] here somewhere. Uh let me also load this
[03:35:52] credential and let's go to the video ID
[03:35:55] part. Okay. So
[03:35:59] so here is uh our video on on like
[03:36:03] [snorts] building a rag pipeline which
[03:36:05] we did uh couple of days earlier in uh
[03:36:08] video number 17. So I'm just going to
[03:36:11] copy this particular video ID from from
[03:36:14] the URL and then paste it in my code.
[03:36:22] Okay. So this is going to be my video
[03:36:24] ID.
[03:36:28] Then what I'm going to do is I'm going
[03:36:30] to try uh
[03:36:34] and then I'm going to initialize an
[03:36:36] object of YouTube API or YouTube
[03:36:39] transcript API
[03:36:41] and then I'm going to
[03:36:45] pull my transcript here. So y ai dot
[03:36:50] fetch
[03:36:52] my video ID will be my video ID and then
[03:36:57] uh the language of the video is English.
[03:37:00] I want transcript in English.
[03:37:03] Then I'm going to flatten
[03:37:06] the transcript
[03:37:09] to plain text.
[03:37:11] So for this what we're going to do is
[03:37:15] transcript equals to
[03:37:18] dot join
[03:37:21] chunk [snorts]
[03:37:22] dot text for
[03:37:25] chunk
[03:37:26] in transcript list.
[03:37:31] We'll also put an exceptions here. So if
[03:37:33] transcripts are
[03:37:36] disabled then we'll say
[03:37:41] no captions available
[03:37:44] for the video.
[03:37:48] Okay. So this is step one. We'll move to
[03:37:52] step two.
[03:37:54] In step two we'll do indexing uh which
[03:37:57] means our text splitting.
[03:38:01] So for that we already have our splitter
[03:38:03] here. So let me initialize the object of
[03:38:06] the splitter. So splitter equals to
[03:38:09] recursive character text splitter. I'm
[03:38:11] going to define a chunk size of maybe
[03:38:14] 1,000 and then a chunk overlap. Okay,
[03:38:17] we'll not do 1,000. 1,000 is too long.
[03:38:19] So we'll do a chunk size of 300 and then
[03:38:22] a chunk overlap of 50.
[03:38:29] And then I'm going to use the splitter
[03:38:31] to split my text here or split my
[03:38:33] transcript. So create documents
[03:38:38] transcript
[03:38:42] if you want to see how many chunks we've
[03:38:45] broken it down into. So let's see if we
[03:38:48] can indeed uh extract the captions of
[03:38:51] transcript from our video or not. So let
[03:38:53] me run this.
[03:39:02] Okay, so we have 33 chunks. We can uh we
[03:39:05] could extract the extract the transcript
[03:39:08] from our video. So let's go to step
[03:39:11] three. The step three is embedding
[03:39:15] generation
[03:39:19] and storing in vector database.
[03:39:25] Okay. So embedding model
[03:39:28] will be used from hugging base
[03:39:30] embeddings and then the model name is
[03:39:36] uh sentence
[03:39:43] transformers all
[03:39:46] in LM L6
[03:39:51] we do uh the model I found it from our
[03:39:57] hogging face library. Uh let's also
[03:40:00] initialize our vector store. So vector
[03:40:03] store is done using
[03:40:06] files. So from documents
[03:40:12] chunks and then embedding equals to
[03:40:15] embedding model. Okay. Next is retrieval
[03:40:22] retriever. Uh so I'm going to create my
[03:40:25] retriever from
[03:40:28] my vector store as
[03:40:31] uh as a retriever
[03:40:34] and then the search type is going to be
[03:40:37] based on similarity
[03:40:39] and then uh search
[03:40:42] keyword arguments. Uh let me do this
[03:40:46] again.
[03:40:47] So search keyword arguments
[03:40:51] is equal to uh the top let's say results
[03:40:56] here.
[03:41:01] Okay. Let me design my prompt using my
[03:41:06] prompt template.
[03:41:11] So in case of prompt template let me
[03:41:13] define my template here.
[03:41:17] So let's
[03:41:20] provide you are a helpful
[03:41:28] assistant
[03:41:30] answer only from the
[03:41:34] provided
[03:41:36] transcript
[03:41:39] context. If the context is
[03:41:43] insufficient
[03:41:47] just answer I don't know and then uh
[03:41:54] let me add a line break and then mention
[03:41:58] context
[03:42:00] is equal to context
[03:42:04] and uh question
[03:42:07] another line break question is equal to
[03:42:12] question.
[03:42:15] Okay. So this will be my template here.
[03:42:19] Uh
[03:42:28] I don't think I need to put an string.
[03:42:30] So let me remove this. So input
[03:42:32] variables are context and questions.
[03:42:38] and text and question.
[03:42:42] Okay, so this is done.
[03:42:44] Now let me deise my question here. Uh
[03:42:49] what is the video
[03:42:52] talking about
[03:42:56] and then we will also join a content
[03:42:59] context text. So context text is going
[03:43:03] to be joined from uh let's do this / m
[03:43:07] [clears throat]
[03:43:08] dot join
[03:43:10] dot dot
[03:43:13] page content for
[03:43:17] for in
[03:43:21] uh retrieved docs and then
[03:43:25] retrieve docs is going to The
[03:43:33] retrieve doc is going to be retriever
[03:43:36] dot
[03:43:38] invoke question.
[03:43:42] Okay. So after that I'm going to create
[03:43:44] my final prompt.
[03:43:50] So final
[03:43:54] prompt equals to prompt dot invoke. I
[03:43:58] need to pass two variables. One is the
[03:44:01] context which I can provide from context
[03:44:04] text
[03:44:05] and then the other is the question which
[03:44:07] I can provide from my question here.
[03:44:14] And finally I can invoke my model. Uh so
[03:44:18] model dot invoke
[03:44:21] final prompt
[03:44:25] I've defined my model right okay I've
[03:44:26] not defined my model so let me also
[03:44:28] define my model here so model equal to
[03:44:31] chat global generative AI
[03:44:35] model equals to Gemini 2.5
[03:44:39] /
[03:44:43] answer dot content from here so let Let
[03:44:46] me run this and then see if we can
[03:44:49] actually get the answer from our
[03:44:52] generated transcript or not.
[03:44:56] Let me remove this print statement for
[03:44:58] now and then run it.
[03:45:03] Uh I missed a comma. Let's see. Yeah, I
[03:45:06] should have puted a comma here
[03:45:09] at the end of the text.
[03:45:12] Let me run it again.
[03:45:22] It will take some time for transcript
[03:45:23] generation as well as um the embedding
[03:45:26] model loading and also uh it will take
[03:45:30] some time uh for the retriever to work
[03:45:35] here. So at first the model has been
[03:45:37] downloaded.
[03:45:39] I think I've already used this model
[03:45:41] earlier. I might have changed something
[03:45:43] here. Let me [clears throat] check.
[03:45:46] Okay. So,
[03:45:48] yeah. Okay. So, model was uh downloaded.
[03:45:52] So, the video is talking about using
[03:45:54] embeddings to make a model retrieve and
[03:45:56] reason over real data. It will build a
[03:45:58] simple table generation. Okay, it works.
[03:46:01] Uh in fact, we're talking about the PC
[03:46:03] model in that particular video. Uh and
[03:46:06] then it works. So, I'll pass something
[03:46:09] that is not present in the context.
[03:46:12] So I'll pass this question here. Uh my
[03:46:15] question will be
[03:46:18] so does the video or like
[03:46:23] what does
[03:46:26] what does the creator say
[03:46:30] creator say about
[03:46:34] Brazil in the
[03:46:37] world cup football?
[03:46:40] I don't think the context for this is
[03:46:41] present in the video. So the model
[03:46:44] should say that it simply doesn't know
[03:46:45] about it. Let me run this again.
[03:46:59] It would be efficient uh to just uh
[03:47:03] store this uh [snorts]
[03:47:05] transcript locally once it is
[03:47:07] downloaded. that every time um the
[03:47:09] transcript fetching part is not done as
[03:47:12] well as the vector store can also be
[03:47:13] stored. So as you can see uh for this
[03:47:17] question what does the creator say about
[03:47:19] Brazil in the World Cup football? It
[03:47:20] simply says I don't know because that
[03:47:22] particular context is not present in our
[03:47:24] transcript. So this is it. So we have
[03:47:28] successfully implemented a YouTube
[03:47:30] transcript uh knowledge base and then
[03:47:32] from that created a retrieval augmented
[03:47:34] generation system uh answering our
[03:47:37] particular question. So I hope uh it
[03:47:39] runs on your end too. In the earlier
[03:47:42] videos we've used language models in a
[03:47:44] very traditional way at chatbased
[03:47:46] systems. You'd give them a prompt, they
[03:47:48] would generate a response and that was
[03:47:49] it. But now things are evolving. The new
[03:47:53] wave of this agentic AI isn't just about
[03:47:55] generating text. It's about actions.
[03:47:58] Models are no longer limited to just
[03:48:00] answering questions. They can now call
[03:48:02] functions, interact with external
[03:48:03] systems, and even perform real
[03:48:05] operations on the behalf of user. This
[03:48:08] is where tools in Langen comes into
[03:48:10] play. Tools act as a bridge between the
[03:48:12] reasoning power of an LLM and the
[03:48:14] functional capabilities of your code.
[03:48:17] Instead of the model telling you what to
[03:48:19] do, it can now do it by invoking the
[03:48:21] right tool. Imagine this. You ask an AI,
[03:48:25] what is the product of five and 9? So
[03:48:27] instead of reasoning through the
[03:48:29] multiplication itself, it recognizes
[03:48:31] that there's already a defined tool that
[03:48:33] can perform this exact task and call it
[03:48:35] automatically. This shift is massive
[03:48:38] because it transforms LLM from being
[03:48:39] just text generators into decision-m
[03:48:41] agents. They can analyze context, plan
[03:48:45] what needs to be done, and then use the
[03:48:47] appropriate functions to get accurate
[03:48:49] results all autonomously. In this video,
[03:48:51] we'll explore how to define and register
[03:48:54] tools in Langen using the tool decorator
[03:48:56] which turns ordinary Python function
[03:48:58] into callable AI tools. And by the end
[03:49:00] of this video, you'll understand how
[03:49:02] this small but powerful addition lays
[03:49:04] the foundation for building LLM power
[03:49:06] agents that can think,
[03:49:09] reason, and act, not just chat. So,
[03:49:12] let's go to the implementation.
[03:49:18] So again I'm going to create a new
[03:49:20] folder
[03:49:22] folder 14 and then name it tools.
[03:49:26] Inside this I'm going to create a new
[03:49:29] file
[03:49:30] tools.py.
[03:49:33] So here uh first of all from langen core
[03:49:36] I'm going to import
[03:49:39] tools.
[03:49:44] So let's create a function here. So our
[03:49:46] function will simply be a diff multiply
[03:49:48] function
[03:49:50] uh
[03:49:52] def multiply a comma b
[03:49:57] and then uh this will result
[03:50:00] into a integer or I'll also define it in
[03:50:04] this way. So, a is supposed to be an
[03:50:05] integer. B is also supposed to be an
[03:50:07] integer. And then the product or
[03:50:11] whatever this does uh should return an
[03:50:14] integer here. So, a into b also make
[03:50:17] sure to include the dock string that
[03:50:19] actually defines what this function does
[03:50:22] because that is important here. So let
[03:50:25] me write multiply to numbers
[03:50:29] and then I incorporate this using the
[03:50:33] add tool decorator. Okay. Now this is
[03:50:36] not just a normal function but it is a
[03:50:38] langen
[03:50:40] tool function here. So now what I'm
[03:50:42] going to do is I'm going to invoke this
[03:50:45] multiply function.
[03:50:48] multiply dot invoke
[03:50:51] and then simply pass a = 3
[03:50:57] and then b = 5.
[03:51:01] So now
[03:51:03] uh also this should be passed within a
[03:51:06] within a curly brackets. So let me
[03:51:10] provide it in that way
[03:51:12] and then what I can do is I can print
[03:51:15] out the result. Now you can see that
[03:51:18] this particular tool will be invoked or
[03:51:22] or the tool will invoke the following uh
[03:51:24] values and then return our
[03:51:27] multiplication result here. So let me
[03:51:30] run this
[03:51:32] and it's pretty easy. 5 into 4 is equal
[03:51:34] to 20. So this is how you do it. You can
[03:51:38] also see uh the function name here. You
[03:51:44] can also see what the dock string in the
[03:51:47] function says
[03:51:50] dot do string uh or
[03:51:54] and then you can also see what arguments
[03:51:57] you need to pass inside this particular
[03:52:00] tool. So let me run this again and then
[03:52:02] you can see that the function name is
[03:52:05] multiply. You can also see this dock
[03:52:07] string uh for this second line here. And
[03:52:09] then the argument you need to pass is
[03:52:12] uh
[03:52:14] a val a variable a which needs to be an
[03:52:18] integer and variable b which also needs
[03:52:20] to be an integer.
[03:52:23] What you can also do is you can also see
[03:52:27] uh the argument schema in terms of JSON.
[03:52:31] So for that model
[03:52:34] JSON schema
[03:52:37] run this again
[03:52:40] and then you can see everything
[03:52:44] that we have talked about here in the
[03:52:46] form of our JSON schema. So this is just
[03:52:51] a basic introduction of using tool in
[03:52:56] lang. In the further videos, we'll
[03:52:58] explore how we can integrate this with
[03:53:00] LLM2. In the last video, we saw how the
[03:53:03] tool decorator helps turn a simple
[03:53:05] Python function into a callable AI tool,
[03:53:07] something our language model can
[03:53:08] recognize and use when reasoning. But
[03:53:11] what if we want more structure and
[03:53:13] control? What if we want to clearly
[03:53:15] define the input parameters, their
[03:53:16] types, and even attach risk rich uh
[03:53:21] detail for each, making the tool more
[03:53:24] transparent and reliable for the model
[03:53:26] to use. That's where the structure tool
[03:53:28] comes in. Structure tool takes the
[03:53:30] concept of tools a step further. It lets
[03:53:33] it
[03:53:35] wrap a function with a parentic model
[03:53:37] that defines exactly what inputs the
[03:53:40] tool expects. That means every parameter
[03:53:43] has a type, a detail, and validation
[03:53:45] rules, ensuring the LLM knows precisely
[03:53:47] how to use the tool. Think of it like
[03:53:50] giving the model a manual. Instead of
[03:53:52] saying, "Here's a function. Good luck
[03:53:54] figuring it out. You're saying here's a
[03:53:57] tool that multiplies two numbers. It
[03:53:59] require exactly two inteious A and B and
[03:54:02] here's what they represent. This
[03:54:04] structured approach becomes increas
[03:54:07] incredibly useful when you're working
[03:54:09] with multiple tools or building complex
[03:54:12] complex agent agents. It reduces
[03:54:15] ambiguity and helps the LM call your
[03:54:18] tools correctly every time. So in this
[03:54:20] video we'll explore how to define a
[03:54:22] structure tool using structure tool from
[03:54:25] function. How to specify input schemas
[03:54:27] using pyic and why this approach is
[03:54:30] considered the more scalable and
[03:54:32] professional way to build tools for
[03:54:33] lenses. So let's go to the
[03:54:35] implementation.
[03:54:39] So here I'm going to create a new file
[03:54:41] again
[03:54:43] and then call it structured
[03:54:46] tool.py.
[03:54:47] Pi
[03:54:51] here I will have langen
[03:54:54] from langen dot tools I'm going to
[03:54:57] import structure tool
[03:54:59] and then from pyic
[03:55:03] we're going to import base model
[03:55:06] and a field
[03:55:08] okay so
[03:55:11] I'll first define my parent class here
[03:55:14] so [snorts] multiply input
[03:55:17] This will import base model here and
[03:55:19] then I'll have two parameters a it will
[03:55:22] be an integer. I can write a field for
[03:55:25] this one and then details of this
[03:55:27] particular field. So description
[03:55:31] equals to the first
[03:55:35] number to multiply.
[03:55:38] Uh I'll also say this is a required
[03:55:41] value. So required equals to true. And
[03:55:45] then similarly I'll have the second
[03:55:48] number here.
[03:55:50] Uh let me call this second number to
[03:55:54] multiply
[03:55:56] and then write B here.
[03:56:00] Now
[03:56:02] what I can do is I can define the
[03:56:04] multiply function. Multiply function. A
[03:56:07] will accept an integer. B will also
[03:56:09] accept an integer.
[03:56:11] And then we'll also return the integer.
[03:56:14] So I will return A into B.
[03:56:18] I'll define my multiply tool using the
[03:56:20] structure tool function dot from
[03:56:24] function.
[03:56:26] Uh and inside this I'm going to write my
[03:56:30] function name which is multiply
[03:56:32] function. Then I'm going to provide a
[03:56:34] name to this which is multiply.
[03:56:38] Then I'm going to write a dock string
[03:56:40] for this. So multiplies
[03:56:44] to numbers and then provide the argument
[03:56:49] schema and then argument schema is based
[03:56:51] on the P multiply that we have which is
[03:56:53] multiply input. Okay. Now after this
[03:56:56] what I can do is I can invoke this
[03:56:58] structure tool multiply
[03:57:02] tool dot invoke then I can pass in the
[03:57:06] two values. Let's call a = 5 and b can
[03:57:11] be passed as four and from this I can
[03:57:15] print out my result
[03:57:19] and then run this again.
[03:57:21] So in our previous video what we had
[03:57:23] done is we had uh used the tool
[03:57:29] decorator to define the the tool
[03:57:33] function but in this case we've defined
[03:57:34] a py class for validation too and then
[03:57:38] uh we have used structure tool to invoke
[03:57:41] this particular function here which
[03:57:43] follows the validation rules provided
[03:57:46] provided in the spiral class. So I hope
[03:57:48] you understood the concept and then the
[03:57:50] major uh difference between tool and
[03:57:53] structured tool in line chain. So far
[03:57:56] we've talked about how to create
[03:57:57] individual tools simple functions that
[03:58:00] can that an AI model can understand,
[03:58:02] interpret and use. But in real world
[03:58:05] application we rarely rely on just one
[03:58:07] tool. Think about it an AI assistant
[03:58:10] might need to add numbers, search the
[03:58:12] web, analyze text or fetch data from a
[03:58:14] database. Each of these capabilities is
[03:58:16] a separate tool.
[03:58:18] And when you have several of them, it
[03:58:20] makes sense to group them inside a
[03:58:22] toolkit. So a toolkit in langen is
[03:58:25] simply a collection of related tools
[03:58:27] bundled together, usually around a
[03:58:29] specific purpose. For example, you might
[03:58:31] have a Mac toolkit for arithmetic
[03:58:33] operation or database toolkit for
[03:58:35] interacting with SQL or MongoDB or a web
[03:58:37] toolkit for scraping and browsing data.
[03:58:40] Toolkits make your code modular and
[03:58:42] organized. Instead of handling each tool
[03:58:45] individually, you can register, manage
[03:58:48] or pass around entire group of tools as
[03:58:51] a single unit, especially when
[03:58:52] integrating them with agents. It's like
[03:58:54] giving your AI or toolbox instead of
[03:58:57] just one range. Now it can pick the
[03:58:59] right tool for the right job. In this
[03:59:01] video, we'll explore how to define a
[03:59:03] simple toolkit in Langen, how to group
[03:59:06] multiple tools inside it, and how this
[03:59:08] concept becomes the foundation for
[03:59:09] building intelligent multiskilled AI
[03:59:12] agents that can reason and act
[03:59:14] automatically or dynamically. So, let's
[03:59:17] move to the code.
[03:59:19] So, I'm going to create a new file here
[03:59:22] called
[03:59:24] toolkit.py.
[03:59:28] And inside this I'm again going to
[03:59:30] import tools
[03:59:32] langen_core
[03:59:35] dot tools import
[03:59:38] tool and then in a decorator what I'm
[03:59:42] going to do is I'm going to create two
[03:59:43] tools here. So one will be for addition
[03:59:48] uh which will contain two parameter and
[03:59:50] integer b will also be an integer
[03:59:54] and then it will also return an integer
[03:59:56] here. So return a + b. I want to include
[04:00:00] something in the dock string to here and
[04:00:03] and this will say add two numbers.
[04:00:06] Similarly I have I'll have another tool
[04:00:10] uh for multiply and then it will also
[04:00:12] take in two numbers integer b is also
[04:00:16] integer and then it will reply or return
[04:00:20] an integer itself. dock string says
[04:00:23] multiply to numbers
[04:00:27] and then it will do return a into b.
[04:00:32] Okay. So I have multiple tools
[04:00:34] implementation here. So what I'm going
[04:00:36] to do is I'm going to define a toolkit
[04:00:38] here called Mac toolkit
[04:00:41] and then uh inside this
[04:00:44] I'll have a get tools function
[04:00:51] uh which will contain a self keyword and
[04:00:54] it will return add and then
[04:00:57] [clears throat] multiplication
[04:00:59] here
[04:01:05] a tool here.
[04:01:08] Okay.
[04:01:09] Then what I'm going to do is I'm going
[04:01:11] to create a toolkit object of this map
[04:01:15] toolkit class.
[04:01:17] And then inside this I'm going to get my
[04:01:21] two different uh tools using this
[04:01:24] toolkit. So get tools
[04:01:27] and then I'm I'm going to print each and
[04:01:29] every tools here. So ptl in tools
[04:01:33] let's print out the name of the tool. So
[04:01:36] PL dot name
[04:01:38] and then what we'll do is
[04:01:41] we'll also print out the detail of this
[04:01:42] tool.
[04:01:46] So TL
[04:01:48] and then the detail will be TL dot
[04:01:51] description.
[04:01:54] So if you run this, you'll see that we
[04:01:56] have bound these two different tools.
[04:01:58] Okay, something's wrong here. Let me
[04:02:01] check what I've
[04:02:04] what I've done. Uh
[04:02:09] so I've defined a class.
[04:02:17] I've also defined an object
[04:02:20] or the matt class. Okay, the object
[04:02:24] definition is wrong here. So, let me run
[04:02:26] this again. And then using
[04:02:28] [clears throat] this toolkit class, uh I
[04:02:31] can get a list of all available tools
[04:02:34] that I have. So, I have two tools here.
[04:02:37] One is for add and then the other is for
[04:02:39] multiply. So if I need to add one more
[04:02:42] tool here, let's add one more tool
[04:02:45] uh called sub which will take in a and b
[04:02:51] both are inteious for now. It will also
[04:02:55] return an integer and I'll include a
[04:02:58] dock string subtract two numbers and
[04:03:02] inside this I'll return a minus b
[04:03:05] and then I'll also include this tool
[04:03:07] here for sub. Then again the toolkit
[04:03:10] wraps all of my tools and then uh it
[04:03:13] gives me a choice
[04:03:17] choice choice to choose one among all of
[04:03:19] these tools here. So this is how you
[04:03:21] implement toolkit. So I'm ending this
[04:03:23] video right now. I hope you understood
[04:03:25] the concept. We'll further work on tools
[04:03:27] and then integrate it with LLMs in the
[04:03:29] upcoming video. Up until now we've seen
[04:03:32] how tools can be created and grouped
[04:03:34] into toolkits. But what if we want our
[04:03:36] AI model to actively use those tools
[04:03:39] during conversation? That's where tool
[04:03:41] binding comes in. So toolbinding is the
[04:03:43] process of connecting your AI model
[04:03:45] directly with one or more tools. So the
[04:03:48] model can recognize when a tool should
[04:03:50] be used and even suggest calling it with
[04:03:52] the right parameters.
[04:03:54] Essentially the model becomes aware of
[04:03:56] the tools at
[04:04:03] essentially the model becomes aware of
[04:04:05] the tools it has. So this is a critical
[04:04:08] step towards agent AI because now the AI
[04:04:10] isn't just generating text it can reason
[04:04:13] about actions and leverage external
[04:04:15] functionality to get things done. So for
[04:04:17] example, instead of manually calculating
[04:04:19] a sum or quering a database, the AI can
[04:04:22] now identify the need, prepare the
[04:04:24] inputs and suggest invoking the relevant
[04:04:26] tool. It's important to note that in
[04:04:29] this setup, the model itself doesn't
[04:04:31] execute the tool. It only proposes a
[04:04:34] tool call complete with arguments. The
[04:04:36] actual extension is handled
[04:04:38] programmatically giving uh developers
[04:04:40] control over safety, validation, and
[04:04:42] workflow. So in this video we'll focus
[04:04:45] on binding a tool to our LM seeing how
[04:04:48] the model suggest tool usage and then
[04:04:50] executing the tools action based on the
[04:04:51] model suggestion. This is going to be a
[04:04:54] crucial step toward creating intelligent
[04:04:56] agent that can work or that can do task
[04:05:01] beyond just generating text. So let's go
[04:05:04] for the implementation.
[04:05:10] So here I'm going to create a new file
[04:05:13] called a toolbinding.py.
[04:05:17] Let's import tool. So from langen
[04:05:20] core
[04:05:23] lang core dot tools import tool. Okay.
[04:05:27] What else do I need? Uh we'll import our
[04:05:30] model. So from langen Google geni import
[04:05:35] uh chat Google generative AI. And then
[04:05:38] I'm going to load my credential from env
[04:05:41] import
[04:05:43] load env. So let me first load my
[04:05:46] credential. Let me then load my model.
[04:05:50] My model name is uh Gemini
[04:05:56] 2.5/model.
[04:06:00] Let me create a tool here. So, so my
[04:06:03] first tool
[04:06:05] here is add
[04:06:08] which will take in two numbers a and b
[04:06:11] both will be integers and it will also
[04:06:13] return an integer value. I'll add a
[04:06:16] docking to this. So add two numbers
[04:06:22] and then uh I will return
[04:06:26] a + b.
[04:06:30] Okay. So this is done. Uh the tool
[04:06:32] import I think is wrong. So it should be
[04:06:34] small to do tool. Uh
[04:06:37] what else? Okay, we just one tool. We'll
[04:06:40] try to bind this with lm. Okay, so lmm
[04:06:42] with tools
[04:06:44] equals to uh model dot
[04:06:49] bind tools. And then I'm going to bind
[04:06:52] my uh tool into this. Uh so
[04:06:58] we can see uh invoking a query with this
[04:07:02] particular uh LLM which contains tools
[04:07:06] here. So let's invoke this uh and then
[04:07:08] uh we'll say can you
[04:07:12] add three with 14
[04:07:16] and then basically see the
[04:07:20] result here or uh what I can do is we'll
[04:07:23] first print out the result and then
[04:07:25] we'll see it accordingly.
[04:07:27] So if we print out the result then the
[04:07:31] model will not itself start doing a
[04:07:33] computation but it will look at this
[04:07:35] particular query and then uh and then
[04:07:39] the dock string and then based on the
[04:07:41] similar doc string with the query it
[04:07:43] will understand that now this tool needs
[04:07:45] to be called. Okay let's run this and
[04:07:47] then you'll get a clear picture of what
[04:07:49] I'm trying to say here. So if we run
[04:07:51] this
[04:07:59] so as you can see uh the content is
[04:08:03] actually not an exact answer but it is a
[04:08:07] tool call here or a function call. So it
[04:08:09] says function call and then and then the
[04:08:12] function name here is add. The arguments
[04:08:14] are a and b and then and then three and
[04:08:18] 14 are passed to a and b here. And then
[04:08:21] uh what the model is suggesting is it is
[04:08:25] suggesting me to call this particular
[04:08:27] function or call this tool to perform
[04:08:30] the task that is mentioned in the query
[04:08:32] instead of the model doing the
[04:08:34] computation itself here. So this is how
[04:08:37] we bind the tools and then the model
[04:08:40] like I said earlier the model does not
[04:08:42] itself call the tool but it's
[04:08:45] but it actually provides you the
[04:08:47] suggestion uh suggestion to the user
[04:08:50] that this particular tool uh can be
[04:08:53] called to perform this particular task
[04:08:55] that is asked to do here. Up until the
[04:08:58] previous video, we explored tool binding
[04:09:00] where the AI could suggest using a tool,
[04:09:03] but it didn't actually execute it.
[04:09:05] That's a big step towards agentic
[04:09:07] behavior, but it still required a human
[04:09:08] or programmatic step to run the tool. In
[04:09:11] this video, we're taking it one step
[04:09:13] further. We're going to enforce the
[04:09:15] model to actually perform the tool
[04:09:17] operation as part of the workflow. This
[04:09:19] means the AI isn't just suggesting. It
[04:09:21] can now actively interact with tools,
[04:09:23] gather results and continue reasoning
[04:09:26] based on those results. The process
[04:09:28] works like a conversation flow. First,
[04:09:30] the user provides a query. The model
[04:09:33] aware of the tools,
[04:09:35] chooses which tool to call and then
[04:09:38] prepares the arguments. Next, we execute
[04:09:41] the suggested tool call
[04:09:43] programmatically. And finally, the model
[04:09:46] gets the tools output and integrates it
[04:09:48] into its response, allowing it to
[04:09:51] continue the dialogue seamlessly with
[04:09:53] real results. This approach is critical
[04:09:55] for building truly intelligent agents,
[04:09:57] one that just doesn't answer questions,
[04:10:00] but can perform task or compute results
[04:10:02] or fetch data dynamically. So, in this
[04:10:04] video, our focus will be on implementing
[04:10:06] this inforce tool execution workflow.
[04:10:08] The model identifies the tool, we run
[04:10:10] it, and then the AI incorporates the
[04:10:12] output back into the conversation,
[04:10:14] making the interaction fully functional
[04:10:16] and autonomous. So let's dive into the
[04:10:18] code.
[04:10:23] So here I'm going to create a new file
[04:10:25] again
[04:10:27] call it final tool
[04:10:31] calling.py.
[04:10:35] Let me import few libraries here. So
[04:10:37] from langen core dot tools I'll import
[04:10:42] tool
[04:10:44] then from langen core dot messages I'll
[04:10:49] import human message
[04:10:52] then I'll import my model
[04:10:57] and after that I will uh import
[04:11:04] okay Now
[04:11:07] I'll import the credential. Then I'll
[04:11:09] define my model
[04:11:19] chat Google
[04:11:21] generative AI. So the model name is
[04:11:23] Gemini 2.5.
[04:11:28] And then I'm going to create a tool for
[04:11:30] basically addition like we did in the
[04:11:32] earlier video. So def add a is going to
[04:11:36] be an integer. B is also going to be an
[04:11:37] integer
[04:11:40] and I will return the result as integer.
[04:11:42] I'll add a dock string add two
[04:11:46] numbers
[04:11:48] and then based on this I'm going to
[04:11:49] return a + b.
[04:11:53] Now I'll bind this tool. So, llm with
[04:11:58] tools equals to llm llm
[04:12:02] dot
[04:12:04] bind tools and I'm going to bind my add
[04:12:09] function tool here. My user query is
[04:12:13] going to be in u uh add
[04:12:19] 10 and 9.
[04:12:23] Okay. And then I'm going to convert this
[04:12:26] into human message.
[04:12:29] So my query is a human message.
[04:12:31] So we'll append this in our message
[04:12:36] list. Our query now
[04:12:39] and then we'll uh print our
[04:12:43] result. basically call
[04:12:46] uh call the LLM using our
[04:12:51] messages and then print out the result.
[04:12:54] We'll see the result what happens here.
[04:12:57] Okay. Okay. So if you run this,
[04:13:05] you'll see that it does suggest a uh
[04:13:08] function call here uh for add to
[04:13:12] basically solve my query. So what I'm
[04:13:14] going to do here is
[04:13:19] uh I'm going to append this to my my
[04:13:23] messages. So messages dot append it will
[04:13:29] go inside here also I want to print
[04:13:31] something here. So let me print out
[04:13:33] result dot tool calls. I think we have
[04:13:36] tool calls here. Yeah we have tool calls
[04:13:39] here. So tool call and then we'll invoke
[04:13:42] our first tool call and see what it
[04:13:45] gives me. So let me run this again.
[04:13:55] So if we print tool call then we can see
[04:13:58] that this particular tool is reference
[04:14:02] or the add tool is reference. My values
[04:14:05] are correctly gone to a and bp.
[04:14:08] So now what I'm going to do is I'm again
[04:14:10] going to remove this and then I'm going
[04:14:12] to invoke the tool add dot invoke
[04:14:17] result dot tool call zero.
[04:14:23] Then after this I'm going to append
[04:14:25] append the tool result also inside my
[04:14:30] messages and then the final result will
[04:14:33] be the llm call again dot invoke and
[04:14:37] then I'll print my final
[04:14:41] result here. So print final result.
[04:14:47] So let me clear this and then run this
[04:14:49] again and see what happens.
[04:14:57] Okay, as you can see the sum of 10 and 9
[04:15:01] is 19. The content is
[04:15:04] generated. If you only want to see the
[04:15:06] content then you can see that the
[04:15:09] content is shown.
[04:15:17] Okay. So what we did here is we did in
[04:15:19] fact invoke the invoke the tool but we
[04:15:24] did it by ourselves. So basically we
[04:15:26] took the model suggestion of invoking
[04:15:29] the add tool. We invoke the add tool and
[04:15:32] then basically uh regenerated our
[04:15:36] response based on our query year. Uh
[04:15:39] that's not actually uh what we want but
[04:15:42] I actually wanted to show you how to
[04:15:44] call the tool here. In the upcoming
[04:15:46] video we will fix this and then we will
[04:15:48] let the model uh suggest the tool as
[04:15:51] well as call the tool automatically
[04:15:53] here. So I think I uh you understood the
[04:15:55] concept. In our previous videos we
[04:15:58] explored how an LLM can suggest tools
[04:16:00] and how we can execute those tools
[04:16:02] manually. But what if we want the model
[04:16:05] to actually carry out a multi-step
[04:16:07] workflow, handle immediate results and
[04:16:09] inject critical information into
[04:16:11] subsequent tool calls automatically. And
[04:16:13] that's where the concept of injected
[04:16:14] tools comes in and it's what we're
[04:16:17] exploring in this video. So imagine the
[04:16:20] LLM as a helpful assistant with access
[04:16:23] to a set of tools like a calculator or a
[04:16:25] currency converter. When you ask it a
[04:16:27] question, it might realize that to
[04:16:30] answer fully, it needs to use more than
[04:16:32] one tool in a sequence. For example, if
[04:16:34] you ask like what is the conversion
[04:16:36] factor between USD and NPR and based on
[04:16:39] that can you convert
[04:16:41] 10 USD to NPR? The assistant first needs
[04:16:44] to fetch the conversion rate and then
[04:16:46] apply that rate to the value you want to
[04:16:48] convert. The magic happens through
[04:16:50] injected tools arguments.
[04:16:53] Uh this tool
[04:16:55] allows the LLM to recognize that some
[04:16:57] tools require additional input like the
[04:17:00] conversion rate for this case which
[04:17:02] might not be explicitly provided by the
[04:17:04] user but is generated by a previous tool
[04:17:07] call. Essentially it allows the LLM to
[04:17:09] remember and pass context between tool
[04:17:12] executions automatically. And here's how
[04:17:14] the workflow unfolds. First of all we
[04:17:16] start with the LM call. So we send the
[04:17:19] users query to the LLM bound with tools.
[04:17:21] The LLM analyzes the query and chooses
[04:17:25] which tools need to be executed. For
[04:17:27] instance, it first calls the get
[04:17:29] conversion factor tool and then plans to
[04:17:32] call the convert tool. The second is a
[04:17:34] multi-turn tool execution loop. Here the
[04:17:38] code then executes each suggested tool.
[04:17:40] When the LM calls convert, it might not
[04:17:43] know the exact conversion rate yet. This
[04:17:46] is where the injected argument comes
[04:17:47] into play.
[04:17:49] uh the program automatically injects the
[04:17:51] conversion rate obtained from the
[04:17:53] previous tool call ensuring the tool has
[04:17:55] all the information it needs and the
[04:17:57] final is the feedback or feeding results
[04:18:01] back to the LLM. So after each tool
[04:18:03] execution the result is packaged into a
[04:18:05] tool message and then sent back to the
[04:18:07] LLM. The LLM then uses these output to
[04:18:11] uh generate the upcoming step or
[04:18:15] finalize its response. The loop
[04:18:19] continues until LLM produces a final
[04:18:21] human readable answer in the content
[04:18:23] field. So this approach is powerful
[04:18:25] because it transforms the LLM from a
[04:18:27] simple chat model into a true agentic
[04:18:29] system. It can now plan, execute and
[04:18:32] chain multiple operations together while
[04:18:34] intelligently handling uh dependencies
[04:18:36] between them. So in this video we will
[04:18:38] walk through a live implementation of
[04:18:42] this workflow. We'll see the LLM first
[04:18:46] retrieve the conversion rate and then
[04:18:48] use it to convert a currency amount and
[04:18:50] finally produce a complete readable
[04:18:54] answer for the user all automatically.
[04:18:56] So this pattern is not only limited to
[04:18:59] uh
[04:19:00] currency conversion. It's a blueprint
[04:19:02] for like building multi-step AI agents
[04:19:05] that can handle complex task with
[04:19:07] multiple tools and dependencies. Now
[04:19:10] let's move on to the implementation.
[04:19:17] So I'm going to create a new file here.
[04:19:20] Call it test
[04:19:24] multiple
[04:19:27] uh tool call.py.
[04:19:33] Okay. So inside this first of all the
[04:19:35] imports
[04:19:46] first import tool.
[04:19:49] After that import
[04:19:52] tool message as well as event message
[04:20:03] then load the model
[04:20:12] then env
[04:20:16] here from inside lang line to lend code
[04:20:20] dot tools I'm also going to in add
[04:20:24] injected tool ar
[04:20:27] and then uh last one from typing I'm
[04:20:30] going to import annotated
[04:20:33] okay so first of all load the
[04:20:34] credentials
[04:20:36] then I'm going to define a tool here
[04:20:39] so this tool will be get conversion rate
[04:20:46] it will contain two strings So one is
[04:20:49] base currency.
[04:20:51] It is it will be a string and then the
[04:20:54] other is target currency.
[04:20:57] It also be a string
[04:20:59] and then it will basically return our
[04:21:02] float value.
[04:21:03] So write something in the dock string.
[04:21:06] Return the realtime currency
[04:21:11] conversion
[04:21:13] uh conversion rate from base currency to
[04:21:18] target
[04:21:20] to target currency
[04:21:25] using some API.
[04:21:28] And here I'm actually not going to call
[04:21:30] the API but I'm directly going to use
[04:21:32] this uh static conversion rate. Let's
[04:21:35] say 140.3.
[04:21:39] Okay. And then I'm going to return this
[04:21:41] conversion rate from this tool.
[04:21:44] Next I'm going to create another another
[04:21:46] tool here
[04:21:49] uh that is going to be named as convert.
[04:21:53] Here I will have a base currency value
[04:21:58] which will be in float
[04:22:01] and then I'll have a conversion rate
[04:22:05] conversion rate uh which will also be in
[04:22:08] float but it will be annotated and then
[04:22:15] float and injected tool arc. Basically
[04:22:19] first of all uh the value will come from
[04:22:22] the other tool to this particular tool
[04:22:24] here and then it will also return a
[04:22:26] float value.
[04:22:31] to write a dock string
[04:22:34] converts a base currency
[04:22:38] value into
[04:22:40] target currency value
[04:22:44] using
[04:22:49] a
[04:22:52] conversion rate. Okay. So
[04:22:56] this is going to return
[04:22:58] base currency value into
[04:23:01] conversion rate. Now we will set up llm.
[04:23:05] Uh so lm equal to chat Google generative
[04:23:08] AI.
[04:23:10] The model is going to be Gemini
[04:23:13] 2.5/model.
[04:23:18] Then what I'm going to do is I'm going
[04:23:19] to bind these tools. So lm
[04:23:22] with
[04:23:24] with tools equals to lm dot
[04:23:31] by tools.
[04:23:33] The first tool is get conversion rate
[04:23:35] and then this and then the second tool
[04:23:36] is convert. Now I'm going to pass in my
[04:23:39] query. So my query is going to be what
[04:23:43] is the
[04:23:45] conversion factor between
[04:23:48] USD and NPR and based on it
[04:23:54] then you convert
[04:23:56] 10 USD to NPR.
[04:24:03] Okay. So this is going to be my query
[04:24:05] here.
[04:24:08] Now what I'm going to do is I'm going to
[04:24:10] include this query as a human message.
[04:24:14] Human message
[04:24:16] with the content is going to be query
[04:24:19] and I'm going to wrap up wrap this up in
[04:24:22] a list itself.
[04:24:25] Okay. So let me invoke the tool and then
[04:24:29] get the AI message from this. So, lmm
[04:24:32] with tools dot invoke
[04:24:35] uh messages and then whatever I get I'm
[04:24:38] going to append it in the messages
[04:24:42] itself. So, append AI message.
[04:24:47] Okay. Now in step two we go for
[04:24:50] multi-turn toolation loop. So while uh
[04:24:56] AI AI message
[04:24:59] dot content
[04:25:02] equals to an empty string and AI dot AI
[04:25:08] message
[04:25:10] uh dot tool calls
[04:25:14] tool calls.
[04:25:17] So if something is present in the tool
[04:25:19] calls what I'm going to do is
[04:25:22] I am going to create a list of tool
[04:25:24] message
[04:25:27] tool messages
[04:25:29] and then based on this I'm going to
[04:25:31] execute all suggested tool. So for tool
[04:25:35] call in AI dot sorry AI message dot tool
[04:25:42] calls uh [snorts]
[04:25:44] I'll first call in the tool name which
[04:25:47] is going to come from tool call
[04:25:52] name.
[04:25:54] I will also try to get its ID. So tool
[04:25:58] id equals to tool call
[04:26:02] id and then I'll get the arguments. So
[04:26:05] tool arcs equals to tool call
[04:26:10] uh
[04:26:12] tool call and then ars here. Okay. So
[04:26:16] let me print
[04:26:19] every tool that I've got. So executing
[04:26:25] executing tool
[04:26:29] and
[04:26:31] here will be my tool name.
[04:26:36] Tool name will be arcs
[04:26:38] and then here will be my tools.
[04:26:41] So this will be made as an f string
[04:26:44] here.
[04:26:46] Okay, this will be
[04:26:49] or I can just do this and then this is
[04:26:52] going to be my string.
[04:26:56] So now if the tool name is equals to
[04:27:02] get
[04:27:04] conversion rate
[04:27:08] then I'll invoke that function here dot
[04:27:11] invoke
[04:27:15] or invoke that tool and then I'll get
[04:27:18] the tool output
[04:27:21] in the form of a string.
[04:27:25] and then that will be my conversion
[04:27:27] rate.
[04:27:32] So else uh if the tool name
[04:27:36] is equals to convert.
[04:27:42] So if the tool name is directly convert
[04:27:44] then what we need to do is we need to uh
[04:27:49] first inject the conversion rate from
[04:27:52] the previous result step. So if uh
[04:27:56] conversion
[04:27:57] rate
[04:27:59] not in tool arcs
[04:28:04] ensure the conversion rate is actually
[04:28:06] uh
[04:28:08] defined from the get conversion factor
[04:28:10] runs. So if
[04:28:12] uh
[04:28:16] conversion rate
[04:28:18] not in locals
[04:28:24] or
[04:28:26] our conversion rate is none.
[04:28:31] Then what we need to do is we need to
[04:28:34] raise a value error
[04:28:36] uh saying that
[04:28:39] conversion rate is required
[04:28:43] but it is not found.
[04:28:48] else what we need to do we need to get
[04:28:51] the conversion rate from tool arcs
[04:28:55] conversion rate equal to conversion rate
[04:29:05] and then based on this I need to execute
[04:29:07] my tools so converted value equals to
[04:29:11] convert
[04:29:13] dot invoke
[04:29:15] to larks
[04:29:17] and then to log output
[04:29:21] can be converted to a string value using
[04:29:26] str function.
[04:29:28] Okay, if none of this is possible,
[04:29:32] we'll do tool output equals to
[04:29:37] unknown
[04:29:41] unknown tool and then we will say tool
[04:29:44] name
[04:29:48] Okay, most of our work is done. Uh what
[04:29:51] we need to do is now we need to since
[04:29:54] every condition returns a tool message
[04:29:56] to us. So what we're going to do is
[04:29:59] we're going to create a tool message. It
[04:30:02] will be wrapped inside this tool message
[04:30:05] here. The content
[04:30:07] is going to be tool output
[04:30:11] tool output. And then the tool called
[04:30:15] id
[04:30:18] ID will come from the tool ID
[04:30:22] and I'm going to append uh tool messages
[04:30:26] dot append
[04:30:28] tool message
[04:30:32] tool msg
[04:30:35] and then and then now
[04:30:39] I'm going to append everything to our to
[04:30:43] our messages here. So still I means I I
[04:30:46] am supposed to be inside this loop here.
[04:30:49] Uh okay. I think I think I did some
[04:30:52] mistake here. So this has to go inside
[04:30:55] the Y loop
[04:31:02] inside uh inside the Y loop. And then
[04:31:05] now what I'm going to do is I'm going to
[04:31:08] messages extend.
[04:31:11] You can use anything to messages.
[04:31:16] Then I'll again prompt for AI message
[04:31:18] and then invoke the model
[04:31:22] with with a updated
[04:31:25] messages and then I'm again going to
[04:31:28] append it
[04:31:31] in my AI message. Okay. So finally
[04:31:38] we have we already should have obtained
[04:31:40] our result inside this particular part
[04:31:43] here. So what I'm going to do is I'm
[04:31:45] going to take out the last result. So
[04:31:47] messages minus one
[04:31:53] minus one and then I'm going to print
[04:31:55] the final result dot content. So let's
[04:31:59] see my query is what is the conversion
[04:32:02] factor between USD and NPR and based on
[04:32:03] it can you convert it from 10 USD to
[04:32:05] NPR. So if you run this
[04:32:11] let's see what happens.
[04:32:14] So the model is called
[04:32:17] the model is initialized.
[04:32:24] uh so okay uh the conversion rate
[04:32:27] between USD and NPR is [clears throat]
[04:32:29] 140.3 this is done using this get
[04:32:32] conversion rate tool and then from that
[04:32:35] after that we call this convert tool uh
[04:32:38] with the base currency value of 10 and
[04:32:40] then the exchange rate or conversion
[04:32:42] rate of uh 140.3 and then 10 USD is
[04:32:46] equivalent to 1403 NPR so this is the
[04:32:50] result so here we've not only uh like
[04:32:54] integrated multiple LLMs into it into
[04:32:58] sorry multiple tools into an LLM but
[04:33:00] we've also uh used this concept of
[04:33:03] injected tool where the result of the
[04:33:07] previous tool will be the input for the
[04:33:10] upcoming tool. So I hope you understand
[04:33:12] the concept of injected tool uh and then
[04:33:16] you had fun implementing this particular
[04:33:18] code here. If you have any problem, do
[04:33:21] comment down below and I'll try to help
[04:33:22] you out. And in the
[04:33:27] next few videos, we're going to see AI
[04:33:30] agents demo using Langen. So, we are
[04:33:33] almost at the end of this Langen series
[04:33:36] here. Hello everyone and welcome back to
[04:33:39] the channel. So far, we've done our
[04:33:42] Langen series. If you haven't watched
[04:33:44] that, I'll put a playlist link down
[04:33:47] below and then you can check it out. And
[04:33:49] in that language series, we've learned
[04:33:51] how to build LLM powered applications
[04:33:53] step by step. We have explored chains,
[04:33:57] agents, retrievers, and even tool
[04:33:59] execution.
[04:34:01] We saw how Langen helps us connect large
[04:34:03] language models with external data
[04:34:05] sources, APIs, and other tools. But as
[04:34:09] we started building more complex
[04:34:11] systems, you might have noticed
[04:34:12] something missing. Langen is actually
[04:34:15] great for creating individual component.
[04:34:17] But when you try to build multi-step
[04:34:19] workflows or systems where an LLM needs
[04:34:22] to make choices dynamically, things
[04:34:24] start getting a bit messy. You have to
[04:34:27] manage the controls for manually, handle
[04:34:30] intermediate steps, and sometimes even
[04:34:33] patch the logic together with eels
[04:34:34] conditions. It works, but it's not
[04:34:37] scalable and it's definitely not
[04:34:40] elegant. So that's exactly where Lang
[04:34:43] graph comes in. Lang graph takes
[04:34:46] everything we've learned from Langen and
[04:34:47] gives it a structure. It lets us
[04:34:50] represent our LLM workflows as a graph
[04:34:52] with nodes for actions and edges for
[04:34:55] choices parts. In simple terms, it's
[04:34:58] like giving our agent a map to follow.
[04:35:00] So it knows what to do, when to do it,
[04:35:03] and how to handle intermediate results.
[04:35:05] With Langraph, we can build stateful,
[04:35:08] reliable and controllable AI systems
[04:35:10] where every step is transparent and the
[04:35:13] workflow is easy to debug, modify or
[04:35:16] extend.
[04:35:18] So if Langen was all about learning the
[04:35:21] tools, Langraph is about learning how to
[04:35:23] orchestrate them intelligently. And
[04:35:25] that's exactly what we're going to do
[04:35:27] next. We're starting a brand new series
[04:35:29] on Lang Graph where we'll go from the
[04:35:32] basics all the way up to building
[04:35:34] advanced multi-step aentic workflows. So
[04:35:36] get ready because if you love what
[04:35:38] Langen could do, Langraph is going to
[04:35:41] take things to a whole new level. So
[04:35:43] let's get started. In the last video, we
[04:35:46] talked about why we're moving from
[04:35:47] Langen to Langraph. And today we're
[04:35:49] taking our very first step into it.
[04:35:52] So imagine you have a chatbot that takes
[04:35:55] some input, let's say a name, and then
[04:35:58] it needs to process that information
[04:35:59] step by step
[04:36:02] before giving a response. So in line
[04:36:05] chain, we probably just call a function
[04:36:08] or a chain directly. But in langraph, we
[04:36:11] think differently. We treat our program
[04:36:13] as a graph, a flow of states moving
[04:36:16] through connected nodes. Each node
[04:36:18] represents a specific action or step and
[04:36:21] the state carries data as it moves
[04:36:23] through those steps.
[04:36:26] In the example that we'll be doing, our
[04:36:28] state is just a collection that holds a
[04:36:32] single key, which is messages. Think of
[04:36:35] it as a small memory that keeps track of
[04:36:37] whatever our chatbot knows at the
[04:36:39] moment. Then we we will define a node. A
[04:36:42] simple function that takes this state,
[04:36:44] modifies it by adding a friendly
[04:36:46] greeting and then returns the updated
[04:36:48] state. That's all a node does. It only
[04:36:51] transforms data. Next, the graph
[04:36:53] connects the dots. So we say when the
[04:36:56] process starts, go to this node, execute
[04:36:58] it and then end the process. It's like
[04:37:00] drawing a mini flowchart. Start then do
[04:37:03] something and then end. So when we run
[04:37:05] it, Lang graph automatically handles the
[04:37:07] execution. It passes the state through
[04:37:09] the node, updates it, and gives us the
[04:37:12] final result. The output you see isn't
[04:37:14] just a printed message. It's the outcome
[04:37:17] of data flowing through structured
[04:37:18] logical graph. And that's the beauty of
[04:37:21] Lang Graph. You're not just writing code
[04:37:24] anymore. You're designing a process. A
[04:37:26] process that's visual, controllable, and
[04:37:29] scalable. So in the upcoming videos
[04:37:31] we'll slowly build on this foundation
[04:37:33] adding more nodes and more edges and
[04:37:35] eventually intelligent choice making to
[04:37:38] our graph. So stick around because this
[04:37:41] simple example is just the beginning of
[04:37:43] how langraph turns logic into flow. So
[04:37:45] let's go to the example now.
[04:37:48] So I'll be creating a new folder here
[04:37:51] and then I'll call it lang graph
[04:37:54] and then inside this uh I'll create my
[04:37:57] first file. So basic [snorts] uh
[04:38:02] graph dot ip nb will this we'll do this
[04:38:07] in the notebook format here.
[04:38:10] Okay. So first of all I need to install
[04:38:12] lang graph here. So lang graph
[04:38:16] let me run this
[04:38:24] and then once line graph line graph is
[04:38:27] installed we're ready to build our first
[04:38:29] graph here. So from typing
[04:38:32] import typed dict
[04:38:36] uh and dicict dict we'll run this and
[04:38:39] then select the interpreter here python
[04:38:41] environments and then our recommended
[04:38:43] interpreter is this one. So as you can
[04:38:46] see it can run the interpreter. Okay I
[04:38:48] would also like to
[04:38:50] uh import from langraph.graph graph
[04:38:54] import
[04:38:56] state graph start and then end.
[04:39:00] Okay, this is going to be our first
[04:39:02] import here. Okay, our first cell is
[04:39:05] running. Now I'd like to create a class
[04:39:08] called my message state which will uh
[04:39:13] have a type text as inside it. So inside
[04:39:17] this I'll have a simple message
[04:39:21] that will be in the string format.
[04:39:24] Then after this
[04:39:27] what I'm going to do is I'm now going to
[04:39:29] define my graph directly here. So my
[04:39:33] graph will be from state graph
[04:39:38] and then inside this I'm going to pass
[04:39:40] my class that I've just created.
[04:39:43] So I'll add nodes to this graph. The
[04:39:46] first node will be uh we need to provide
[04:39:50] a string name to this. Let's say initial
[04:39:53] and then provide a function here. So
[04:39:55] greeting node. Okay. So this particular
[04:39:59] function needs to be implemented on top
[04:40:01] of this. Let's write down this function
[04:40:03] greeting node. This is always going to
[04:40:07] have this parameter
[04:40:09] of this class that I've just created.
[04:40:12] And then it is going to return the same
[04:40:15] class that
[04:40:18] we have now. Okay. What does this do?
[04:40:21] This is a simple node
[04:40:24] that adds a greeting
[04:40:27] message
[04:40:29] to the state.
[04:40:32] Okay. So let me write state
[04:40:37] or basically update the state here. So
[04:40:42] up until now this is all empty. Now I'm
[04:40:45] updating this. So
[04:40:47] I'm writing hello
[04:40:50] uh plus sorry
[04:40:54] hello plus state message whatever we
[04:40:57] have in message
[04:40:59] uh plus
[04:41:02] uh and then maybe give full stop and
[04:41:06] welcome to lang graph. Okay, so this is
[04:41:11] going to be my function and then I've
[04:41:13] already added it as a node in node in my
[04:41:17] graph here. So we only have one node for
[04:41:20] now. Now we're going to add ages to this
[04:41:23] node. So graph dot add age. It is going
[04:41:27] to at first we'll start
[04:41:32] uh the first flow is going to be or the
[04:41:35] first age is going to be from start to
[04:41:37] this particular node here which is
[04:41:38] initial
[04:41:41] and then after this I'm I'm going to add
[04:41:44] another age from initial
[04:41:48] to end. So we'll only have one one
[04:41:52] single node for this particular code
[04:41:54] here. So I'm going to compile this. So
[04:41:57] to compile we only need to do particle
[04:41:59] to graph.compile
[04:42:02] and then run this.
[04:42:04] Okay. So we have some error. I think
[04:42:06] it's some spelling mistake here. So this
[04:42:08] should have been initial. Let me run
[04:42:11] this again.
[04:42:14] Initial right. Uh okay this is wrong. So
[04:42:19] initial.
[04:42:21] Okay. Our uh graph is compiled. If you
[04:42:24] want to print this, you can also
[04:42:26] directly run bot. And then you can see
[04:42:28] that we have one single node. We
[04:42:33] we begin with the start part then the
[04:42:36] then the process flows through the
[04:42:38] initial node and then it goes to the
[04:42:40] end. So this is our basic graph workflow
[04:42:44] in lang
[04:42:46] graph that we've created. So now
[04:42:50] in order to uh invoke this graph what we
[04:42:53] need to do is we simply need to invoke
[04:42:55] this bot
[04:42:57] object that we have and then
[04:43:00] we need to pass something here. We'll
[04:43:02] pass messages and then pass our channel
[04:43:05] name learning hub here
[04:43:09] uh and then we'll print our response. So
[04:43:12] what happens here is at first the
[04:43:15] initial state in this particular uh
[04:43:18] variable contains this string called
[04:43:20] learning hub. Then it moves to greeting
[04:43:23] node and then along with that learning
[04:43:26] hub uh the state is now updated to this
[04:43:31] complete message here and then basically
[04:43:34] what we get in the end is is that
[04:43:37] particular complete uh content that we
[04:43:40] have processed. So if we run this
[04:43:45] uh okay something is wrong here. So
[04:43:47] message or messages let's see message
[04:43:50] state message let me just
[04:43:53] see if I've done any any kind of
[04:43:55] spelling mistakes here.
[04:43:57] Okay. So this must message. Okay. So if
[04:44:01] you see the response
[04:44:05] uh then you can see. Okay. Why is it
[04:44:08] only showing just one response here? I
[04:44:11] have invoke B right.
[04:44:14] Ah something that I've not done here is
[04:44:17] return
[04:44:18] state
[04:44:20] because it should return the updated
[04:44:22] state here. Let me run this again.
[04:44:26] And then if I run this, so it adds some
[04:44:29] new text as per the process function or
[04:44:33] the greeting node function here. And
[04:44:35] then uh it gives me the response. So
[04:44:39] this is a very simple implementation of
[04:44:42] our graph flow or our uh workflow using
[04:44:47] our graph here or using lang graph. So I
[04:44:50] hope you understood the concept of lang
[04:44:52] graph and then uh how is how it varies
[04:44:56] from langen. In the last two videos we
[04:44:59] explored the basics of langraph how
[04:45:01] nodes represent logical units of work
[04:45:04] and how the flow between them creates an
[04:45:06] AI reasoning pipeline. But until now our
[04:45:09] examples worked with simple single
[04:45:11] message states. In this video, we're
[04:45:14] taking the next big step, moving towards
[04:45:16] structured states that carry multiple
[04:45:18] pieces of information together, just
[04:45:20] like an agent's memory. So, think of
[04:45:23] state as a data package. It holds
[04:45:26] everything your graph needs to process,
[04:45:28] pass, and transform information at each
[04:45:32] step.
[04:45:34] We'll start with the code and then I'll
[04:45:36] try to explain the code accordingly. So,
[04:45:38] let me create a new file here.
[04:45:45] complex graph [snorts] ipv
[04:45:53] first of all from typing
[04:45:58] import type dict
[04:46:01] and list
[04:46:04] let me run this and then select the
[04:46:06] kernel so it's running uh from
[04:46:12] line graph dot graph import
[04:46:17] state
[04:46:19] graph comma start,
[04:46:23] end. Okay, so these are the inputs that
[04:46:24] we'll be needing.
[04:46:26] So the cell is running. Now I'm going to
[04:46:29] create a class uh that contains our
[04:46:33] state here. So class agent state
[04:46:40] and then the type will be typed date.
[04:46:45] Inside this I'll have a name.
[04:46:48] I'll have age.
[04:46:52] I'll also have skills
[04:46:56] and then a result.
[04:47:01] So
[04:47:03] unlike our previous video, instead of
[04:47:05] just one text, our our now stage
[04:47:08] contains multiple attributes like a
[04:47:10] person's name, age, and skills.
[04:47:13] After this, we'll be creating our nodes
[04:47:16] here. So for the first node, we're going
[04:47:18] to create a function.
[04:47:23] The parameter will be our agent state.
[04:47:32] And I'll write a doc string for this.
[04:47:34] This is the first node.
[04:47:38] And then here I'm going to update my
[04:47:41] state here. So the result
[04:47:46] variable in the state will be updated.
[04:47:53] state name
[04:47:59] welcome to the system
[04:48:03] then I will return the complete state
[04:48:05] here okay so this is going to be my
[04:48:08] first node similarly I'm going to type
[04:48:10] in the second node now def second node
[04:48:16] again it will have a parameter of state
[04:48:18] the node will always have the parameter
[04:48:20] of state and then it will return the
[04:48:22] entire state here
[04:48:27] write a doc string this is a second node
[04:48:31] and after this I'm going to update uh
[04:48:35] update the state result again here but
[04:48:38] first of all I'm going to uh bring out
[04:48:41] my skills and then convert them from a
[04:48:44] list to a string
[04:48:47] dot join state
[04:48:51] skills this
[04:48:56] and finally I'm going to update my
[04:48:58] result.
[04:49:01] So state
[04:49:03] result
[04:49:06] plus
[04:49:10] you have skills in
[04:49:14] state
[04:49:16] skills
[04:49:19] and then again I'm going to uh or let me
[04:49:23] just do skills here not state skills
[04:49:25] because I've already extracted my state
[04:49:27] skills from this. So again I'm going to
[04:49:30] pass out the entire
[04:49:33] state here.
[04:49:35] Okay.
[04:49:37] So each node uh in this particular graph
[04:49:40] that you see here or the or the graph
[04:49:43] that I'm going to build uh reads these
[04:49:46] structured states and then does it task
[04:49:48] and then passes it forward uh enriching
[04:49:53] its uh step by step.
[04:49:56] So the first node uh here acts like an
[04:50:00] initial greeter. It welcomes the person
[04:50:02] into the system and then the second node
[04:50:05] uh that I have uh adds more context like
[04:50:10] like uh like the skills that they have
[04:50:14] and then
[04:50:16] uh I'll also have a third node here.
[04:50:20] So
[04:50:22] uh what's that? Let me write down third
[04:50:26] node will contain an state agent state
[04:50:30] again and then it will return agent
[04:50:33] state for now.
[04:50:36] So let me write down this is the third
[04:50:39] node.
[04:50:44] Uh and then here what I'm going to do is
[04:50:46] I'm going to update my state
[04:50:51] uh equals to state result plus let me
[04:50:56] add something more here. to string. So
[04:50:59] in string uh you are
[04:51:04] uh state age
[04:51:07] years old
[04:51:10] and then end string here
[04:51:23] and then again I'm going to return
[04:51:27] the
[04:51:43] So the third node uh completes the flow
[04:51:45] by including the age creating a full
[04:51:48] personalized summary year. uh so the
[04:51:50] data flows from one node to another uh
[04:51:53] gradually building the final message
[04:51:54] just like a well organized thought
[04:51:56] process inside an AI agent. So so now
[04:51:59] we'll build that particular graph. So
[04:52:01] let me run this. It's running. We'll
[04:52:04] define a state graph uh state graph and
[04:52:09] then inside it I'll have agent state
[04:52:14] agent state
[04:52:19] then I'm going to add my first node
[04:52:21] first node will be
[04:52:24] uh
[04:52:26] first node
[04:52:29] uh I'll I will now define the function
[04:52:32] with that first node Then I'll also have
[04:52:34] a second node similarly. And then the
[04:52:36] third node.
[04:52:43] Okay. Copy this down. This is going to
[04:52:45] be my second node.
[04:52:53] And then finally I'll have my third
[04:52:54] node.
[04:53:03] So I'm going to add ages now. So first
[04:53:06] of all we will go from start to our
[04:53:08] first node. Then
[04:53:12] we'll go from first node to second node.
[04:53:17] Then we'll go from graph.add_age
[04:53:23] second node to third node. And then
[04:53:27] finally after third node we'll go to
[04:53:29] end. Let me compile this. So gra uh let
[04:53:33] me write in the object name bot equals
[04:53:36] to graph dot
[04:53:38] compile
[04:53:40] and then print out the part here or the
[04:53:42] graph here. So as we can see
[04:53:46] it goes from start to first node to
[04:53:48] second node to third node and then
[04:53:50] finally to the end.
[04:53:52] So the three simple notes here uh
[04:53:55] highlights the true power of lang graph.
[04:53:57] Uh it helps you modularize reasoning uh
[04:54:00] breaking large task into small reusable
[04:54:03] logical units uh that form a clear and
[04:54:07] and more uh traceable part of uh
[04:54:10] execution. So instead of handling
[04:54:13] everything in one complex step, Langraph
[04:54:15] lets you think and build in stages
[04:54:17] exactly like how agents reason in real
[04:54:20] life.
[04:54:22] So we'll complete this and then see the
[04:54:24] result here. So let me build my input
[04:54:27] state.
[04:54:31] I'll type out the name here. Name can be
[04:54:33] Alice.
[04:54:35] Uh age and skills can be this one here.
[04:54:38] So I don't need to pass in the result
[04:54:40] yet because that will be formed from
[04:54:42] within the nodes. And then I'm I'm only
[04:54:44] going to pass until this uh skills here.
[04:54:47] So let me say data science. Okay. Then
[04:54:50] finally what I can do is I I can invoke
[04:54:54] the bot using this input state and then
[04:54:57] finally print out my response. So my
[04:55:00] response will be printed. Uh first of
[04:55:02] all what will happen is it will go to
[04:55:04] this particular node here. So it will
[04:55:07] take a name and then it will say welcome
[04:55:09] to the system with this entire message.
[04:55:13] It'll add you have following skills and
[04:55:15] then after that uh along with this
[04:55:17] entire
[04:55:19] message it will add the age of the
[04:55:21] person and then we'll print the
[04:55:23] response. So let's see
[04:55:27] skills. Okay, what is it? Skills. What
[04:55:32] else here?
[04:55:34] Okay, here I've done some mistake. Added
[04:55:36] an extra space. So let me run this
[04:55:37] again.
[04:55:40] And then as you can see uh the result is
[04:55:43] Alice welcome to the system. You have
[04:55:45] skills in Python, ML and data science
[04:55:48] and you are 30 years old. So based on
[04:55:51] the flow of data in between these nodes
[04:55:54] the result had been updated or basically
[04:55:57] some extra strings have been have been
[04:55:59] appended in each of these results here.
[04:56:03] So I hope you understood the code and
[04:56:05] then understood the concept of this
[04:56:07] multiple node that we have been
[04:56:09] implementing here. Um so far uh we built
[04:56:12] a linear graph that processes structured
[04:56:15] input and composes a final result step
[04:56:17] by step. Right? But this is just a
[04:56:20] beginning in langraph. In the upcoming
[04:56:22] video, we'll take this concept further
[04:56:24] by introducing branching logic where you
[04:56:26] uh where your graph can make choices
[04:56:28] dynamically uh based on the state. In
[04:56:32] the last video, we learned how data can
[04:56:34] move from one node to another with each
[04:56:36] node performing its task and enriching
[04:56:39] the overall result. But what if your
[04:56:42] workflow needs to take different paths
[04:56:44] depending on certain conditions? That's
[04:56:46] where things start to get interesting
[04:56:48] because in real world AI systems, not
[04:56:51] every query or task follows a single
[04:56:54] linear route. Sometimes your graph needs
[04:56:57] to choose where to go next and Lang
[04:56:59] graph allows that using conditional
[04:57:02] edges. So in today's video we're going
[04:57:04] to see how to introduce
[04:57:07] choice making inside your graph. How it
[04:57:10] can intelligently choose between
[04:57:12] multiple nodes based on logic you
[04:57:14] define.
[04:57:16] First of all we'll write the code and
[04:57:18] then I'll explain you the code here.
[04:57:21] So let me create a new file
[04:57:30] 3 conditional
[04:57:33] graph ipy nbv
[04:57:38] I'll have some imports first of all from
[04:57:41] typing I'm going to import typic
[04:57:49] then from
[04:57:52] lang graph dot graph. I'll import
[04:57:57] state graph
[04:58:00] start and end.
[04:58:02] Let me run this and then select the
[04:58:04] default interpreter.
[04:58:08] After that we're going to write our
[04:58:10] agent state. So agent state is going to
[04:58:13] be of type dict
[04:58:16] and I'll have number one which will be
[04:58:19] an integer
[04:58:21] number two which will also be an integer
[04:58:25] operation which will be a float sorry
[04:58:28] string and then I'll have a result which
[04:58:31] will also be an integer. Okay. So this
[04:58:34] will be our agent state here. Let me run
[04:58:37] this too. Now I'm going to create few
[04:58:40] nodes here. First of all, the first node
[04:58:42] will be adder. It will contain state
[04:58:46] agent state
[04:58:49] and it will also result and or return an
[04:58:52] agent state here. Now here what I'm
[04:58:56] going to do is I'm going to write a dock
[04:58:58] string. So this node adds two numbers.
[04:59:04] After this I'm going to update my
[04:59:08] uh final
[04:59:12] final number or I can sorry it's not
[04:59:14] final number it is result. So state
[04:59:16] result equals to state
[04:59:20] number one plus state number two
[04:59:24] and then I'm going to return a state
[04:59:26] here.
[04:59:28] Okay.
[04:59:33] Then I'm going to define another node
[04:59:36] here which is called subtract
[04:59:39] and state
[04:59:41] age and state.
[04:59:43] Uh the node will basically subtract two
[04:59:45] numbers and then what I'm doing here is
[04:59:48] doing number one minus number two and
[04:59:49] then returning the state. Now I will
[04:59:53] define a router node here which chooses
[04:59:57] where should I go next. So
[05:00:00] decide
[05:00:02] next node it will also contain an agent
[05:00:05] state. It will be of type agent state
[05:00:11] and then it is simply going to return a
[05:00:13] string here.
[05:00:15] So this node will will decide or will
[05:00:19] select
[05:00:20] the next
[05:00:22] node of the graph.
[05:00:26] Now I'm going to check
[05:00:30] one uh state called operation here. So
[05:00:33] if state operation
[05:00:38] double equals to add
[05:00:42] then what I'm going to do is I'm going
[05:00:44] to return add operation and then
[05:00:50] else if
[05:00:52] state
[05:00:54] operation is subtract then I will return
[05:00:58] subtract up. Okay so this will be my
[05:01:01] router node here. So let me run this.
[05:01:04] Then after this I'm going to create my
[05:01:07] final graph. My final graph will be
[05:01:10] based on state graph and then it will
[05:01:13] contain this agent state object.
[05:01:17] So agent state sorry
[05:01:21] agent state class.
[05:01:24] Let me add nodes here. So the first node
[05:01:28] will be add node and then and then the
[05:01:32] function for this node is adder. Second
[05:01:35] node is subtract node and then uh and
[05:01:38] then the function for that is uh
[05:01:41] subtract. Then I'm also going to add a
[05:01:43] third node here. So grab dot add node.
[05:01:47] The third node will be named router. And
[05:01:49] then what I'm going to do here is I'm
[05:01:51] going to pass
[05:01:54] uh pass the state as it is here. So it
[05:01:58] will also be called a pass through
[05:02:00] function. So whatever we get will just
[05:02:03] be passed uh passed to that router stage
[05:02:06] here. So now I'm going to go and add
[05:02:09] ages. So first age is going to be start
[05:02:12] and then it will go to router. Then I'm
[05:02:14] going to add conditional age here. So
[05:02:17] add conditional age.
[05:02:19] Uh
[05:02:21] what will this be based on? So this will
[05:02:23] be based on the router node. And then
[05:02:29] what will happen here is its function is
[05:02:31] this one
[05:02:35] decide next node.
[05:02:38] So
[05:02:39] so the function is here. And then the
[05:02:42] two options from this node is
[05:02:46] uh
[05:02:49] the two options from this node is one is
[05:02:53] the add up which will take us to add un
[05:02:57] node and then the other is
[05:03:01] uh and then the other is the subtract up
[05:03:03] which will take us to subtract node. So
[05:03:06] basically we're referring to add up and
[05:03:08] subtract up from this particular node
[05:03:10] here. And then if we get add up we'll go
[05:03:13] to add node which means our adder uh
[05:03:17] function and and then if we get subtract
[05:03:19] up we'll go to our subtract node which
[05:03:21] is our subtract function. Okay.
[05:03:25] And then what we also need to do is
[05:03:27] since u both of these add and subtract
[05:03:31] will show the result and then go to the
[05:03:33] end of the graph. So what we need to do
[05:03:35] is we need to add two different ages
[05:03:37] here from add to end and then subtract
[05:03:39] to end.
[05:03:41] Now since this is done I'm going to
[05:03:43] compile my graph.
[05:03:45] Let me compile my graph and then if I
[05:03:47] print out
[05:03:49] uh my graph here we'll see that first of
[05:03:53] all we'll start from here. Then we go to
[05:03:56] the router node. The router node fixes
[05:03:58] where where we should go next based on
[05:04:01] the agent uh
[05:04:04] agent state u called operation here. If
[05:04:07] we get plus then we go to add node. If
[05:04:10] we if we get minus we go to subtract
[05:04:12] node from either of these add or
[05:04:14] subtract node we go to the end here. So
[05:04:17] this is how we can introduce conditional
[05:04:19] graphs in our line chain. Now I'm going
[05:04:23] to declare my input state here. So input
[05:04:27] state
[05:04:28] is going to be uh the number one will be
[05:04:33] 10. Let's say uh the number number one
[05:04:38] is going to be
[05:04:41] 10. Okay, I'll keep it 10. Number two is
[05:04:44] going to be four. I don't need this
[05:04:46] result here. The result will be operated
[05:04:49] on its own. And then basically operation
[05:04:52] is minus. Now if I invoke
[05:04:57] if I invoke my boat
[05:05:02] using input state
[05:05:06] then and then if I print my final
[05:05:07] response then I can see that the result
[05:05:10] is set and then since the since the
[05:05:13] operation is subtract so the result is
[05:05:15] six. If I change this operation from
[05:05:18] plus
[05:05:20] now the result goes to 14. So either of
[05:05:23] these two nodes are chosen based on the
[05:05:26] uh operation uh state uh present in our
[05:05:31] agent state here.
[05:05:37] Okay to summarize now we start with an
[05:05:40] agent state that carries our data two
[05:05:42] numbers the operation we want to to do
[05:05:46] and either addition or subtraction. Next
[05:05:49] we define two nodes, one that adds, one
[05:05:51] that subtracts. But the real magic is
[05:05:54] inside this router
[05:05:57] uh function here that we have. So this
[05:05:59] function acts like our choice maker. It
[05:06:03] inspects the current state and then
[05:06:04] returns which node the graph should go
[05:06:06] next. So if the operation is positive
[05:06:09] then we go to add node. If the operation
[05:06:12] is negative then we go to the subtract
[05:06:14] node. So lang graph then uses these uh
[05:06:18] conditional ages to to make it run. So
[05:06:21] these ages dynamically connect the flow
[05:06:24] uh at runtime based on the conditions uh
[05:06:28] based on the condition functions output.
[05:06:31] So uh instead of a single linear chain
[05:06:34] what we have here is it
[05:06:38] it is a conditional chain and it behaves
[05:06:41] like an intelligent uh tree. So capable
[05:06:44] of branching out and adapping to the
[05:06:46] data it receives. So this concept
[05:06:49] conditional routing is at the heart of
[05:06:51] making agent test system flexible. So in
[05:06:53] the upcoming videos we'll take this
[05:06:55] concept further including memory as well
[05:06:57] as message passing inside langraph so
[05:07:00] agents can remember and react
[05:07:02] contextually and that is where lang
[05:07:05] graph toy
[05:07:07] uh starts to feel alive. In the previous
[05:07:09] video, we learned how to create
[05:07:11] conditional routes in Lang graph where
[05:07:12] our graph intelligently decides which
[05:07:15] node to visit next based on user input
[05:07:18] or data state. But what if we want to
[05:07:20] chain multiple conditional flows
[05:07:22] together like a series of choices where
[05:07:25] one operation leads to another? That's
[05:07:27] exactly what we're going to explore
[05:07:28] today. So, in this video, we're taking
[05:07:31] things one step further and see how
[05:07:33] Langraph can handle multiple branching
[05:07:35] routes, letting you
[05:07:38] create more complex and intelligent
[05:07:40] workflows that don't just stop after one
[05:07:43] choice. So, we'll first write down the
[05:07:46] code and then I'll explain you the code
[05:07:47] here.
[05:07:51] Okay. So let me create a new file here
[05:07:56] for complex
[05:08:00] complex conditional
[05:08:04] ipv.
[05:08:08] So first of all I'll have my code I'll
[05:08:12] have my imports here.
[05:08:16] So the import are going to be from line
[05:08:18] graph
[05:08:20] dot graph import
[05:08:24] state graph
[05:08:27] start and end
[05:08:30] and from typing I will have type dict
[05:08:35] type dict
[05:08:38] I can choose the interpreter and then
[05:08:39] while this runs uh I'll create my agent
[05:08:42] state so agent state this will be have a
[05:08:46] parameter of type date.
[05:08:49] So type date I'll have number one here,
[05:08:53] number one as integer,
[05:08:56] number two also as an integer
[05:09:00] and I'll have number three as an
[05:09:04] integer.
[05:09:05] Number four also as an integer.
[05:09:11] I will have operation one
[05:09:15] as a string,
[05:09:20] operation two also as a string. And then
[05:09:24] I'll save the
[05:09:27] result of operation between number one
[05:09:29] and number two in result one which is
[05:09:31] going to be an integer. And similarly
[05:09:34] operation two for number three and
[05:09:36] number four is going to be saved in
[05:09:38] result two which is also an integer.
[05:09:42] Okay. So let me run this.
[05:09:44] So while this is running now we'll
[05:09:46] create our functions here. So first of
[05:09:48] all we'll have added sorry adder where
[05:09:52] we'll pass the
[05:09:54] parameter as agent state. it will again
[05:09:59] return an agent state.
[05:10:02] So I'll update state
[05:10:07] uh result one equals to
[05:10:11] state uh number one
[05:10:14] plus state
[05:10:17] number two
[05:10:20] and then I will return the state here.
[05:10:23] So let me copy this and then create
[05:10:26] another
[05:10:27] uh subtraction operation here.
[05:10:30] So I will have uh subtractor two or su
[05:10:36] okay I'll write the full function name
[05:10:37] subtractor two where I'm going to
[05:10:40] subtract these two number one and number
[05:10:43] two here similarly I'll have adder two
[05:10:45] and subtractor two. So let me just copy
[05:10:48] this down and then copy it here. So here
[05:10:50] I'll have adder two. The result will be
[05:10:53] stored in result two. The numbers are
[05:10:56] number three and
[05:10:59] number four. Similarly in subtractor two
[05:11:04] we are going to store the result in
[05:11:07] result two where the numbers are number
[05:11:08] three and number four.
[05:11:14] Okay. We also need to create two router
[05:11:17] functions. So let's do that.
[05:11:19] choose
[05:11:21] next node one.
[05:11:24] It will have an state of type agent
[05:11:27] state
[05:11:30] and then it will return a string.
[05:11:37] So if state
[05:11:40] uh operation 1
[05:11:44] is equal to plus
[05:11:46] then what we want to do is we want to
[05:11:49] return
[05:11:52] add one
[05:11:55] else if uh state
[05:11:59] operation 2
[05:12:01] is equal to minus
[05:12:05] then we want to return sub one.
[05:12:10] Okay, I'll also create a router for our
[05:12:13] number three and number four part here.
[05:12:16] So choose next node two.
[05:12:21] Uh okay sorry this has to be operation
[05:12:23] one and then here we will have operation
[05:12:25] two
[05:12:27] add two oper operation two sub two. Okay
[05:12:31] so these are our uh router nodes. Now
[05:12:34] we'll go on to create our graph here. So
[05:12:39] graph equals to state graph
[05:12:43] state graph. I'm not sure why this
[05:12:44] position is not being shown but anyway
[05:12:47] agent state I can just type this uh
[05:12:50] first of all I'm going to add my first
[05:12:52] node here
[05:12:54] so the first node is adder one and then
[05:12:58] I'll give it give a name adder one here
[05:13:01] similarly I have my second node
[05:13:04] add node this is subtractor one
[05:13:10] let me write down the function name here
[05:13:13] which is
[05:13:15] okay what do you name it? Okay,
[05:13:16] subtractor one
[05:13:22] subtractor one.
[05:13:25] Similarly, I have adder two and
[05:13:26] subtractor two which I'll just create
[05:13:29] here by copying this
[05:13:33] adder two and then subtractor two.
[05:13:38] Now I'm going to add a node for router
[05:13:40] one and router two which will basically
[05:13:43] uh act as a pass through function here.
[05:13:45] So router one uh will pass lambda state
[05:13:50] and then basically pass the state here
[05:13:55] and then similarly in router two or this
[05:13:58] should have been a comma.
[05:14:02] Okay. And then in
[05:14:06] router two we'll do the same thing.
[05:14:14] So router to lambda state state. Okay.
[05:14:17] Uh now what we'll do is we'll start
[05:14:21] adding age. So the first age is going to
[05:14:23] be from start to router one. Then
[05:14:28] I'll add a conditional age here. So add
[05:14:31] conditional ages. Now the detail of this
[05:14:34] conditional is just from router one
[05:14:38] it will go to the choose next node one
[05:14:42] choose next node one
[05:14:47] and from here we we have two options we
[05:14:49] can either go to uh okay what is the
[05:14:53] function name let's see
[05:14:55] so add one and sub one right so we can
[05:14:58] either go to add one
[05:15:00] so if add one occurs then we go to adder
[05:15:03] one and if uh sub one occurs we go to
[05:15:06] subtractor one.
[05:15:09] Now I'll add one more age here. So add
[05:15:12] age from adder one to router two and
[05:15:16] then subtractor one to router two.
[05:15:19] Whichever works uh whichever works in
[05:15:23] the following case here. Adder one and
[05:15:25] subtractor one both should go to router
[05:15:26] two here. Now I'm going to add another
[05:15:28] conditional age for router two here.
[05:15:33] Uh so the name is router two
[05:15:39] comma
[05:15:41] and after this uh the function is choose
[05:15:43] next node two and then within this I'll
[05:15:46] have one more
[05:15:49] [music]
[05:15:50] uh
[05:15:54] I'll have add two add two which will go
[05:15:57] to add two and sub sub two which will go
[05:15:59] to subtract
[05:16:01] Now after this I'm going to uh add two
[05:16:05] edges either from addit two to end and
[05:16:08] subtract two to end again. Now this is
[05:16:11] my final graph. Let me compile this
[05:16:13] graph dot compile and then if I print
[05:16:16] the bot then we will see our conditional
[05:16:19] graph here. So, so from start we'll go
[05:16:22] to router one and then either to add or
[05:16:24] sub add one or sub one uh depending upon
[05:16:28] the operation and then
[05:16:30] and then we'll go to router two and then
[05:16:32] add two to sub two depending upon the
[05:16:35] operation that we have. So now what
[05:16:38] we're going to do is we are going to
[05:16:40] finally uh run this using our input
[05:16:43] state. Let me provide the input state. I
[05:16:44] will just going I'm just going to copy
[05:16:47] this here. So number one is one, number
[05:16:49] two is two, the operation is plus. So
[05:16:51] basically we need to see the result
[05:16:53] three in result one. And then in case of
[05:16:55] number four and number seven, we need to
[05:16:57] see the subtraction operation here. So
[05:16:59] now what I'm going to do is result equal
[05:17:01] to B dot invoke and then provide the
[05:17:04] input state here. And finally we print
[05:17:07] out the result
[05:17:10] and then we can see our result here.
[05:17:16] So uh what did we do here? We started by
[05:17:20] defining an agent state that holds two
[05:17:23] two separate mathematical operation. So
[05:17:25] each operation has its own pair of
[05:17:26] numbers and operators. One for each step
[05:17:28] and then one for the second. Now we
[05:17:31] define four simple nodes here. Two
[05:17:32] adders and two subtractors. So each of
[05:17:35] these node does the operation and store
[05:17:37] the result back into the state. But the
[05:17:39] interesting part here is the two routers
[05:17:41] that we have. So uh router one and
[05:17:45] router two. So these so these routers
[05:17:48] act like our uh checkpoints where
[05:17:51] choices are made. The first router looks
[05:17:53] at operation one and then chooses
[05:17:54] whether to go to the first order or the
[05:17:56] first optractor and then uh similarly
[05:17:58] for the second router again. So lang
[05:18:00] graph hence handles this beautifully
[05:18:03] with uh multiple conditional ages uh
[05:18:07] joined together allowing our graph to
[05:18:09] branch and rebranch as per needed just
[05:18:12] like how complex reasoning systems work
[05:18:14] in the real world. It's a simple simple
[05:18:16] yet powerful demonstration of how Lang
[05:18:19] graph gives you total control over your
[05:18:20] workflows direction without any uh
[05:18:24] hardcoded if else change in your logic.
[05:18:27] So now uh instead of having a single
[05:18:30] choice your system can make multiple
[05:18:32] sequential choices each one based on the
[05:18:34] operative state of the graph. So this
[05:18:36] opens the door to designing more
[05:18:37] intelligent uh multi-step workflows like
[05:18:40] multi-turn reasoning agents, multi-stage
[05:18:43] data processor or even uh
[05:18:47] uh complex uh system that can react to
[05:18:51] evolving uh inputs. So far in this line
[05:18:55] graph series, we built conditional and
[05:18:57] multi-step workflows, graphs that decide
[05:19:00] where to go based on the data in the
[05:19:02] state. In this video, we're going to
[05:19:05] make things a bit more fun and
[05:19:06] interactive. We'll design a mini number
[05:19:09] guessing game using Langraph where the
[05:19:12] system makes guesses, checks its
[05:19:15] progress, and keeps looping
[05:19:17] intelligently until it it gets the right
[05:19:20] answer or runs out of it atems. This
[05:19:24] example shows how lag graph can handle
[05:19:26] iterations and choice loops. Something
[05:19:30] that's incredibly important when you
[05:19:32] want your agent to keep reasoning,
[05:19:34] refining, and trying again just like
[05:19:36] humans do when solving a problem. Okay,
[05:19:39] so without any delay, let's first go
[05:19:41] into the code.
[05:19:43] [snorts]
[05:19:49] So here I'm going to create a new file
[05:19:55] to call it number game.
[05:20:01] Number game
[05:20:04] do ipy nb.
[05:20:12] So from line graph
[05:20:15] I'm going to import
[05:20:19] state graph start
[05:20:22] and end
[05:20:25] from typing
[05:20:28] I'll import type
[05:20:31] and list
[05:20:33] and we'll also import random here.
[05:20:38] So let me select the virtual
[05:20:39] environment.
[05:20:42] I'm going to create create a class
[05:20:44] called agent state
[05:20:48] agent state.
[05:20:53] So here I'll have three variables here.
[05:20:56] The first one will be name which is
[05:20:58] going to be a string. The second is
[05:21:00] going to be a number which is going to
[05:21:03] be list of integer.
[05:21:06] uh this is basically going to contain
[05:21:08] the guesses that the model makes and a
[05:21:12] counter which will also be an integer.
[05:21:16] So
[05:21:18] at first we'll have a greeting node
[05:21:23] which will contain
[05:21:25] agent state as its parameter
[05:21:31] and it will again return an agent state.
[05:21:37] Let me write down a drop string here. So
[05:21:41] let me say [snorts] greeting
[05:21:45] node
[05:21:46] which says hi to a person.
[05:21:53] So here what I'm going to do is I'm
[05:21:56] going to update state name
[05:21:59] to
[05:22:01] hi there.
[05:22:07] I have a state name that I'll pass
[05:22:10] in the input here. So, state name.
[05:22:33] we will start
[05:22:36] the G.
[05:22:39] And what I'm going to do is I'm going to
[05:22:41] set state
[05:22:45] counter to zero
[05:22:48] and then return state.
[05:22:51] I'll have another state called uh or
[05:22:54] another function called random state.
[05:22:57] This will contain agent state.
[05:23:03] age and state.
[05:23:07] So this is going to generate
[05:23:10] number
[05:23:12] it will be random between
[05:23:18] between 0 and 10. [clears throat]
[05:23:23] So state
[05:23:26] number will be appended
[05:23:29] with the random number guessed by this
[05:23:32] model here 0 to 10.
[05:23:36] Then I'm going to update the state
[05:23:37] counter.
[05:23:39] State counter will be updated
[05:23:42] by one. And then I'm going to return
[05:23:44] state here.
[05:23:49] The third function will be our router
[05:23:51] function
[05:23:53] which will say should continue
[05:23:56] contain an agent state
[05:24:01] that will return a string.
[05:24:05] So this will be a function
[05:24:08] to decide
[05:24:11] what to do next.
[05:24:17] What to do next
[05:24:26] here? If
[05:24:29] state
[05:24:32] counter
[05:24:33] is less than five.
[05:24:38] I'm going to enter
[05:24:41] loop
[05:24:44] where this will be my state counter
[05:24:46] value.
[05:25:10] And I will return
[05:25:13] loop here.
[05:25:16] And in the else part,
[05:25:21] I'm going to exit the loop and I'll
[05:25:23] return exit here.
[05:25:26] Now let me create a graph using the
[05:25:29] graph
[05:25:31] using the state graph
[05:25:35] state graph and inside this I'm going to
[05:25:37] pass my agent state
[05:25:43] I'll add a node graph dot add node.
[05:25:47] So first of all we'll have a greet node
[05:25:51] using greeting node function.
[05:25:54] Then I'll have random node
[05:26:02] using
[05:26:04] random state function.
[05:26:10] I'll also start adding the ages. So
[05:26:14] first of all the first age will go from
[05:26:16] start to grid.
[05:26:22] The second will go from grid to random.
[05:26:26] And then here we're going to have
[05:26:28] conditional ages.
[05:26:30] So add conditional ages.
[05:26:34] It will start from
[05:26:37] random.
[05:26:40] The function that it should check is
[05:26:42] should continue.
[05:26:45] And we'll have two different cases here.
[05:26:50] The first case if it's loop
[05:26:53] uh then it should go to random
[05:27:00] or if else if it is exit then it should
[05:27:05] go to
[05:27:07] end.
[05:27:13] Now I'm going to have one more uh edge
[05:27:17] here.
[05:27:19] If the counter is greater than five then
[05:27:21] I need to end this loop. So one age will
[05:27:25] be from uh random to end. So let me
[05:27:29] initialize my graph or compile my graph.
[05:27:34] And if I print my graph
[05:27:37] uh okay what's wrong? Let's see. So add
[05:27:41] age edge. Okay. Add edg edge.
[05:27:46] Okay, as you can see, so once uh once
[05:27:51] the model greets the user, then it will
[05:27:53] enter inside this random node. Uh then a
[05:27:56] loop will be carried out uh if it stays
[05:28:00] within a certain condition or else it
[05:28:03] will exit. Now
[05:28:05] what I'm going to do is I'm going to
[05:28:07] take my input input state here.
[05:28:14] So input state
[05:28:19] equals to name
[05:28:23] shake
[05:28:28] and
[05:28:30] and the number list will will now be
[05:28:33] empty and with this I'm going to invoke
[05:28:36] my board
[05:28:41] with my input data and I'm going to
[05:28:42] print my response.
[05:28:45] So if we run this in loop one, loop 2,
[05:28:49] loop three, loop four, loop five because
[05:28:51] we've entered uh a condition for the
[05:28:54] value less than five. So in loop one it
[05:28:58] guess 10. In loop 2 it guessed 8, 7, 2
[05:29:01] and 3 and respectively. So this is how
[05:29:04] we initialize loop in case of langraph.
[05:29:11] So we'll go to our our very beginning of
[05:29:14] the code and then we'll see what is
[05:29:16] happening here. So we start by uh
[05:29:19] defining this agent state that holds
[05:29:22] everything about this game. So it holds
[05:29:24] the player names, the target number, the
[05:29:26] last guesses, the total attempts and the
[05:29:28] range of the and the range of the number
[05:29:30] you can choose from. Uh then we have
[05:29:33] three things. We have the setup node. So
[05:29:38] this basically initializes the state uh
[05:29:41] resetting uh attempts as well as the
[05:29:45] guesses. Then we have the guest node
[05:29:46] here and then we have the uh
[05:29:50] decision node or the router node that we
[05:29:53] have here. So uh this is where the power
[05:29:56] of the line graph shines. So instead of
[05:29:58] using a while loop, we simply create a
[05:30:01] conditional edge that loops back to the
[05:30:04] same node until a certain condition is
[05:30:07] met. So the condition is placed here in
[05:30:11] this particular part of the code.
[05:30:13] So each loop uh iteration updates the
[05:30:16] state meaning uh lang graph remembers
[05:30:19] the previous attempts making the
[05:30:21] upcoming choices context of it. So
[05:30:25] essentially uh we've not completely
[05:30:28] implemented the game here but we've
[05:30:29] turned this simple uh guessing game into
[05:30:32] an uh autonomous uh iterative reasoning
[05:30:36] process uh which holds the same uh
[05:30:39] mechanism behind how our agentic systems
[05:30:42] plans act [clears throat] and retries
[05:30:45] while solving complex task. And I'm
[05:30:49] going to end this video for now. But
[05:30:51] what I want you to do is I also want you
[05:30:53] to add a target number here. And then uh
[05:30:56] basically in this particular uh router
[05:31:00] function here, you basically check uh if
[05:31:03] the model has correctly guessed the
[05:31:04] number or not. If the model has
[05:31:06] correctly guessed the number then then
[05:31:09] the model has won the game or if uh if
[05:31:13] the model has correctly uh or if the
[05:31:15] model uh could not guess the number
[05:31:18] within the given number of attempts
[05:31:20] basically the model has lost the game.
[05:31:22] So I think you can implement that by
[05:31:25] yourself. In the last video, we explored
[05:31:27] the basic structure of Lang graph where
[05:31:29] we learned how nodes and edges from the
[05:31:32] foundation of state-driven AI workflow.
[05:31:35] We built a simple example that took an
[05:31:38] input message, processed it through a
[05:31:40] node, and returned a response. Now,
[05:31:43] we'll take that idea one step further.
[05:31:45] In this video, we'll connect our Lang
[05:31:47] graph with a real AI model, Google's
[05:31:50] Gemini 2.5 Flash and see how a complete
[05:31:53] interaction look can be created between
[05:31:55] a user and an intelligent agent. Here
[05:31:58] we'll represent our state as a
[05:32:00] collection of messages. Each message
[05:32:02] captured in the conversation between a
[05:32:04] human and the AI. The power of Langraph
[05:32:07] truly begins to shine here. Instead of
[05:32:09] hard coding a linear sequence of actions
[05:32:12] like we often did in Langchen, Langraph
[05:32:14] lets us visualize and manage the flow of
[05:32:17] thought where each step is an
[05:32:19] independent node that can evolve,
[05:32:20] connect or branch dynamically. And by
[05:32:23] the end of this video, you'll understand
[05:32:25] how a line graph based chatbot can
[05:32:27] process user inputs, generate
[05:32:29] intelligent responses and maintain
[05:32:31] conversation flow all through a graphic
[05:32:34] structure. This marks our first step
[05:32:36] towards building intelligent agent
[05:32:39] multi-step conversational AI system
[05:32:41] using lang. So let's get started and see
[05:32:44] how easy is it to make your AI think in
[05:32:47] graphs. So we'll proceed to the code.
[05:32:51] I'm going to create a new file here
[05:32:59] and I'll name it AI agent
[05:33:02] agents do ipy lv
[05:33:06] first of all start with the import from
[05:33:09] typing I'll import typic
[05:33:12] and list
[05:33:15] then from lang graph
[05:33:19] dot graph I'll import state graph
[05:33:24] start
[05:33:27] and end.
[05:33:32] Then from langen_core
[05:33:34] dot messages
[05:33:37] I'm going to import human message.
[05:33:42] Then the model
[05:33:46] import chat Google generative AI then
[05:33:50] from env I'm going to import load env
[05:33:56] load the credentials first and then I'm
[05:33:59] also going to load the model here. So
[05:34:01] the model is
[05:34:04] >> as I said earlier it is Gemini
[05:34:07] 2.5/model.
[05:34:11] Okay. So let me run this. I'll select
[05:34:13] the interpreter and then create an agent
[05:34:16] state here.
[05:34:25] So the agent state will be of type
[05:34:28] picked uh
[05:34:31] I'll [snorts] have one single messages
[05:34:34] which will be a list of
[05:34:38] human message.
[05:34:41] Then I'll have a function called process
[05:34:44] where I'll pass in the state agent state
[05:34:47] and then this will again return agent
[05:34:50] state here.
[05:34:55] the
[05:34:58] response will be uh invoked from the
[05:35:01] model here. So whatever is present in
[05:35:04] the state will be passed to the model
[05:35:06] and then I'll get the
[05:35:12] response here.
[05:35:14] What I'm also going to do is I'm going
[05:35:16] to append the same state messages
[05:35:21] dot append
[05:35:23] response
[05:35:25] and I'll also print this. So AI
[05:35:30] uh AI has passed this response content.
[05:35:38] Let me also add a line break here. And
[05:35:41] finally let me return
[05:35:44] state here.
[05:35:47] Now [snorts]
[05:35:50] >> after this I'll pass state graph
[05:35:54] uh and inside this I'll pass agent
[05:35:56] state.
[05:36:00] Let me add a new edge uh sorry new node
[05:36:03] first.
[05:36:05] So the node name will be process and the
[05:36:08] function name is process.
[05:36:12] Let me add two different ages here. So
[05:36:15] add age start to process.
[05:36:21] Another age will be from process to end.
[05:36:30] Process to end.
[05:36:35] Now compile the graph
[05:36:39] and then we can see the workflow of our
[05:36:42] graph here.
[05:36:52] Okay, run this agent state and then we
[05:36:55] can see our graph here which goes from
[05:36:57] start to process and then to end. So
[05:36:59] basically in the process part what
[05:37:01] happens is whatever uh message is being
[05:37:05] typed by the user is sent to the is sent
[05:37:07] to the model or the AI model and from
[05:37:10] there the AI model generates a
[05:37:14] response. Okay. Now uh
[05:37:18] what we'll have here is a user input.
[05:37:21] Let me ask for the user message from the
[05:37:23] user input.
[05:37:32] enter your
[05:37:34] message
[05:37:37] and
[05:37:39] and I'll run a loop
[05:37:41] until the user types exit.
[05:37:44] So not equals to exit.
[05:37:54] And I'm going to print
[05:37:57] print the human message
[05:38:05] [snorts]
[05:38:12] then my input state is going to be
[05:38:16] the messages.
[05:38:18] uh it key will be messages.
[05:38:22] It will be a list of
[05:38:26] or I can do it like this.
[05:38:29] I can code it under human message.
[05:38:34] invoke
[05:38:35] the bot
[05:38:38] using our input state
[05:38:42] and then
[05:38:44] basically uh ask for another
[05:38:48] user input again. So if I run this,
[05:38:51] I can pass any message here. Hello
[05:38:57] and then the model has replied me back
[05:39:00] ask what is your
[05:39:04] what is your name
[05:39:07] and then AI uh Apex bag as well. So my
[05:39:11] uh each time I enter uh enter some text
[05:39:16] that will be taken to the model it will
[05:39:19] be invoked within our model and then our
[05:39:21] model will generate some response here.
[05:39:24] So this is how we integrate a real world
[05:39:27] AI into our langraph workflow. In our
[05:39:31] previous video, we saw how to build a
[05:39:33] simple conversational agent using
[05:39:35] Langraph, one that could interact with a
[05:39:38] real AI model and respond dynamically to
[05:39:42] human input. But what happens when we
[05:39:45] want to want our AI to do more than just
[05:39:48] talk? What if it could reason, maybe
[05:39:51] perform calculations, or use specialized
[05:39:53] tools to find answers? That is exactly
[05:39:56] what we will do or what we'll explore in
[05:39:58] this video. We're introducing the
[05:40:00] concept of tool nodes in Langraph. A
[05:40:03] powerful way to let your AI agent call
[05:40:05] external functions like the functions
[05:40:08] you've created
[05:40:10] and many more. Instead of relying on the
[05:40:13] model to guess or holutionate results,
[05:40:16] we give it direct access to real tools
[05:40:18] and langraph handles the flow between
[05:40:20] model calls and tool execution
[05:40:22] seamlessly. Here we also use conditional
[05:40:25] ages, the graph that chooses whether the
[05:40:28] model should stop or continue based on
[05:40:30] whether there are tool calls remaining.
[05:40:33] This introduces intelligent flow
[05:40:34] control, something that was often more
[05:40:37] complex to manage in Langen. By
[05:40:39] combining the reasoning power of
[05:40:41] language model with the precision of
[05:40:43] actual code functions, we're moving
[05:40:45] closer to a truly capable AI system,
[05:40:48] ones that can both understand and act.
[05:40:51] And by the end of this video, you'll see
[05:40:53] how the model calls the right tools,
[05:40:56] performs the operation, and keeps
[05:40:57] reasoning step by step just like an
[05:40:59] autonomous agent. And this is where
[05:41:01] Langra begins to bridge the gap between
[05:41:03] intelligent thinking and practical
[05:41:05] agent. So without any delay, let's dive
[05:41:08] in and how and see how your AI can now
[05:41:12] think, plan, and calculate all on its
[05:41:15] own. So now let's jump to the code.
[05:41:20] I'm going to create a new file here
[05:41:24] 6 tool calls ipv
[05:41:30] first of all we'll write the imports
[05:42:02] from lang code messages we'll have
[05:42:07] uh dot messages
[05:42:10] h import
[05:42:13] I'll have a base message
[05:42:15] I'll and I'll have a system message
[05:42:20] now about the model this will be my
[05:42:23] model and then from langen core
[05:42:28] dot tools
[05:42:30] I'll import
[05:42:32] tool
[05:42:34] then from lang graph
[05:42:39] dot graph
[05:42:42] dot messages
[05:42:46] I'll import
[05:42:48] add messages
[05:42:51] then finally from langra
[05:42:55] dot pre-built
[05:42:56] import
[05:42:58] download.
[05:43:06] So this should be message not messages.
[05:43:09] Now everything is imported. Let's run
[05:43:11] this.
[05:43:16] And this is running. First of all, we'll
[05:43:18] define
[05:43:20] our model here or first of all we'll do
[05:43:22] the credential. then define our model as
[05:43:26] Gemini 2.5 flash and then run this. In
[05:43:31] the next node, I'm going to define my
[05:43:34] agent state.
[05:43:36] My agent state will be of type type dict
[05:43:41] and then inside this I'll have messages
[05:43:45] which will be an annotated
[05:43:49] sequence of base message and then
[05:43:54] in between I'll write add
[05:43:58] messages function. Okay. Now I'm going
[05:44:01] to create a few tools. uh in this
[05:44:03] particular case we're going to write
[05:44:06] four different functions or four
[05:44:07] different tools for addition,
[05:44:08] subtraction, multiplication as well as
[05:44:11] division. So now we'll create the
[05:44:12] functions for them. So add the rate tool
[05:44:16] def
[05:44:18] integer b integer
[05:44:23] this will also return an integer here.
[05:44:25] Let me
[05:44:28] write down the dock string.
[05:44:30] This will
[05:44:32] add two numbers
[05:44:36] then return a + b. Similarly, we'll do
[05:44:39] the same for subtraction but I'm I'm
[05:44:41] just going to copy this code multiple
[05:44:44] times. Subtraction multiplication as
[05:44:46] well as division.
[05:44:48] Let me change the function name.
[05:44:52] This will be sub the two numbers. So
[05:44:55] subtract the two numbers. Here we'll
[05:44:57] have a minus b.
[05:45:00] This will multiply the two numbers
[05:45:05] multiply
[05:45:07] we'll have a into b and then this will
[05:45:10] divide the two numbers
[05:45:15] divide and then a / b. Okay. So these
[05:45:19] will be my tools uh uh for this
[05:45:22] particular
[05:45:24] system. Now I'm going to
[05:45:27] list all my tools under this my tools
[05:45:30] list. So add s mult and div.
[05:45:38] Now after this what I'm going to do is
[05:45:40] I'm going to bind my tools
[05:45:43] with the lm. So okay we have our model.
[05:45:46] So model dotbind
[05:45:51] tools.
[05:45:53] Let's say my tools.
[05:45:57] Okay.
[05:46:00] Now we'll create our nodes here. So
[05:46:03] write the function for those nodes. So
[05:46:05] model call will be our first node here
[05:46:08] which will have have a type agent state
[05:46:11] and it will also return
[05:46:14] agent state.
[05:46:17] So the system prompt
[05:46:20] is going to be
[05:46:22] a system message
[05:46:28] uh and its content will be you are an AI
[05:46:33] assistant
[05:46:34] please answer my query to the best of
[05:46:39] your ability.
[05:46:42] Okay.
[05:46:44] Now I'll pro I will provide the inputs.
[05:46:47] So inputs will be our system prompt
[05:46:52] plus
[05:46:56] the state passages that we have.
[05:47:00] Then I'll invoke the model with this
[05:47:03] inputs
[05:47:08] uh
[05:47:10] inputs and then finally I'm going to
[05:47:13] return
[05:47:17] uh messages.
[05:47:22] So this is going to be state messages
[05:47:26] plus
[05:47:31] response.
[05:47:38] Okay,
[05:47:40] I will have another router node here
[05:47:43] which would say should
[05:47:47] continue.
[05:47:49] It will contain
[05:47:52] agent state as its parameter
[05:47:56] and we'll have message equals to state
[05:48:00] messages
[05:48:04] I will pick up the last message from
[05:48:06] here.
[05:48:08] So message minus one
[05:48:11] and then and then if the last message
[05:48:14] does not contain any tool calls
[05:48:17] last message does not contain any tool
[05:48:20] calls
[05:48:22] then I will
[05:48:26] take uh the flow to end
[05:48:30] or the conversation end or else
[05:48:34] I will continue with the conversation.
[05:48:39] so as to allow the model to call those
[05:48:41] tools here. Okay. So these are my nodes.
[05:48:45] Let me run this. Create a graph from
[05:48:48] state graph.
[05:49:03] It will say graph dot add node
[05:49:09] model
[05:49:12] call will
[05:49:14] will be represented by model call
[05:49:16] function.
[05:49:19] Then
[05:49:22] here I'll have a tool node object from
[05:49:25] class tool node and then
[05:49:29] it will hold all of my tools.
[05:49:32] from my tools list
[05:49:35] and I'm going to add a node
[05:49:41] called tools
[05:49:44] using
[05:49:46] two load function. Okay. So now I'm
[05:49:49] going to add edges. So graph dot add age
[05:49:51] edge. The first will be from start to
[05:49:54] model call.
[05:49:58] The second will be a conditional edge.
[05:50:06] It will go from model call
[05:50:12] to the function should continue.
[05:50:23] And if if the result from should
[05:50:26] continue is end then it will end
[05:50:30] or else if it is continue
[05:50:34] then it will call
[05:50:36] tools.
[05:50:41] So I'll have one more uh edge here.
[05:50:43] Graph dot add edge tools to model call.
[05:50:50] And I should have one more I guess.
[05:50:52] graph dot add age edge
[05:50:55] uh model call
[05:50:58] to end.
[05:51:01] Let me compile this
[05:51:04] and then see the graph.
[05:51:08] So if you visualize the graph you can
[05:51:09] see that we start from here we go to
[05:51:12] model call. If it is a tool call then we
[05:51:14] go to continue and then call the tool
[05:51:16] and again we go to the model call. Or
[05:51:19] else if there are no more tool calls
[05:51:22] tool calls involved then we go to the
[05:51:23] end.
[05:51:25] I'm going to create a function here
[05:51:26] called print stream.
[05:51:30] This will contain a stream object.
[05:51:34] So for s in stream
[05:51:40] I will pull up the last message.
[05:51:47] So
[05:51:50] if is instance
[05:51:52] message message
[05:52:00] then I will print the message
[05:52:06] or else
[05:52:10] message.
[05:52:11] Print.
[05:52:14] Okay. Now uh this is going to show the
[05:52:19] stream stream of operation that will
[05:52:22] happen while our tool is being called.
[05:52:26] So now uh we'll define our input
[05:52:31] input. So input will be messages
[05:52:37] and then it will be from our
[05:52:41] user
[05:52:43] and the message will be add 40 and 12
[05:52:48] and then
[05:52:49] calculate the product
[05:52:53] with six.
[05:52:58] also
[05:53:06] tell me a joke at the end.
[05:53:11] Okay, we will not do 40 and 12. we'll do
[05:53:15] uh maybe
[05:53:18] two and four and then uh and and then
[05:53:22] the product with six and then [snorts]
[05:53:24] at at last I'm also asking the model for
[05:53:27] a joke. So what should happen here is
[05:53:30] this particular part should be done
[05:53:33] using our tools and then for this
[05:53:35] particular part the model uh should call
[05:53:38] the LLM and then the LLM should a should
[05:53:43] be able to generate the joke without
[05:53:45] using any tools because there are no
[05:53:47] tools present to uh generate the joke.
[05:53:50] Now at last what I'm going to do here is
[05:53:52] print stream
[05:53:55] print stream. Uh
[05:53:59] so bot dot streamm
[05:54:04] stream. Now inside this I'm going to
[05:54:06] pass input
[05:54:09] and then stream load.
[05:54:12] Sorry there should be a comma here. So
[05:54:14] stream node
[05:54:17] equals to values.
[05:54:22] Okay. Now this p brings us to the end of
[05:54:26] our program. If we run this,
[05:54:30] we should see a stream of operation that
[05:54:33] has been happening uh in order to
[05:54:36] uh fulfill our current operation. But I
[05:54:39] guess we have an error. Let's see what
[05:54:40] the error is. Okay, I've removed this uh
[05:54:44] last part. So, so let me run it again.
[05:54:48] Okay, I think I might have found the
[05:54:50] error here. So what I'm going to do here
[05:54:53] is node name comma node value equals to
[05:54:58] next iteration iterator s dot items
[05:55:05] and inside this I'm going to check if
[05:55:08] messages
[05:55:12] is present in
[05:55:17] node values
[05:55:22] And uh if it is present
[05:55:27] uh then what I'm going to do is
[05:55:37] so message equals to message one and
[05:55:40] then
[05:55:43] node value equal to node messages minus
[05:55:46] one sorry Okay,
[05:55:49] sorry [snorts] I missed this
[05:55:51] uh node value.
[05:55:54] So misses so misses minus one. Let me
[05:55:57] run this again.
[05:56:00] What happened here? Okay, extra bracket.
[05:56:06] So as you can see
[05:56:09] uh our query is taken and then these
[05:56:13] four first two numbers are taken as two
[05:56:15] and four here and then pass to the add
[05:56:19] uh add tool. The result is six. Then uh
[05:56:24] both of these six and then and then the
[05:56:27] following six is taken as a and b and
[05:56:28] then the multiplication tool is called
[05:56:30] and then the product is calculated and
[05:56:33] at last the joke is also uh generated.
[05:56:37] So this is how we can implement our own
[05:56:40] tools uh in case of uh llm in langraph.
[05:56:46] In the last video, we explored how
[05:56:48] Langraph lets your AI not just think but
[05:56:52] act. We saw how to connect tools like
[05:56:54] addition, subtraction, multiplication,
[05:56:57] division so that the model could reason,
[05:56:59] calculate, and decide its own next
[05:57:01] steps. Now, we're taking that idea even
[05:57:04] further. In this video, we're building
[05:57:06] something more practical, a document
[05:57:08] editing agent powered by Langraph. We'll
[05:57:11] call it an email drafter. Your
[05:57:13] intelligent writing assistant that can
[05:57:15] update, modify, and then save document
[05:57:18] automatically using AI and tools. But
[05:57:23] before we jump into the code, we'll try
[05:57:25] to understand what's happening
[05:57:26] conceptually here. Our agent can combine
[05:57:30] LLM reasoning using Gemini tool nodes
[05:57:33] for doing real world actions and
[05:57:35] conditional graph control to keep
[05:57:37] interacting until the document is saved.
[05:57:40] We'll define two tools here. Update and
[05:57:42] save. Update to modify the document
[05:57:46] context content dynamically and save to
[05:57:49] store the final version into a txt file.
[05:57:52] The system prompt that we're going to
[05:57:55] provide will ensure the AI always knows
[05:57:59] what the current document state is and
[05:58:01] the langraph manages when to loop or
[05:58:03] exit depending on whether the user has
[05:58:06] saved the document or not. This
[05:58:08] structure will make your AI truly
[05:58:10] stateful, capable of handling multiple
[05:58:13] user interactions over time and goal
[05:58:15] oriented. Something that's much harder
[05:58:18] to achieve in plain lang. By the end of
[05:58:20] this video, you'll see how Langraph
[05:58:23] turns your language model into a
[05:58:24] functional writing agent. One that just
[05:58:27] doesn't respond, but works with you to
[05:58:29] create and save real content. So, we'll
[05:58:32] dive in and bring in Raptor to life. So
[05:58:36] I'm going to create a new file here.
[05:58:40] Call it email
[05:58:44] crafter
[05:58:46] ipy nv.
[05:58:50] Write down the imports.
[05:59:45] Okay, we'll load the credential first
[05:59:47] and then we'll also uh define our Linear
[05:59:54] run this
[05:59:59] and then we'll have a global variable
[06:00:05] a global variable to store
[06:00:08] document content.
[06:00:11] So we'll write document content equals
[06:00:13] to an empty string.
[06:00:16] >> Now we'll have our agency class.
[06:00:20] Any
[06:00:23] other messages will be of type annotated
[06:00:28] sequence uh paste message and then add
[06:00:32] messages.
[06:00:35] Now as I said I'm going to define two
[06:00:37] different tools here. So the first tool
[06:00:40] will be update.
[06:00:43] Uh we'll have a cont a string content
[06:00:45] inside this and then we'll also return a
[06:00:48] string content here.
[06:00:50] So I'll write down the dock string.
[06:00:52] Sorry for this.
[06:00:56] So this is going to update the document
[06:01:00] with the provided
[06:01:03] content.
[06:01:10] Okay. So I'll access the global document
[06:01:13] content here. Then uh
[06:01:16] what I'm going to do is
[06:01:20] document content
[06:01:23] equal to the content that I get here.
[06:01:27] And then I'm going to return a string
[06:01:31] here.
[06:01:33] Uh which says document has
[06:01:38] been updated
[06:01:41] successfully.
[06:01:43] The current
[06:01:45] content is
[06:01:53] document content.
[06:01:55] Okay. So this is my first function or my
[06:01:59] first tool function that I have.
[06:02:02] Next, I'm going to create another tool
[06:02:06] called save where I'll provide a file
[06:02:08] name in string format and then I will
[06:02:12] return a string here.
[06:02:15] Write down the doc string. Save the
[06:02:18] current
[06:02:19] document to
[06:02:22] to text file and finish the process.
[06:02:28] The arguments that I'll be passing here
[06:02:30] is the file name. So which will indicate
[06:02:34] the name of the
[06:02:38] text file.
[06:02:42] So again I'm going to access the global
[06:02:44] document content.
[06:02:52] Then if there is no file name
[06:02:55] uh created then um then I will provide a
[06:03:00] file name txt file here.
[06:03:05] Then I'll try to open this file
[06:03:12] as file.
[06:03:16] uh
[06:03:19] I'll try to write the document content
[06:03:23] into this file
[06:03:28] and then print document saved
[06:03:30] successfully as file name
[06:03:36] and then also return the same. If we
[06:03:39] have an exception
[06:03:42] then I'm going to uh return an
[06:03:47] error message here.
[06:03:49] Okay. So these are my two tools that
[06:03:51] I'll be using.
[06:03:52] Finally I'll create a list of my
[06:03:55] available tools. So the first one is
[06:03:58] update
[06:04:00] and then the second one is save.
[06:04:03] I am going to bind my tools.
[06:04:06] I bind the lm using my tools.
[06:04:11] So my tools and then I'm going to create
[06:04:13] a tool tool node object
[06:04:17] using my tools here.
[06:04:23] Okay. Now I need to define my nodes. So
[06:04:26] our first node is going to be our agent.
[06:04:30] It will contain agent state
[06:04:33] type. It will also return
[06:04:37] and agent state.
[06:04:40] So what I'm going to do here is I'm I'm
[06:04:43] going to provide a system prompt. Let me
[06:04:45] just copy this prompt from somewhere.
[06:04:47] System. Okay. I'll just copy this entire
[06:04:49] thing from somewhere so that uh you can
[06:04:52] pause the video and then see what the
[06:04:56] actual prompt is.
[06:04:59] Okay. So, the prompt is uh you are
[06:05:04] you are an email drafter,
[06:05:09] a helpful writing assistant. You're
[06:05:10] going to help uh help the user update
[06:05:14] and modify document. If the user want to
[06:05:16] update or modify content, use the update
[06:05:19] tool. And then if the user want to save
[06:05:22] and finish, use the save tool. Okay. So,
[06:05:24] this is done. the current document uh
[06:05:26] content is also passed here. After this,
[06:05:28] what I'm going to do is
[06:05:31] I'm going to
[06:05:34] check
[06:05:37] if
[06:05:38] user message is not provided.
[06:05:41] And based on this, I am ready to help
[06:05:46] you
[06:05:49] update a document.
[06:05:52] what would you like to create? Okay,
[06:05:56] this is the first message that the user
[06:05:57] will be seeing and then I am going to
[06:06:00] encode this inside
[06:06:05] human message
[06:06:08] or else if there is already a
[06:06:12] already some content that has been
[06:06:14] generated then the user input is going
[06:06:16] to be
[06:06:20] so this should be an input
[06:06:29] Uh, what would you sorry
[06:06:34] what
[06:06:36] would you like
[06:06:38] to do
[06:06:40] with this document?
[06:06:52] Then I will print
[06:07:02] user
[06:07:06] and then print the user input.
[06:07:19] then put it inside the
[06:07:22] user message again. Okay, now these two
[06:07:25] states are done.
[06:07:28] What I'm going to do is I'm going to
[06:07:30] combine combine the system prompt as
[06:07:33] well as the user message that we have.
[06:07:36] So this will go inside all messages. It
[06:07:39] will have
[06:07:41] system prompt plus list of state
[06:07:43] messages plus user message. Now I'm
[06:07:47] going to invoke the model response equal
[06:07:49] to model dot invoke
[06:07:52] uh invoke using all messages.
[06:07:57] Sorry, it's model year.
[06:08:08] Okay. Then I'm going to print out AI
[06:08:12] response here
[06:08:18] or just write down AI
[06:08:22] uh and then print out
[06:08:25] response.content. content.
[06:08:30] Now, now I'm going to check uh if there
[06:08:33] is any tool calls uh provided in this
[06:08:36] particular
[06:08:38] response. So, if has
[06:08:42] TTR response
[06:08:47] to calls
[06:08:50] and response
[06:08:54] dot
[06:08:57] Sorry for the autocomplete part.
[06:08:59] response.tool
[06:09:01] calls
[06:09:04] then I will print which tool is being
[06:09:07] used uh right now.
[06:09:11] So
[06:09:15] invoking tool
[06:09:19] please be careful with the brackets
[06:09:20] here.
[06:09:24] TC
[06:09:27] uh tool name
[06:09:31] for TC in response. call
[06:09:37] and then I'm going to return
[06:09:42] the messages
[06:09:45] uh which will be the list
[06:09:49] of state messages
[06:09:52] of state messages
[06:10:00] plus
[06:10:13] user message as well as the response
[06:10:16] again. I I think I missed a bracket
[06:10:19] here. Okay, this one extra bracket
[06:10:21] extra. Okay, so this is done. So this is
[06:10:24] for for our agent
[06:10:27] uh node here. Now I'm going to create a
[06:10:31] router node.
[06:10:34] So router node will be shared
[06:10:43] continue.
[06:10:49] It will contain agent state
[06:10:54] and then it will return a string.
[06:10:57] So the doc string for this determine if
[06:11:00] we should continue or end the
[06:11:04] conversation.
[06:11:09] Okay. So first of all access our state
[06:11:11] messages
[06:11:17] and then
[06:11:19] if there is nothing then we should
[06:11:21] continue
[06:11:26] or else if there is something inside
[06:11:28] this
[06:11:30] then we reverse the list list
[06:11:39] And then check uh check the instance uh
[06:11:44] and see if it is save or like uh
[06:11:52] if the tool call name is
[06:11:55] present is in the form of save. So is
[06:11:57] instance
[06:12:00] message
[06:12:02] it is message right?
[06:12:06] Okay. some message
[06:12:10] uh and then
[06:12:15] to message
[06:12:17] the spelling is wrong here. So for each
[06:12:20] instance message and then two message
[06:12:26] and saved
[06:12:29] in message dot content dot lower
[06:12:34] this is not complete
[06:12:38] and
[06:12:40] document in
[06:12:50] message.contain.l
[06:12:52] then we return end or else we return
[06:12:55] continue.
[06:12:57] Okay. So our router node is also fixed.
[06:13:00] So what we're basically saying is if we
[06:13:02] have if we don't have anything then we
[06:13:05] should continue.
[06:13:07] If we have save then we should end the
[06:13:10] flow or else if we don't have save or
[06:13:13] like if we have update then again we
[06:13:14] should continue the flow. Okay. So this
[06:13:17] is done. Save this.
[06:13:20] Call our state graph.
[06:13:23] Uh add a node.
[06:13:31] This will point to our agent. Add
[06:13:33] another node.
[06:13:38] I'll have tools.
[06:13:40] Now I'll start adding ages.
[06:13:45] So from start we go to agent and then
[06:13:49] from agent we go to tools. Then after
[06:13:51] this I'm going to add conditional ages.
[06:13:53] Here
[06:13:58] we'll start from tools.
[06:14:03] We'll go to should continue function
[06:14:08] and then from should continue function
[06:14:10] we have two options.
[06:14:15] If we have continue we go to agent. If
[06:14:17] we have end then we end our flow.
[06:14:23] So let me compile this graph
[06:14:25] graph.compile and then print out our
[06:14:29] state graph here. So as you can see we
[06:14:32] start from here we go to agent
[06:14:35] we go to tools. If we have to keep on
[06:14:39] updating our document then we continue
[06:14:41] this particular loop here from from
[06:14:44] agent to tools and then tools to agent
[06:14:46] and then once and then once we call the
[06:14:49] save tool then we go to the end of the
[06:14:51] conversation.
[06:14:56] Okay. Now I'm going to create some
[06:15:00] function for prints.
[06:15:02] So print messages it will contain our
[06:15:07] messages inside this
[06:15:11] function made to print the messages
[06:15:16] in more
[06:15:20] readable format.
[06:15:26] Okay. So if not messages we we just
[06:15:30] return
[06:15:32] uh if nothing is there we just uh return
[06:15:37] empty. But if we have messages and then
[06:15:41] we especially focus on the last three
[06:15:43] messages that we have
[06:15:48] then what I'm going to do is I'm going
[06:15:51] to check if
[06:15:54] is instance uh is
[06:15:58] instance message is a tool message
[06:16:04] then I'm going to print out uh tool
[06:16:07] message result content.
[06:16:13] Now to run the document agent,
[06:16:20] I'll create a new function.
[06:16:23] So at first
[06:16:25] the state is going to be
[06:16:29] messages and then empty message.
[06:16:34] Then let me uh run this. So first step
[06:16:36] in port dot stream state
[06:16:44] uh if messages in step
[06:16:48] then print messages step messages
[06:16:53] and then it's done and then at last we
[06:16:57] can print out conversation ended.
[06:17:00] Okay, so let me run this
[06:17:08] and then finally call run
[06:17:11] document agent.
[06:17:14] Now if we run this so
[06:17:19] what it asks me is I'm ready to help you
[06:17:22] update a document. What would you like
[06:17:24] to create? So write me an
[06:17:29] write me a leave requesting
[06:17:34] email for 22nd October
[06:17:39] October uh October sorry for the
[06:17:43] spelling
[06:17:44] October 2025 Five.
[06:17:57] Me an email.
[06:18:02] Uh, okay. The AI says, "What should the
[06:18:05] email say?" Uh,
[06:18:08] it should be about
[06:18:11] leave application.
[06:18:15] So the AI agent does write me an email.
[06:18:19] Now I want to uh replace the state start
[06:18:23] date replace start date
[06:18:27] uh to 22nd
[06:18:30] October and uh end date to 23rd October
[06:18:37] 2025.
[06:18:39] Let me save this file directly.
[06:18:45] Uh or I can say the email should include
[06:18:52] my name as Abby
[06:18:59] and then it does uh replace my name here
[06:19:02] as Abby. So
[06:19:05] everything is done. Uh
[06:19:08] what I need to do is I need to save this
[06:19:11] file. So if I say save the file now,
[06:19:20] save it.
[06:19:24] So uh it asks me for a file name. So I
[06:19:27] can say
[06:19:29] uh
[06:19:31] email draft
[06:19:37] and then if we see uh somewhere in our
[06:19:42] folder location then we have then we see
[06:19:44] that we have an email draft file uh
[06:19:47] where the AI generated content is saved
[06:19:49] here. So this is uh
[06:19:54] all about the email drafter application.
[06:19:56] I've made a few changes uh here in this
[06:20:00] particular part here as well as
[06:20:03] in this particular uh cell here. So
[06:20:07] please go through the changes and then
[06:20:09] uh I hope it runs on your end as well.
[06:20:12] So in this video we've seen uh how we
[06:20:17] can use lang graph as well as our real
[06:20:19] world AI model uh to
[06:20:24] to invoke the tools that we have and and
[06:20:27] then uh do something meaningful for us.
[06:20:30] In this video we'll see how we can build
[06:20:32] our rag agent using langra. So let's
[06:20:35] start our video by creating a new file
[06:20:41] 8_rag
[06:20:44] agent ipy nbv.
[06:20:47] Well for this rag agent I'm going to use
[06:20:49] a file uh I have a pdf file uh that I'll
[06:20:53] be using. So let me paste that file here
[06:20:55] first.
[06:21:00] So this is a stock PDF file. uh I'll be
[06:21:03] using
[06:21:06] using the data from this particular file
[06:21:08] uh for this rag agent here. Okay. So now
[06:21:11] first of all start with imports.
[06:21:41] import type dictotated
[06:21:46] and sequence.
[06:21:49] Now from langen code I'm going to import
[06:21:51] something called human messages tool
[06:21:55] messages system message and base
[06:21:57] message. So import human message. Uh I
[06:22:00] don't need AI message. I I'll need a
[06:22:02] tool message
[06:22:04] and a base message and a system message
[06:22:09] from operator uh
[06:22:13] import
[06:22:14] add as add messages.
[06:22:20] Uh then I'll open the model or import
[06:22:23] the model import chat Google generative
[06:22:26] AI as well as
[06:22:29] the Google uh Google generative AI
[06:22:33] embeddings.
[06:22:36] Then from langen community
[06:22:39] I'll import pipdf loader
[06:22:42] to open the pdf file.
[06:22:46] I PDF loader.
[06:22:50] Then we'll import recursive text sorry
[06:22:53] recursive character text splitter line
[06:22:55] chain.ext splitter import
[06:22:58] recursive character text splitter.
[06:23:02] Then for the vector database I'm going
[06:23:04] to use chroma
[06:23:07] import chroma.
[06:23:11] And finally for the tool part from lang
[06:23:14] core
[06:23:16] I'm going to import tool
[06:23:20] load the credential first
[06:23:25] then I'll load my model here
[06:23:30] the model will not be Gemini pro uh I'll
[06:23:33] remove the temperature for now
[06:23:36] but it is going to be Gemini 2.5
[06:23:39] flash model and for the embedding model
[06:23:46] I'll be using
[06:23:57] uh
[06:24:00] so model equals to
[06:24:03] model/
[06:24:05] Gemini
[06:24:08] embedding
[06:24:10] 001. Okay, let me run this
[06:24:14] first cell
[06:24:17] and the cell is running.
[06:24:23] Okay, there is some uh error here. Let
[06:24:26] me see what the error is. So, Gemini 2.5
[06:24:30] flash should be correct.
[06:24:33] Okay, it should not be model name but it
[06:24:36] should be model
[06:24:38] uh rerun it again.
[06:24:42] Okay, the model is imported. I'm going
[06:24:44] to copy this uh not put it here but put
[06:24:48] the PDF file inside this line graph
[06:24:51] folder so that it can be easily accessed
[06:24:54] by the
[06:24:56] notebook file present in this folder. So
[06:24:58] PDF
[06:25:00] path equals to stock
[06:25:04] PDF. So this is going to be my PDF path.
[06:25:08] And then we'll try to load the file
[06:25:11] first.
[06:25:13] So for that what I'm going to do is I'm
[06:25:15] going to check if the file exists or
[06:25:18] not.
[06:25:21] path.exist PDF path. But like if it does
[06:25:25] exist then I'm going to do PDF loader
[06:25:27] equals to pi PDF loader PDF path.
[06:25:32] Okay, this is also running.
[06:25:35] Now I'm going to load the pages from the
[06:25:37] PDF path. So load the pages
[06:25:41] from the PDF. Uh
[06:25:44] so I'll put it inside uh try block PDF
[06:25:48] loader.load.
[06:25:51] Uh let's also print something. So
[06:25:57] a PDF has been loaded and
[06:26:01] has
[06:26:05] a certain number of pages. It if it
[06:26:08] cannot be loaded then we will load an
[06:26:11] exception and then print out our
[06:26:14] exception here. an error occurred while
[06:26:16] loading PDF
[06:26:18] and then
[06:26:20] simply raise an exception.
[06:26:26] So our PDF has been loaded and then it
[06:26:29] contains nine pages.
[06:26:32] Now what we're going to do is you we are
[06:26:35] going to use our splitter here. So text
[06:26:37] splitter
[06:26:42] equals to recursive character text
[06:26:44] splitter
[06:26:46] uh the chunk size is going to be 1,000
[06:26:49] and then the chunk overlap is going to
[06:26:50] be 200. That's okay. I'll keep that for
[06:26:53] now. But you can change the values
[06:26:54] according to your need. Uh if you want
[06:26:57] to make
[06:26:59] make smaller chunks more smaller chunks
[06:27:01] then you please reduce the chunk size.
[06:27:04] uh
[06:27:06] and then uh if you want to uh overlap
[06:27:09] some information between chunks then you
[06:27:11] uh increase the value of this chunk
[06:27:13] overlap.
[06:27:17] So now let me split the pages. So pages
[06:27:21] split equals to textsplitter dotsplit
[06:27:24] document pages.
[06:27:28] So if we want to see total number of
[06:27:30] chunks then we can print it print it out
[06:27:34] and then we can see that we have now uh
[06:27:37] divided it into 24 chunks. If we reduce
[06:27:40] this chunk size to maybe 500 then we
[06:27:44] should see that the chunk uh that our
[06:27:48] chunks are or the total chunks number
[06:27:52] has should be increased here. So if we
[06:27:56] keep it to 500 then we go to 60 chunks
[06:27:58] but right now I'll keep it to 1,000 and
[06:28:01] then we have 24 chunks. Okay. Now
[06:28:04] [snorts] we go to our vector database
[06:28:06] part.
[06:28:08] So for vector database I'm going to give
[06:28:10] a collection name. So collection name is
[06:28:12] going to be stock market.
[06:28:16] So we'll try to create a vector store
[06:28:18] from this one. So vector store equals to
[06:28:22] Roma dot from documents.
[06:28:26] So document equal to page split.
[06:28:30] For embeddings, I'm going to use my
[06:28:32] embedding model. And then for collection
[06:28:34] name, I'm going to use my collection
[06:28:35] name.
[06:28:39] And then finally, uh we're going to see
[06:28:42] our success message here. But if we run
[06:28:45] into any kind of exception, then we'll
[06:28:47] print an exception. and then raise some
[06:28:50] error.
[06:28:51] So if we run this,
[06:28:54] it will take some time uh to be
[06:28:57] vectorzed but our vector store has been
[06:29:00] successfully created means the try block
[06:29:02] has been executed successfully.
[06:29:04] Okay. [snorts] Now we'll define our
[06:29:07] retriever path. So, so for retriever
[06:29:11] we'll do uh vector store dot as
[06:29:16] retriever
[06:29:19] and we'll define our search type. Search
[06:29:21] type will be based on similarity and
[06:29:23] then the search keyword arguments will
[06:29:25] be uh we'll keep it with three for now.
[06:29:28] So the retriever part is also executed.
[06:29:30] Now we define our tool.
[06:29:35] This tool will be our retriever tool
[06:29:42] which will [snorts] contain an query of
[06:29:44] perform string and then it will again
[06:29:48] return an string here
[06:29:52] provide a dock string for this. So this
[06:29:54] tool
[06:29:56] searches and returns
[06:29:59] information from the stock
[06:30:02] market performance
[06:30:06] performance report
[06:30:09] document. Okay,
[06:30:15] we're going to invoke our retriever
[06:30:17] using our query. So retriever.
[06:30:22] So retriever dot invoke
[06:30:26] query.
[06:30:29] So if nothing is found uh
[06:30:33] with with uh similarity to query in our
[06:30:37] document then we print out or we return
[06:30:41] no relevant information found or if
[06:30:44] something is found then we are going to
[06:30:46] embed this in a list.
[06:30:49] for I do in enumerate documents. So I'm
[06:30:54] going to append everything inside this
[06:30:57] uh results list here. And then what I'm
[06:31:01] going to do is I'm going to uh convert
[06:31:05] this list in string form.
[06:31:11] Now we only have one tool which I will
[06:31:14] wrap inside this list.
[06:31:16] Then I'm going to bind my llm uh using
[06:31:20] this
[06:31:21] tool uh with the help of the function
[06:31:24] bind tool
[06:31:28] and then run this.
[06:31:30] Now we'll have our class agent state.
[06:31:33] It'll be of type dict uh type dict
[06:31:38] I'll have messages which will be an
[06:31:41] annotated sequence of base message. And
[06:31:44] then here what we want to do is we want
[06:31:46] to keep adding our
[06:31:49] messages. So I'm going to use this add
[06:31:51] messages function.
[06:31:55] And then I will define a router function
[06:31:59] should continue state
[06:32:03] should continue state
[06:32:06] agent state. uh this will
[06:32:12] return the tool calls if it has. So
[06:32:16] what it is going to do it check
[06:32:20] if the last message
[06:32:23] contains
[06:32:25] tool calls.
[06:32:28] So for that I'm going to see my last
[06:32:31] message
[06:32:33] and then I'm going to return
[06:32:40] the result
[06:32:43] uh tool calls and len uh l tool calls is
[06:32:50] greater than zero. Okay. So this is also
[06:32:52] done.
[06:32:54] Now what I'm going to do is I'm going to
[06:32:55] write a system prompt which I'm going to
[06:32:57] copy uh from my source. So this is my
[06:33:02] system prompt. You are an intelligent AI
[06:33:04] assistant who answers uh questions about
[06:33:06] the stock market performance in 2024
[06:33:09] based on the PDF document loaded in into
[06:33:11] the knowledge base. Use the retriever
[06:33:13] tool available to answer questions about
[06:33:15] the stock of data. You can make multiple
[06:33:17] calls if needed. If you need to look up
[06:33:19] some information before asking a
[06:33:20] follow-up question, you're allowed to do
[06:33:22] that. Please always site the specific
[06:33:23] parts of the document you use in our
[06:33:25] answers.
[06:33:27] So now what I'm going to do next is run
[06:33:29] this and then I'm going to create a tool
[06:33:33] state
[06:33:35] and then here I'm going to do our
[06:33:40] tool dot name
[06:33:45] uh our tool for our tool in tool.
[06:33:50] So it should be tool right? Uh yeah in
[06:33:54] tool
[06:33:58] run this again. So this is also running.
[06:34:01] Now we'll define our llm agent.
[06:34:04] So def call [snorts] llm
[06:34:07] it will contain agent state.
[06:34:11] It will also return agent state
[06:34:20] object.
[06:34:25] So function to call the llm with the
[06:34:28] current state. So here what I'm going to
[06:34:32] do is I'm going to make a list of my
[06:34:35] messages. So, list of state
[06:34:40] messages.
[06:34:42] Then I'm going to convert this into a
[06:34:45] system message or I'm going to append
[06:34:49] append my uh system prompt as well as
[06:34:52] the
[06:34:54] messages that we have. And finally,
[06:34:56] we're going to uh invoke our LLM using
[06:35:02] the combined method that we have.
[06:35:06] Okay, so this is done.
[06:35:09] Uh I don't think I need to mention this
[06:35:11] messages.
[06:35:13] So I can just do message here.
[06:35:16] And then what I'm going to do is I'm
[06:35:18] going to return message
[06:35:21] uh messages
[06:35:25] list of [snorts] message.
[06:35:29] Okay,
[06:35:30] this is also running.
[06:35:33] [snorts]
[06:35:35] Now we create one more function for our
[06:35:37] people agent. So def take action
[06:35:43] state agent state.
[06:35:47] It will also return agent state object.
[06:35:50] So what this function will do is this
[06:35:54] function to execute
[06:35:57] tools from the
[06:36:00] llm's response.
[06:36:03] So for this what I'm going to do is I'm
[06:36:06] going to check uh if if we contain any
[06:36:10] tool calls from the lm. So tool calls
[06:36:14] equals to system message minus one for
[06:36:16] tool calls. If there is then we'll
[06:36:19] append everything inside results. So now
[06:36:22] we'll look through our tool calls.
[06:36:32] So we try to understand what tool is
[06:36:35] being called here. So print
[06:36:38] f executing tool name with certain
[06:36:41] input.
[06:36:46] Uh
[06:36:49] so if not
[06:36:52] t name
[06:36:55] in date
[06:36:58] uh
[06:37:01] I'll do tool not found
[06:37:11] or I can just keep keep it inside. the
[06:37:15] result uh but it's okay uh I can keep it
[06:37:18] like this for now but uh I don't want to
[06:37:21] directly append this so what I'm going
[06:37:23] to do here is I'm going to do a result
[06:37:26] equals to
[06:37:29] uh tool not found
[06:37:33] else
[06:37:35] uh I'm going to append this inside the
[06:37:40] results using the tool name
[06:37:44] so D name
[06:37:51] D name dot
[06:37:54] dot
[06:37:56] invoke
[06:37:58] D ars
[06:38:02] dot get
[06:38:06] then print
[06:38:10] uh tool result here.
[06:38:19] Then what I'm going to do is I'm going
[06:38:21] to append the tool message that we get
[06:38:25] from the above loop.
[06:38:32] So here results dot append
[06:38:36] bool message.
[06:38:40] So tool call id equals to t
[06:38:50] id
[06:38:52] uh
[06:38:55] what else? name equals to D name and
[06:39:00] uh content
[06:39:02] content equals to str
[06:39:07] result.
[06:39:19] This should be inside the for loop.
[06:39:20] Sorry.
[06:39:22] And finally I'm going to print tools
[06:39:26] execution
[06:39:28] tools executed and then return
[06:39:35] the agent state response.
[06:39:38] Okay. Now we build our graph using state
[06:39:41] graph. State graph agent state.
[06:39:46] add our first node graph dot add node uh
[06:39:50] which will be our
[06:39:53] add node which is be lm represented by
[06:39:56] all lm function.
[06:39:59] Then the second node will be
[06:40:03] uh add
[06:40:05] node. The second node will be retriever
[06:40:07] agent
[06:40:11] which will be represented by take action
[06:40:13] function
[06:40:18] and then the first edge will be craft
[06:40:23] craft dot add edge
[06:40:27] and edge it will go from start.
[06:40:31] I've not imported start I guess. So let
[06:40:34] me also input start.
[06:40:39] So the first node will be from start to
[06:40:42] lm.
[06:40:46] Then what I'll do is I'll add a
[06:40:48] conditional edge.
[06:40:51] Add conditional age. This will go from
[06:40:55] llm
[06:40:57] to
[06:40:58] should continue.
[06:41:01] And then we'll have two different cases
[06:41:03] here. For true,
[06:41:06] we'll go to retriever agent. And then if
[06:41:09] false, we'll go to end.
[06:41:13] I'll add one more age here. From
[06:41:15] retriever agent to LLM and then the
[06:41:18] entry point will be from LL
[06:41:23] from LM itself. Okay. What's wrong with
[06:41:26] should continue? Let's see.
[06:41:29] Okay. [snorts] The spelling is wrong
[06:41:30] here. showed underscore continue.
[06:41:36] Uh something's wrong here. Now
[06:41:42] function is not callable. Okay, let's
[06:41:45] rerun everything from the beginning.
[06:41:51] So this is running. Tool collection is
[06:41:53] running. This is also running.
[06:41:56] running running running
[06:42:00] the tool call is also running.
[06:42:03] Now the graph is also built. Let me
[06:42:05] compile the graph. Call it rag agent
[06:42:08] equal to graph dot compile
[06:42:12] and then if we bring out our rag agent
[06:42:17] then we should see our flow here. So, so
[06:42:19] from start we go to LLM. If it has tool
[06:42:22] calls then we go to retriever agent then
[06:42:24] we go back to LLM. If it has multiple
[06:42:26] tool calls we again reciprocate through
[06:42:29] these uh retriever agents and then once
[06:42:32] our LLM call is complete then we go to
[06:42:35] false and then end the conversation.
[06:42:39] So finally we'll define a function for
[06:42:41] running our agent. So def running agent.
[06:42:49] Uh so we'll
[06:42:52] use a continuous loop here and then
[06:42:55] we'll ask user for their question
[06:42:59] input. What sorry
[06:43:03] what is your
[06:43:06] question?
[06:43:10] So if the user input is exit or quit
[06:43:14] then we exit the agent
[06:43:18] or else we're going to append
[06:43:22] append uh append the user given text
[06:43:25] into a human message.
[06:43:31] Then we will invoke our rag agent.
[06:43:39] Then we'll print the
[06:43:42] uh agent response
[06:43:48] >> here. Okay. So this is also done. And
[06:43:51] finally we'll call this running agent
[06:43:53] function
[06:43:55] since uh it was a long code. I hope we
[06:43:58] don't have any errors here. So we can
[06:44:00] run the application.
[06:44:03] Okay. So, so initially uh this is being
[06:44:08] run now.
[06:44:10] Uh okay, what do we ask here? So, we'll
[06:44:14] ask what is the document about?
[06:44:24] Okay, we have an error. Let's see what
[06:44:25] the error is.
[06:44:28] Uh
[06:44:30] I think I found my error here. So this
[06:44:32] should be inside a list. The system
[06:44:35] message should be inside a list here
[06:44:39] because uh if we don't keep it inside
[06:44:42] the list then this is not considered as
[06:44:44] a base message. Let me uh rerun
[06:44:46] everything again.
[06:44:56] Okay. So what is the document about?
[06:45:10] We still have an error. Let's let me
[06:45:12] check again.
[06:45:14] Uh for this one, I'm also going to uh
[06:45:18] edit my
[06:45:20] uh retriever agent function.
[06:45:25] So let me rerun this again and then see
[06:45:28] if I get an error.
[06:45:32] So what is the
[06:45:35] what is the document about?
[06:45:40] Let's see if we get any error. Okay, so
[06:45:43] the query is gone. Uh and then we have
[06:45:48] two different sources uh from where
[06:45:50] we're getting result and then the agent
[06:45:52] responses. The document is about stock
[06:45:54] market performance in 2024. Uh
[06:45:57] specifically focusing on something
[06:45:58] something something. Okay. Now we'll
[06:46:00] open this uh stock market document
[06:46:04] uh and then see uh what this document
[06:46:08] actually contains
[06:46:11] what happened here.
[06:46:16] Okay. So let me rerun this again and
[06:46:18] then and then check. Meanwhile, I'm
[06:46:20] going to open this document.
[06:46:25] >> [snorts]
[06:46:34] >> Okay. So this is our stock market
[06:46:36] document. Uh it contains some data and
[06:46:38] it will be asking question based on this
[06:46:41] here.
[06:46:48] So we'll rerun everything again and then
[06:46:51] see if we can continuously talk to it or
[06:46:53] not because I think we're getting some
[06:46:55] error there. Uh [snorts] we'll also fix
[06:46:57] that.
[06:47:00] Tell me about
[06:47:03] about the EV leaders. Uh,
[06:47:10] who is the electric
[06:47:13] vehicle
[06:47:16] leaders in the market?
[06:47:20] It should find that the EV leader
[06:47:23] vehicles are this company here.
[06:47:27] Uh
[06:47:29] so the agent response is correctly given
[06:47:33] and then we'll we'll ask uh
[06:47:38] we'll ask how much did they gain. So how
[06:47:41] much
[06:47:42] did
[06:47:45] Tesla gain in 2024?
[06:47:56] So from late 2023 to 2024 2024 gains
[06:48:00] occurring in there. So it contains a lot
[06:48:03] of content here. So it does give me uh
[06:48:07] give me the share price and then and
[06:48:10] then the growth as well as the sources
[06:48:12] as I asked earlier. So yeah, let me go
[06:48:15] to something else and then ask it.
[06:48:18] Uh [snorts]
[06:48:22] what was S NP's
[06:48:26] gain?
[06:48:30] So it should give me that S&P's gain was
[06:48:32] 25%.
[06:48:34] Okay. So this is working quite well.
[06:48:38] So this is how we uh implement rag
[06:48:43] using our langraph. Uh okay, I'll ask
[06:48:47] it. uh something that is not uh present
[06:48:50] in the document and then we'll see what
[06:48:51] it tells us. So what is
[06:48:58] why does
[06:49:00] why does the sun rises in the east
[06:49:05] and sets in the west.
[06:49:09] So it should not have any response for
[06:49:12] this. So it says I cannot answer this
[06:49:14] question using the provided document as
[06:49:16] it was stock market performance and not
[06:49:18] astronomy. So this is working quite
[06:49:21] well. Uh I'm going to end the video
[06:49:23] here. So I hope it uh implements on your
[06:49:27] end too. Be careful about the content of
[06:49:29] this particular function here because
[06:49:31] there are too many brackets being
[06:49:32] involved here. So might make some error.
[06:49:35] If you have any questions feel free to
[06:49:37] comment down below and I'll try to help
[06:49:38] you out. and I'll see you in the next
[06:49:41] video again.